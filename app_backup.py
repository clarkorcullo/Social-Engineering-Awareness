from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import random
import re # Added for password validation
import json # Added for json.dumps

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
    birthday = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(200), nullable=True)
    profile_picture = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Progress tracking attributes
    modules_completed = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    simulations_completed = db.Column(db.Integer, default=0)

# Module Model
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    has_simulation = db.Column(db.Boolean, default=False)
    simulation_type = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Knowledge Check Question Model
class KnowledgeCheckQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(500), nullable=False)
    option_b = db.Column(db.String(500), nullable=False)
    option_c = db.Column(db.String(500), nullable=False)
    option_d = db.Column(db.String(500), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # 'a', 'b', 'c', 'd'
    explanation = db.Column(db.Text, nullable=False)
    question_set = db.Column(db.Integer, default=1)  # For multiple question sets
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Final Assessment Question Model
class FinalAssessmentQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(500), nullable=False)
    option_b = db.Column(db.String(500), nullable=False)
    option_c = db.Column(db.String(500), nullable=False)
    option_d = db.Column(db.String(500), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    question_set = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# User Progress Model
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    status = db.Column(db.String(20), default='not_started')  # not_started, in_progress, completed
    score = db.Column(db.Integer, default=0)
    attempts = db.Column(db.Integer, default=0)
    time_spent = db.Column(db.Integer, default=0)  # in minutes
    completed_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Assessment Result Model
class AssessmentResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assessment_type = db.Column(db.String(50), nullable=False)  # knowledge_check, final_assessment
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=True)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Integer, default=0)  # in seconds
    passed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Simulation Result Model
class SimulationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    simulation_type = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    decisions_made = db.Column(db.Text, nullable=True)  # JSON string of decisions
    time_taken = db.Column(db.Integer, default=0)  # in seconds
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Feedback Survey Model
class FeedbackSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=True)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 scale
    feedback_text = db.Column(db.Text, nullable=True)
    difficulty_level = db.Column(db.String(20), nullable=True)  # easy, medium, hard
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading index: {str(e)}"

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    try:
        errors = {}
        form_data = {}
        success_message = ""
        
        if request.method == 'POST':
            if 'update_profile' in request.form:
                # Handle profile update
                full_name = request.form.get('full_name', '').strip()
                birthday = request.form.get('birthday', '')
                address = request.form.get('address', '').strip()
                
                # Validate full name
                if not full_name:
                    errors['full_name'] = 'Full name is required'
                elif len(full_name) < 2:
                    errors['full_name'] = 'Full name must be at least 2 characters'
                
                # Validate birthday format if provided
                if birthday:
                    try:
                        datetime.strptime(birthday, '%Y-%m-%d')
                    except ValueError:
                        errors['birthday'] = 'Invalid date format'
                
                if not errors:
                    # Update user profile
                    current_user.full_name = full_name
                    if birthday:
                        current_user.birthday = datetime.strptime(birthday, '%Y-%m-%d')
                    current_user.address = address
                    
                    # Handle profile picture upload
                    if 'profile_picture' in request.files:
                        file = request.files['profile_picture']
                        if file and file.filename:
                            # Validate file type
                            allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                            if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions:
                                # Generate unique filename
                                filename = f"{current_user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file.filename.rsplit('.', 1)[1].lower()}"
                                file_path = os.path.join('static', 'profile_pictures', filename)
                                
                                # Ensure directory exists
                                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                                
                                # Save file
                                file.save(file_path)
                                current_user.profile_picture = filename
                            else:
                                errors['profile_picture'] = 'Invalid file type. Please upload PNG, JPG, JPEG, GIF, or WEBP files only.'
                    
                    db.session.commit()
                    success_message = "Profile updated successfully!"
                    form_data = {'full_name': full_name, 'birthday': birthday, 'address': address}
                
            elif 'change_password' in request.form:
                # Handle password change
                old_password = request.form.get('old_password', '')
                new_password = request.form.get('new_password', '')
                confirm_new_password = request.form.get('confirm_new_password', '')
                
                # Validate old password
                if not check_password_hash(current_user.password_hash, old_password):
                    errors['old_password'] = 'Current password is incorrect'
                
                # Validate new password
                if len(new_password) < 12:
                    errors['new_password'] = 'Password must be at least 12 characters'
                elif not re.search(r'[A-Z]', new_password):
                    errors['new_password'] = 'Password must contain at least one capital letter'
                elif not re.search(r'[a-z]', new_password):
                    errors['new_password'] = 'Password must contain at least one lowercase letter'
                elif not re.search(r'\d', new_password):
                    errors['new_password'] = 'Password must contain at least one number'
                elif not re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', new_password):
                    errors['new_password'] = 'Password must contain at least one special character'
                
                # Validate password confirmation
                if new_password != confirm_new_password:
                    errors['confirm_new_password'] = 'Passwords do not match'
                
                if not errors:
                    # Update password
                    current_user.password_hash = generate_password_hash(new_password)
                    db.session.commit()
                    success_message = "Password changed successfully!"
                    form_data = {'new_password': new_password, 'confirm_new_password': confirm_new_password}
        
        return render_template('profile.html', 
                             user=current_user, 
                             errors=errors, 
                             form_data=form_data,
                             success_message=success_message)
    except Exception as e:
        return f"Error loading profile: {str(e)}"

def check_module_prerequisites(user_id, module_id):
    """Check if user has completed all prerequisite modules"""
    if module_id == 1:
        return True  # First module is always accessible
    
    # Check if all previous modules are completed
    for prev_module_id in range(1, module_id):
        # Check if user has passed the knowledge check for this module
        latest_assessment = AssessmentResult.query.filter_by(
            user_id=user_id,
            module_id=prev_module_id,
            assessment_type='knowledge_check'
        ).order_by(AssessmentResult.created_at.desc()).first()
        
        # Module is not completed if no assessment exists or if the latest assessment failed
        if not latest_assessment or not latest_assessment.passed:
            return False
    
    return True

@app.route('/module/<int:module_id>')
@login_required
def module(module_id):
    try:
        # Special handling for Module 8 (Final Assessment)
        if module_id == 8:
            # Check if user has completed all modules 1-7
            completed_modules = UserProgress.query.filter_by(
                user_id=current_user.id,
                status='completed'
            ).count()
            
            if completed_modules < 7:
                flash('You must complete all modules 1-7 before accessing the Final Assessment.', 'error')
                return redirect(url_for('dashboard'))
            
            # Redirect to final assessment page
            return redirect(url_for('final_assessment'))
        
        # Check if user has completed prerequisite modules
        if not check_module_prerequisites(current_user.id, module_id):
            flash(f'You must complete Module {module_id - 1} before accessing Module {module_id}', 'error')
            return redirect(url_for('dashboard'))
        
        # Get module data
        module = Module.query.get_or_404(module_id)
        
        # Get user progress for this module
        progress = UserProgress.query.filter_by(
            user_id=current_user.id,
            module_id=module_id
        ).first()
        
        if not progress:
            progress = UserProgress(
                user_id=current_user.id,
                module_id=module_id,
                status='not_started'
            )
            db.session.add(progress)
            db.session.commit()
        
        # Get the latest knowledge check score from AssessmentResult
        latest_assessment = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            module_id=module_id,
            assessment_type='knowledge_check'
        ).order_by(AssessmentResult.created_at.desc()).first()
        
        # Calculate the actual knowledge check score percentage
        if latest_assessment:
            # Use correct_answers instead of score, and ensure percentage doesn't exceed 100%
            percentage = (latest_assessment.correct_answers / latest_assessment.total_questions) * 100
            knowledge_check_score = min(round(percentage), 100)  # Cap at 100%
        else:
            knowledge_check_score = 0
        
        return render_template('module.html', 
                             module=module, 
                             progress=progress, 
                             knowledge_check_score=knowledge_check_score)
    except Exception as e:
        return f"Error loading module: {str(e)}"

