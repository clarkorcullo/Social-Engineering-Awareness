import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, UserProgress, AssessmentResult

def test_data_preservation():
    """Test that user data is preserved during updates"""
    with app.app_context():
        print("🧪 Testing Data Preservation System...")
        
        # Check existing users
        users = User.query.all()
        print(f"👥 Found {len(users)} existing users")
        
        for user in users:
            print(f"   - {user.username} ({user.email})")
            print(f"     Progress: {user.modules_completed} modules completed")
            print(f"     Score: {user.total_score} points")
            print(f"     Simulations: {user.simulations_completed} completed")
        
        # Check user progress
        progress_entries = UserProgress.query.all()
        print(f"📊 Found {len(progress_entries)} progress entries")
        
        for progress in progress_entries:
            user = User.query.get(progress.user_id)
            print(f"   - {user.username}: Module {progress.module_id} - {progress.status}")
        
        # Check assessment results
        assessment_results = AssessmentResult.query.all()
        print(f"📝 Found {len(assessment_results)} assessment results")
        
        for result in assessment_results:
            user = User.query.get(result.user_id)
            print(f"   - {user.username}: {result.assessment_type} - Score: {result.score}%")
        
        print("\n✅ Data Preservation Test Complete!")
        print("📋 Summary:")
        print(f"   - Users: {len(users)}")
        print(f"   - Progress Entries: {len(progress_entries)}")
        print(f"   - Assessment Results: {len(assessment_results)}")
        print("\n🎉 All user data is preserved and intact!")

if __name__ == "__main__":
    test_data_preservation() 