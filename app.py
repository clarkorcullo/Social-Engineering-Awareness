"""
Refactored Social Engineering Awareness Program
Main application file using OOP principles and design patterns
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.middleware.proxy_fix import ProxyFix
import os
from datetime import datetime, timedelta
import random
import json
import secrets

# Import our OOP components
from data_models.base_models import db
from data_models import *
from data_models.user_models import User, PasswordResetToken
from business_services import *
from helper_utilities.data_structures import *

# Initialize Flask app
app = Flask(__name__)
# Use environment secret in production; fallback for local dev
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

# Database configuration
if os.environ.get('RENDER'):
    db_path = '/tmp/social_engineering_awareness.db'
else:
    db_path = 'social_engineering_awareness.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Reverse proxy and cookie settings for Render/HTTPS
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
if os.environ.get('RENDER'):
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['REMEMBER_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['REMEMBER_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['REMEMBER_COOKIE_HTTPONLY'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize services
user_service = UserService()
assessment_service = AssessmentService()
simulation_service = SimulationService()

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return User.get_by_id(int(user_id))

# Application Factory Pattern
def create_app():
    """Application factory for better testing and configuration"""
    with app.app_context():
        init_database()
    return app

def init_database():
    """Initialize database with all models"""
    try:
        db.create_all()
        create_default_data()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization error: {e}")

def create_default_data():
    """Create default data if it doesn't exist"""
    try:
        # Create default admin if not exists (use 'administrator' with strong password)
        admin_user = User.get_by_username('administrator')
        if not admin_user:
            admin_data = {
                'username': 'administrator',
                'email': os.environ.get('ADMIN_EMAIL', 'admin@mmdc.edu.ph'),
                'password': os.environ.get('ADMIN_PASSWORD', 'Admin123!@#'),
                'full_name': 'System Administrator',
                'specialization': 'Information Technology',
                'year_level': '4th Year'
            }
            user_service.create_user(admin_data)
            print("✅ Admin user created (administrator)")
        else:
            print("✅ Admin user already exists (administrator)")
        
        # Create modules if they don't exist
        if Module.count() == 0:
            create_default_modules()
            print("✅ Default modules created")
        else:
            print("✅ Modules already exist")
        
        # Create questions if they don't exist
        if KnowledgeCheckQuestion.count() == 0:
            create_default_questions()
            print("✅ Default questions created")
        else:
            print("✅ Questions already exist")
            
    except Exception as e:
        print(f"❌ Error creating default data: {e}")

