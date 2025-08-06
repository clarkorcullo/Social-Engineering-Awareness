#!/usr/bin/env python3
"""
Script to populate the database with Knowledge Check questions for each module
and Final Assessment questions.
"""

from app import app, db, KnowledgeCheckQuestion, FinalAssessmentQuestion

def populate_module_questions():
    """Populate Knowledge Check questions for each module"""
    
    # Module 1: Introduction to Social Engineering
    module1_questions = [
        {
            'module_id': 1,
            'question_text': 'What is the primary goal of social engineering?',
            'option_a': 'To gain unauthorized access to systems through technical means',
            'option_b': 'To manipulate people into giving up sensitive information or access',
            'option_c': 'To create computer viruses and malware',
            'option_d': 'To hack into computer networks directly',
            'correct_answer': 'b',
            'explanation': 'Social engineering focuses on manipulating human psychology rather than technical vulnerabilities.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'Which of the following is NOT a common human vulnerability exploited by social engineers?',
            'option_a': 'Desire to be helpful',
            'option_b': 'Fear of getting in trouble',
            'option_c': 'Natural curiosity',
            'option_d': 'Advanced technical knowledge',
            'correct_answer': 'd',
            'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense against social engineering.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'What makes social engineering attacks so effective?',
            'option_a': 'They use sophisticated technology',
            'option_b': 'They target human psychology and natural behaviors',
            'option_c': 'They are always anonymous',
            'option_d': 'They require no planning',
            'correct_answer': 'b',
            'explanation': 'Social engineering works because it exploits natural human behaviors and psychological tendencies.',
            'question_set': 1
        },
        {
            'module_id': 1,
            'question_text': 'Which psychological principle do social engineers often exploit?',
            'option_a': 'Authority - people tend to comply with perceived authority figures',
            'option_b': 'Random chance',
            'option_c': 'Technical expertise',
            'option_d': 'Physical strength',
            'correct_answer': 'a',
            'explanation': 'Authority is a key psychological principle that social engineers exploit to gain compliance.',
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
            'explanation': 'The human factor refers to how human behavior and psychology often represent the weakest link in security systems.',
            'question_set': 1
        }
    ]
    
    # Module 2: Types of Social Engineering Attacks
    module2_questions = [
        {
            'module_id': 2,
            'question_text': 'What is the most common form of social engineering?',
            'option_a': 'Baiting',
            'option_b': 'Phishing',
            'option_c': 'Pretexting',
            'option_d': 'Quid pro quo',
            'correct_answer': 'b',
            'explanation': 'Phishing is the most common form of social engineering, using fraudulent communications to steal information.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is spear phishing?',
            'option_a': 'Phishing using fishing metaphors',
            'option_b': 'Targeted phishing attacks against specific individuals',
            'option_c': 'Phishing using spear-like tools',
            'option_d': 'Phishing in the ocean',
            'correct_answer': 'b',
            'explanation': 'Spear phishing involves targeted attacks against specific individuals, often using personalized information.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is pretexting?',
            'option_a': 'Creating fake scenarios to obtain information',
            'option_b': 'Sending spam emails',
            'option_c': 'Hacking computer systems',
            'option_d': 'Creating fake websites',
            'correct_answer': 'a',
            'explanation': 'Pretexting involves creating fabricated scenarios or pretexts to obtain sensitive information.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is baiting in social engineering?',
            'option_a': 'Using physical media or digital lures to entice victims',
            'option_b': 'Sending threatening emails',
            'option_c': 'Creating fake social media profiles',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Baiting uses physical media (like USB drives) or digital lures to entice victims into taking harmful actions.',
            'question_set': 1
        },
        {
            'module_id': 2,
            'question_text': 'What is quid pro quo in social engineering?',
            'option_a': 'Offering a service in exchange for information or access',
            'option_b': 'Sending threatening messages',
            'option_c': 'Creating fake websites',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Quid pro quo involves offering a service or benefit in exchange for sensitive information or access.',
            'question_set': 1
        }
    ]
    
    # Module 3: Identifying Red Flags
    module3_questions = [
        {
            'module_id': 3,
            'question_text': 'Which of the following is a red flag in a suspicious email?',
            'option_a': 'Professional formatting',
            'option_b': 'Urgency and pressure to act immediately',
            'option_c': 'Clear sender information',
            'option_d': 'Proper grammar and spelling',
            'correct_answer': 'b',
            'explanation': 'Urgency and pressure to act immediately are common red flags in phishing emails.',
            'question_set': 1
        },
        {
            'module_id': 3,
            'question_text': 'What should you do if you receive a suspicious phone call?',
            'option_a': 'Provide all requested information immediately',
            'option_b': 'Hang up and call back using a known number',
            'option_c': 'Give them your password',
            'option_d': 'Transfer money as requested',
            'correct_answer': 'b',
            'explanation': 'Always hang up and call back using a known, legitimate number to verify the caller\'s identity.',
            'question_set': 1
        },
        {
            'module_id': 3,
            'question_text': 'Which is NOT a red flag in social media?',
            'option_a': 'Fake profiles with limited information',
            'option_b': 'Requests from unknown connections',
            'option_c': 'Phishing links in messages',
            'option_d': 'Professional networking opportunities',
            'correct_answer': 'd',
            'explanation': 'Professional networking opportunities are legitimate, while the other options are common red flags.',
            'question_set': 1
        },
        {
            'module_id': 3,
            'question_text': 'What is caller ID spoofing?',
            'option_a': 'Making phone calls louder',
            'option_b': 'Faking the caller ID to appear as a legitimate organization',
            'option_c': 'Recording phone calls',
            'option_d': 'Blocking unwanted calls',
            'correct_answer': 'b',
            'explanation': 'Caller ID spoofing involves faking the caller ID to make it appear as if the call is coming from a legitimate organization.',
            'question_set': 1
        },
        {
            'module_id': 3,
            'question_text': 'Which of the following is a physical security red flag?',
            'option_a': 'Authorized personnel with proper ID badges',
            'option_b': 'Unauthorized personnel in restricted areas',
            'option_c': 'Proper lighting in work areas',
            'option_d': 'Locked doors',
            'correct_answer': 'b',
            'explanation': 'Unauthorized personnel in restricted areas is a significant physical security red flag.',
            'question_set': 1
        }
    ]
    
    # Module 4: Defense Strategies
    module4_questions = [
        {
            'module_id': 4,
            'question_text': 'What is the best way to verify someone\'s identity over the phone?',
            'option_a': 'Use the phone number they provide',
            'option_b': 'Call back using a known, legitimate number',
            'option_c': 'Ask for their password',
            'option_d': 'Trust their caller ID',
            'correct_answer': 'b',
            'explanation': 'Always call back using a known, legitimate number rather than trusting the provided number.',
            'question_set': 1
        },
        {
            'module_id': 4,
            'question_text': 'What should you do with suspicious emails?',
            'option_a': 'Click all links to investigate',
            'option_b': 'Reply with your personal information',
            'option_c': 'Report them to IT and delete them',
            'option_d': 'Forward them to all your contacts',
            'correct_answer': 'c',
            'explanation': 'Suspicious emails should be reported to IT and deleted without clicking links or providing information.',
            'question_set': 1
        },
        {
            'module_id': 4,
            'question_text': 'What is two-factor authentication?',
            'option_a': 'Using two passwords',
            'option_b': 'An additional verification method beyond just a password',
            'option_c': 'Having two email accounts',
            'option_d': 'Using two computers',
            'correct_answer': 'b',
            'explanation': 'Two-factor authentication adds an additional verification method beyond just a password.',
            'question_set': 1
        },
        {
            'module_id': 4,
            'question_text': 'What should you do if someone asks for your password?',
            'option_a': 'Give it to them if they seem legitimate',
            'option_b': 'Never share your password with anyone',
            'option_c': 'Share it only with IT support',
            'option_d': 'Create a new password for them',
            'correct_answer': 'b',
            'explanation': 'Never share your password with anyone, including IT support. Legitimate IT staff will never ask for your password.',
            'question_set': 1
        },
        {
            'module_id': 4,
            'question_text': 'What should you do with unknown USB devices?',
            'option_a': 'Plug them into your computer immediately',
            'option_b': 'Never plug unknown USB devices into your computer',
            'option_c': 'Give them to IT without checking',
            'option_d': 'Format them and use them',
            'correct_answer': 'b',
            'explanation': 'Never plug unknown USB devices into your computer as they may contain malware.',
            'question_set': 1
        }
    ]
    
    # Module 5: Real-world Case Studies
    module5_questions = [
        {
            'module_id': 5,
            'question_text': 'What was the main lesson from the Target data breach?',
            'option_a': 'Target had poor security',
            'option_b': 'Third-party vendors can be entry points for attacks',
            'option_c': 'Credit cards are unsafe',
            'option_d': 'Large companies are always secure',
            'correct_answer': 'b',
            'explanation': 'The Target breach showed that third-party vendors can be entry points for attacks.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What type of attack was used in the Google and Facebook case?',
            'option_a': 'Direct hacking',
            'option_b': 'Fake invoice scam',
            'option_c': 'Phishing emails',
            'option_d': 'Physical break-in',
            'correct_answer': 'b',
            'explanation': 'The Google and Facebook case involved a fake invoice scam that stole over $100 million.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What was the Twitter hack primarily about?',
            'option_a': 'Stealing money',
            'option_b': 'Phone spear phishing',
            'option_c': 'Direct system hacking',
            'option_d': 'Physical security breach',
            'correct_answer': 'b',
            'explanation': 'The Twitter hack involved phone spear phishing to gain access to high-profile accounts.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What is a common pattern in these real-world attacks?',
            'option_a': 'They all used the same password',
            'option_b': 'They exploited trust relationships and human weaknesses',
            'option_c': 'They all happened on the same day',
            'option_d': 'They all used the same software',
            'correct_answer': 'b',
            'explanation': 'These attacks all exploited trust relationships and human weaknesses rather than technical vulnerabilities.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What was the impact of the Ubiquiti Networks attack?',
            'option_a': 'No financial loss',
            'option_b': '$46 million stolen',
            'option_c': 'Only data was stolen',
            'option_d': 'Only reputation was damaged',
            'correct_answer': 'b',
            'explanation': 'The Ubiquiti Networks attack resulted in $46 million being stolen through email impersonation.',
            'question_set': 1
        }
    ]
    
    # Module 6: Advanced Techniques
    module6_questions = [
        {
            'module_id': 6,
            'question_text': 'What is clone phishing?',
            'option_a': 'Copying legitimate emails with malicious links',
            'option_b': 'Creating fake websites',
            'option_c': 'Sending spam emails',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Clone phishing involves copying legitimate emails and replacing links with malicious ones.',
            'question_set': 1
        },
        {
            'module_id': 6,
            'question_text': 'What is an evil twin attack?',
            'option_a': 'Creating fake WiFi networks to capture data',
            'option_b': 'Sending fake emails',
            'option_c': 'Creating fake websites',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Evil twin attacks create fake WiFi networks that appear legitimate to capture user data.',
            'question_set': 1
        },
        {
            'module_id': 6,
            'question_text': 'How can deepfake technology be used in attacks?',
            'option_a': 'Creating fake voice calls from executives',
            'option_b': 'Making movies',
            'option_c': 'Improving security',
            'option_d': 'Creating art',
            'correct_answer': 'a',
            'explanation': 'Deepfake technology can be used to create fake voice calls from executives to trick employees.',
            'question_set': 1
        },
        {
            'module_id': 6,
            'question_text': 'What is social media intelligence gathering?',
            'option_a': 'Collecting information from social media profiles',
            'option_b': 'Creating fake profiles',
            'option_c': 'Posting on social media',
            'option_d': 'Blocking social media',
            'correct_answer': 'a',
            'explanation': 'Social media intelligence gathering involves collecting information from public social media profiles.',
            'question_set': 1
        },
        {
            'module_id': 6,
            'question_text': 'What is a watering hole attack?',
            'option_a': 'Compromising websites frequented by targets',
            'option_b': 'Creating fake websites',
            'option_c': 'Sending phishing emails',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Watering hole attacks compromise websites that are frequently visited by the target audience.',
            'question_set': 1
        }
    ]
    
    # Module 7: Incident Response
    module7_questions = [
        {
            'module_id': 7,
            'question_text': 'What is the first step when you suspect a social engineering attack?',
            'option_a': 'Provide more information to verify',
            'option_b': 'Stop and don\'t provide any more information',
            'option_c': 'Call the police immediately',
            'option_d': 'Delete all your accounts',
            'correct_answer': 'b',
            'explanation': 'The first step is to stop and not provide any more information to the attacker.',
            'question_set': 1
        },
        {
            'module_id': 7,
            'question_text': 'What should you document about a social engineering incident?',
            'option_a': 'Only the date and time',
            'option_b': 'All details including method of contact, information requested, and attacker\'s claimed identity',
            'option_c': 'Only the attacker\'s name',
            'option_d': 'Only the amount of money lost',
            'correct_answer': 'b',
            'explanation': 'Document all details including method of contact, information requested, and attacker\'s claimed identity.',
            'question_set': 1
        },
        {
            'module_id': 7,
            'question_text': 'What should you do with suspicious communications?',
            'option_a': 'Delete them immediately',
            'option_b': 'Preserve them as evidence',
            'option_c': 'Forward them to everyone',
            'option_d': 'Ignore them completely',
            'correct_answer': 'b',
            'explanation': 'Preserve suspicious communications as evidence for the security investigation.',
            'question_set': 1
        },
        {
            'module_id': 7,
            'question_text': 'What is the first recovery step after a social engineering incident?',
            'option_a': 'Change all passwords immediately',
            'option_b': 'Wait for IT to contact you',
            'option_c': 'Tell all your friends',
            'option_d': 'Ignore the incident',
            'correct_answer': 'a',
            'explanation': 'The first recovery step is to change all passwords immediately to prevent further access.',
            'question_set': 1
        },
        {
            'module_id': 7,
            'question_text': 'What should you do to prevent future incidents?',
            'option_a': 'Learn from the incident and share lessons with colleagues',
            'option_b': 'Forget about it completely',
            'option_c': 'Blame others for the incident',
            'option_d': 'Quit your job',
            'correct_answer': 'a',
            'explanation': 'Learn from the incident and share lessons with colleagues to prevent future attacks.',
            'question_set': 1
        }
    ]
    
    # Module 8: Final Assessment
    module8_questions = [
        {
            'module_id': 8,
            'question_text': 'What is the primary goal of social engineering?',
            'option_a': 'To gain unauthorized access through technical means',
            'option_b': 'To manipulate people into giving up sensitive information',
            'option_c': 'To create computer viruses',
            'option_d': 'To hack networks directly',
            'correct_answer': 'b',
            'explanation': 'Social engineering focuses on manipulating human psychology to gain unauthorized access.',
            'question_set': 1
        },
        {
            'module_id': 8,
            'question_text': 'Which of the following is NOT a common social engineering technique?',
            'option_a': 'Phishing',
            'option_b': 'Pretexting',
            'option_c': 'Direct system hacking',
            'option_d': 'Baiting',
            'correct_answer': 'c',
            'explanation': 'Direct system hacking is a technical attack, not a social engineering technique.',
            'question_set': 1
        },
        {
            'module_id': 8,
            'question_text': 'What should you do if you receive a suspicious email?',
            'option_a': 'Click all links to investigate',
            'option_b': 'Reply with your personal information',
            'option_c': 'Report it to IT and delete it',
            'option_d': 'Forward it to all contacts',
            'correct_answer': 'c',
            'explanation': 'Suspicious emails should be reported to IT and deleted without clicking links.',
            'question_set': 1
        },
        {
            'module_id': 8,
            'question_text': 'What is the best way to verify someone\'s identity?',
            'option_a': 'Trust their caller ID',
            'option_b': 'Use the phone number they provide',
            'option_c': 'Call back using a known legitimate number',
            'option_d': 'Ask for their password',
            'correct_answer': 'c',
            'explanation': 'Always call back using a known legitimate number to verify identity.',
            'question_set': 1
        },
        {
            'module_id': 8,
            'question_text': 'What should you do with unknown USB devices?',
            'option_a': 'Plug them into your computer',
            'option_b': 'Never plug unknown USB devices into your computer',
            'option_c': 'Format them first',
            'option_d': 'Give them to IT immediately',
            'correct_answer': 'b',
            'explanation': 'Never plug unknown USB devices into your computer as they may contain malware.',
            'question_set': 1
        }
    ]
    
    # Add all module questions
    all_module_questions = [
        module1_questions, module2_questions, module3_questions, module4_questions,
        module5_questions, module6_questions, module7_questions, module8_questions
    ]
    
    for module_questions in all_module_questions:
        for question_data in module_questions:
            question = KnowledgeCheckQuestion(**question_data)
            db.session.add(question)