@app.route('/module/<int:module_id>/knowledge-check')
@login_required
def module_knowledge_check(module_id):
    try:
        module = Module.query.filter_by(id=module_id).first()
        if not module:
            flash('Module not found', 'error')
            return redirect(url_for('dashboard'))
        
        # Check if user has completed prerequisite modules
        if not check_module_prerequisites(current_user.id, module_id):
            flash(f'You must complete Module {module_id - 1} before accessing Module {module_id}', 'error')
            return redirect(url_for('dashboard'))
        
        # Get questions for this module
        questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
        
        if not questions:
            flash('No questions available for this module', 'error')
            return redirect(url_for('module', module_id=module_id))
        
        # Assessment rules
        rules = {
            'questions_per_attempt': 5,
            'passing_rate': 80,
            'passing_score': 4  # 4 out of 5 questions correct
        }
        
        return render_template('module_knowledge_check.html', 
                             module=module, 
                             questions=questions, 
                             rules=rules)
    except Exception as e:
        return f"Error loading knowledge check: {str(e)}"

@app.route('/api/knowledge-check/<int:module_id>/questions')
@login_required
def get_knowledge_check_questions(module_id):
    try:
        # Get user's previous attempts for this module
        previous_attempts = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            module_id=module_id,
            assessment_type='knowledge_check'
        ).count()
        
        # Get all questions for this module
        all_questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
        
        if not all_questions:
            return jsonify({'error': 'No questions available for this module'}), 404
        
        # For retakes, we'll use different subsets of questions to provide variety
        # First attempt: Use first 5 questions
        # Second attempt: Use next 5 questions (if available)
        # Third attempt+: Use random 5 questions
        
        if previous_attempts == 0:
            # First attempt - use first 5 questions
            selected_questions = all_questions[:5]
        elif previous_attempts == 1 and len(all_questions) >= 10:
            # Second attempt - use next 5 questions
            selected_questions = all_questions[5:10]
        else:
            # Third attempt or more - use random questions
            selected_questions = random.sample(all_questions, min(5, len(all_questions)))
        
        # Ensure we have exactly 5 questions (or all available if less than 5)
        if len(selected_questions) < 5 and len(all_questions) >= 5:
            # If we don't have enough questions in the selected subset, add random ones
            remaining_questions = [q for q in all_questions if q not in selected_questions]
            additional_needed = 5 - len(selected_questions)
            if remaining_questions:
                additional_questions = random.sample(remaining_questions, min(additional_needed, len(remaining_questions)))
                selected_questions.extend(additional_questions)
        
        # Format questions for frontend
        questions_data = []
        for question in selected_questions:
            questions_data.append({
                'id': question.id,
                'question_text': question.question_text,
                'options': {
                    'a': question.option_a,
                    'b': question.option_b,
                    'c': question.option_c,
                    'd': question.option_d
                },
                'correct_answer': question.correct_answer,
                'explanation': question.explanation
            })
        
        return jsonify({
            'questions': questions_data,
            'total_questions': len(questions_data),
            'passing_score': 4,  # 4 out of 5 correct
            'attempt_number': previous_attempts + 1,
            'questions_available': len(all_questions)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/knowledge-check/<int:module_id>/submit', methods=['POST'])
@login_required
def submit_knowledge_check(module_id):
    try:
        data = request.get_json()
        answers = data.get('answers', {})
        time_taken = data.get('time_taken', 0)
        
        # Get questions to check answers
        questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
        question_dict = {q.id: q for q in questions}
        
        correct_answers = 0
        total_questions = len(answers)
        
        # Check each answer
        for question_id, answer in answers.items():
            question = question_dict.get(int(question_id))
            if question and question.correct_answer == answer:
                correct_answers += 1
        
        # Calculate score
        score = int((correct_answers / total_questions) * 100)
        passed = score >= 80  # 80% passing rate
        
        # Save result
        result = AssessmentResult(
            user_id=current_user.id,
            assessment_type='knowledge_check',
            module_id=module_id,
            score=score,
            total_questions=total_questions,
            correct_answers=correct_answers,
            time_taken=time_taken,
            passed=passed
        )
        db.session.add(result)
        
        # Update user progress if passed
        if passed:
            progress = UserProgress.query.filter_by(
                user_id=current_user.id, 
                module_id=module_id
            ).first()
            
            if progress:
                progress.status = 'completed'
                progress.score = score
                progress.attempts += 1
                progress.completed_at = datetime.utcnow()
            
            # Update user's overall progress
            current_user.modules_completed = UserProgress.query.filter_by(
                user_id=current_user.id, 
                status='completed'
            ).count()
            current_user.total_score += score
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'score': score,
            'correct_answers': correct_answers,
            'total_questions': total_questions,
            'passed': passed,
            'message': 'Congratulations! You passed!' if passed else 'Try again to improve your score.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/simulation/<simulation_type>')
@login_required
def simulation(simulation_type):
    try:
        simulation_names = {
            'phishing': 'Phishing Simulation',
            'pretexting': 'Pretexting Simulation',
            'baiting': 'Baiting Simulation',
            'quid_pro_quo': 'Quid Pro Quo Simulation'
        }
        
        simulation_name = simulation_names.get(simulation_type, f'{simulation_type.title()} Simulation')
        
        return render_template('simulation_phishing.html', simulation_type=simulation_type, simulation_name=simulation_name)
    except Exception as e:
        return f"Error loading simulation: {str(e)}"

@app.route('/simulation_result', methods=['POST'])
@login_required
def simulation_result():
    try:
        data = request.get_json()
        simulation_type = data.get('simulation_type', 'phishing')
        scenario_id = data.get('scenario_id', 1)
        user_choice = data.get('user_choice', '')
        correct_choice = data.get('correct_choice', '')
        is_correct = data.get('is_correct', False)
        time_taken = data.get('time_taken', 0)
        
        # Calculate score (100 if correct, 0 if incorrect)
        score = 100 if is_correct else 0
        
        # Create simulation result record
        simulation_result = SimulationResult(
            user_id=current_user.id,
            simulation_type=simulation_type,
            score=score,
            decisions_made=json.dumps({
                'scenario_id': scenario_id,
                'user_choice': user_choice,
                'correct_choice': correct_choice,
                'is_correct': is_correct,
                'time_taken': time_taken
            }),
            time_taken=time_taken,
            completed=True
        )
        
        db.session.add(simulation_result)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Simulation result saved successfully',
            'score': score,
            'is_correct': is_correct
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/update-progress', methods=['POST'])
@login_required
def update_progress():
    try:
        data = request.get_json()
        module_id = data.get('module_id')
        status = data.get('status')
        score = data.get('score', 0)
        time_spent = data.get('time_spent', 0)
        
        progress = UserProgress.query.filter_by(
            user_id=current_user.id, 
            module_id=module_id
        ).first()
        
        if not progress:
            progress = UserProgress(
                user_id=current_user.id,
                module_id=module_id
            )
            db.session.add(progress)
        
        # Only allow 'completed' status if user has passed the knowledge check
        if status == 'completed':
            # Check if user has passed the knowledge check for this module
            passed_assessment = AssessmentResult.query.filter_by(
                user_id=current_user.id,
                module_id=module_id,
                assessment_type='knowledge_check',
                passed=True
            ).first()
            
            if not passed_assessment:
                # If no passed assessment, set status to 'in_progress' instead of 'completed'
                status = 'in_progress'
        
        progress.status = status
        progress.score = score
        progress.time_spent = time_spent
        
        if status == 'completed':
            progress.completed_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        # Check if user has completed all modules
        completed_modules = UserProgress.query.filter_by(
            user_id=current_user.id, 
            status='completed'
        ).count()
        
        total_modules = Module.query.count()
        
        if completed_modules < total_modules:
            flash('You must complete all modules before taking the final assessment.', 'warning')
            return redirect(url_for('dashboard'))
        
        # Get user's final assessment attempts
        attempts = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment'
        ).count()
        
        max_attempts = 3
        remaining_attempts = max_attempts - attempts
        
        if remaining_attempts <= 0:
            flash('You have used all your final assessment attempts. You must restart all modules.', 'error')
            return redirect(url_for('dashboard'))
        
        return render_template('final_assessment.html', 
                             remaining_attempts=remaining_attempts,
                             total_attempts=max_attempts)
    except Exception as e:
        return f"Error loading final assessment: {str(e)}"