def create_default_modules():
    """Create default learning modules with content from modules folder"""
    try:
        # Import module content classes
        from learning_modules import (
            Module1Content, Module2Content, Module3Content, Module4Content,
            Module5Content, Module6Content, Module7Content, FinalAssessmentContent
        )
        
        # Module content classes
        module_classes = [
            Module1Content, Module2Content, Module3Content, Module4Content,
            Module5Content, Module6Content, Module7Content, FinalAssessmentContent
        ]
        
        for i, module_class in enumerate(module_classes, 1):
            # Get content from module class
            content_data = module_class.get_content()
            
            # Create module data
            module_data = {
                'name': content_data['title'],
                'description': content_data['description'],
                'content': content_data['content'],
                'order': i,
                'has_simulation': i in [2, 3, 4, 5],  # Modules 2-5 have simulations
                'simulation_type': 'quid_pro_quo' if i == 2 else 'phishing' if i == 3 else 'pretexting' if i == 4 else 'baiting' if i == 5 else None
            }
            
            # Create and save module
            module = Module(**module_data)
            if module.save():
                print(f"✅ Created module {i}: {content_data['title']}")
            else:
                print(f"❌ Failed to create module {i}")
                
    except Exception as e:
        print(f"❌ Error creating modules: {e}")
        # Fallback to basic modules if import fails
        modules_data = [
            {
                'name': 'Introduction to Social Engineering',
                'description': 'Understanding the basics of social engineering attacks',
                'content': 'Social engineering is a manipulation technique that exploits human error to gain private information...',
                'order': 1,
                'has_simulation': False
            },
            {
                'name': 'Types of Social Engineering Attacks',
                'description': 'Learn about different types of social engineering attacks',
                'content': 'There are several types of social engineering attacks...',
                'order': 2,
                'has_simulation': True,
                'simulation_type': 'phishing'
            },
            {
                'name': 'Phishing Attacks',
                'description': 'Learn about phishing techniques and prevention',
                'content': 'Phishing is a type of social engineering attack where attackers impersonate legitimate entities...',
                'order': 3,
                'has_simulation': True,
                'simulation_type': 'phishing'
            },
            {
                'name': 'Pretexting and Impersonation',
                'description': 'Understanding pretexting and impersonation techniques',
                'content': 'Pretexting involves creating a fabricated scenario...',
                'order': 4,
                'has_simulation': True,
                'simulation_type': 'pretexting'
            },
            {
                'name': 'Baiting and Quid Pro Quo',
                'description': 'Learn about baiting and quid pro quo attacks',
                'content': 'Baiting involves leaving a physical device...',
                'order': 5,
                'has_simulation': True,
                'simulation_type': 'baiting'
            },
            {
                'name': 'Advanced Techniques',
                'description': 'Advanced social engineering techniques and countermeasures',
                'content': 'Advanced social engineering techniques include...',
                'order': 6,
                'has_simulation': False
            },
            {
                'name': 'Incident Response',
                'description': 'How to respond to social engineering incidents',
                'content': 'When a social engineering incident occurs...',
                'order': 7,
                'has_simulation': False
            }
        ]
        
        for module_data in modules_data:
            module = Module(**module_data)
            module.save()

def create_default_questions():
    """Create default assessment questions from modules folder"""
    try:
        # Import module question classes
        from learning_modules import (
            Module1Questions, Module2Questions, Module3Questions, Module4Questions,
            Module5Questions, Module6Questions, Module7Questions, FinalAssessmentQuestions
        )
        
        # Module question classes
        question_classes = [
            Module1Questions, Module2Questions, Module3Questions, Module4Questions,
            Module5Questions, Module6Questions, Module7Questions, FinalAssessmentQuestions
        ]
        
        for module_id, question_class in enumerate(question_classes, 1):
            # Get questions from module class
            questions_data = question_class.get_question_set_1()
            
            for question_data in questions_data:
                # Add module_id to question data
                question_data['module_id'] = module_id
                
                # Create and save question
                question = KnowledgeCheckQuestion(**question_data)
                if question.save():
                    print(f"✅ Created question for module {module_id}")
                else:
                    print(f"❌ Failed to create question for module {module_id}")
                    
    except Exception as e:
        print(f"❌ Error creating questions: {e}")
        # Fallback to basic questions if import fails
        questions_data = [
            {
                'module_id': 1,
                'question_text': 'What is social engineering?',
                'option_a': 'A type of software',
                'option_b': 'A manipulation technique that exploits human error',
                'option_c': 'A hardware component',
                'option_d': 'A programming language',
                'correct_answer': 'b',
                'explanation': 'Social engineering is a manipulation technique that exploits human error to gain private information.',
                'question_set': 1
            }
        ]
        
        for question_data in questions_data:
            question = KnowledgeCheckQuestion(**question_data)
            question.save()

