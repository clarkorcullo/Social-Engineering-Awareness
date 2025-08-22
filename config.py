"""
Configuration settings for Social Engineering Awareness Program
"""

import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me-in-production')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    DEBUG = FLASK_ENV == 'development'
    
    # Database Configuration
    if os.environ.get('RENDER'):
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/social_engineering_awareness.db'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///social_engineering_awareness.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = os.environ.get('RENDER', False)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security Configuration
    PASSWORD_MIN_LENGTH = 12
    PASSWORD_REQUIRE_UPPERCASE = True
    PASSWORD_REQUIRE_LOWERCASE = True
    PASSWORD_REQUIRE_NUMBERS = True
    PASSWORD_REQUIRE_SPECIAL = False
    
    # Assessment Configuration
    KNOWLEDGE_CHECK_PASSING_SCORE = 80  # Percentage
    FINAL_ASSESSMENT_PASSING_SCORE = 70  # Percentage
    MAX_ASSESSMENT_ATTEMPTS = 3
    ASSESSMENT_COOLDOWN_HOURS = 48
    
    # Module Configuration
    TOTAL_MODULES = 7
    MODULES_WITH_SIMULATIONS = [2, 3, 4, 5]  # Module IDs that have simulations
    
    # Simulation Configuration
    SIMULATION_TYPES = ['phishing', 'pretexting', 'baiting', 'quid_pro_quo']
    
    # Admin Configuration
    DEFAULT_ADMIN_USERNAME = 'administrator'
    DEFAULT_ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@mmdc.edu.ph')
    DEFAULT_ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Admin123!@#2025')
    
    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = 'app.log'
    
    # File Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = 'static/profile_pictures'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Email Configuration (for password reset)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Application Information
    APP_NAME = 'Social Engineering Awareness Program'
    APP_VERSION = '1.0.0'
    APP_DESCRIPTION = 'Educational platform for social engineering awareness'
    ORGANIZATION = 'Mapúa Malayan Digital College (MMDC)'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    FLASK_ENV = 'development'
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    FLASK_ENV = 'production'
    LOG_LEVEL = 'WARNING'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
