from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, generate_csrf
from functools import wraps
import json
import datetime
import os
import random
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)  # Generate secure random key
# Use a more reliable database path for production
import os
if os.environ.get('RENDER'):
    # On Render, use /tmp directory which is always writable
    db_path = '/tmp/social_engineering_awareness.db'
else:
    # Local development
    db_path = 'social_engineering_awareness.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# Security configurations
app.config['WTF_CSRF_ENABLED'] = False
app.config['WTF_CSRF_TIME_LIMIT'] = 3600  # 1 hour
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Ensure CSRF token is available in all templates
@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

# Configure CSRF protection
csrf = CSRFProtect(app)
csrf.init_app(app)

# File upload configuration
app.config['UPLOAD_FOLDER'] = 'static/profile_pictures'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)  # NEW: required
    birthday = db.Column(db.Date, nullable=True)           # NEW: optional
    address = db.Column(db.String(255), nullable=True)     # NEW: optional
    profile_picture = db.Column(db.String(255), nullable=True)  # NEW: profile picture filename
    specialization = db.Column(db.String(50), nullable=False)
    year_level = db.Column(db.String(20), nullable=False)
    cybersecurity_experience = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default='student')  # NEW: student, trainer, admin
    is_active = db.Column(db.Boolean, default=True)      # NEW: account status
    failed_login_attempts = db.Column(db.Integer, default=0)  # NEW: security tracking
    locked_until = db.Column(db.DateTime)                # NEW: account lockout
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Progress tracking
    modules_completed = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    simulations_completed = db.Column(db.Integer, default=0)
    
    # Assessment tracking
    final_assessment_attempts = db.Column(db.Integer, default=0)
    final_assessment_passed = db.Column(db.Boolean, default=False)
    
    # Relationships
    assessments = db.relationship('Assessment', backref='user', lazy=True)
    progress = db.relationship('Progress', backref='user', lazy=True)
    simulation_results = db.relationship('SimulationResult', backref='user', lazy=True)
    module_assessments = db.relationship('ModuleAssessment', backref='user', lazy=True)
    final_assessments = db.relationship('FinalAssessment', backref='user', lazy=True)

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assessment_type = db.Column(db.String(50), nullable=False)  # baseline, post, followup
    knowledge_score = db.Column(db.Integer)
    attitude_score = db.Column(db.Integer)
    behavioral_score = db.Column(db.Integer)
    total_score = db.Column(db.Integer)
    responses = db.Column(db.Text)  # JSON string of responses
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, nullable=False)
    module_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='not_started')  # not_started, in_progress, completed
    score = db.Column(db.Integer, default=0)
    time_spent = db.Column(db.Integer, default=0)  # in minutes
    completed_at = db.Column(db.DateTime)

class SimulationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    simulation_type = db.Column(db.String(50), nullable=False)  # phishing, pretexting, etc.
    scenario_id = db.Column(db.Integer, nullable=False)
    user_choice = db.Column(db.String(50), nullable=False)
    correct_choice = db.Column(db.String(50), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    time_taken = db.Column(db.Integer)  # in seconds
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# New Models for Knowledge Check System
class KnowledgeCheckQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # a, b, c, or d
    explanation = db.Column(db.Text, nullable=False)
    question_set = db.Column(db.Integer, default=1)  # Different sets of questions
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ModuleAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, nullable=False)
    attempt_number = db.Column(db.Integer, default=1)
    score = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, default=False)
    questions_used = db.Column(db.Text)  # JSON string of question IDs used
    answers_given = db.Column(db.Text)  # JSON string of answers
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class FinalAssessmentQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    question_set = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class FinalAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    attempt_number = db.Column(db.Integer, default=1)
    score = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, default=False)
    questions_used = db.Column(db.Text)  # JSON string of question IDs used
    answers_given = db.Column(db.Text)  # JSON string of answers
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class FeedbackSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    overall_rating = db.Column(db.Integer, nullable=False)
    relevance = db.Column(db.Integer, nullable=False)
    simulations_helpful = db.Column(db.Integer, nullable=False)
    confidence = db.Column(db.Integer, nullable=False)
    improvements = db.Column(db.Text)
    current_situation_help = db.Column(db.Text)
    recommendation = db.Column(db.String(20), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-db')
def test_db():
    try:
        # Test database connection
        user_count = User.query.count()
        return jsonify({'status': 'success', 'user_count': user_count, 'message': 'Database is working'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        errors = {}
        form_data = {
            'username': username,
            'password': password
        }
        
        user = User.query.filter_by(username=username).first()
        
        # Check if account is locked
        if user and user.locked_until and user.locked_until > datetime.utcnow():
            remaining_time = user.locked_until - datetime.utcnow()
            minutes = int(remaining_time.total_seconds() / 60)
            errors['general'] = f'Account temporarily locked. Try again in {minutes} minutes.'
            return render_template('login.html', errors=errors, form_data=form_data)
        
        # Check if account is active
        if user and not user.is_active:
            errors['general'] = 'Account is deactivated. Contact administrator.'
            return render_template('login.html', errors=errors, form_data=form_data)
        
        if user and check_password_hash(user.password_hash, password):
            # Reset failed login attempts on successful login
            user.failed_login_attempts = 0
            user.locked_until = None
            user.last_login = datetime.now(datetime.UTC)
            db.session.commit()
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            # Increment failed login attempts
            if user:
                user.failed_login_attempts += 1
                # Lock account after 5 failed attempts for 30 minutes
                if user.failed_login_attempts >= 5:
                    user.locked_until = datetime.utcnow() + timedelta(minutes=30)
                db.session.commit()
            
            errors['general'] = 'Invalid username or password'
            return render_template('login.html', errors=errors, form_data=form_data)
    
    return render_template('login.html')

def validate_username(username):
    """Validate username requirements"""
    if len(username) < 8:
        return False, "Username must be at least 8 characters long"
    if not username.isalnum():
        return False, "Username must contain only letters and numbers"
    return True, ""

def validate_email(email):
    """Validate email format (allow any domain for now)"""
    import re
    email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if not re.match(email_pattern, email, re.IGNORECASE):
        return False, "Invalid email address"
    return True, ""

def validate_password(password):
    """Validate password requirements"""
    if len(password) < 12:
        return False, "Password must be at least 12 characters long"
    
    has_capital = any(c.isupper() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    has_number = any(c.isdigit() for c in password)
    
    if not has_capital:
        return False, "Password must contain at least 1 capital letter"
    if not has_special:
        return False, "Password must contain at least 1 special character"
    if not has_number:
        return False, "Password must contain at least 1 number"
    
    return True, ""

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        specialization = request.form.get('specialization', '')
        year_level = request.form.get('year_level', '')
        cybersecurity_experience = request.form.get('cybersecurity_experience') == 'on'
        
        errors = {}
        form_data = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'specialization': specialization,
            'year_level': year_level,
            'cybersecurity_experience': cybersecurity_experience
        }
        
        # Validate username
        username_valid, username_error = validate_username(username)
        if not username_valid:
            errors['username'] = username_error
        
        # Validate email
        email_valid, email_error = validate_email(email)
        if not email_valid:
            errors['email'] = email_error
        
        # Validate password
        password_valid, password_error = validate_password(password)
        if not password_valid:
            errors['password'] = password_error
        
        # Check password confirmation
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            errors['username'] = 'Username already exists'
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            errors['email'] = 'Email already registered'
        
        # Validate required fields
        if not specialization or specialization == '':
            errors['specialization'] = 'Please select your IT specialization'
        
        if not year_level or year_level == '':
            errors['year_level'] = 'Please select your year level'
        
        # If there are errors, return the form with errors and preserved data
        if errors:
            return render_template('register.html', errors=errors, form_data=form_data)
        
        # Set default full_name from username (can be changed in profile later)
        full_name = username.title()  # Use username as default full name
        
        try:
            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password),
                full_name=full_name,
                specialization=specialization,
                year_level=year_level,
                cybersecurity_experience=cybersecurity_experience
            )
            
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Registration failed: {str(e)}')
            return render_template('register.html', form_data=form_data)
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get user progress
    progress = Progress.query.filter_by(user_id=current_user.id).all()
    completed_modules = len([p for p in progress if p.status == 'completed'])
    total_score = sum([p.score for p in progress])
    
    # Calculate average score
    average_score = round(total_score / max(completed_modules, 1), 1)
    
    # Get recent simulation results
    recent_simulations = SimulationResult.query.filter_by(user_id=current_user.id).order_by(SimulationResult.completed_at.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                         progress=progress,
                         completed_modules=completed_modules,
                         total_score=total_score,
                         average_score=average_score,
                         recent_simulations=recent_simulations)

@app.route('/assessment/<assessment_type>', methods=['GET', 'POST'])
@login_required
def assessment(assessment_type):
    if request.method == 'POST':
        data = request.get_json()
        
        # Calculate scores based on responses
        knowledge_score = calculate_knowledge_score(data.get('knowledge_responses', {}))
        attitude_score = calculate_attitude_score(data.get('attitude_responses', {}))
        behavioral_score = calculate_behavioral_score(data.get('behavioral_responses', {}))
        total_score = (knowledge_score + attitude_score + behavioral_score) // 3
        
        assessment = Assessment(
            user_id=current_user.id,
            assessment_type=assessment_type,
            knowledge_score=knowledge_score,
            attitude_score=attitude_score,
            behavioral_score=behavioral_score,
            total_score=total_score,
            responses=json.dumps(data)
        )
        
        db.session.add(assessment)
        db.session.commit()
        
        return jsonify({'success': True, 'total_score': total_score})
    
    return render_template(f'assessment_{assessment_type}.html')

@app.route('/module/<int:module_id>')
@login_required
def module(module_id):
    module = Module.query.get_or_404(module_id)
    
    # Check if user has access to this module
    if module_id > 1:
        prev_progress = Progress.query.filter_by(
            user_id=current_user.id, 
            module_id=module_id-1
        ).first()
        if not prev_progress or prev_progress.status != 'completed':
            flash('Please complete the previous module first')
            return redirect(url_for('dashboard'))
    
    # Get or create progress record
    progress = Progress.query.filter_by(
        user_id=current_user.id, 
        module_id=module_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            module_id=module_id,
            module_name=module.name,
            status='in_progress'
        )
        db.session.add(progress)
        db.session.commit()
    
    return render_template('module.html', module=module, progress=progress)

@app.route('/module/<int:module_id>/knowledge-check')
@login_required
def module_knowledge_check(module_id):
    module = Module.query.get_or_404(module_id)
    
    # Check if user has completed the module content
    progress = Progress.query.filter_by(
        user_id=current_user.id, 
        module_id=module_id
    ).first()
    
    if not progress or progress.status == 'not_started':
        flash('Please complete the module content first')
        return redirect(url_for('module', module_id=module_id))
    
    # Get assessment rules
    rules = {
        'passing_rate': 80,
        'questions_per_attempt': 5,
        'unlimited_retakes': True,
        'randomized_questions': True
    }
    
    return render_template('module_knowledge_check.html', 
                         module=module, 
                         progress=progress, 
                         rules=rules)

@app.route('/api/module-assessment/<int:module_id>', methods=['POST'])
@login_required
def submit_module_assessment(module_id):
    data = request.get_json()
    answers = data.get('answers', {})
    
    # Get questions used in this attempt
    questions_used = data.get('questions_used', [])
    
    # Calculate score
    correct_answers = 0
    total_questions = len(questions_used)
    
    for question_id, answer in answers.items():
        question = KnowledgeCheckQuestion.query.get(question_id)
        if question and answer == question.correct_answer:
            correct_answers += 1
    
    score = int((correct_answers / total_questions) * 100)
    passed = score >= 80
    
    # Get attempt number
    previous_attempts = ModuleAssessment.query.filter_by(
        user_id=current_user.id,
        module_id=module_id
    ).count()
    attempt_number = previous_attempts + 1
    
    # Create assessment record
    assessment = ModuleAssessment(
        user_id=current_user.id,
        module_id=module_id,
        attempt_number=attempt_number,
        score=score,
        passed=passed,
        questions_used=json.dumps(questions_used),
        answers_given=json.dumps(answers)
    )
    
    db.session.add(assessment)
    
    # If passed, mark module as completed
    if passed:
        progress = Progress.query.filter_by(
            user_id=current_user.id,
            module_id=module_id
        ).first()
        if progress:
            progress.status = 'completed'
            progress.score = score
            progress.completed_at = datetime.utcnow()
            current_user.modules_completed += 1
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'score': score,
        'passed': passed,
        'attempt_number': attempt_number,
        'correct_answers': correct_answers,
        'total_questions': total_questions
    })

