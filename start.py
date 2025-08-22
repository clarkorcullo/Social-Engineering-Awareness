#!/usr/bin/env python3
"""
Startup script for Social Engineering Awareness Program
"""

import os
import sys
import subprocess
import time
import requests

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'flask',
        'flask-sqlalchemy', 
        'flask-login',
        'werkzeug'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    else:
        print("✅ All dependencies are installed")

def check_database():
    """Check if database exists and is accessible"""
    try:
        from app import app, db
        with app.app_context():
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
        print("✅ Database is accessible")
        return True
    except Exception as e:
        print(f"⚠️ Database issue: {e}")
        return False

def start_application():
    """Start the Flask application"""
    print("🚀 Starting Social Engineering Awareness Program...")
    
    # Set environment variables
    os.environ['FLASK_ENV'] = 'development'
    os.environ['LOG_LEVEL'] = 'INFO'
    
    try:
        # Import and run the application
        from app import app
        
        port = int(os.environ.get('PORT', 5000))
        debug = os.environ.get('FLASK_ENV') == 'development'
        
        print(f"✅ Application starting on port {port}")
        print(f"🌐 Access the application at: http://localhost:{port}")
        print(f"📊 Health check at: http://localhost:{port}/health")
        print("👤 Default admin: administrator / Admin123!@#2025")
        print("🛑 Press Ctrl+C to stop the application")
        
        app.run(debug=debug, host='0.0.0.0', port=port)
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        sys.exit(1)

def main():
    """Main function"""
    print("🔧 Social Engineering Awareness Program - Startup")
    print("=" * 50)
    
    # Check dependencies
    check_dependencies()
    
    # Check database
    if not check_database():
        print("🔧 Initializing database...")
        try:
            from app import init_database
            init_database()
            print("✅ Database initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize database: {e}")
            sys.exit(1)
    
    # Start application
    start_application()

if __name__ == '__main__':
    main()
