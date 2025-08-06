# 🚀 Social Engineering Awareness Program - Full Scale Implementation

## 📋 Project Overview

This is a comprehensive, production-ready implementation of the Social Engineering Awareness Program for MMDC IT students. The system provides a complete learning management platform with user authentication, progress tracking, interactive assessments, and realistic simulations.

## 🎯 Key Features

### 🔐 **User Management System**
- User registration with detailed student information
- Secure login/logout functionality
- Role-based access control
- Profile management and progress tracking

### 📚 **Learning Management System (LMS)**
- 8 structured learning modules
- Progressive learning path with prerequisites
- Interactive content delivery
- Progress tracking and analytics
- Certificate generation upon completion

### 📊 **Assessment System**
- Baseline assessment for initial evaluation
- Post-training assessment for measuring improvement
- Follow-up assessment for long-term retention
- Multi-dimensional evaluation (Knowledge, Attitude, Behavior)
- Automated scoring and feedback

### 🎮 **Interactive Simulations**
- Realistic phishing email scenarios
- Pretexting attack simulations
- Baiting and quid pro quo exercises
- Immediate feedback and learning points
- Performance tracking and analytics

### 📈 **Analytics & Reporting**
- Individual student progress tracking
- Class-wide performance analytics
- Assessment score analysis
- Simulation performance metrics
- Export capabilities for research

## 🛠️ Technical Stack

### **Backend**
- **Flask 2.3.3** - Web framework
- **SQLAlchemy 2.0.42** - Database ORM
- **Flask-Login 0.6.3** - User authentication
- **Werkzeug 2.3.7** - Security utilities

### **Frontend**
- **Bootstrap 5.1.3** - UI framework
- **Font Awesome 6.0.0** - Icons
- **jQuery 3.6.0** - JavaScript library
- **Custom CSS/JS** - Enhanced functionality

### **Database**
- **SQLite** - Lightweight database (production-ready for PostgreSQL/MySQL)

### **Additional Tools**
- **PyPDF2 3.0.1** - PDF processing
- **python-dotenv 1.0.0** - Environment management
- **email-validator 2.0.0** - Email validation

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- pip package manager
- Modern web browser

### **Installation**

1. **Clone or download the project**
   ```bash
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
   - Open your browser
   - Go to: `http://localhost:5000`
   - Register a new account or login

### **First-Time Setup**

1. **Create an admin account**
   ```python
   # In Python console or script
   from app import app, db, User
   from werkzeug.security import generate_password_hash
   
   with app.app_context():
       admin = User(
           username='admin',
           email='admin@mmdc.edu.ph',
           password_hash=generate_password_hash('admin123'),
           specialization='Computer Programming',
           year_level='4th Year',
           cybersecurity_experience=True
       )
       db.session.add(admin)
       db.session.commit()
   ```

2. **Initialize the database**
   - The database will be automatically created on first run
   - Default modules will be populated

## 📁 Project Structure

```
CapstoneProject/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navigation
│   ├── index.html                 # Home page
│   ├── login.html                 # Login page
│   ├── register.html              # Registration page
│   ├── dashboard.html             # User dashboard
│   └── assessment_baseline.html   # Assessment form
├── static/                        # Static files (CSS, JS, images)
├── social_engineering_awareness.db # SQLite database
├── README.md                      # Original project documentation
├── FULL_SCALE_README.md           # This file
└── [Other project files...]
```

## 🎮 Usage Guide

### **For Students**

1. **Registration**
   - Visit the homepage
   - Click "Get Started" or "Register"
   - Fill in your details (specialization, year level, etc.)
   - Create your account

2. **Taking Assessments**
   - Login to your account
   - Navigate to "Assessment" in the menu
   - Complete the baseline assessment
   - Review your scores and feedback

3. **Learning Modules**
   - Access modules from your dashboard
   - Complete modules in order (prerequisites enforced)
   - Track your progress and scores
   - Review completed modules anytime

4. **Simulations**
   - Try interactive phishing simulations
   - Practice identifying red flags
   - Receive immediate feedback
   - Track your performance over time

### **For Instructors**

1. **Admin Access**
   - Login with admin credentials
   - Access admin dashboard at `/admin`
   - View all student progress and scores