@app.route('/api/get-module-questions/<int:module_id>')
@login_required
def get_module_questions(module_id):
    # Get all questions for this module
    all_questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
    
    if not all_questions:
        return jsonify({'error': 'No questions available for this module'}), 404
    
    # Get previous attempts to avoid repeating questions
    previous_attempts = ModuleAssessment.query.filter_by(
        user_id=current_user.id,
        module_id=module_id
    ).all()
    
    used_question_ids = set()
    for attempt in previous_attempts:
        used_ids = json.loads(attempt.questions_used)
        used_question_ids.update(used_ids)
    
    # Filter out previously used questions
    available_questions = [q for q in all_questions if q.id not in used_question_ids]
    
    # If not enough questions, reset and use all questions
    if len(available_questions) < 5:
        available_questions = all_questions
    
    # Randomly select 5 questions
    selected_questions = random.sample(available_questions, min(5, len(available_questions)))
    
    questions_data = []
    for question in selected_questions:
        questions_data.append({
            'id': question.id,
            'question': question.question_text,
            'options': {
                'a': question.option_a,
                'b': question.option_b,
                'c': question.option_c,
                'd': question.option_d
            },
            'explanation': question.explanation
        })
    
    return jsonify({
        'questions': questions_data,
        'question_ids': [q.id for q in selected_questions]
    })

@app.route('/final-assessment')
@login_required
def final_assessment():
    # Check if all modules are completed
    progress = Progress.query.filter_by(user_id=current_user.id).all()
    completed_modules = len([p for p in progress if p.status == 'completed'])
    
    if completed_modules < 8:
        flash('You must complete all 8 modules before taking the final assessment')
        return redirect(url_for('dashboard'))
    
    # Check if user has already passed
    if current_user.final_assessment_passed:
        flash('You have already passed the final assessment')
        return redirect(url_for('dashboard'))
    
    # Check attempt limit
    if current_user.final_assessment_attempts >= 3:
        flash('You have reached the maximum attempts for the final assessment. You must repeat all modules.')
        return redirect(url_for('dashboard'))
    
    rules = {
        'passing_rate': 80,
        'questions_per_attempt': 10,
        'max_attempts': 3,
        'current_attempts': current_user.final_assessment_attempts,
        'randomized_questions': True
    }
    
    return render_template('final_assessment.html', rules=rules)

