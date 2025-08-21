# Social Engineering Awareness Program

A comprehensive web-based learning platform for social engineering awareness training, built with Flask and modern OOP principles.

## 🚀 Project Overview

This application provides an interactive learning experience for understanding social engineering attacks, prevention strategies, and incident response. It features a complete learning path with modules, assessments, simulations, and progress tracking.

## 📁 Project Structure

```
CapstoneProject/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python runtime version
├── Procfile                        # Heroku deployment configuration
├── .gitignore                      # Git ignore rules
├── README.md                       # This documentation file
├── reload_modules.py               # Script to reload module content
│
├── data_models/                    # Database models and data structures
│   ├── __init__.py
│   ├── base_models.py              # Base model classes and mixins
│   ├── user_models.py              # User and authentication models
│   ├── content_models.py           # Module and content models
│   └── progress_models.py          # Progress tracking models
│
├── business_services/              # Business logic and service layer
│   ├── __init__.py
│   ├── user_service.py             # User management services
│   ├── module_service.py           # Module management services
│   ├── assessment_service.py       # Assessment and grading services
│   ├── simulation_service.py       # Simulation management services
│   ├── progress_service.py         # Progress tracking services
│   ├── analytics_service.py        # Analytics and reporting services
│   └── module_manager_service.py   # Module coordination services
│
├── learning_modules/               # Learning content and questions
│   ├── __init__.py
│   ├── module1.py                  # Introduction to Social Engineering
│   ├── module2.py                  # Types of Social Engineering Attacks
│   ├── module3.py                  # Phishing Detection and Prevention
│   ├── module4.py                  # Password Security and Authentication
│   ├── module5.py                  # Social Media Security
│   ├── module6.py                  # Physical Security and Social Engineering
│   ├── module7.py                  # Incident Response and Reporting
│   └── final_assessment.py         # Final assessment content
│
├── helper_utilities/               # Utility functions and data structures
│   ├── __init__.py
│   ├── constants.py                # Application constants
│   ├── data_structures.py          # Custom data structures (LinkedList, Stack, etc.)
│   ├── formatters.py               # Data formatting utilities
│   └── validators.py               # Input validation utilities
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── index.html                  # Home page
│   ├── login.html                  # Login page
│   ├── register.html               # Registration page
│   ├── dashboard.html              # User dashboard
│   ├── module.html                 # Module content page
│   ├── assessment_simple.html      # Assessment interface
│   ├── simulation_simple.html      # Simulation interface
│   ├── final_assessment_simple.html # Final assessment interface
│   ├── survey.html                 # Feedback survey
│   ├── certificate.html            # Certificate generation
│   ├── profile.html                # User profile
│   ├── forgot_password.html        # Password reset
│   ├── reset_password.html         # Password reset confirmation
│   ├── 404.html                    # Error page
│   └── 500.html                    # Server error page
│
├── static/                         # Static assets
│   ├── MMDCLogo.png               # MMDC logo
│   ├── SEALogo.png                # Social Engineering Awareness logo
│   ├── Background.png             # Background image
│   └── profile_pictures/          # User profile pictures
│
└── instance/                       # Database and instance files
    └── social_engineering_awareness.db
```

## 🎯 Key Features

### 📚 Learning Modules
- **7 Comprehensive Modules** covering all aspects of social engineering
- **Rich Content** with HTML formatting and interactive elements
- **Progressive Learning Path** with module dependencies
- **Knowledge Checks** with detailed explanations

### 🎮 Interactive Simulations
- **Phishing Simulations** - Email-based attack scenarios
- **Pretexting Simulations** - Phone call and impersonation scenarios
- **Baiting Simulations** - Physical device and social media scenarios
- **Real-time Feedback** with explanations and learning points

### 📊 Assessment System
- **Module Knowledge Checks** - 5 questions per module
- **Final Assessment** - Comprehensive evaluation
- **Automatic Grading** with detailed feedback
- **Progress Tracking** with completion statistics

### 👤 User Management
- **User Registration** with validation
- **Secure Authentication** with password hashing
- **Profile Management** with customizable information
- **Progress Tracking** across all modules

### 📈 Analytics & Reporting
- **Learning Analytics** with completion rates
- **Performance Metrics** with score tracking
- **Survey System** for feedback collection
- **Certificate Generation** upon completion

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Architecture**: Object-Oriented Programming (OOP)
- **Design Patterns**: Service Layer, Repository Pattern, Factory Pattern

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CapstoneProject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Login with default admin credentials:
     - Username: `administrator`
     - Password: `Admin123!@#`

### Database Setup

The application automatically creates the database and loads content on first run. If you need to reload the module content:

```bash
python reload_modules.py
```

## 📋 Learning Modules

1. **Introduction to Social Engineering**
   - Basic concepts and psychology
   - Why social engineering works
   - Common targets and impacts

2. **Types of Social Engineering Attacks**
   - Phishing, pretexting, baiting
   - Quid pro quo and tailgating
   - Attack vectors and techniques

3. **Phishing Detection and Prevention**
   - Email phishing identification
   - Website spoofing detection
   - Prevention strategies

4. **Password Security and Authentication**
   - Strong password creation
   - Multi-factor authentication
   - Security best practices

5. **Social Media Security**
   - Privacy settings and controls
   - Information sharing risks
   - Social media attack vectors

6. **Physical Security and Social Engineering**
   - Physical access control
   - Social engineering in person
   - Environmental security

7. **Incident Response and Reporting**
   - Incident detection
   - Response procedures
   - Reporting protocols

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `PORT`: Application port (default: 5000)
- `RENDER`: Set for deployment on Render platform

### Database Configuration
- **Development**: SQLite database in `instance/` folder
- **Production**: Can be configured for PostgreSQL or MySQL

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
The application includes configuration for:
- **Heroku**: Use the provided `Procfile`
- **Render**: Configured for cloud deployment
- **Docker**: Can be containerized for deployment

## 📊 API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### Learning
- `GET /dashboard` - User dashboard
- `GET /module/<id>` - Module content
- `GET /assessment/<id>` - Module assessment
- `POST /submit_assessment/<id>` - Submit assessment

### Simulations
- `GET /simulation/<type>` - Access simulation
- `POST /submit_simulation` - Submit simulation results

### Progress
- `POST /update_progress` - Update user progress
- `GET /profile` - User profile
- `POST /update_profile` - Update profile

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the documentation in each module
- Review the code comments
- Create an issue in the repository

## 🎉 Acknowledgments

- Built for educational purposes
- Designed to raise awareness about social engineering
- Promotes cybersecurity best practices

---

**Note**: This application is designed for educational purposes to raise awareness about social engineering attacks and prevention strategies.