# Route handlers using OOP principles
@app.route('/')
def index():
    """Home page route"""
    try:
        return render_template('index.html')
    except Exception as e:
        flash(f"Error loading page: {e}", 'error')
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if request.method == 'POST':
        try:
            # Get form data
            username = request.form.get('username', '').strip()
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '')
            confirm_password = request.form.get('confirm_password', '')
            full_name = request.form.get('full_name', '').strip()
            specialization = request.form.get('specialization', '')
            year_level = request.form.get('year_level', '')
            
            # Validate required fields
            if not all([username, email, password, confirm_password, full_name, specialization, year_level]):
                flash('All fields are required.', 'error')
                return render_template('register.html', form_data=request.form)
            
            # Validate password confirmation
            if password != confirm_password:
                flash('Passwords do not match.', 'error')
                return render_template('register.html', form_data=request.form)
            
            # Create user data
            user_data = {
                'username': username,
                'email': email,
                'password': password,
                'full_name': full_name,
                'specialization': specialization,
                'year_level': year_level
            }
            
            try:
                user = user_service.create_user(user_data)
                if user:
                    flash('Registration successful! Please login.', 'success')
                    return redirect(url_for('login'))
            except ValueError as ve:
                flash(str(ve), 'error')
                
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f'Registration error: {e}', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            user = user_service.authenticate_user(username, password)
            if user:
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.', 'error')
                
        except Exception as e:
            flash(f'Login error: {e}', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout route"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard route"""
    try:
        # Get user statistics using service
        user_stats = user_service.get_user_statistics(current_user.id)
        
        # Get user progress using data structures
        progress_list = LinkedList()
        user_progress = UserProgress.get_user_progress(current_user.id)
        for progress in user_progress:
            progress_list.append(progress)
        
        # Get modules
        modules = Module.get_all_ordered()
        
        # Get total modules count
        total_modules = Module.count()
        
        # Get properly completed modules using validation
        completed_module_ids = user_service.get_user_completed_modules(current_user.id)
        completed_modules = len(completed_module_ids)
        
        # Get final assessment result
        final_result = AssessmentResult.query.filter_by(
            user_id=current_user.id, 
            assessment_type='final_assessment', 
            passed=True
        ).first()
        
        # Get survey completion status
        survey_completed = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
        
        # Calculate accessible modules (modules 1 to total_modules)
        accessible_modules = []
        for i in range(1, total_modules + 1):  # Modules 1 to total_modules
            if i == 1:
                # First module is always accessible
                accessible_modules.append(True)
            else:
                # Other modules are accessible if previous module is fully completed
                previous_module_completed = user_service.is_module_fully_completed(current_user.id, i-1)
                accessible_modules.append(previous_module_completed)
        
        # Build recent activity feed (simulations, assessments, module completions, surveys)
        recent_activities = []

        # Simulations
        sim_results = SimulationResult.query.filter_by(
            user_id=current_user.id
        ).order_by(SimulationResult.created_at.desc()).limit(10).all()
        for sim in sim_results:
            recent_activities.append({
                'type': 'simulation',
                'title': f"{(sim.simulation_type or '').replace('_', ' ').title()} Simulation",
                'detail': f"Score: {sim.score}%",
                'badge_text': 'Completed' if sim.completed else 'In Progress',
                'badge_class': 'bg-success' if sim.completed else 'bg-warning',
                'timestamp': sim.updated_at or sim.created_at
            })

        # Assessments (knowledge checks, final, baseline)
        assess_results = AssessmentResult.query.filter_by(user_id=current_user.id)\
            .order_by(AssessmentResult.created_at.desc()).limit(10).all()
        for ar in assess_results:
            module_name = None
            if ar.module_id:
                m = Module.get_by_id(ar.module_id)
                module_name = m.name if m else None
            assessment_label = {
                'knowledge_check': 'Knowledge Check',
                'final_assessment': 'Final Assessment',
                'baseline': 'Baseline Assessment',
                'follow_up': 'Follow-up Assessment'
            }.get(ar.assessment_type, 'Assessment')
            title = f"{assessment_label}" + (f" - {module_name}" if module_name else '')
            percent = int((ar.score / ar.total_questions) * 100) if ar.total_questions else ar.score
            recent_activities.append({
                'type': 'assessment',
                'title': title,
                'detail': f"Score: {percent}% ({ar.correct_answers}/{ar.total_questions})",
                'badge_text': 'Passed' if getattr(ar, 'passed', False) else 'Failed',
                'badge_class': 'bg-success' if getattr(ar, 'passed', False) else 'bg-danger',
                'timestamp': ar.created_at
            })

        # Module completions
        completed_progress = UserProgress.query.filter_by(
            user_id=current_user.id,
            status='completed'
        ).order_by(UserProgress.completed_at.desc()).limit(10).all()
        for up in completed_progress:
            m = Module.get_by_id(up.module_id)
            recent_activities.append({
                'type': 'module',
                'title': f"Module Completed - {m.name if m else f'ID {up.module_id}'}",
                'detail': f"Score: {up.score}%",
                'badge_text': 'Completed',
                'badge_class': 'bg-success',
                'timestamp': up.completed_at or up.updated_at or up.created_at
            })

        # Surveys
        surveys = FeedbackSurvey.query.filter_by(user_id=current_user.id)\
            .order_by(FeedbackSurvey.created_at.desc()).limit(10).all()
        for s in surveys:
            m = Module.get_by_id(s.module_id) if s.module_id else None
            recent_activities.append({
                'type': 'survey',
                'title': f"Feedback Submitted" + (f" - {m.name}" if m else ''),
                'detail': f"Rating: {s.rating}/5",
                'badge_text': 'Submitted',
                'badge_class': 'bg-info',
                'timestamp': s.created_at
            })

        # Sort by timestamp and take top 5
        recent_activities = sorted(
            recent_activities,
            key=lambda a: a['timestamp'] or datetime.utcnow(),
            reverse=True
        )[:5]
        
        # Calculate average score from assessment results
        assessment_results = AssessmentResult.query.filter_by(user_id=current_user.id).all()
        if assessment_results:
            total_score = sum(result.score for result in assessment_results)
            total_questions = sum(result.total_questions for result in assessment_results)
            average_score = int((total_score / total_questions) * 100) if total_questions > 0 else 0
        else:
            average_score = 0
        
        # Calculate total time spent (estimate: 30 minutes per completed module)
        total_time_spent = completed_modules * 30
        
        return render_template('dashboard.html', 
                             user_stats=user_stats,
                             progress_list=progress_list,
                             modules=modules,
                             completed_modules=completed_modules,
                             completed_module_ids=completed_module_ids,
                             total_modules=total_modules,
                             final_result=final_result,
                             survey_completed=survey_completed,
                             accessible_modules=accessible_modules,
                             recent_activities=recent_activities,
                             average_score=average_score,
                             total_time_spent=total_time_spent)
    except Exception as e:
        flash(f'Error loading dashboard: {e}', 'error')
        return redirect(url_for('index'))

@app.route('/module/<int:module_id>')
@login_required
def module(module_id):
    """Module view route"""
    try:
        module_obj = Module.get_by_id(module_id)
        if not module_obj:
            flash('Module not found.', 'error')
            return redirect(url_for('dashboard'))
            
        # Check if user can access this module
        if module_id == 1:
            # First module is always accessible
            pass
        else:
            # Check if previous module is fully completed
            previous_module_completed = user_service.is_module_fully_completed(current_user.id, module_id - 1)
            if not previous_module_completed:
                flash('You must complete the previous module before accessing this one.', 'warning')
                return redirect(url_for('dashboard'))
        
        # Get user progress for this module
        progress = UserProgress.get_module_progress(current_user.id, module_id)
        if not progress:
            progress = UserProgress(
                user_id=current_user.id,
                module_id=module_id,
                status='not_started'
            )
            progress.save()
        
        # Get knowledge check score for this module
        knowledge_check_result = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            module_id=module_id,
            assessment_type='knowledge_check'
        ).order_by(AssessmentResult.created_at.desc()).first()
        
        # Calculate percentage score
        if knowledge_check_result:
            knowledge_check_score = int((knowledge_check_result.score / knowledge_check_result.total_questions) * 100)
        else:
            knowledge_check_score = 0
        
        return render_template('module.html', 
                             module=module_obj,
                             progress=progress, 
                             knowledge_check_score=knowledge_check_score)
    except Exception as e:
        flash(f'Error loading module: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/assessment/<int:module_id>')