@app.route('/api/final-assessment/questions')
@login_required
def get_final_assessment_questions():
    try:
        # Check if user has completed all modules 1-7
        completed_modules = UserProgress.query.filter_by(
            user_id=current_user.id,
            status='completed'
        ).count()
        
        if completed_modules < 7:
            return jsonify({'error': 'You must complete all modules 1-7 before taking the final assessment'}), 403
        
        # Get user's previous final assessment attempts
        previous_attempts = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment'
        ).count()
        
        if previous_attempts >= 3:
            return jsonify({'error': 'You have reached the maximum number of attempts. You must restart from Module 1.'}), 403
        
        # Get questions from modules 1-7 only (not module 8)
        all_questions = []
        for module_id in range(1, 8):  # Modules 1-7
            module_questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
            all_questions.extend(module_questions)
        
        if len(all_questions) < 25:
            return jsonify({'error': 'Not enough questions available for final assessment'}), 404
        
        # For retakes, use different question sets to provide variety
        if previous_attempts == 0:
            # First attempt - use first 25 questions
            selected_questions = all_questions[:25]
        elif previous_attempts == 1 and len(all_questions) >= 50:
            # Second attempt - use next 25 questions
            selected_questions = all_questions[25:50]
        elif previous_attempts == 2 and len(all_questions) >= 75:
            # Third attempt - use next 25 questions
            selected_questions = all_questions[50:75]
        else:
            # Fallback - use random questions
            selected_questions = random.sample(all_questions, 25)
        
        # Ensure we have exactly 25 questions
        if len(selected_questions) < 25:
            # If we don't have enough questions in the selected subset, add random ones
            remaining_questions = [q for q in all_questions if q not in selected_questions]
            additional_needed = 25 - len(selected_questions)
            if remaining_questions:
                additional_questions = random.sample(remaining_questions, min(additional_needed, len(remaining_questions)))
                selected_questions.extend(additional_questions)
        
        # Format questions for frontend
        questions_data = []
        for question in selected_questions:
            questions_data.append({
                'id': question.id,
                'question_text': question.question_text,
                'options': {
                    'a': question.option_a,
                    'b': question.option_b,
                    'c': question.option_c,
                    'd': question.option_d
                },
                'correct_answer': question.correct_answer,
                'explanation': question.explanation
            })
        
        return jsonify({
            'questions': questions_data,
            'total_questions': len(questions_data),
            'passing_score': 20,  # 20 out of 25 correct (80%)
            'attempt_number': previous_attempts + 1,
            'max_attempts': 3,
            'questions_available': len(all_questions)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/final-assessment/submit', methods=['POST'])
@login_required
def submit_final_assessment():
    try:
        data = request.get_json()
        answers = data.get('answers', {})
        time_taken = data.get('time_taken', 0)
        
        # Check attempts
        attempts = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment'
        ).count()
        
        if attempts >= 3:
            return jsonify({'error': 'Maximum attempts reached'}), 403
        
        # Get questions from modules 1-7 to check answers
        all_questions = []
        for module_id in range(1, 8):  # Modules 1-7
            module_questions = KnowledgeCheckQuestion.query.filter_by(module_id=module_id).all()
            all_questions.extend(module_questions)
        
        question_dict = {q.id: q for q in all_questions}
        
        correct_answers = 0
        total_questions = len(answers)
        
        # Check each answer
        for question_id, answer in answers.items():
            question = question_dict.get(int(question_id))
            if question and question.correct_answer == answer:
                correct_answers += 1
        
        # Calculate score
        score = int((correct_answers / total_questions) * 100)
        passed = score >= 80  # 80% passing rate
        
        # Save result
        result = AssessmentResult(
            user_id=current_user.id,
            assessment_type='final_assessment',
            module_id=None,  # Final assessment is not tied to a specific module
            score=score,
            total_questions=total_questions,
            correct_answers=correct_answers,
            time_taken=time_taken,
            passed=passed
        )
        db.session.add(result)
        
        # Handle the result based on pass/fail and attempt count
        if passed:
            # User passed the final assessment
            db.session.commit()
            return jsonify({
                'success': True,
                'score': score,
                'correct_answers': correct_answers,
                'total_questions': total_questions,
                'passed': True,
                'message': 'Congratulations! You passed the Final Assessment! You can now complete the satisfaction survey to receive your certificate.',
                'redirect_to_survey': True
            })
        else:
            # User failed - check if this was the 3rd attempt
            attempts_after_this = attempts + 1
            if attempts_after_this >= 3:
                # Reset all module progress to force restart from Module 1
                UserProgress.query.filter_by(user_id=current_user.id).delete()
                current_user.modules_completed = 0
                current_user.total_score = 0
                
                db.session.commit()
                
                return jsonify({
                    'success': False,
                    'score': score,
                    'correct_answers': correct_answers,
                    'total_questions': total_questions,
                    'passed': False,
                    'message': f'You failed the Final Assessment (Score: {score}%). This was your 3rd attempt. All module progress has been reset. You must restart from Module 1.',
                    'reset_modules': True,
                    'attempts_remaining': 0
                })
            else:
                # Failed but still has attempts remaining
                attempts_remaining = 3 - attempts_after_this
                db.session.commit()
                
                return jsonify({
                    'success': False,
                    'score': score,
                    'correct_answers': correct_answers,
                    'total_questions': total_questions,
                    'passed': False,
                    'message': f'You failed the Final Assessment (Score: {score}%). You have {attempts_remaining} attempt(s) remaining.',
                    'attempts_remaining': attempts_remaining
                })
                
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/survey')
@login_required
def survey():
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
        
        return render_template('survey.html')
    except Exception as e:
        return f"Error loading survey: {str(e)}"

@app.route('/api/submit-survey', methods=['POST'])
@login_required
def submit_survey():
    try:
        data = request.get_json()
        rating = data.get('rating')
        feedback_text = data.get('feedback_text', '')
        difficulty_level = data.get('difficulty_level', 'medium')
        
        # Check if user has already submitted a survey
        existing_survey = FeedbackSurvey.query.filter_by(user_id=current_user.id).first()
        if existing_survey:
            return jsonify({'error': 'You have already submitted a survey'}), 400
        
        # Check if user has passed the final assessment
        final_assessment_result = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment',
            passed=True
        ).first()
        
        if not final_assessment_result:
            return jsonify({'error': 'You must pass the Final Assessment before submitting the survey'}), 403
        
        # Create survey entry
        survey = FeedbackSurvey(
            user_id=current_user.id,
            rating=rating,
            feedback_text=feedback_text,
            difficulty_level=difficulty_level
        )
        db.session.add(survey)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Survey submitted successfully! You can now view your certificate.',
            'redirect_to_certificate': True
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/certificate')
@login_required
def certificate():
    try:
        # Check if user has passed the final assessment
        final_assessment_result = AssessmentResult.query.filter_by(
            user_id=current_user.id,
            assessment_type='final_assessment',
            passed=True
        ).order_by(AssessmentResult.created_at.desc()).first()
        
        if not final_assessment_result:
            flash('You must pass the Final Assessment before receiving a certificate.', 'error')
            return redirect(url_for('dashboard'))
        
        # Check if user has completed the satisfaction survey
        survey_completed = FeedbackSurvey.query.filter_by(
            user_id=current_user.id
        ).first()
        
        if not survey_completed:
            flash('You must complete the satisfaction survey before receiving your certificate.', 'error')
            return redirect(url_for('survey'))
        
        # Calculate completion date
        completion_date = final_assessment_result.created_at
        
        # Generate certificate data
        certificate_data = {
            'student_name': current_user.full_name,
            'completion_date': completion_date.strftime('%B %d, %Y'),
            'final_score': final_assessment_result.score,
            'total_modules': 7,  # Modules 1-7
            'program_name': 'Social Engineering Awareness Program',
            'institution': 'Mapúa Malayan Digital College'
        }
        
        return render_template('certificate.html', **certificate_data)
    except Exception as e:
        return f"Error generating certificate: {str(e)}"

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
        
        # Calculate average score professionally from actual assessment results
        average_score = 0
        if completed_modules > 0:
            # Get all passed knowledge check results for this user
            passed_assessments = AssessmentResult.query.filter_by(
                user_id=current_user.id,
                assessment_type='knowledge_check',
                passed=True
            ).all()
            
            if passed_assessments:
                # Calculate average from actual assessment scores
                total_assessment_score = sum(assessment.score for assessment in passed_assessments)
                average_score = round(total_assessment_score / len(passed_assessments), 1)
            else:
                # Fallback: if no passed assessments, use the old method but with better logic
                average_score = round((total_score / completed_modules), 1) if completed_modules > 0 else 0
        
        # Calculate which modules are accessible based on prerequisites
        accessible_modules = []
        for module_id in range(1, 9):  # Modules 1-8
            is_accessible = check_module_prerequisites(current_user.id, module_id)
            accessible_modules.append(is_accessible)
        
        dashboard_data = {
            'completed_modules': completed_modules,
            'total_score': total_score,
            'average_score': average_score,
            'simulations_completed': simulations_completed,
            'accessible_modules': accessible_modules
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

# Database initialization with data preservation
def init_db():
    """Initialize database with migration support and data preservation"""
    try:
        # Check if database exists and has tables
        with app.app_context():
            # Test if we can connect to existing database
            try:
                # Try to query existing tables
                existing_tables = db.engine.table_names()
                print("🔍 Checking existing database structure...")
                
                if existing_tables:
                    print(f"✅ Found existing database with {len(existing_tables)} tables")
                    
                    # Check if all required tables exist
                    required_tables = ['user', 'module', 'knowledge_check_question', 'final_assessment_question', 
                                     'user_progress', 'assessment_result', 'simulation_result', 'feedback_survey']
                    
                    missing_tables = []
                    for table in required_tables:
                        if table not in existing_tables:
                            missing_tables.append(table)
                    
                    if missing_tables:
                        print(f"⚠️  Missing tables: {missing_tables}")
                        print("🔧 Creating missing tables only...")
                        db.create_all()
                        print("✅ Missing tables created successfully")
                        
                        # Initialize only missing data
                        initialize_missing_data()
                    else:
                        print("✅ All required tables exist - preserving existing data")
                        # Only initialize data if tables are empty
                        initialize_missing_data()
                else:
                    print("📝 Creating new database...")
                    db.create_all()
                    print("✅ New database created successfully")
                    initialize_all_data()
                    
            except Exception as e:
                print(f"⚠️  Database connection issue: {e}")
                print("📝 Creating new database...")
                db.create_all()
                print("✅ New database created successfully")
                initialize_all_data()
                
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        raise

def initialize_missing_data():
    """Initialize only missing data without affecting existing data"""
    try:
        # Check and create admin user only if it doesn't exist
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            print("👤 Creating admin user...")
            admin_user = User(
                username='admin',
                email='admin@socialengineering.com',
                password_hash=generate_password_hash('admin123'),
                full_name='System Administrator',
                specialization='Information Technology',
                year_level='Graduate'
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Admin user created")
        else:
            print("✅ Admin user already exists")

        # Check and create modules only if they don't exist
        existing_modules = Module.query.count()
        if existing_modules == 0:
            print("📚 Creating modules...")
            create_default_modules()
            print("✅ Modules created")
        else:
            print(f"✅ {existing_modules} modules already exist")

        # Check and create questions only if they don't exist
        existing_questions = KnowledgeCheckQuestion.query.count()
        if existing_questions == 0:
            print("❓ Creating knowledge check questions...")
            create_default_questions()
            print("✅ Knowledge check questions created")
        else:
            print(f"✅ {existing_questions} knowledge check questions already exist")

        # Check and create final assessment questions only if they don't exist
        existing_final_questions = FinalAssessmentQuestion.query.count()
        if existing_final_questions == 0:
            print("🎯 Creating final assessment questions...")
            create_default_final_questions()
            print("✅ Final assessment questions created")
        else:
            print(f"✅ {existing_final_questions} final assessment questions already exist")
            
    except Exception as e:
        print(f"❌ Error initializing missing data: {e}")
        db.session.rollback()
        raise

def initialize_all_data():
    """Initialize all data for new database"""
    try:
        # Check if admin user already exists
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            print("👤 Creating admin user...")
            admin_user = User(
                username='admin',
                email='admin@socialengineering.com',
                password_hash=generate_password_hash('admin123'),
                full_name='System Administrator',
                specialization='Information Technology',
                year_level='Graduate'
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Admin user created")
        else:
            print("✅ Admin user already exists")
        
        # Create modules if they don't exist
        if Module.query.count() == 0:
            print("📚 Creating modules...")
            modules_data = [
                {
                    'id': 1,
                    'title': 'Introduction to Social Engineering',
                    'description': 'Understanding the basics of social engineering and its psychological foundations.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-brain"></i> Introduction to Social Engineering</h2>
                    <p class="lead">Understanding the psychological manipulation techniques used by cyber attackers.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Define social engineering and its role in cybersecurity</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand the psychological principles behind social engineering</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common social engineering tactics</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn basic defense strategies</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Social Engineering?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Social Engineering</strong> is the art of manipulating people into performing actions or divulging confidential information. Unlike technical hacking, social engineering relies on human psychology and social interaction to achieve malicious goals.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">98%</div>
                        <div class="stat-label">of cyber attacks involve social engineering</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">90%</div>
                        <div class="stat-label">of successful data breaches start with social engineering</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">$6.9B</div>
                        <div class="stat-label">estimated annual cost of social engineering attacks</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-psychology"></i> Psychological Principles</h3>
                
                <div class="psychology-grid">
                    <div class="psychology-card">
                        <div class="psychology-icon">
                            <i class="fas fa-handshake"></i>
                        </div>
                        <h4>Authority</h4>
                        <p>People tend to obey authority figures, even when the authority is fake or questionable.</p>
                    </div>
                    
                    <div class="psychology-card">
                        <div class="psychology-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <h4>Social Proof</h4>
                        <p>Individuals look to others' behavior to determine their own actions in uncertain situations.</p>
                    </div>
                    
                    <div class="psychology-card">
                        <div class="psychology-icon">
                            <i class="fas fa-gift"></i>
                        </div>
                        <h4>Reciprocity</h4>
                        <p>People feel obligated to return favors, even when the initial "favor" was unsolicited.</p>
                    </div>
                    
                    <div class="psychology-card">
                        <div class="psychology-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Urgency</h4>
                        <p>Creating time pressure reduces rational thinking and increases compliance.</p>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Attack Vectors</h3>
                
                <div class="attack-types">
                    <div class="attack-card">
                        <div class="attack-header">
                            <i class="fas fa-envelope"></i>
                            <h4>Email Attacks</h4>
                        </div>
                        <p>Phishing emails that appear to come from legitimate sources, designed to trick recipients into clicking malicious links or providing sensitive information.</p>
                    </div>
                    
                    <div class="attack-card">
                        <div class="attack-header">
                            <i class="fas fa-phone"></i>
                            <h4>Phone Calls</h4>
                        </p>Vishing (voice phishing) where attackers call victims pretending to be from legitimate organizations to extract information.</p>
                    </div>
                    
                    <div class="attack-card">
                        <div class="attack-header">
                            <i class="fas fa-user-tie"></i>
                            <h4>Impersonation</h4>
                        </div>
                        <p>Attackers pretend to be someone they're not, such as IT support, bank officials, or company executives.</p>
                    </div>
                    
                    <div class="attack-card">
                        <div class="attack-header">
                            <i class="fas fa-usb"></i>
                            <h4>Physical Baiting</h4>
                        </div>
                        <p>Leaving infected USB drives or other physical devices in public places to tempt people into using them.</p>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-shield-alt"></i> Defense Strategies</h3>
                
                <div class="defense-grid">
                    <div class="defense-item">
                        <div class="defense-icon">
                            <i class="fas fa-eye"></i>
                        </div>
                        <h4>Be Skeptical</h4>
                        <p>Question unexpected requests, especially those involving sensitive information or urgent action.</p>
                    </div>
                    
                    <div class="defense-item">
                        <div class="defense-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <h4>Verify Independently</h4>
                        <p>Contact the organization directly using known contact information, not information provided in suspicious communications.</p>
                    </div>
                    
                    <div class="defense-item">
                        <div class="defense-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                    
                    <div class="defense-item">
                        <div class="defense-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-brain"></i>
                        </div>
                        <h4>Human Factor</h4>
                        <p>Social engineering targets human psychology, not technical vulnerabilities.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h4>Growing Threat</h4>
                        <p>Social engineering attacks are increasing in frequency and sophistication.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Awareness is Key</h4>
                        <p>Education and awareness are the first line of defense against social engineering.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <h4>Everyone is a Target</h4>
                        <p>No organization or individual is immune to social engineering attacks.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 2,
                    'title': 'Types of Social Engineering Attacks',
                    'description': 'Exploring different social engineering techniques and attack methods.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-mask"></i> Types of Social Engineering Attacks</h2>
                    <p class="lead">Explore the various techniques attackers use to manipulate people and gain unauthorized access.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Identify different types of social engineering attacks</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand the psychology behind each attack type</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize warning signs and red flags</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn defensive strategies for each attack type</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-envelope"></i> Phishing Attacks</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-fish"></i>
                            <h4>What is Phishing?</h4>
                        </div>
                        <p>Phishing is the most common social engineering attack, where attackers send fraudulent messages designed to trick people into revealing sensitive information or downloading malicious software.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">90%</div>
                        <div class="stat-label">of social engineering attacks are phishing attacks</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">3.4B</div>
                        <div class="stat-label">phishing emails sent daily worldwide</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">25%</div>
                        <div class="stat-label">of phishing emails are opened by recipients</div>
                    </div>
                </div>

                <div class="phishing-types">
                    <div class="type-card">
                        <div class="type-header email">
                            <i class="fas fa-envelope"></i>
                            <h4>Email Phishing</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Fraudulent emails that appear to come from legitimate sources.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Urgent requests for action</li>
                                    <li>Requests for sensitive information</li>
                                    <li>Suspicious sender addresses</li>
                                    <li>Poor grammar or spelling</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="type-card">
                        <div class="type-header spear">
                            <i class="fas fa-crosshairs"></i>
                            <h4>Spear Phishing</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Targeted attacks against specific individuals or organizations. The key difference from regular phishing is that spear phishing uses personalized information about the target.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Personalized information about you</li>
                                    <li>References to recent events</li>
                                    <li>Appears to come from known contacts</li>
                                    <li>Requests for unusual actions</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="type-card">
                        <div class="type-header whaling">
                            <i class="fas fa-crown"></i>
                            <h4>Whaling</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Phishing attacks targeting high-level executives and decision-makers.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Targets senior management</li>
                                    <li>Requests for financial transfers</li>
                                    <li>Confidential business matters</li>
                                    <li>Urgent executive decisions</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-phone"></i> Vishing (Voice Phishing)</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-phone-alt"></i>
                            <h4>Voice-Based Social Engineering</h4>
                        </div>
                        <p>Vishing attacks use phone calls to manipulate victims into providing sensitive information or performing actions that benefit the attacker.</p>
                    </div>
                </div>

                <div class="vishing-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-bank"></i>
                            <h4>Bank Impersonation</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from your bank's security department, reporting suspicious activity on your account.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Requests for account verification</li>
                                <li>Asks for PIN or password</li>
                                <li>Creates sense of urgency</li>
                                <li>Won't let you call back</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-tools"></i>
                            <h4>Technical Support Scam</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from Microsoft or Apple support, saying your computer has been infected with viruses.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Claims to detect problems remotely</li>
                                <li>Requests remote access to your computer</li>
                                <li>Asks for payment for "services"</li>
                                <li>Creates fear about data loss</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-user-tie"></i> Pretexting</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-theater-masks"></i>
                            <h4>Creating False Scenarios</h4>
                        </div>
                        <p>Pretexting involves creating a fabricated scenario to obtain information from a target. Attackers build trust by pretending to be someone they're not.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">5%</div>
                        <div class="stat-label">of social engineering attacks are pretexting</div>
                    </div>
                </div>

                <div class="pretexting-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-id-card"></i>
                            <h4>Identity Verification</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from HR or IT, needing to verify employee information for "system updates."</p>

                            <h5>Information Sought:</h5>
                            <ul>
                                <li>Employee ID numbers</li>
                                <li>Date of birth</li>
                                <li>Social Security numbers</li>
                                <li>Password resets</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-clipboard-list"></i>
                            <h4>Survey Scams</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be conducting a legitimate survey or research study, asking for personal information.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Asks for sensitive personal data</li>
                                <li>Offers rewards for participation</li>
                                <li>Refuses to provide company details</li>
                                <li>Creates pressure to participate</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-handshake"></i> Baiting</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-bait"></i>
                            <h4>Physical and Digital Lures</h4>
                        </div>
                        <p>Baiting attacks use physical or digital "bait" to lure victims into a trap. The bait is designed to trigger human curiosity and greed.</p>
                    </div>
                </div>

                <div class="baiting-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-usb"></i>
                            <h4>USB Drop Attack</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Attackers leave infected USB drives in public places, hoping someone will plug them into a computer.</p>

                            <h5>Defense Strategy:</h5>
                            <ul>
                                <li>Never plug in unknown USB devices</li>
                                <li>Disable autorun on computers</li>
                                <li>Use USB security policies</li>
                                <li>Train employees on risks</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-gift"></i>
                            <h4>Digital Baiting</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Attackers offer free software, games, or other digital content that contains malware.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Too good to be true offers</li>
                                <li>Requests for personal information</li>
                                <li>Unknown or suspicious sources</li>
                                <li>Pressure to act quickly</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-users"></i> Quid Pro Quo</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-exchange-alt"></i>
                            <h4>Something for Something</h4>
                        </div>
                        <p>Quid pro quo attacks promise a benefit in exchange for information or access. Attackers exploit the human tendency to reciprocate favors.</p>
                    </div>
                </div>

                <div class="quid-pro-quo-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-laptop"></i>
                            <h4>IT Support Scam</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be IT support offering to "fix" your computer problems in exchange for remote access.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Unsolicited support calls</li>
                                <li>Requests for remote access</li>
                                <li>Claims to detect problems you haven't noticed</li>
                                <li>Demands immediate action</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-ticket-alt"></i>
                            <h4>Prize Scams</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims you've won a prize or lottery, but requires personal information to claim it.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Unsolicited prize notifications</li>
                                <li>Requests for bank account information</li>
                                <li>Demands for upfront fees</li>
                                <li>Pressure to act immediately</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-door-open"></i> Tailgating</h3>

                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-door-open"></i>
                            <h4>Physical Access Through Social Engineering</h4>
                        </div>
                        <p>Tailgating occurs when an unauthorized person follows an authorized person into a restricted area by exploiting their courtesy or lack of awareness.</p>
                    </div>
                </div>

                <div class="tailgating-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-building"></i>
                            <h4>Office Building Access</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>An attacker waits near a secure entrance and follows an employee through the door, pretending to be in a hurry or carrying items.</p>

                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Person without proper ID badge</li>
                                <li>Following too closely</li>
                                <li>Carrying items to appear legitimate</li>
                                <li>Acting rushed or distracted</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="example-content">
                            <h5>Prevention:</h5>
                            <ul>
                                <li>Always verify ID badges</li>
                                <li>Don't hold doors for unknown people</li>
                                <li>Report suspicious behavior</li>
                                <li>Use mantraps or turnstiles</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>

                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <h4>Phishing is Most Common</h4>
                        <p>90% of social engineering attacks are phishing attacks, making it the primary threat.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <h4>Voice Attacks are Effective</h4>
                        <p>Vishing can be more convincing than email due to human voice interaction.</p>    
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-mask"></i>
                        </div>
                        <h4>Pretexting Builds Trust</h4>
                        <p>Attackers create believable scenarios to establish credibility.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 3,
                    'title': 'Phishing Detection and Prevention',
                    'description': 'Identifying and defending against phishing attacks.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-shield-alt"></i> Phishing Detection and Prevention</h2>
                    <p class="lead">Learning how to identify and defend against phishing attacks.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common phishing indicators</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand how phishing attacks work</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn effective defense strategies</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Practice safe browsing habits</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Phishing?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Phishing</strong> is a type of social engineering attack where attackers send fraudulent messages designed to trick people into revealing sensitive information, such as passwords, credit card numbers, or other personal data.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">90%</div>
                        <div class="stat-label">of successful data breaches start with phishing</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">25%</div>
                        <div class="stat-label">of phishing emails are opened by recipients</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">10%</div>
                        <div class="stat-label">of recipients provide sensitive information</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Phishing Indicators</h3>
                
                <div class="phishing-indicators">
                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-envelope"></i>
                            <h4>Email Phishing</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Suspicious Links:</strong> Clickable links that are misspelled, use suspicious domains, or have suspicious formatting.</p>
                            <p><strong>Urgent Requests:</strong> Messages that create a sense of urgency, such as "Your account has been compromised" or "Your password needs to be reset immediately."</p>
                            <p><strong>Poor Grammar/Spelling:</strong> Common in fraudulent emails, especially those impersonating legitimate organizations.</p>
                            <p><strong>Unsolicited Attachments:</strong> Emails that unexpectedly request you to open or download files.</p>
                        </div>
                    </div>

                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Be Skeptical:</strong> Question unexpected requests, especially those involving sensitive information or urgent action.</p>
                            <p><strong>Verify Independently:</strong> Contact the organization directly using known contact information, not information provided in suspicious communications.</p>
                            <p><strong>Use Multi-Factor Authentication:</strong> Where available, enable two-factor authentication for all accounts.</p>
                            <p><strong>Keep Software Updated:</strong> Regularly update your operating system, browser, and security software.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <h4>Be Aware of Phishing</h4>
                        <p>Recognize common indicators and avoid clicking suspicious links.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Sensitive Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 4,
                    'title': 'Vishing and Voice-Based Attacks',
                    'description': 'Understanding and defending against voice-based social engineering.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-phone"></i> Vishing and Voice-Based Attacks</h2>
                    <p class="lead">Understanding and defending against voice-based social engineering attacks.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common vishing indicators</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand how vishing attacks work</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn effective defense strategies</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Practice safe browsing habits</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Vishing?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Vishing</strong> (Voice Phishing) is a social engineering attack that uses phone calls to manipulate victims into providing sensitive information or performing actions that benefit the attacker.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">3.4B</div>
                        <div class="stat-label">phishing emails sent daily worldwide</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">25%</div>
                        <div class="stat-label">of phishing emails are opened by recipients</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">10%</div>
                        <div class="stat-label">of recipients provide sensitive information</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Vishing Indicators</h3>
                
                <div class="vishing-indicators">
                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-phone"></i>
                            <h4>Voice-Based Social Engineering</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Suspicious Calls:</strong> Calls that claim to be from legitimate organizations, but use suspicious numbers or threaten legal action.</p>
                            <p><strong>Urgent Requests:</strong> Calls that create a sense of urgency, such as "Your account has been compromised" or "Your password needs to be reset immediately."</p>
                            <p><strong>Poor Grammar/Spelling:</strong> Common in fraudulent calls, especially those impersonating legitimate organizations.</p>
                            <p><strong>Won't Let You Speak:</strong> Attackers often hang up or refuse to let you speak to a representative.</p>
                        </div>
                    </div>

                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Be Skeptical:</strong> Question unexpected requests, especially those involving sensitive information or urgent action.</p>
                            <p><strong>Verify Independently:</strong> Contact the organization directly using known contact information, not information provided in suspicious communications.</p>
                            <p><strong>Use Multi-Factor Authentication:</strong> Where available, enable two-factor authentication for all accounts.</p>
                            <p><strong>Keep Software Updated:</strong> Regularly update your operating system, browser, and security software.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <h4>Be Aware of Vishing</h4>
                        <p>Recognize common indicators and avoid clicking suspicious links.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Sensitive Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 5,
                    'title': 'Physical Social Engineering',
                    'description': 'Defending against in-person manipulation techniques.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-user-tie"></i> Physical Social Engineering</h2>
                    <p class="lead">Defending against in-person manipulation techniques.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common physical social engineering indicators</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand how physical social engineering attacks work</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn effective defense strategies</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Practice safe browsing habits</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Physical Social Engineering?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Physical Social Engineering</strong> involves manipulating people in physical spaces to gain unauthorized access or information. This can include tailgating, dumpster diving, and other techniques.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">10%</div>
                        <div class="stat-label">of data breaches involve physical theft</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">50%</div>
                        <div class="stat-label">of data breaches start with a physical compromise</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Physical Social Engineering Indicators</h3>
                
                <div class="physical-indicators">
                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-door-open"></i>
                            <h4>Tailgating</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Following Too Closely:</strong> Someone who seems to be following you or is in a hurry, often to distract you.</p>
                            <p><strong>Person Without Proper ID:</strong> Someone who doesn't have a proper ID badge or identification.</p>
                            <p><strong>Acting Rushed or Distracted:</strong> Someone who is acting in a way that suggests they are in a hurry or are distracted.</p>
                        </div>
                    </div>

                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Always Verify ID Badges:</strong> Always ask for a badge or identification to enter a secure area.</p>
                            <p><strong>Don't Hold Doors:</strong> Don't hold doors for people you don't know or who are not authorized to be there.</p>
                            <p><strong>Report Suspicious Behavior:</strong> If you see someone acting suspiciously, report it to security immediately.</p>
                            <p><strong>Use Mantraps or Turnstiles:</strong> Where appropriate, use physical security measures to control access.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-door-open"></i>
                        </div>
                        <h4>Be Aware of Physical Social Engineering</h4>
                        <p>Recognize common indicators and avoid following people you don't know.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Sensitive Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 6,
                    'title': 'Advanced Defense Strategies',
                    'description': 'Implementing comprehensive social engineering defenses.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-shield-alt"></i> Advanced Defense Strategies</h2>
                    <p class="lead">Implementing comprehensive social engineering defenses.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common advanced social engineering indicators</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand how advanced social engineering attacks work</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn effective defense strategies</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Practice safe browsing habits</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Advanced Social Engineering?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Advanced Social Engineering</strong> encompasses a wide range of sophisticated techniques, including deepfakes, targeted phishing, and sophisticated impersonation.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">10%</div>
                        <div class="stat-label">of data breaches involve advanced social engineering</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">50%</div>
                        <div class="stat-label">of data breaches start with advanced social engineering</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Advanced Social Engineering Indicators</h3>
                
                <div class="advanced-indicators">
                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Be Skeptical:</strong> Question unexpected requests, especially those involving sensitive information or urgent action.</p>
                            <p><strong>Verify Independently:</strong> Contact the organization directly using known contact information, not information provided in suspicious communications.</p>
                            <p><strong>Use Multi-Factor Authentication:</strong> Where available, enable two-factor authentication for all accounts.</p>
                            <p><strong>Keep Software Updated:</strong> Regularly update your operating system, browser, and security software.</p>
                            <p><strong>Use Advanced Security Tools:</strong> Utilize advanced security tools and technologies, such as AI-powered phishing detection and behavioral analysis.</p>
                            <p><strong>Train Regularly:</strong> Stay updated with the latest social engineering trends and attack methods.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Be Aware of Advanced Social Engineering</h4>
                        <p>Recognize common indicators and avoid following people you don't know.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Sensitive Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                },
                {
                    'id': 7,
                    'title': 'Incident Response and Recovery',
                    'description': 'Responding to and recovering from social engineering attacks.',
                    'content': '''
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-first-aid"></i> Incident Response and Recovery</h2>
                    <p class="lead">Responding to and recovering from social engineering attacks.</p>
                </div>

                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize common incident response indicators</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand how to respond to social engineering incidents</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn effective recovery strategies</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Practice safe browsing habits</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Incident Response?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Incident Response</strong> is the process of detecting, investigating, and responding to incidents that threaten an organization's security.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">10%</div>
                        <div class="stat-label">of data breaches involve advanced social engineering</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">50%</div>
                        <div class="stat-label">of data breaches start with advanced social engineering</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Common Incident Response Indicators</h3>
                
                <div class="incident-indicators">
                    <div class="indicator-card">
                        <div class="indicator-header">
                            <i class="fas fa-shield-alt"></i>
                            <h4>Defense Strategies</h4>
                        </div>
                        <div class="indicator-content">
                            <p><strong>Be Skeptical:</strong> Question unexpected requests, especially those involving sensitive information or urgent action.</p>
                            <p><strong>Verify Independently:</strong> Contact the organization directly using known contact information, not information provided in suspicious communications.</p>
                            <p><strong>Use Multi-Factor Authentication:</strong> Where available, enable two-factor authentication for all accounts.</p>
                            <p><strong>Keep Software Updated:</strong> Regularly update your operating system, browser, and security software.</p>
                            <p><strong>Use Advanced Security Tools:</strong> Utilize advanced security tools and technologies, such as AI-powered phishing detection and behavioral analysis.</p>
                            <p><strong>Train Regularly:</strong> Stay updated with the latest social engineering trends and attack methods.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Be Aware of Advanced Social Engineering</h4>
                        <p>Recognize common indicators and avoid following people you don't know.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-user-shield"></i>
                        </div>
                        <h4>Protect Sensitive Information</h4>
                        <p>Never share passwords, PINs, or other sensitive information in response to unsolicited requests.</p>
                    </div>

                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <h4>Take Your Time</h4>
                        <p>Don't rush into decisions. Social engineers often create urgency to prevent rational thinking.</p>
                    </div>
                </div>
            </div>
        </div>
                    '''
                }
            ]
    
    for module_data in modules_data:
        existing_module = Module.query.filter_by(id=module_data['id']).first()
        if not existing_module:
            module = Module(**module_data)
            db.session.add(module)
    
    db.session.commit()

def create_default_questions():
    """Create default knowledge check questions if they don't exist"""
    # Module 1 questions
    module1_questions = [
        {
            'module_id': 1,
            'question_text': 'What percentage of cyberattacks rely on social engineering?',
            'option_a': '75%',
            'option_b': '85%',
            'option_c': '98%',
            'option_d': '90%',
            'correct_answer': 'c',
            'explanation': '98% of cyberattacks rely on social engineering, making it crucial for cybersecurity.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'Which of the following is NOT listed as a natural human behavior exploited by social engineers?',
            'option_a': 'Desire to be helpful',
            'option_b': 'Fear of getting in trouble',
            'option_c': 'Natural curiosity',
            'option_d': 'Advanced technical knowledge',
            'correct_answer': 'd',
            'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense. The other options are natural human behaviors that can be exploited.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'What is the "human factor" in cybersecurity?',
            'option_a': 'The number of people in an organization',
            'option_b': 'The tendency for human behavior to be the weakest link in security',
            'option_c': 'The cost of hiring security personnel',
            'option_d': 'The physical security of buildings',
            'correct_answer': 'b',
            'explanation': 'The "human factor" refers to how human behavior and psychology often represent the weakest link in security systems.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'What is the first step in the social engineering attack process?',
            'option_a': 'Building trust',
            'option_b': 'Information gathering',
            'option_c': 'Exploiting vulnerabilities',
            'option_d': 'Maintaining access',
            'correct_answer': 'b',
            'explanation': 'The attack process begins with information gathering, where attackers research their targets to understand vulnerabilities.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'Which psychological principle involves people feeling obligated to return favors?',
            'option_a': 'Authority',
            'option_b': 'Reciprocity',
            'option_c': 'Social proof',
            'option_d': 'Scarcity',
            'correct_answer': 'b',
            'explanation': 'Reciprocity involves feeling obligated to return favors, which social engineers exploit.',
            'question_set': 1
        }
    ]
    
    # Module 2 questions
    module2_questions = [
        {
            'module_id': 2,
            'question_text': 'What percentage of social engineering attacks are phishing attacks?',
            'option_a': '45%',
            'option_b': '55%',
            'option_c': '65%',
            'option_d': '75%',
            'correct_answer': 'c',
            'explanation': 'Phishing accounts for 65% of social engineering attacks, making it the most common type.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is the key difference between regular phishing and spear phishing?',
            'option_a': 'Spear phishing uses better grammar',
            'option_b': 'Spear phishing targets specific individuals with personalized information',
            'option_c': 'Spear phishing is always sent by email',
            'option_d': 'Spear phishing is less effective',
            'correct_answer': 'b',
            'explanation': 'Spear phishing involves targeted attacks against specific individuals or organizations. The key difference from regular phishing is that spear phishing uses personalized information about the target.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'Which of the following is NOT a common pretexting scenario?',
            'option_a': 'IT Support claiming to need account verification',
            'option_b': 'Bank representative reporting suspicious activity',
            'option_c': 'Government official requiring cooperation',
            'option_d': 'Fake lottery winner notification',
            'correct_answer': 'd',
            'explanation': 'Fake lottery winner notifications are not listed as common pretexting scenarios.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What percentage of social engineering attacks are pretexting?',
            'option_a': '10%',
            'option_b': '15%',
            'option_c': '20%',
            'option_d': '25%',
            'correct_answer': 'c',
            'explanation': 'Pretexting accounts for 20% of social engineering attacks.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is the main characteristic of baiting attacks?',
            'option_a': 'They always involve email',
            'option_b': 'They use physical media or digital lures to entice victims',
            'option_c': 'They target only executives',
            'option_d': 'They require technical skills',
            'correct_answer': 'b',
            'explanation': 'Baiting is defined as using physical media or digital lures to entice victims into taking harmful actions.',
            'question_set': 1
        }
    ]
    
    all_questions = module1_questions + module2_questions
    
    for question_data in all_questions:
        # Check if question already exists
        existing_question = KnowledgeCheckQuestion.query.filter_by(
            module_id=question_data['module_id'],
            question_text=question_data['question_text']
        ).first()
        
        if not existing_question:
            question = KnowledgeCheckQuestion(**question_data)
            db.session.add(question)
    
    db.session.commit()

def create_default_final_questions():
    """Create default final assessment questions if they don't exist"""
    # This will be populated by the populate_final_assessment.py script
    # For now, we'll create a few basic questions
    basic_questions = [
        {
            'question_text': 'What percentage of cyberattacks rely on social engineering?',
            'option_a': '75%',
            'option_b': '85%',
            'option_c': '98%',
            'option_d': '90%',
            'correct_answer': 'c',
            'explanation': '98% of cyberattacks rely on social engineering, making it crucial for cybersecurity.',
            'question_set': 1
        },
        {
            'question_text': 'Which of the following is NOT a natural human behavior exploited by social engineers?',
            'option_a': 'Desire to be helpful',
            'option_b': 'Fear of getting in trouble',
            'option_c': 'Natural curiosity',
            'option_d': 'Advanced technical knowledge',
            'correct_answer': 'd',
            'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense.',
            'question_set': 1
        }
    ]
    
    for question_data in basic_questions:
        # Check if question already exists
        existing_question = FinalAssessmentQuestion.query.filter_by(
            question_text=question_data['question_text']
        ).first()
        
        if not existing_question:
            question = FinalAssessmentQuestion(**question_data)
            db.session.add(question)
    
    db.session.commit()

if __name__ == '__main__':
    print("🚀 Initializing database with migration support...")
    init_db()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port) 