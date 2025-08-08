#!/usr/bin/env python3
"""
Simple script to add remaining modules
"""

from app import app, db, Module, KnowledgeCheckQuestion

def main():
    with app.app_context():
        # Add remaining modules
        modules_data = [
            {
                'name': 'Phishing Attacks',
                'description': 'Understanding and identifying phishing attempts',
                'content': '<h3>Phishing Attacks</h3><p>Learn to identify and defend against phishing attacks.</p>',
                'order': 3,
                'has_simulation': True,
                'simulation_type': 'phishing'
            },
            {
                'name': 'Pretexting and Impersonation',
                'description': 'Learning about pretexting techniques',
                'content': '<h3>Pretexting and Impersonation</h3><p>Understand pretexting and impersonation techniques.</p>',
                'order': 4,
                'has_simulation': True,
                'simulation_type': 'pretexting'
            },
            {
                'name': 'Baiting and Quid Pro Quo',
                'description': 'Understanding baiting and quid pro quo attacks',
                'content': '<h3>Baiting and Quid Pro Quo</h3><p>Learn about baiting and quid pro quo attacks.</p>',
                'order': 5,
                'has_simulation': True,
                'simulation_type': 'baiting'
            },
            {
                'name': 'Advanced Techniques',
                'description': 'Advanced social engineering methods',
                'content': '<h3>Advanced Techniques</h3><p>Explore advanced social engineering techniques.</p>',
                'order': 6,
                'has_simulation': True,
                'simulation_type': 'advanced'
            },
            {
                'name': 'Incident Response',
                'description': 'How to respond to social engineering incidents',
                'content': '<h3>Incident Response</h3><p>Learn proper incident response procedures.</p>',
                'order': 7,
                'has_simulation': False
            },
            {
                'name': 'Final Assessment',
                'description': 'Comprehensive evaluation of all learning outcomes',
                'content': '<h3>Final Assessment</h3><p>Complete a comprehensive assessment of all learning outcomes.</p>',
                'order': 8,
                'has_simulation': False
            }
        ]
        
        for module_data in modules_data:
            module = Module(**module_data)
            db.session.add(module)
        
        # Add basic questions for each module
        for module_id in range(3, 9):
            for i in range(5):
                question = KnowledgeCheckQuestion(
                    module_id=module_id,
                    question_text=f'Question {i+1} for Module {module_id}',
                    option_a=f'Option A for question {i+1}',
                    option_b=f'Option B for question {i+1}',
                    option_c=f'Option C for question {i+1}',
                    option_d=f'Option D for question {i+1}',
                    correct_answer='b',
                    explanation=f'Explanation for question {i+1}',
                    question_set=1
                )
                db.session.add(question)
        
        db.session.commit()
        print("✅ Added remaining modules and questions")

if __name__ == '__main__':
    main() 