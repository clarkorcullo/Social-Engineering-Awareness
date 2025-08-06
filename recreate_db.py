#!/usr/bin/env python3
"""
Script to recreate the database with all current models
"""

from app import app, db, User, Module, KnowledgeCheckQuestion, FinalAssessmentQuestion, FeedbackSurvey

def recreate_database():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("✅ Dropped all existing tables")
        
        # Create all tables
        db.create_all()
        print("✅ Created all tables with current models")
        
        # Create admin user
        from werkzeug.security import generate_password_hash
        admin_user = User(
            username='admin',
            email='admin@mmdc.mcl.edu.ph',
            password_hash=generate_password_hash('AdminPass123!'),
            full_name='Admin User',
            birthday=None,
            address='MMDC Main Campus',
            specialization='Network & Cybersecurity',
            year_level='4th Year',
            cybersecurity_experience=True
        )
        db.session.add(admin_user)
        print("✅ Created admin user")
        
        # Initialize modules
        modules_data = [
            {
                'name': 'Introduction to Social Engineering',
                'description': 'Understanding the basics of social engineering attacks',
                'content': 'This module introduces the fundamental concepts of social engineering...',
                'order': 1
            },
            {
                'name': 'Types of Social Engineering Attacks',
                'description': 'Exploring different attack vectors and methods',
                'content': 'This module covers various types of social engineering attacks...',
                'order': 2
            },
            {
                'name': 'Phishing Attacks',
                'description': 'Understanding and identifying phishing attempts',
                'content': 'This module focuses on phishing attacks and how to recognize them...',
                'order': 3
            },
            {
                'name': 'Pretexting and Impersonation',
                'description': 'Learning about pretexting techniques',
                'content': 'This module covers pretexting and impersonation tactics...',
                'order': 4
            },
            {
                'name': 'Baiting and Quid Pro Quo',
                'description': 'Understanding baiting and quid pro quo attacks',
                'content': 'This module explores baiting and quid pro quo techniques...',
                'order': 5
            },
            {
                'name': 'Advanced Techniques',
                'description': 'Advanced social engineering methods',
                'content': 'This module covers advanced social engineering techniques...',
                'order': 6
            },
            {
                'name': 'Incident Response',
                'description': 'How to respond to social engineering incidents',
                'content': 'This module teaches proper incident response procedures...',
                'order': 7
            },
            {
                'name': 'Final Assessment',
                'description': 'Comprehensive evaluation of all learning outcomes',
                'content': 'This module provides a comprehensive assessment...',
                'order': 8
            }
        ]
        
        for module_data in modules_data:
            module = Module(**module_data)
            db.session.add(module)
        
        print("✅ Added all learning modules")
        
        # Commit all changes
        db.session.commit()
        print("✅ Database setup completed successfully!")
        print("\n📋 Database Summary:")
        print(f"   - Users: {User.query.count()}")
        print(f"   - Modules: {Module.query.count()}")
        print(f"   - Knowledge Check Questions: {KnowledgeCheckQuestion.query.count()}")
        print(f"   - Final Assessment Questions: {FinalAssessmentQuestion.query.count()}")
        print(f"   - Feedback Surveys: {FeedbackSurvey.query.count()}")

if __name__ == '__main__':
    recreate_database() 