2. **Monitoring Progress**
   - Track individual student performance
   - View class-wide analytics
   - Export data for research purposes

3. **Content Management**
   - Update learning modules
   - Add new simulation scenarios
   - Modify assessment questions

## 🔧 Configuration

### **Environment Variables**
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///social_engineering_awareness.db
FLASK_ENV=development
```

### **Database Configuration**
The application uses SQLite by default. For production, consider:

```python
# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dbname'

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/dbname'
```

## 📊 Database Schema

### **Core Tables**
- **users** - Student information and progress
- **assessments** - Assessment responses and scores
- **progress** - Module completion tracking
- **simulation_results** - Simulation performance data
- **modules** - Learning content

### **Key Relationships**
- Users have multiple assessments
- Users have progress records for each module
- Users have simulation results
- Modules are ordered and have prerequisites

## 🎯 Assessment Framework

### **Knowledge Assessment**
- Multiple choice questions
- Technical understanding evaluation
- Cybersecurity concept testing

### **Attitude Assessment**
- Likert scale responses (1-5)
- Perceived threat assessment
- Confidence level evaluation

### **Behavioral Assessment**
- Real-world scenario responses
- Decision-making evaluation
- Security practice assessment

## 🎮 Simulation Features

### **Phishing Simulations**
- Realistic email scenarios
- Multiple choice responses
- Immediate feedback with explanations
- Red flag identification training

### **Pretexting Scenarios**
- Social manipulation attempts
- Authority figure impersonation
- Information gathering techniques

### **Baiting Exercises**
- Physical device scenarios
- USB drop attacks
- Social media manipulation

## 📈 Analytics & Reporting

### **Individual Analytics**
- Progress tracking across modules
- Assessment score trends
- Simulation performance metrics
- Time spent on learning

### **Class Analytics**
- Average performance metrics
- Module completion rates
- Assessment score distributions
- Simulation success rates

### **Research Data**
- Pre/post assessment comparisons
- Long-term retention analysis
- Behavioral change tracking
- Export capabilities for research

## 🔒 Security Features

### **Authentication**
- Secure password hashing
- Session management
- Role-based access control
- CSRF protection

### **Data Protection**
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- Secure headers

## 🚀 Deployment

### **Development**
```bash
python app.py
```

### **Production (Gunicorn)**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### **Docker Deployment**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 🧪 Testing

### **Manual Testing**
1. Register new accounts
2. Complete assessments
3. Try simulations
4. Test module progression
5. Verify data persistence

### **Automated Testing**
```bash
# Run tests (when implemented)
python -m pytest tests/
```

## 📝 API Endpoints

### **Authentication**
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### **Assessments**
- `GET /assessment/<type>` - Load assessment
- `POST /assessment/<type>` - Submit assessment

### **Modules**
- `GET /module/<id>` - Access learning module
- `POST /api/progress/update` - Update progress

### **Simulations**
- `GET /simulation/<type>` - Load simulation
- `POST /api/simulation/result` - Submit result

## 🔄 Future Enhancements

### **Planned Features**
- Real-time notifications
- Advanced analytics dashboard
- Mobile app development
- Integration with existing LMS
- Multi-language support
- Advanced simulation scenarios

### **Research Integration**
- Export data for statistical analysis
- Integration with research tools
- Longitudinal study support
- Comparative analysis capabilities

## 🤝 Contributing

### **Development Setup**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### **Code Standards**
- Follow PEP 8 Python style guide
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

## 📞 Support

### **Technical Issues**
- Check the logs in the console
- Verify database connectivity
- Ensure all dependencies are installed
- Test with different browsers

### **Feature Requests**
- Submit through GitHub issues
- Provide detailed use case descriptions
- Include mockups if applicable

## 📄 License

This project is developed for educational purposes at MMDC. All rights reserved.

## 👥 Team

**Capstone Project Team:**
- David Algerico Diaz
- Jan Thadeus Mercado
- Claros Orcullo
- Jasmin Pascual

**Supervisor:** S3102 Group 4

---

## 🎉 Getting Started Right Now!

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Register a new account and start learning!**

The full-scale implementation is now ready for production use and research purposes. 🚀 