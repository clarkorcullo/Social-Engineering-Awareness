import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Module, KnowledgeCheckQuestion, FinalAssessmentQuestion

def fix_assessment_questions():
    """Fix assessment questions to be based on actual module content"""
    with app.app_context():
        print("🔧 Fixing assessment questions to match module content...")
        
        # Delete problematic questions that ask for statistics not in content
        problematic_questions = [
            'What percentage of social engineering attacks are phishing attacks?',
            'What percentage of social engineering attacks are pretexting?',
            'What percentage of social engineering attacks are baiting?',
            'What percentage of social engineering attacks are quid pro quo?'
        ]
        
        for question_text in problematic_questions:
            # Delete from knowledge check questions
            KnowledgeCheckQuestion.query.filter_by(question_text=question_text).delete()
            # Delete from final assessment questions
            FinalAssessmentQuestion.query.filter_by(question_text=question_text).delete()
            print(f"❌ Deleted problematic question: {question_text}")
        
        # Create new questions based on actual module content
        new_module_questions = [
            # Module 1 questions (based on actual content)
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
                'question_text': 'What percentage of data breaches involve human error?',
                'option_a': '75%',
                'option_b': '85%',
                'option_c': '90%',
                'option_d': '95%',
                'correct_answer': 'b',
                'explanation': '85% of data breaches involve human error, highlighting the importance of social engineering awareness.',
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
                'question_text': 'What is the primary goal of social engineering?',
                'option_a': 'To steal money directly',
                'option_b': 'To manipulate people into performing actions or divulging information',
                'option_c': 'To damage computer systems',
                'option_d': 'To spread viruses',
                'correct_answer': 'b',
                'explanation': 'Social engineering is the art of manipulating people into performing actions or divulging confidential information.',
                'question_set': 1
            },
            
            # Module 2 questions (based on actual content)
            {
                'module_id': 2,
                'question_text': 'What is phishing?',
                'option_a': 'A type of fishing',
                'option_b': 'A social engineering attack that uses fraudulent emails or websites',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Phishing is a social engineering attack that uses fraudulent emails or websites to trick people into revealing sensitive information.',
                'question_set': 1
            },
            {
                'module_id': 2,
                'question_text': 'What is pretexting?',
                'option_a': 'A type of email attack',
                'option_b': 'Creating a fabricated scenario to obtain information',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Pretexting involves creating a fabricated scenario to obtain information from a target.',
                'question_set': 1
            },
            {
                'module_id': 2,
                'question_text': 'What is baiting?',
                'option_a': 'Using food to lure people',
                'option_b': 'Leaving physical devices in public places to tempt people',
                'option_c': 'A type of email attack',
                'option_d': 'A type of virus',
                'correct_answer': 'b',
                'explanation': 'Baiting involves leaving physical devices in public places to tempt people into using them.',
                'question_set': 1
            },
            {
                'module_id': 2,
                'question_text': 'What is quid pro quo?',
                'option_a': 'A type of email attack',
                'option_b': 'Offering a service in exchange for information',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Quid pro quo involves offering a service in exchange for information or access.',
                'question_set': 1
            },
            {
                'module_id': 2,
                'question_text': 'Which social engineering technique relies on human curiosity?',
                'option_a': 'Phishing',
                'option_b': 'Baiting',
                'option_c': 'Pretexting',
                'option_d': 'Quid pro quo',
                'correct_answer': 'b',
                'explanation': 'Baiting relies on human curiosity by leaving tempting devices in public places.',
                'question_set': 1
            }
        ]
        
        # Add new questions
        for question_data in new_module_questions:
            existing = KnowledgeCheckQuestion.query.filter_by(
                module_id=question_data['module_id'],
                question_text=question_data['question_text']
            ).first()
            
            if not existing:
                question = KnowledgeCheckQuestion(**question_data)
                db.session.add(question)
                print(f"✅ Added question: {question_data['question_text'][:50]}...")
        
        # Create new final assessment questions based on actual content
        new_final_questions = [
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
                'question_text': 'What percentage of data breaches involve human error?',
                'option_a': '75%',
                'option_b': '85%',
                'option_c': '90%',
                'option_d': '95%',
                'correct_answer': 'b',
                'explanation': '85% of data breaches involve human error, highlighting the importance of social engineering awareness.',
                'question_set': 1
            },
            {
                'question_text': 'What is the primary goal of social engineering?',
                'option_a': 'To steal money directly',
                'option_b': 'To manipulate people into performing actions or divulging information',
                'option_c': 'To damage computer systems',
                'option_d': 'To spread viruses',
                'correct_answer': 'b',
                'explanation': 'Social engineering is the art of manipulating people into performing actions or divulging confidential information.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is NOT a natural human behavior exploited by social engineers?',
                'option_a': 'Desire to be helpful',
                'option_b': 'Fear of getting in trouble',
                'option_c': 'Natural curiosity',
                'option_d': 'Advanced technical knowledge',
                'correct_answer': 'd',
                'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense. The other options are natural human behaviors that can be exploited.',
                'question_set': 1
            },
            {
                'question_text': 'What is phishing?',
                'option_a': 'A type of fishing',
                'option_b': 'A social engineering attack that uses fraudulent emails or websites',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Phishing is a social engineering attack that uses fraudulent emails or websites to trick people into revealing sensitive information.',
                'question_set': 1
            },
            {
                'question_text': 'What is pretexting?',
                'option_a': 'A type of email attack',
                'option_b': 'Creating a fabricated scenario to obtain information',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Pretexting involves creating a fabricated scenario to obtain information from a target.',
                'question_set': 1
            },
            {
                'question_text': 'What is baiting?',
                'option_a': 'Using food to lure people',
                'option_b': 'Leaving physical devices in public places to tempt people',
                'option_c': 'A type of email attack',
                'option_d': 'A type of virus',
                'correct_answer': 'b',
                'explanation': 'Baiting involves leaving physical devices in public places to tempt people into using them.',
                'question_set': 1
            },
            {
                'question_text': 'What is quid pro quo?',
                'option_a': 'A type of email attack',
                'option_b': 'Offering a service in exchange for information',
                'option_c': 'A type of virus',
                'option_d': 'A physical security breach',
                'correct_answer': 'b',
                'explanation': 'Quid pro quo involves offering a service in exchange for information or access.',
                'question_set': 1
            },
            {
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
                'question_text': 'Which social engineering technique relies on human curiosity?',
                'option_a': 'Phishing',
                'option_b': 'Baiting',
                'option_c': 'Pretexting',
                'option_d': 'Quid pro quo',
                'correct_answer': 'b',
                'explanation': 'Baiting relies on human curiosity by leaving tempting devices in public places.',
                'question_set': 1
            }
        ]
        
        # Add new final assessment questions
        for question_data in new_final_questions:
            existing = FinalAssessmentQuestion.query.filter_by(
                question_text=question_data['question_text']
            ).first()
            
            if not existing:
                question = FinalAssessmentQuestion(**question_data)
                db.session.add(question)
                print(f"✅ Added final assessment question: {question_data['question_text'][:50]}...")
        
        db.session.commit()
        print("✅ Assessment questions fixed successfully!")
        print("📝 All questions now based on actual module content")

if __name__ == '__main__':
    fix_assessment_questions() 