@login_required
def assessment(module_id):
    """Assessment route"""
    try:
        module_obj = Module.get_by_id(module_id)
        if not module_obj:
            flash('Module not found.', 'error')
            return redirect(url_for('dashboard'))
        
        # Check if user can access this module
        if module_id == 1:
            # First module is always accessible
            pass
        else:
            # Check if previous module is fully completed
            previous_module_completed = user_service.is_module_fully_completed(current_user.id, module_id - 1)
            if not previous_module_completed:
                flash('You must complete the previous module before taking this assessment.', 'warning')
                return redirect(url_for('dashboard'))
        
        # Create assessment using service
        questions = assessment_service.create_knowledge_check(module_id)
        
        if not questions:
            flash('No questions available for this module.', 'error')
            return redirect(url_for('module', module_id=module_id))
        
        return render_template('assessment_simple.html',
                             module=module_obj,
                             questions=questions)
    except Exception as e:
        flash(f'Error loading assessment: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/submit_assessment/<int:module_id>', methods=['POST'])
@login_required
def submit_assessment(module_id):
    """Submit assessment route"""
    try:
        # Get questions for this module
        questions = assessment_service.create_knowledge_check(module_id)
        
        # Get user answers
        user_answers = {}
        for question in questions:
            answer = request.form.get(f'question_{question.id}')
            if answer:
                user_answers[str(question.id)] = answer
        
        # Validate answers
        if not assessment_service.validate_assessment_answers(questions, user_answers):
            flash('Please answer all questions.', 'error')
            return redirect(url_for('assessment', module_id=module_id))
        
        # Grade assessment
        score, total_questions, percentage, detailed_results = assessment_service.grade_assessment(
            questions, user_answers
        )
        
        # Save assessment result
        assessment_result = assessment_service.save_assessment_result(
            user_id=current_user.id,
            assessment_type='knowledge_check',
            score=score,
            total_questions=total_questions,
            correct_answers=score,
            module_id=module_id,
            answers_data=user_answers
        )
        
        # Update user progress
        if assessment_result:
            current_user.update_progress(module_id, score)
        
        return render_template('assessment_result.html',
                             score=score,
                             total_questions=total_questions,
                             percentage=percentage,
                             detailed_results=detailed_results,
                             module_id=module_id)
        
    except Exception as e:
        flash(f'Error submitting assessment: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/profile')
