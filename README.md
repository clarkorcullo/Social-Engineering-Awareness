# Social Engineering Awareness Program

A production-ready, OOP‑driven Flask application that delivers interactive learning on social engineering threats, defenses, and incident response. The system provides a structured curriculum with knowledge checks, real‑world simulations, analytics, and certification.

Repository: [`clarkorcullo/Social-Engineering-Awareness`](https://github.com/clarkorcullo/Social-Engineering-Awareness)

## 🚀 Overview

This platform guides learners through seven modules and a final assessment, enforcing completion rules and offering realistic practice via simulations (Phishing, Pretexting, Baiting, Quid Pro Quo). It tracks progress, scores, time spent, and recent activity, and supports survey and certificate generation upon completion.

Key principles:
- Clean separation of concerns via a service layer (`business_services/`) and data models (`data_models/`).
- Content is code-first and versioned in `learning_modules/`.
- Simulations follow a Base → Concrete OOP pattern in `simulations/`.

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

## 🎯 Core Features

### 📚 Learning Modules
- 7 comprehensive modules with practical examples and guidance
- Progressive unlocking: each module requires the previous one to be fully completed
- Knowledge checks per module with detailed feedback

### 🎮 Interactive Simulations
- Phishing, Pretexting, Baiting, Quid Pro Quo
- OOP design: `BaseSimulation` + specific implementations
- Real-time feedback with red‑flag explanations

### 📊 Assessment System
- Module Knowledge Checks: 5 questions/module, unlimited retakes
- Final Assessment: 25 questions, 3 retakes allowed every 48 hours
- Automatic grading, percentage computation, attempts tracking
- Recent activity feed (assessments, simulations, completions)

### 👤 User Management
- Registration with validation, secure authentication (Flask‑Login)
- Profile updates, avatars, and consistent progress tracking

### 📈 Analytics & Reporting
- Completion rate, average scores, simulations done, and time spent
- Survey and certificate unlocking based on completion rules

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Architecture**: Object-Oriented Programming (OOP)
- **Design Patterns**: Service Layer, Repository Pattern, Factory Pattern

## ✅ Completion Rules (Access Control)
- A module is considered fully completed when:
  - Knowledge check score ≥ 80% (configurable) AND
  - Simulation completed when the module includes one (Modules 2–5)
- Modules unlock sequentially. Final Assessment unlocks only after all modules are completed.

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

## 🧠 Content, Questions, and Simulations
- Edit learning content and questions in `learning_modules/`. Each module exposes content and a question factory.
- Simulations live in `simulations/` with a shared `BaseSimulation` API and per‑type logic.
- The app bootstraps modules and questions on first run and can be reloaded via `reload_modules.py`.

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

## 🧩 Architecture Notes
- `app.py` defines routes and wires services to templates.
- `data_models/` contains SQLAlchemy models (Users, Modules, Progress, Assessments, Simulations).
- `business_services/` encapsulates domain logic (assessment creation/validation, progress rules, analytics, simulations orchestration, user access checks).
- `templates/` are presentation-only; heavy logic is in services. The dashboard is fed by the `/dashboard` route.

## 📊 Dashboard Metrics
- Modules Completed vs Total Modules
- Simulations Completed
- Average Score (assessments)
- Time Spent (aggregated from progress)
- Final Assessment readiness, survey/certificate status, recent activities

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

### Render + GitHub
- The repository `main` branch is deployable to Render. A force‑push will roll the environment forward.

## 🖼️ Screenshots

Place screenshots under `static/screenshots/` and they will render below. Suggested filenames are provided.

| Dashboard | Module | Assessment |
| --- | --- | --- |
| ![Dashboard](static/screenshots/dashboard.png) | ![Module](static/screenshots/module.png) | ![Assessment](static/screenshots/assessment.png) |

| Simulation | Final Assessment | Certificate |
| --- | --- | --- |
| ![Simulation](static/screenshots/simulation.png) | ![Final](static/screenshots/final_assessment.png) | ![Certificate](static/screenshots/certificate.png) |

> Tip: Capture at 1440×900 or similar for crisp previews.

## ▶️ Quickstart GIF

Add a short walkthrough GIF at `static/screenshots/quickstart.gif` to showcase:
1. Login → Dashboard
2. Open Module → Take Knowledge Check (submit)
3. Run a Simulation → Submit
4. Final Assessment info page

Embed (auto‑renders when the file exists):

![Quickstart](static/screenshots/quickstart.gif)

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

## 🧪 Testing & Quality
- Service‑level boundaries make business logic testable in isolation.
- Templates avoid DB queries; data should be provided via routes.

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

**Note**: This application is for educational use to raise awareness about social engineering attacks and prevention strategies.
