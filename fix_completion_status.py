import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, UserProgress, AssessmentResult

def fix_completion_status():
    """Fix completion status for all users to ensure modules are only completed if knowledge check is passed"""
    with app.app_context():
        print("🔧 Fixing completion status for all users...")
        
        # Get all users
        users = User.query.all()
        
        for user in users:
            print(f"👤 Processing user: {user.username}")
            
            # Get all user progress records
            progress_records = UserProgress.query.filter_by(user_id=user.id).all()
            
            for progress in progress_records:
                # Check if user has passed the knowledge check for this module
                passed_assessment = AssessmentResult.query.filter_by(
                    user_id=user.id,
                    module_id=progress.module_id,
                    assessment_type='knowledge_check',
                    passed=True
                ).first()
                
                # If progress status is 'completed' but no passed assessment exists, fix it
                if progress.status == 'completed' and not passed_assessment:
                    print(f"  ❌ Module {progress.module_id}: Status 'completed' but no passed knowledge check found")
                    print(f"     → Changing status to 'in_progress'")
                    progress.status = 'in_progress'
                    progress.completed_at = None
                elif progress.status == 'completed' and passed_assessment:
                    print(f"  ✅ Module {progress.module_id}: Status 'completed' and passed knowledge check confirmed")
                elif progress.status != 'completed':
                    print(f"  ℹ️  Module {progress.module_id}: Status '{progress.status}' (no change needed)")
            
            # Commit changes for this user
            db.session.commit()
            print(f"  ✅ Completed processing for user: {user.username}")
        
        print("🎉 All completion statuses have been fixed!")

if __name__ == "__main__":
    fix_completion_status() 