@login_required
def profile():
    """User profile route"""
    try:
        return render_template('profile.html', user=current_user)
    except Exception as e:
        flash(f'Error loading profile: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    """Update profile route"""
    try:
        profile_data = {
            'full_name': request.form['full_name'],
            'email': request.form['email'],
            'specialization': request.form['specialization'],
            'year_level': request.form['year_level']
        }
        
        if user_service.update_user_profile(current_user.id, profile_data):
            flash('Profile updated successfully!', 'success')
        else:
            flash('Failed to update profile.', 'error')
            
    except ValueError as e:
        flash(str(e), 'error')
    except Exception as e:
        flash(f'Error updating profile: {e}', 'error')
    
    return redirect(url_for('profile'))

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Forgot password route"""
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            user = User.get_by_email(email)
            if user:
                token = user.create_password_reset_token()
                if token:
                    flash('Password reset instructions have been sent to your email.', 'success')
                else:
                    flash('Error creating reset token. Please try again.', 'error')
            else:
                flash('Email not found in our system.', 'error')
        else:
            flash('Please enter your email address.', 'error')
    
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Reset password route"""
    reset_token = PasswordResetToken.get_valid_token(token)
    
    if not reset_token:
        flash('Invalid or expired reset token.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters long.', 'error')
        else:
            user = User.query.get(reset_token.user_id)
            if user and user.set_password(password):
                reset_token.mark_as_used()
                flash('Password has been reset successfully!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Error resetting password. Please try again.', 'error')
    
    return render_template('reset_password.html', token=token)

# Additional routes for dashboard functionality
@app.route('/final_assessment')
@login_required
def final_assessment():
    """Final assessment route"""
    try:
        # Check if user has completed all modules
        completed_modules = UserProgress.query.filter_by(
            user_id=current_user.id, 
            status='completed'
        ).count()
        
        total_modules = Module.count()
        
        return render_template('final_assessment_simple.html', 
                             completed_modules=completed_modules,
                             total_modules=total_modules)
    except Exception as e:
        flash(f'Error loading final assessment: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/final_assessment_questions')
@login_required
def final_assessment_questions():
    """Final assessment questions route"""
    try:
        # Check if user has completed all modules
        completed_modules = UserProgress.query.filter_by(
            user_id=current_user.id, 
            status='completed'
        ).count()
        
        total_modules = Module.count()
        
        if completed_modules < total_modules:
            flash('You must complete all modules before taking the final assessment.', 'warning')
            return redirect(url_for('dashboard'))
        
        # Get final assessment questions
        questions = assessment_service.create_final_assessment(question_count=25)
        
        if not questions:
            flash('No final assessment questions available.', 'error')
            return redirect(url_for('dashboard'))
        
        return render_template('final_assessment_questions.html', questions=questions)
    except Exception as e:
        flash(f'Error loading final assessment questions: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/submit_final_assessment', methods=['POST'])
@login_required
def submit_final_assessment():
    """Submit final assessment route"""
    try:
        # Get final assessment questions
        questions = assessment_service.create_final_assessment()
        
        # Get user answers
        user_answers = {}
        for question in questions:
            answer = request.form.get(f'question_{question.id}')
            if answer:
                user_answers[str(question.id)] = answer
        
        # Validate answers
        if not assessment_service.validate_assessment_answers(questions, user_answers):
            flash('Please answer all questions.', 'error')
            return redirect(url_for('final_assessment'))
        
        # Grade assessment
        score, total_questions, percentage, detailed_results = assessment_service.grade_assessment(
            questions, user_answers
        )
        
        # Determine if passed (70% or higher)
        passed = percentage >= 70
        
        # Save assessment result
        assessment_result = assessment_service.save_assessment_result(
            user_id=current_user.id,
            assessment_type='final_assessment',
            score=score,
            total_questions=total_questions,
            correct_answers=score,
            module_id=None,
            answers_data=user_answers,
            passed=passed
        )
        
        return render_template('final_assessment_result.html',
                             score=score,
                             total_questions=total_questions,
                             percentage=percentage,
                             passed=passed,
                             detailed_results=detailed_results)
        
    except Exception as e:
        flash(f'Error submitting final assessment: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/simulation/<simulation_type>')
@login_required
def simulation(simulation_type):
    """Simulation route"""
    try:
        # Validate simulation type
        valid_types = ['phishing', 'pretexting', 'baiting', 'quid_pro_quo']
        if simulation_type not in valid_types:
            flash('Invalid simulation type.', 'error')
            return redirect(url_for('dashboard'))
        
        # Get simulation content
        simulation_content = simulation_service.get_simulation_content(simulation_type)
        
        return render_template('simulation_simple.html',
                             simulation_type=simulation_type,
                             content=simulation_content)
    except Exception as e:
        flash(f'Error loading simulation: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/submit_simulation/<simulation_type>', methods=['POST'])
@login_required
def submit_simulation(simulation_type):
    """Submit simulation route"""
    try:
        # Validate simulation type
        valid_types = ['phishing', 'pretexting', 'baiting', 'quid_pro_quo']
        if simulation_type not in valid_types:
            flash('Invalid simulation type.', 'error')
            return redirect(url_for('dashboard'))
        
        # Get simulation content
        simulation_content = simulation_service.get_simulation_content(simulation_type)
        
        # Get user answers
        user_answers = {}
        for option in simulation_content.get('options', []):
            answer = request.form.get(f'option_{option["id"]}')
            if answer:
                user_answers[str(option['id'])] = answer
        
        # Validate answers
        if not simulation_service.validate_simulation_answers(simulation_content, user_answers):
            flash('Please answer all questions.', 'error')
            return redirect(url_for('simulation', simulation_type=simulation_type))
        
        # Grade simulation
        results = simulation_service.grade_simulation(simulation_content, user_answers)
        
        # Determine module_id based on simulation type
        module_id = None
        if simulation_type == 'phishing':
            module_id = 3  # Module 3 has phishing simulation
        elif simulation_type == 'pretexting':
            module_id = 4  # Module 4 has pretexting simulation
        elif simulation_type == 'baiting':
            module_id = 5  # Module 5 has baiting simulation
        elif simulation_type == 'quid_pro_quo':
            module_id = 2  # Module 2 has quid pro quo simulation
        
        # Save simulation result
        simulation_result = simulation_service.save_simulation_result(
            user_id=current_user.id,
            simulation_type=simulation_type,
            score=results['score'],
            total_questions=results['total_questions'],
            decisions_made=results['detailed_results'],
            scenario_data=simulation_content,
            time_taken=0,  # Could be tracked in future
            module_id=module_id
        )
        
        if simulation_result:
            flash(f'Simulation completed! Score: {results["score"]}/{results["total_questions"]} ({results["percentage"]:.1f}%)', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Failed to save simulation result.', 'error')
            return redirect(url_for('simulation', simulation_type=simulation_type))
                
    except Exception as e:
        flash(f'Error submitting simulation: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/survey')
@login_required
def survey():
    """Survey route"""
    try:
        # Check if user has passed final assessment
        final_result = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment',
            passed=True
        ).first()
        
        if not final_result:
            flash('You must pass the final assessment before taking the survey.', 'warning')
            return redirect(url_for('dashboard'))
        
        # Check if survey already completed
        existing_survey = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
        if existing_survey:
            flash('You have already completed the survey.', 'info')
            return redirect(url_for('dashboard'))
        
        return render_template('survey.html')
    except Exception as e:
        flash(f'Error loading survey: {e}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/submit_survey', methods=['POST'])
@login_required
def submit_survey():
    """Submit survey route"""
    try:
        # Get survey data
        survey_data = {
            'user_id': current_user.id,
            'program_rating': request.form.get('program_rating'),
            'content_quality': request.form.get('content_quality'),
            'difficulty_level': request.form.get('difficulty_level'),
            'recommendation_likelihood': request.form.get('recommendation_likelihood'),
            'additional_comments': request.form.get('additional_comments')
        }
        
        # Save survey
        survey = FeedbackSurvey(**survey_data)
        if survey.save():
            flash('Survey submitted successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Failed to submit survey.', 'error')
            return redirect(url_for('survey'))
        
    except Exception as e:
        flash(f'Error submitting survey: {e}', 'error')
        return redirect(url_for('survey'))

@app.route('/update_progress', methods=['POST'])
@login_required
def update_progress():
    """Update user progress via AJAX"""
    try:
        data = request.get_json()
        module_id = data.get('module_id')
        status = data.get('status')
        score = data.get('score', 0)
        time_spent = data.get('time_spent', 0)
        
        if not module_id or not status:
            return jsonify({'success': False, 'error': 'Missing required data'})
        
        # Update or create progress record
        progress = UserProgress.query.filter_by(
            user_id=current_user.id,
            module_id=module_id
        ).first()
        
        if not progress:
            progress = UserProgress(
                user_id=current_user.id,
                module_id=module_id,
                status=status,
                score=score,
                time_spent=time_spent
            )
        else:
            progress.status = status
            progress.score = score
            progress.time_spent = time_spent
        
        if progress.save():
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Failed to save progress'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/certificate')
@login_required
def certificate():
    """Certificate generation route"""
    try:
        # Check if user has completed all requirements
        final_result = AssessmentResult.query.filter_by(
                user_id=current_user.id,
            assessment_type='final_assessment',
                passed=True
        ).first()
        
        survey_completed = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
        
        if not final_result:
            flash('You must pass the final assessment to generate a certificate.', 'warning')
            return redirect(url_for('dashboard'))
        
        if not survey_completed:
            flash('You must complete the survey to generate a certificate.', 'warning')
            return redirect(url_for('dashboard'))
        
        return render_template('certificate.html', user=current_user)
    except Exception as e:
        flash(f'Error generating certificate: {e}', 'error')
        return redirect(url_for('dashboard'))

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('500.html'), 500

# Main application entry point
if __name__ == '__main__':
    print("🚀 Initializing Social Engineering Awareness Program with OOP...")
    app = create_app()
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"✅ Application ready on port {port}")
    app.run(debug=debug, host='0.0.0.0', port=port) 