def populate_final_questions():
    """Populate Final Assessment questions"""
    
    final_questions = [
        {
            'question_text': 'What is the primary goal of social engineering?',
            'option_a': 'To gain unauthorized access through technical means',
            'option_b': 'To manipulate people into giving up sensitive information',
            'option_c': 'To create computer viruses',
            'option_d': 'To hack networks directly',
            'correct_answer': 'b',
            'explanation': 'Social engineering focuses on manipulating human psychology to gain unauthorized access.',
            'question_set': 1
        },
        {
            'question_text': 'Which of the following is the most common form of social engineering?',
            'option_a': 'Baiting',
            'option_b': 'Phishing',
            'option_c': 'Pretexting',
            'option_d': 'Quid pro quo',
            'correct_answer': 'b',
            'explanation': 'Phishing is the most common form of social engineering.',
            'question_set': 1
        },
        {
            'question_text': 'What is spear phishing?',
            'option_a': 'Phishing using fishing metaphors',
            'option_b': 'Targeted phishing attacks against specific individuals',
            'option_c': 'Phishing using spear-like tools',
            'option_d': 'Phishing in the ocean',
            'correct_answer': 'b',
            'explanation': 'Spear phishing involves targeted attacks against specific individuals.',
            'question_set': 1
        },
        {
            'question_text': 'Which of the following is a red flag in a suspicious email?',
            'option_a': 'Professional formatting',
            'option_b': 'Urgency and pressure to act immediately',
            'option_c': 'Clear sender information',
            'option_d': 'Proper grammar and spelling',
            'correct_answer': 'b',
            'explanation': 'Urgency and pressure to act immediately are common red flags.',
            'question_set': 1
        },
        {
            'question_text': 'What should you do if you receive a suspicious phone call?',
            'option_a': 'Provide all requested information immediately',
            'option_b': 'Hang up and call back using a known number',
            'option_c': 'Give them your password',
            'option_d': 'Transfer money as requested',
            'correct_answer': 'b',
            'explanation': 'Always hang up and call back using a known, legitimate number.',
            'question_set': 1
        },
        {
            'question_text': 'What is two-factor authentication?',
            'option_a': 'Using two passwords',
            'option_b': 'An additional verification method beyond just a password',
            'option_c': 'Having two email accounts',
            'option_d': 'Using two computers',
            'correct_answer': 'b',
            'explanation': 'Two-factor authentication adds an additional verification method.',
            'question_set': 1
        },
        {
            'question_text': 'What should you do with unknown USB devices?',
            'option_a': 'Plug them into your computer',
            'option_b': 'Never plug unknown USB devices into your computer',
            'option_c': 'Format them first',
            'option_d': 'Give them to IT immediately',
            'correct_answer': 'b',
            'explanation': 'Never plug unknown USB devices into your computer.',
            'question_set': 1
        },
        {
            'question_text': 'What is the first step when you suspect a social engineering attack?',
            'option_a': 'Provide more information to verify',
            'option_b': 'Stop and don\'t provide any more information',
            'option_c': 'Call the police immediately',
            'option_d': 'Delete all your accounts',
            'correct_answer': 'b',
            'explanation': 'The first step is to stop and not provide any more information.',
            'question_set': 1
        },
        {
            'question_text': 'What is caller ID spoofing?',
            'option_a': 'Making phone calls louder',
            'option_b': 'Faking the caller ID to appear as a legitimate organization',
            'option_c': 'Recording phone calls',
            'option_d': 'Blocking unwanted calls',
            'correct_answer': 'b',
            'explanation': 'Caller ID spoofing involves faking the caller ID.',
            'question_set': 1
        },
        {
            'question_text': 'What should you do with suspicious emails?',
            'option_a': 'Click all links to investigate',
            'option_b': 'Reply with your personal information',
            'option_c': 'Report them to IT and delete them',
            'option_d': 'Forward them to all your contacts',
            'correct_answer': 'c',
            'explanation': 'Suspicious emails should be reported to IT and deleted.',
            'question_set': 1
        }
    ]
    
    for question_data in final_questions:
        question = FinalAssessmentQuestion(**question_data)
        db.session.add(question)

def main():
    with app.app_context():
        # Clear existing questions
        KnowledgeCheckQuestion.query.delete()
        FinalAssessmentQuestion.query.delete()
        
        # Populate questions
        populate_module_questions()
        populate_final_questions()
        
        # Commit changes
        db.session.commit()
        
        print("Successfully populated database with Knowledge Check questions!")
        print(f"Added {KnowledgeCheckQuestion.query.count()} module questions")
        print(f"Added {FinalAssessmentQuestion.query.count()} final assessment questions")

if __name__ == '__main__':
    main() 