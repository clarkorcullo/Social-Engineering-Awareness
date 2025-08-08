#!/usr/bin/env python3
"""
Script to populate Final Assessment with 25 comprehensive questions
based on actual module content that students learn
"""

import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, FinalAssessmentQuestion

def populate_final_assessment():
    with app.app_context():
        # Clear existing questions
        FinalAssessmentQuestion.query.delete()
        
        # Final Assessment Questions - All based on module content but without "in Module X" references
        questions = [
            # Module 1: Introduction to Social Engineering
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
                'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense. The other options are natural human behaviors that can be exploited.',
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
                'question_text': 'Which psychological principle involves people feeling obligated to return favors?',
                'option_a': 'Authority',
                'option_b': 'Reciprocity',
                'option_c': 'Social proof',
                'option_d': 'Scarcity',
                'correct_answer': 'b',
                'explanation': 'Reciprocity involves feeling obligated to return favors, which social engineers exploit.',
                'question_set': 1
            },

            # Module 2: Types of Social Engineering Attacks
            {
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
                'question_text': 'What is the key difference between regular phishing and spear phishing?',
                'option_a': 'Spear phishing uses better grammar',
                'option_b': 'Spear phishing targets specific individuals with personalized information',
                'option_c': 'Spear phishing is always sent by email',
                'option_d': 'Spear phishing is less effective',
                'correct_answer': 'b',
                'explanation': 'Spear phishing involves targeted attacks against specific individuals using personalized information.',
                'question_set': 1
            },
            {
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
                'question_text': 'What is the main characteristic of baiting attacks?',
                'option_a': 'They always involve email',
                'option_b': 'They use physical media or digital lures to entice victims',
                'option_c': 'They target only executives',
                'option_d': 'They require technical skills',
                'correct_answer': 'b',
                'explanation': 'Baiting is defined as using physical media or digital lures to entice victims into taking harmful actions.',
                'question_set': 1
            },

            # Module 3: Phishing Attacks
            {
                'question_text': 'What is the most common type of social engineering attack?',
                'option_a': 'Pretexting',
                'option_b': 'Phishing',
                'option_c': 'Baiting',
                'option_d': 'Quid pro quo',
                'correct_answer': 'b',
                'explanation': 'Phishing is the most common type of social engineering attack, accounting for the majority of incidents.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is a red flag for phishing emails?',
                'option_a': 'Professional formatting',
                'option_b': 'Urgent requests for action',
                'option_c': 'Clear sender information',
                'option_d': 'Proper grammar and spelling',
                'correct_answer': 'b',
                'explanation': 'Urgent requests for action are a common red flag in phishing emails, designed to pressure victims into acting quickly.',
                'question_set': 1
            },
            {
                'question_text': 'What is spear phishing?',
                'option_a': 'Phishing that uses fishing metaphors',
                'option_b': 'Targeted phishing against specific individuals or organizations',
                'option_c': 'Phishing that only targets executives',
                'option_d': 'Phishing that uses voice calls',
                'correct_answer': 'b',
                'explanation': 'Spear phishing involves targeted attacks against specific individuals or organizations using personalized information.',
                'question_set': 1
            },
            {
                'question_text': 'What is whaling?',
                'option_a': 'Phishing attacks targeting high-level executives',
                'option_b': 'Phishing attacks using whale sounds',
                'option_c': 'Phishing attacks targeting small businesses',
                'option_d': 'Phishing attacks using voice calls',
                'correct_answer': 'a',
                'explanation': 'Whaling refers to phishing attacks specifically targeting high-level executives and decision-makers.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is NOT a warning sign of phishing?',
                'option_a': 'Suspicious sender addresses',
                'option_b': 'Requests for sensitive information',
                'option_c': 'Professional company branding',
                'option_d': 'Poor grammar or spelling',
                'correct_answer': 'c',
                'explanation': 'Professional company branding is not a warning sign - it\'s actually what legitimate emails should have.',
                'question_set': 1
            },

            # Module 4: Vishing and Pretexting
            {
                'question_text': 'What is vishing?',
                'option_a': 'Voice-based phishing attacks',
                'option_b': 'Video-based phishing attacks',
                'option_c': 'Visual phishing attacks',
                'option_d': 'Virtual phishing attacks',
                'correct_answer': 'a',
                'explanation': 'Vishing stands for "voice phishing" and involves phone calls to manipulate victims.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is a common vishing scenario?',
                'option_a': 'Bank impersonation calls',
                'option_b': 'Social media messages',
                'option_c': 'Email attachments',
                'option_d': 'USB drive drops',
                'correct_answer': 'a',
                'explanation': 'Bank impersonation calls are a common vishing scenario where attackers pretend to be from financial institutions.',
                'question_set': 1
            },
            {
                'question_text': 'What is pretexting?',
                'option_a': 'Creating fake social media profiles',
                'option_b': 'Creating fabricated scenarios to obtain information',
                'option_c': 'Sending phishing emails',
                'option_d': 'Leaving USB drives in public places',
                'correct_answer': 'b',
                'explanation': 'Pretexting involves creating fabricated scenarios to obtain information from targets.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is a red flag for pretexting calls?',
                'option_a': 'Caller asks for your name',
                'option_b': 'Caller refuses to provide company details',
                'option_c': 'Caller has a professional tone',
                'option_d': 'Caller offers to help you',
                'correct_answer': 'b',
                'explanation': 'Callers who refuse to provide company details are a major red flag for pretexting attacks.',
                'question_set': 1
            },
            {
                'question_text': 'What is the main goal of pretexting?',
                'option_a': 'To sell products',
                'option_b': 'To build trust and obtain sensitive information',
                'option_c': 'To provide customer service',
                'option_d': 'To conduct surveys',
                'correct_answer': 'b',
                'explanation': 'The main goal of pretexting is to build trust and obtain sensitive information through fabricated scenarios.',
                'question_set': 1
            },

            # Module 5: Baiting and Quid Pro Quo
            {
                'question_text': 'What is baiting?',
                'option_a': 'Using physical or digital lures to entice victims',
                'option_b': 'Sending phishing emails',
                'option_c': 'Making phone calls',
                'option_d': 'Creating fake websites',
                'correct_answer': 'a',
                'explanation': 'Baiting involves using physical or digital lures to entice victims into taking harmful actions.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is an example of physical baiting?',
                'option_a': 'USB drives left in public places',
                'option_b': 'Phishing emails',
                'option_c': 'Phone calls',
                'option_d': 'Fake websites',
                'correct_answer': 'a',
                'explanation': 'USB drives left in public places are a common example of physical baiting.',
                'question_set': 1
            },
            {
                'question_text': 'What is quid pro quo?',
                'option_a': 'Something for something - offering benefits in exchange for information',
                'option_b': 'A type of phishing email',
                'option_c': 'A security protocol',
                'option_d': 'A type of malware',
                'correct_answer': 'a',
                'explanation': 'Quid pro quo means "something for something" and involves offering benefits in exchange for information or access.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is a common quid pro quo scenario?',
                'option_a': 'IT support offering to fix your computer for remote access',
                'option_b': 'Receiving a phishing email',
                'option_c': 'Finding a USB drive',
                'option_d': 'Getting a phone call from your bank',
                'correct_answer': 'a',
                'explanation': 'IT support offering to fix your computer in exchange for remote access is a common quid pro quo scenario.',
                'question_set': 1
            },
            {
                'question_text': 'What is the main psychological principle exploited in quid pro quo attacks?',
                'option_a': 'Fear',
                'option_b': 'Reciprocity',
                'option_c': 'Authority',
                'option_d': 'Urgency',
                'correct_answer': 'b',
                'explanation': 'Quid pro quo attacks exploit the principle of reciprocity - the human tendency to return favors.',
                'question_set': 1
            },

            # Module 6: Defense Strategies
            {
                'question_text': 'What is the first line of defense against social engineering?',
                'option_a': 'Technical controls',
                'option_b': 'Awareness and training',
                'option_c': 'Firewalls',
                'option_d': 'Antivirus software',
                'correct_answer': 'b',
                'explanation': 'Awareness and training are the first line of defense against social engineering attacks.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is NOT a recommended defense strategy?',
                'option_a': 'Verifying requests through known channels',
                'option_b': 'Sharing passwords with trusted colleagues',
                'option_c': 'Being suspicious of urgent requests',
                'option_d': 'Training employees on red flags',
                'correct_answer': 'b',
                'explanation': 'Sharing passwords with colleagues is never recommended, even if they are trusted.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do if you receive a suspicious email?',
                'option_a': 'Click on links to verify them',
                'option_b': 'Reply to ask for clarification',
                'option_c': 'Report it to IT security',
                'option_d': 'Forward it to colleagues',
                'correct_answer': 'c',
                'explanation': 'Suspicious emails should be reported to IT security rather than interacted with.',
                'question_set': 1
            },
            {
                'question_text': 'What is the best way to verify a caller\'s identity?',
                'option_a': 'Ask them to provide your personal information',
                'option_b': 'Call back using a known number',
                'option_c': 'Give them the information they request',
                'option_d': 'Trust their professional tone',
                'correct_answer': 'b',
                'explanation': 'The best way to verify a caller\'s identity is to call back using a known, legitimate number.',
                'question_set': 1
            },
            {
                'question_text': 'What is the purpose of security awareness training?',
                'option_a': 'To make employees paranoid',
                'option_b': 'To teach employees to recognize and respond to threats',
                'option_c': 'To reduce IT support calls',
                'option_d': 'To increase productivity',
                'correct_answer': 'b',
                'explanation': 'Security awareness training teaches employees to recognize and respond appropriately to security threats.',
                'question_set': 1
            },

            # Module 7: Real-World Applications
            {
                'question_text': 'What percentage of data breaches involve human error?',
                'option_a': '65%',
                'option_b': '75%',
                'option_c': '85%',
                'option_d': '95%',
                'correct_answer': 'c',
                'explanation': '85% of data breaches involve human error, highlighting the importance of social engineering awareness.',
                'question_set': 1
            },
            {
                'question_text': 'What is the annual cost of social engineering attacks?',
                'option_a': '$2.9 billion',
                'option_b': '$4.9 billion',
                'option_c': '$6.9 billion',
                'option_d': '$8.9 billion',
                'correct_answer': 'c',
                'explanation': 'Social engineering attacks cost organizations approximately $6.9 billion annually.',
                'question_set': 1
            },
            {
                'question_text': 'Which industry is most targeted by social engineering attacks?',
                'option_a': 'Healthcare',
                'option_b': 'Finance',
                'option_c': 'Technology',
                'option_d': 'Retail',
                'correct_answer': 'a',
                'explanation': 'Healthcare is the most targeted industry by social engineering attacks due to valuable patient data.',
                'question_set': 1
            },
            {
                'question_text': 'What is the most effective way to protect against social engineering?',
                'option_a': 'Technical controls alone',
                'option_b': 'Awareness training alone',
                'option_c': 'A combination of technical controls and awareness training',
                'option_d': 'Hiring more security personnel',
                'correct_answer': 'c',
                'explanation': 'The most effective protection combines technical controls with comprehensive awareness training.',
                'question_set': 1
            },
            {
                'question_text': 'What should organizations do after a social engineering incident?',
                'option_a': 'Ignore it to avoid embarrassment',
                'option_b': 'Use it as a learning opportunity and improve defenses',
                'option_c': 'Blame the victim',
                'option_d': 'Hide the incident from stakeholders',
                'correct_answer': 'b',
                'explanation': 'Organizations should use incidents as learning opportunities to improve their security defenses.',
                'question_set': 1
            }
        ]
        
        # Add all questions
        for question_data in questions:
            question = FinalAssessmentQuestion(**question_data)
            db.session.add(question)
        
        db.session.commit()
        print(f"✅ Successfully created {len(questions)} final assessment questions!")

if __name__ == "__main__":
    populate_final_assessment() 