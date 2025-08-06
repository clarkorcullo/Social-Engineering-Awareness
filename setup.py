#!/usr/bin/env python3
"""
Setup script for Social Engineering Awareness Program
Automates initial configuration and admin user creation
"""

import os
import sys
from werkzeug.security import generate_password_hash

def setup_database():
    """Initialize the database and create admin user"""
    try:
        from app import app, db, User, Module
        
        with app.app_context():
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully")
            
            # Check if admin user exists
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                # Create admin user
                admin = User(
                    username='admin',
                    email='admin@mmdc.edu.ph',
                    password_hash=generate_password_hash('admin123'),
                    specialization='Computer Programming',
                    year_level='4th Year',
                    cybersecurity_experience=True
                )
                db.session.add(admin)
                print("✅ Admin user created successfully")
                print("   Username: admin")
                print("   Password: admin123")
            else:
                print("ℹ️  Admin user already exists")
            
            # Create default modules if they don't exist
            if not Module.query.first():
                modules = [
                    {
                        'name': 'Introduction to Social Engineering',
                        'description': 'Understanding human vulnerabilities and psychological manipulation',
                        'content': 'This module introduces the fundamental concepts of social engineering, including how attackers exploit human psychology to gain unauthorized access to systems and information.',
                        'order': 1
                    },
                    {
                        'name': 'Types of Social Engineering Attacks',
                        'description': 'Phishing, pretexting, baiting, and other manipulation techniques',
                        'content': 'Learn about different types of social engineering attacks including phishing, pretexting, baiting, quid pro quo, and tailgating.',
                        'order': 2
                    },
                    {
                        'name': 'Identifying Red Flags',
                        'description': 'Recognizing warning signs and suspicious behavior',
                        'content': 'Develop skills to identify common red flags in emails, phone calls, and physical interactions that may indicate social engineering attempts.',
                        'order': 3
                    },
                    {
                        'name': 'Defense Strategies',
                        'description': 'Best practices for protecting against attacks',
                        'content': 'Learn effective defense strategies including verification procedures, security policies, and incident response protocols.',
                        'order': 4
                    },
                    {
                        'name': 'Real-world Case Studies',
                        'description': 'Analysis of actual social engineering incidents',
                        'content': 'Examine real-world case studies to understand how social engineering attacks are executed and their impact on organizations.',
                        'order': 5
                    },
                    {
                        'name': 'Advanced Techniques',
                        'description': 'Sophisticated attack methods and countermeasures',
                        'content': 'Explore advanced social engineering techniques and the corresponding countermeasures and detection methods.',
                        'order': 6
                    },
                    {
                        'name': 'Incident Response',
                        'description': 'How to respond when attacks are detected',
                        'content': 'Learn proper incident response procedures when social engineering attacks are suspected or detected.',
                        'order': 7
                    },
                    {
                        'name': 'Final Assessment',
                        'description': 'Comprehensive evaluation of learning outcomes',
                        'content': 'Complete a comprehensive assessment to evaluate your understanding and application of social engineering awareness concepts.',
                        'order': 8
                    }
                ]
                
                for module_data in modules:
                    module = Module(**module_data)
                    db.session.add(module)
                
                print("✅ Default learning modules created successfully")
            else:
                print("ℹ️  Learning modules already exist")
            
            db.session.commit()
            print("✅ Database setup completed successfully")
            
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return False
    
    return True

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'flask',
        'flask_sqlalchemy',
        'flask_login',
        'werkzeug',
        'PyPDF2'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\nPlease install missing packages with:")
        print("pip install -r requirements.txt")
        return False
    
    print("✅ All required dependencies are installed")
    return True

def main():
    """Main setup function"""
    print("🚀 Social Engineering Awareness Program Setup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup database
    if not setup_database():
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run the application: python app.py")
    print("2. Open your browser: http://localhost:5000")
    print("3. Login with admin credentials or register a new account")
    print("\nAdmin credentials:")
    print("   Username: admin")
    print("   Password: admin123")
    print("\nHappy learning! 🎓")

if __name__ == "__main__":
    main() 