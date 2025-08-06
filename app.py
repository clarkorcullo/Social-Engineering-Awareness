from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect, generate_csrf
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
# Use a more reliable database path for production
if os.environ.get('RENDER'):
    # On Render, use /tmp directory which is always writable
    db_path = '/tmp/social_engineering_awareness.db'
else:
    # Local development
    db_path = 'social_engineering_awareness.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CSRF Protection - temporarily disabled
# csrf = CSRFProtect(app)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(50), nullable=False)
    year_level = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Progress tracking attributes
    modules_completed = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    simulations_completed = db.Column(db.Integer, default=0)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading index: {str(e)}"

@app.route('/profile')
@login_required
def profile():
    try:
        return render_template('profile.html')
    except Exception as e:
        return f"Error loading profile: {str(e)}"

@app.route('/module/<int:module_id>')
@login_required
def module(module_id):
    try:
        # For now, just show a simple module page
        module_names = {
            1: "Introduction to Social Engineering",
            2: "Types of Social Engineering Attacks", 
            3: "Phishing Attacks",
            4: "Pretexting and Impersonation",
            5: "Baiting and Quid Pro Quo",
            6: "Advanced Techniques",
            7: "Incident Response",
            8: "Final Assessment"
        }
        
        module_name = module_names.get(module_id, f"Module {module_id}")
        
        return render_template('module_simple.html', module_id=module_id, module_name=module_name)
    except Exception as e:
        return f"Error loading module: {str(e)}"

@app.route('/assessment/<assessment_type>')
@login_required
def assessment(assessment_type):
    try:
        assessment_names = {
            'baseline': 'Baseline Assessment',
            'post': 'Post-Assessment',
            'followup': 'Follow-up Assessment'
        }
        
        assessment_name = assessment_names.get(assessment_type, f'{assessment_type.title()} Assessment')
        
        return render_template('assessment_simple.html', assessment_type=assessment_type, assessment_name=assessment_name)
    except Exception as e:
        return f"Error loading assessment: {str(e)}"

@app.route('/final_assessment')
@login_required
def final_assessment():
    try:
        return render_template('final_assessment_simple.html')
    except Exception as e:
        return f"Error loading final assessment: {str(e)}"

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            username = request.form.get('username', '')
            email = request.form.get('email', '')
            password = request.form.get('password', '')
            confirm_password = request.form.get('confirm_password', '')
            specialization = request.form.get('specialization', '')
            year_level = request.form.get('year_level', '')
            
            errors = {}
            
            if len(username) < 8:
                errors['username'] = 'Username must be at least 8 characters long'
            
            if len(password) < 12:
                errors['password'] = 'Password must be at least 12 characters long'
            
            if password != confirm_password:
                errors['confirm_password'] = 'Passwords do not match'
            
            if User.query.filter_by(username=username).first():
                errors['username'] = 'Username already exists'
            
            if User.query.filter_by(email=email).first():
                errors['email'] = 'Email already registered'
            
            if not specialization:
                errors['specialization'] = 'Please select your IT specialization'
            
            if not year_level:
                errors['year_level'] = 'Please select your year level'
            
            if errors:
                return render_template('register.html', errors=errors)
            
            try:
                user = User(
                    username=username,
                    email=email,
                    password_hash=generate_password_hash(password),
                    full_name=username.title(),
                    specialization=specialization,
                    year_level=year_level
                )
                
                db.session.add(user)
                db.session.commit()
                
                flash('Registration successful! Please login.')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                flash(f'Registration failed: {str(e)}')
                return render_template('register.html')
        
        return render_template('register.html')
    except Exception as e:
        return f"Error in register: {str(e)}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            
            user = User.query.filter_by(username=username).first()
            
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password')
                return render_template('login.html')
        
        return render_template('login.html')
    except Exception as e:
        return f"Error in login: {str(e)}"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    try:
        # Get user progress data
        completed_modules = current_user.modules_completed or 0
        total_score = current_user.total_score or 0
        simulations_completed = current_user.simulations_completed or 0
        
        # Calculate average score
        average_score = 0
        if completed_modules > 0:
            average_score = round((total_score / completed_modules) * 10, 1)
        
        dashboard_data = {
            'completed_modules': completed_modules,
            'total_score': total_score,
            'average_score': average_score,
            'simulations_completed': simulations_completed
        }
        return render_template('dashboard.html', **dashboard_data)
    except Exception as e:
        return f"Error loading dashboard: {str(e)}"

@app.route('/test')
def test():
    return "Test route working! ✅"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running"}

# Initialize database
with app.app_context():
    try:
        db.create_all()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")
        # Try to recreate tables
        try:
            db.drop_all()
            db.create_all()
            print("Database tables recreated successfully")
        except Exception as e2:
            print(f"Failed to recreate database: {e2}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port) 