@app.route('/api/final-assessment', methods=['POST'])
@login_required
def submit_final_assessment():
    data = request.get_json()
    answers = data.get('answers', {})
    
    # Get questions used in this attempt
    questions_used = data.get('questions_used', [])
    
    # Calculate score
    correct_answers = 0
    total_questions = len(questions_used)
    
    for question_id, answer in answers.items():
        question = FinalAssessmentQuestion.query.get(question_id)
        if question and answer == question.correct_answer:
            correct_answers += 1
    
    score = int((correct_answers / total_questions) * 100)
    passed = score >= 80
    
    # Update attempt count
    current_user.final_assessment_attempts += 1
    
    # Create assessment record
    assessment = FinalAssessment(
        user_id=current_user.id,
        attempt_number=current_user.final_assessment_attempts,
        score=score,
        passed=passed,
        questions_used=json.dumps(questions_used),
        answers_given=json.dumps(answers)
    )
    
    db.session.add(assessment)
    
    if passed:
        current_user.final_assessment_passed = True
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'score': score,
        'passed': passed,
        'attempt_number': current_user.final_assessment_attempts,
        'correct_answers': correct_answers,
        'total_questions': total_questions
    })

@app.route('/api/get-final-questions')
@login_required
def get_final_questions():
    # Get all final assessment questions
    all_questions = FinalAssessmentQuestion.query.all()
    
    if not all_questions:
        return jsonify({'error': 'No final assessment questions available'}), 404
    
    # Get previous attempts to avoid repeating questions
    previous_attempts = FinalAssessment.query.filter_by(user_id=current_user.id).all()
    
    used_question_ids = set()
    for attempt in previous_attempts:
        used_ids = json.loads(attempt.questions_used)
        used_question_ids.update(used_ids)
    
    # Filter out previously used questions
    available_questions = [q for q in all_questions if q.id not in used_question_ids]
    
    # If not enough questions, use all questions
    if len(available_questions) < 10:
        available_questions = all_questions
    
    # Randomly select 10 questions
    selected_questions = random.sample(available_questions, min(10, len(available_questions)))
    
    questions_data = []
    for question in selected_questions:
        questions_data.append({
            'id': question.id,
            'question': question.question_text,
            'options': {
                'a': question.option_a,
                'b': question.option_b,
                'c': question.option_c,
                'd': question.option_d
            },
            'explanation': question.explanation
        })
    
    return jsonify({
        'questions': questions_data,
        'question_ids': [q.id for q in selected_questions]
    })

@app.route('/simulation/<simulation_type>')
@login_required
def simulation(simulation_type):
    return render_template(f'simulation_{simulation_type}.html')

@app.route('/api/simulation/result', methods=['POST'])
@login_required
def simulation_result():
    data = request.get_json()
    
    result = SimulationResult(
        user_id=current_user.id,
        simulation_type=data['simulation_type'],
        scenario_id=data['scenario_id'],
        user_choice=data['user_choice'],
        correct_choice=data['correct_choice'],
        is_correct=data['is_correct'],
        time_taken=data.get('time_taken', 0)
    )
    
    db.session.add(result)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/progress/update', methods=['POST'])
@login_required
def update_progress():
    data = request.get_json()
    
    progress = Progress.query.filter_by(
        user_id=current_user.id,
        module_id=data['module_id']
    ).first()
    
    if progress:
        progress.status = data['status']
        progress.score = data.get('score', progress.score)
        progress.time_spent = data.get('time_spent', progress.time_spent)
        
        if data['status'] == 'completed':
            progress.completed_at = datetime.utcnow()
            current_user.modules_completed += 1
        
        db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/submit-feedback', methods=['POST'])
@login_required
def submit_feedback():
    data = request.get_json()
    
    # Check if user has already submitted feedback
    existing_feedback = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
    if existing_feedback:
        return jsonify({'success': False, 'error': 'Feedback already submitted'})
    
    # Create new feedback survey entry
    feedback = FeedbackSurvey(
        user_id=current_user.id,
        overall_rating=int(data['overall_rating']),
        relevance=int(data['relevance']),
        simulations_helpful=int(data['simulations_helpful']),
        confidence=int(data['confidence']),
        improvements=data.get('improvements', ''),
        current_situation_help=data.get('current_situation_help', ''),
        recommendation=data['recommendation']
    )
    
    db.session.add(feedback)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if 'update_profile' in request.form:
            full_name = request.form.get('full_name', '').strip()
            birthday = request.form.get('birthday')
            address = request.form.get('address', '').strip()
            
            errors = {}
            form_data = {
                'full_name': full_name,
                'birthday': birthday,
                'address': address
            }
            
            if not full_name:
                errors['full_name'] = 'Full Name is required!'
            
            # Handle profile picture upload
            if 'profile_picture' in request.files:
                file = request.files['profile_picture']
                if file and file.filename != '':
                    if file and allowed_file(file.filename):
                        # Create upload folder if it doesn't exist
                        create_upload_folder()
                        
                        # Generate unique filename
                        filename = secure_filename(file.filename)
                        file_extension = filename.rsplit('.', 1)[1].lower()
                        unique_filename = f"{current_user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_extension}"
                        
                        # Save file
                        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                        file.save(file_path)
                        
                        # Update user's profile picture
                        current_user.profile_picture = unique_filename
                    else:
                        errors['profile_picture'] = 'Invalid file type. Please upload PNG, JPG, JPEG, GIF, or WEBP files only.'
            
            if errors:
                return render_template('profile.html', user=current_user, errors=errors, form_data=form_data)
            
            try:
                current_user.full_name = full_name
                if birthday:
                    current_user.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
                else:
                    current_user.birthday = None
                current_user.address = address if address else None
                db.session.commit()
                flash('Profile updated successfully!', 'success')
                return redirect(url_for('profile'))
            except Exception as e:
                db.session.rollback()
                flash(f'Profile update failed: {str(e)}', 'danger')
                return render_template('profile.html', user=current_user, form_data=form_data)
        
        elif 'change_password' in request.form:
            old_password = request.form.get('old_password', '')
            new_password = request.form.get('new_password', '')
            confirm_new_password = request.form.get('confirm_new_password', '')
            
            errors = {}
            form_data = {
                'new_password': new_password,
                'confirm_new_password': confirm_new_password
            }
            
            if not check_password_hash(current_user.password_hash, old_password):
                errors['old_password'] = 'Incorrect old password!'
            
            password_valid, password_error = validate_password(new_password)
            if not password_valid:
                errors['new_password'] = password_error
            
            if new_password != confirm_new_password:
                errors['confirm_new_password'] = 'New passwords do not match!'
            
            if errors:
                return render_template('profile.html', user=current_user, errors=errors, form_data=form_data)
            
            try:
                current_user.password_hash = generate_password_hash(new_password)
                db.session.commit()
                flash('Password changed successfully!', 'success')
                return redirect(url_for('profile'))
            except Exception as e:
                db.session.rollback()
                flash(f'Password change failed: {str(e)}', 'danger')
                return render_template('profile.html', user=current_user, form_data=form_data)
    
    return render_template('profile.html', user=current_user)

@app.route('/generate-certificate')
@login_required
def generate_certificate():
    # Check if user has passed final assessment
    if not current_user.final_assessment_passed:
        flash('You must pass the final assessment to generate a certificate', 'warning')
        return redirect(url_for('dashboard'))
    
    # Check if user has submitted feedback
    feedback = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
    if not feedback:
        flash('You must complete the feedback survey before generating a certificate', 'warning')
        return redirect(url_for('final_assessment'))
    
    # Generate certificate data
    certificate_data = {
        'student_name': current_user.full_name,
        'username': current_user.username,
        'specialization': current_user.specialization,
        'year_level': current_user.year_level,
        'completion_date': datetime.now().strftime('%B %d, %Y'),
        'score': current_user.total_score,
        'modules_completed': current_user.modules_completed
    }
    
    return render_template('certificate.html', certificate=certificate_data)

@app.route('/admin')
@login_required
def admin():
    if current_user.username != 'admin':
        flash('Access denied')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    assessments = Assessment.query.all()
    progress = Progress.query.all()
    
    return render_template('admin.html', users=users, assessments=assessments, progress=progress)

# Security helper functions
def add_security_headers(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://code.jquery.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' data:; font-src 'self' https://cdn.jsdelivr.net;"
    return response

def sanitize_input(data):
    """Sanitize user input to prevent XSS"""
    if isinstance(data, str):
        import html
        return html.escape(data.strip())
    return data

# Rate limiting
from collections import defaultdict
import time

request_counts = defaultdict(list)
MAX_REQUESTS = 100  # Max requests per minute
RATE_LIMIT_WINDOW = 60  # 1 minute window

def check_rate_limit(ip):
    """Check if IP has exceeded rate limit"""
    current_time = time.time()
    # Remove old requests outside the window
    request_counts[ip] = [req_time for req_time in request_counts[ip] 
                         if current_time - req_time < RATE_LIMIT_WINDOW]
    
    if len(request_counts[ip]) >= MAX_REQUESTS:
        return False
    
    request_counts[ip].append(current_time)
    return True

# Role-based access control decorators
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Access denied. Admin privileges required.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def trainer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['trainer', 'admin']:
            flash('Access denied. Trainer privileges required.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def student_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['student', 'trainer', 'admin']:
            flash('Access denied. Student privileges required.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# File upload helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_upload_folder():
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

# Security middleware
@app.before_request
def before_request():
    """Security middleware - runs before each request"""
    # Rate limiting
    if not check_rate_limit(request.remote_addr):
        return jsonify({'error': 'Rate limit exceeded'}), 429
    
    # Sanitize form data
    if request.method == 'POST':
        for key, value in request.form.items():
            if isinstance(value, str):
                request.form = request.form.copy()
                request.form[key] = sanitize_input(value)

@app.after_request
def after_request(response):
    """Add security headers after each request"""
    return add_security_headers(response)

# Helper functions
def calculate_knowledge_score(responses):
    # Implement knowledge scoring logic
    score = 0
    correct_answers = {
        'q4': 'b',  # Social engineering definition
        'q6': 'c',  # Suspicious email response
        # Add more correct answers
    }
    
    for question, answer in responses.items():
        if question in correct_answers and answer == correct_answers[question]:
            score += 10
    
    return min(score, 100)

def calculate_attitude_score(responses):
    # Implement attitude scoring logic
    score = 0
    for question, answer in responses.items():
        if isinstance(answer, int):
            score += answer * 20  # Likert scale 1-5
    
    return min(score // len(responses) if responses else 0, 100)

def calculate_behavioral_score(responses):
    # Implement behavioral scoring logic
    score = 0
    safe_behaviors = {
        'q9': 'always',  # Verify email addresses
        'q10': 'c',      # Contact IT support
        'q11': 'no'      # Never share passwords
    }
    
    for question, answer in responses.items():
        if question in safe_behaviors and answer == safe_behaviors[question]:
            score += 15
    
    return min(score, 100)

# Initialize database
def init_db():
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("Database tables created successfully")
            
            # Verify tables exist by checking if User table has any columns
            try:
                # This will fail if the table doesn't exist
                User.query.first()
                print("Database verification successful")
            except Exception as e:
                print(f"Database verification error: {e}")
                # Recreate all tables
                db.drop_all()
                db.create_all()
                print("Database tables recreated successfully")
            
            # Create default modules if they don't exist
            if not Module.query.first():
                modules = [
                {
                    'name': 'Introduction to Social Engineering',
                    'description': 'Understanding human vulnerabilities and psychological manipulation',
                    'content': '''
                    <h4>What is Social Engineering?</h4>
                    <p>Social engineering is the art of manipulating people to gain unauthorized access to systems, networks, or physical locations. Unlike technical hacking, social engineering relies on human psychology and trust.</p>
                    
                    <h4>Key Concepts:</h4>
                    <ul>
                        <li><strong>Human Factor:</strong> The weakest link in cybersecurity is often human behavior</li>
                        <li><strong>Trust Exploitation:</strong> Attackers exploit natural human tendency to trust</li>
                        <li><strong>Authority:</strong> People tend to comply with perceived authority figures</li>
                        <li><strong>Urgency:</strong> Creating time pressure to bypass normal security procedures</li>
                    </ul>
                    
                    <h4>Why Social Engineering Works:</h4>
                    <p>Social engineering attacks are successful because they target fundamental human behaviors:</p>
                    <ul>
                        <li>Desire to be helpful</li>
                        <li>Fear of getting in trouble</li>
                        <li>Respect for authority</li>
                        <li>Natural curiosity</li>
                        <li>Greed or desire for reward</li>
                    </ul>
                    
                    <h4>Real-World Impact:</h4>
                    <p>Social engineering attacks have led to:</p>
                    <ul>
                        <li>Major data breaches affecting millions of people</li>
                        <li>Financial losses in billions of dollars</li>
                        <li>Compromise of critical infrastructure</li>
                        <li>Damage to organizational reputation</li>
                    </ul>
                    ''',
                    'order': 1
                },
                {
                    'name': 'Types of Social Engineering Attacks',
                    'description': 'Phishing, pretexting, baiting, and other manipulation techniques',
                    'content': '''
                    <h4>Phishing Attacks</h4>
                    <p>Phishing is the most common form of social engineering, using fraudulent emails, messages, or websites to steal sensitive information.</p>
                    
                    <h5>Types of Phishing:</h5>
                    <ul>
                        <li><strong>Email Phishing:</strong> Mass emails sent to many recipients</li>
                        <li><strong>Spear Phishing:</strong> Targeted emails to specific individuals</li>
                        <li><strong>Whaling:</strong> Attacks targeting high-level executives</li>
                        <li><strong>Vishing:</strong> Voice-based phishing using phone calls</li>
                        <li><strong>Smishing:</strong> SMS-based phishing attacks</li>
                    </ul>
                    
                    <h4>Pretexting</h4>
                    <p>Creating a fabricated scenario to obtain information or access. Attackers often impersonate:</p>
                    <ul>
                        <li>IT support staff</li>
                        <li>Bank representatives</li>
                        <li>Government officials</li>
                        <li>Co-workers or managers</li>
                    </ul>
                    
                    <h4>Baiting</h4>
                    <p>Using physical media or digital lures to entice victims:</p>
                    <ul>
                        <li>USB drives left in public places</li>
                        <li>Fake software downloads</li>
                        <li>Malicious QR codes</li>
                        <li>Infected physical devices</li>
                    </ul>
                    
                    <h4>Quid Pro Quo</h4>
                    <p>Offering a service in exchange for information or access:</p>
                    <ul>
                        <li>Free technical support in exchange for login credentials</li>
                        <li>Software updates requiring password input</li>
                        <li>Security audits requiring system access</li>
                    </ul>
                    ''',
                    'order': 2
                },
                {
                    'name': 'Identifying Red Flags',
                    'description': 'Recognizing warning signs and suspicious behavior',
                    'content': '''
                    <h4>Email Red Flags</h4>
                    <p>Common indicators of phishing emails:</p>
                    <ul>
                        <li><strong>Urgency:</strong> "Act now or your account will be closed"</li>
                        <li><strong>Authority:</strong> Impersonating executives or IT staff</li>
                        <li><strong>Scarcity:</strong> "Limited time offer" or "Exclusive access"</li>
                        <li><strong>Generic Greetings:</strong> "Dear User" instead of your name</li>
                        <li><strong>Suspicious Links:</strong> Hover to reveal different URLs</li>
                        <li><strong>Poor Grammar:</strong> Spelling and grammar errors</li>
                        <li><strong>Unusual Requests:</strong> Asking for passwords or sensitive data</li>
                    </ul>
                    
                    <h4>Phone Call Red Flags</h4>
                    <ul>
                        <li>Caller ID spoofing</li>
                        <li>High-pressure tactics</li>
                        <li>Requests for immediate action</li>
                        <li>Asking for passwords or PINs</li>
                        <li>Threatening consequences</li>
                    </ul>
                    
                    <h4>Physical Red Flags</h4>
                    <ul>
                        <li>Unauthorized personnel in restricted areas</li>
                        <li>People following you through secure doors</li>
                        <li>Unusual requests for access</li>
                        <li>Devices left in public areas</li>
                    </ul>
                    
                    <h4>Social Media Red Flags</h4>
                    <ul>
                        <li>Fake profiles with limited information</li>
                        <li>Requests from unknown connections</li>
                        <li>Phishing links in messages</li>
                        <li>Fake job offers or opportunities</li>
                    </ul>
                    ''',
                    'order': 3
                },
                {
                    'name': 'Defense Strategies',
                    'description': 'Best practices for protecting against attacks',
                    'content': '''
                    <h4>Verification Procedures</h4>
                    <p>Always verify the identity of people requesting information:</p>
                    <ul>
                        <li><strong>Call Back:</strong> Use known phone numbers, not provided ones</li>
                        <li><strong>Email Verification:</strong> Contact through official channels</li>
                        <li><strong>In-Person Verification:</strong> Check ID badges and credentials</li>
                        <li><strong>Multi-Factor Authentication:</strong> Use additional verification methods</li>
                    </ul>
                    
                    <h4>Password Security</h4>
                    <ul>
                        <li>Never share passwords with anyone</li>
                        <li>Use unique passwords for each account</li>
                        <li>Enable two-factor authentication</li>
                        <li>Use password managers for secure storage</li>
                        <li>Regular password updates</li>
                    </ul>
                    
                    <h4>Email Security</h4>
                    <ul>
                        <li>Don't click suspicious links</li>
                        <li>Hover over links to check URLs</li>
                        <li>Don't open unexpected attachments</li>
                        <li>Use spam filters</li>
                        <li>Report suspicious emails to IT</li>
                    </ul>
                    
                    <h4>Physical Security</h4>
                    <ul>
                        <li>Don't let others follow you through secure doors</li>
                        <li>Challenge unfamiliar people in restricted areas</li>
                        <li>Don't plug in unknown USB devices</li>
                        <li>Lock your computer when away</li>
                        <li>Secure your workspace</li>
                    </ul>
                    
                    <h4>Incident Reporting</h4>
                    <ul>
                        <li>Report suspicious activity immediately</li>
                        <li>Document all details of the incident</li>
                        <li>Follow organizational procedures</li>
                        <li>Preserve evidence if possible</li>
                    </ul>
                    ''',
                    'order': 4
                },
                {
                    'name': 'Real-world Case Studies',
                    'description': 'Analysis of actual social engineering incidents',
                    'content': '''
                    <h4>Case Study 1: Target Data Breach (2013)</h4>
                    <p><strong>Attack Method:</strong> HVAC vendor compromise</p>
                    <p><strong>Impact:</strong> 40 million credit card records stolen</p>
                    <p><strong>Lesson:</strong> Third-party vendors can be entry points for attacks</p>
                    
                    <h4>Case Study 2: Google and Facebook (2017)</h4>
                    <p><strong>Attack Method:</strong> Fake invoice scam</p>
                    <p><strong>Impact:</strong> $100+ million stolen</p>
                    <p><strong>Lesson:</strong> Even large companies can fall victim to social engineering</p>
                    
                    <h4>Case Study 3: Twitter Hack (2020)</h4>
                    <p><strong>Attack Method:</strong> Phone spear phishing</p>
                    <p><strong>Impact:</strong> High-profile accounts compromised</p>
                    <p><strong>Lesson:</strong> Phone-based attacks can be highly effective</p>
                    
                    <h4>Case Study 4: Ubiquiti Networks (2021)</h4>
                    <p><strong>Attack Method:</strong> Email impersonation</p>
                    <p><strong>Impact:</strong> $46 million stolen</p>
                    <p><strong>Lesson:</strong> Email security is critical for financial transactions</p>
                    
                    <h4>Common Patterns in These Attacks:</h4>
                    <ul>
                        <li>Exploitation of trust relationships</li>
                        <li>Use of authority and urgency</li>
                        <li>Targeting of human weaknesses</li>
                        <li>Lack of proper verification procedures</li>
                    </ul>
                    ''',
                    'order': 5
                },
                {
                    'name': 'Advanced Techniques',
                    'description': 'Sophisticated attack methods and countermeasures',
                    'content': '''
                    <h4>Advanced Phishing Techniques</h4>
                    <p>Modern attackers use sophisticated methods:</p>
                    <ul>
                        <li><strong>Clone Phishing:</strong> Copying legitimate emails with malicious links</li>
                        <li><strong>Evil Twin Attacks:</strong> Fake WiFi networks to capture data</li>
                        <li><strong>Watering Hole Attacks:</strong> Compromising websites frequented by targets</li>
                        <li><strong>Man-in-the-Middle:</strong> Intercepting communications</li>
                    </ul>
                    
                    <h4>Deepfake Technology</h4>
                    <p>AI-generated content used in attacks:</p>
                    <ul>
                        <li>Fake voice calls from executives</li>
                        <li>Video calls with impersonated leaders</li>
                        <li>Audio manipulation for voice phishing</li>
                        <li>Countermeasures: Multi-factor verification</li>
                    </ul>
                    
                    <h4>Social Media Intelligence</h4>
                    <p>Attackers gather information from:</p>
                    <ul>
                        <li>LinkedIn profiles and connections</li>
                        <li>Facebook posts and photos</li>
                        <li>Twitter activity and interests</li>
                        <li>Company websites and press releases</li>
                    </ul>
                    
                    <h4>Countermeasures</h4>
                    <ul>
                        <li>Regular security awareness training</li>
                        <li>Multi-factor authentication everywhere</li>
                        <li>Zero-trust security model</li>
                        <li>Regular security assessments</li>
                        <li>Incident response planning</li>
                    </ul>
                    ''',
                    'order': 6
                },
                {
                    'name': 'Incident Response',
                    'description': 'How to respond when attacks are detected',
                    'content': '''
                    <h4>Immediate Response Steps</h4>
                    <p>When you suspect a social engineering attack:</p>
                    <ol>
                        <li><strong>Stop:</strong> Don't provide any more information</li>
                        <li><strong>Document:</strong> Record all details of the interaction</li>
                        <li><strong>Report:</strong> Contact your IT security team immediately</li>
                        <li><strong>Secure:</strong> Change passwords and enable 2FA</li>
                        <li><strong>Monitor:</strong> Watch for suspicious activity</li>
                    </ol>
                    
                    <h4>What to Document</h4>
                    <ul>
                        <li>Date and time of the incident</li>
                        <li>Method of contact (email, phone, in-person)</li>
                        <li>Information requested or provided</li>
                        <li>Attacker's claimed identity</li>
                        <li>Any suspicious behavior observed</li>
                    </ul>
                    
                    <h4>Reporting Procedures</h4>
                    <ul>
                        <li>Follow your organization's incident response plan</li>
                        <li>Contact IT security immediately</li>
                        <li>Preserve any evidence (emails, messages, etc.)</li>
                        <li>Don't delete suspicious communications</li>
                        <li>Cooperate with security investigations</li>
                    </ul>
                    
                    <h4>Recovery Steps</h4>
                    <ul>
                        <li>Change all passwords immediately</li>
                        <li>Enable two-factor authentication</li>
                        <li>Monitor financial accounts</li>
                        <li>Check for unauthorized access</li>
                        <li>Update security settings</li>
                    </ul>
                    
                    <h4>Prevention for Future</h4>
                    <ul>
                        <li>Learn from the incident</li>
                        <li>Share lessons with colleagues</li>
                        <li>Update security procedures</li>
                        <li>Participate in security training</li>
                        <li>Stay vigilant</li>
                    </ul>
                    ''',
                    'order': 7
                },
                {
                    'name': 'Final Assessment',
                    'description': 'Comprehensive evaluation of learning outcomes',
                    'content': '''
                    <h4>Module Completion Summary</h4>
                    <p>Congratulations on completing the Social Engineering Awareness program! This final module will assess your understanding of all concepts covered.</p>
                    
                    <h4>What You've Learned:</h4>
                    <ul>
                        <li>Understanding of social engineering techniques</li>
                        <li>Ability to identify red flags and warning signs</li>
                        <li>Knowledge of defense strategies and best practices</li>
                        <li>Familiarity with real-world case studies</li>
                        <li>Understanding of advanced attack methods</li>
                        <li>Knowledge of proper incident response procedures</li>
                    </ul>
                    
                    <h4>Final Assessment Components:</h4>
                    <ol>
                        <li><strong>Knowledge Test:</strong> Multiple choice questions on all topics</li>
                        <li><strong>Scenario Analysis:</strong> Identify social engineering attempts</li>
                        <li><strong>Practical Exercise:</strong> Apply defense strategies</li>
                        <li><strong>Attitude Assessment:</strong> Measure awareness and confidence</li>
                    </ol>
                    
                    <h4>Certification Requirements:</h4>
                    <ul>
                        <li>Complete all 8 learning modules</li>
                        <li>Achieve minimum 70% on final assessment</li>
                        <li>Participate in at least 3 simulation exercises</li>
                        <li>Demonstrate understanding of key concepts</li>
                    </ul>
                    
                    <h4>Next Steps:</h4>
                    <ul>
                        <li>Take the final comprehensive assessment</li>
                        <li>Review any areas of weakness</li>
                        <li>Download your completion certificate</li>
                        <li>Continue practicing security awareness</li>
                        <li>Share knowledge with colleagues</li>
                    </ul>
                    
                    <div class="alert alert-info">
                        <strong>Ready for Assessment?</strong> Click the button below to begin your final evaluation.
                    </div>
                    ''',
                    'order': 8
                }
            ]
            
            for module_data in modules:
                module = Module(**module_data)
                db.session.add(module)
            
            db.session.commit()
        except Exception as e:
            print(f"Database initialization error: {e}")

if __name__ == '__main__':
    # Initialize database
    init_db()
    # Use environment variables for production deployment
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port) 