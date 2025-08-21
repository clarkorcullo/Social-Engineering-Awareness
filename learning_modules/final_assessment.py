"""
Final Assessment: Comprehensive Social Engineering Awareness
Content and knowledge check questions for the Final Assessment
"""

from typing import List, Dict, Any

class FinalAssessmentContent:
    """Content for Final Assessment: Comprehensive Social Engineering Awareness"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Final Assessment - Comprehensive Social Engineering Awareness',
            'description': 'Comprehensive assessment covering all aspects of social engineering awareness and prevention',
            'content': '''
                <h2>Final Assessment Overview</h2>
                
                <p>This final assessment will test your comprehensive understanding of social engineering awareness, prevention strategies, and incident response. The assessment covers all the topics from Modules 1-7.</p>
                
                <h3>Assessment Structure:</h3>
                <ul>
                    <li><strong>Total Questions:</strong> 25 comprehensive questions</li>
                    <li><strong>Time Limit:</strong> 60 minutes</li>
                    <li><strong>Passing Score:</strong> 80% (20 out of 25 correct)</li>
                    <li><strong>Question Types:</strong> Multiple choice covering all modules</li>
                    <li><strong>Topics Covered:</strong> All aspects of social engineering awareness</li>
                    <li><strong>Retake Policy:</strong> 3 attempts every 48 hours if failed</li>
                </ul>
                
                <h3>Topics Covered:</h3>
                <ul>
                    <li><strong>Module 1:</strong> Introduction to Social Engineering</li>
                    <li><strong>Module 2:</strong> Types of Social Engineering Attacks</li>
                    <li><strong>Module 3:</strong> Phishing Detection and Prevention</li>
                    <li><strong>Module 4:</strong> Password Security and Authentication</li>
                    <li><strong>Module 5:</strong> Social Media Security</li>
                    <li><strong>Module 6:</strong> Physical Security and Social Engineering</li>
                    <li><strong>Module 7:</strong> Incident Response and Reporting</li>
                </ul>
                
                <h3>Assessment Guidelines:</h3>
                <ul>
                    <li><strong>Read carefully:</strong> Pay attention to all details in each question</li>
                    <li><strong>Think critically:</strong> Consider the best security practices</li>
                    <li><strong>Apply knowledge:</strong> Use what you've learned from all modules</li>
                    <li><strong>Choose the best answer:</strong> Select the most appropriate response</li>
                    <li><strong>Manage your time:</strong> Don't spend too long on any single question</li>
                </ul>
                
                <h3>Retake Policy:</h3>
                <ul>
                    <li><strong>Maximum Attempts:</strong> 3 attempts every 48 hours</li>
                    <li><strong>Question Randomization:</strong> Different questions for each retake</li>
                    <li><strong>No Same Questions:</strong> Questions will not repeat from previous attempts</li>
                    <li><strong>48-Hour Cooldown:</strong> Wait 48 hours after 3 failed attempts</li>
                </ul>
                
                <h3>After Passing the Assessment:</h3>
                <ul>
                    <li><strong>Satisfaction Survey:</strong> Mandatory survey must be completed</li>
                    <li><strong>Certification:</strong> Certificate generated only after survey completion</li>
                    <li><strong>No Survey = No Certificate:</strong> Survey is compulsory for certification</li>
                </ul>
                
                <h3>Success Tips:</h3>
                <ul>
                    <li><strong>Review key concepts:</strong> Refresh your memory on important topics</li>
                    <li><strong>Consider real-world scenarios:</strong> Think about practical applications</li>
                    <li><strong>Focus on prevention:</strong> Remember that prevention is better than reaction</li>
                    <li><strong>Think about security:</strong> Always prioritize security best practices</li>
                    <li><strong>Stay calm:</strong> Take your time and think clearly</li>
                </ul>
                
                <p><strong>Good luck with your final assessment! Remember, the goal is not just to pass the test, but to become more security-aware and protect yourself and others from social engineering attacks.</strong></p>
            ''',
            'learning_objectives': [
                'Demonstrate comprehensive understanding of social engineering awareness',
                'Apply knowledge from all modules to real-world scenarios',
                'Show proficiency in prevention and response strategies',
                'Achieve certification in social engineering awareness'
            ],
            'estimated_time': 60,  # minutes
            'difficulty_level': 'advanced',
            'question_count': 25,
            'passing_threshold': 80.0,
            'max_retakes': 3,
            'retake_cooldown_hours': 48
        }

class FinalAssessmentQuestions:
    """Knowledge check questions for Final Assessment"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Final Assessment (25 questions from all modules)"""
        return [
            # Module 1 Questions (4 questions)
            {
                'question_text': 'What is the primary goal of social engineering attacks?',
                'option_a': 'To damage computer hardware',
                'option_b': 'To manipulate people into revealing information or performing actions',
                'option_c': 'To improve network security',
                'option_d': 'To create new software programs',
                'correct_answer': 'b',
                'explanation': 'The primary goal of social engineering is to manipulate people into revealing confidential information or performing security-compromising actions.',
                'question_set': 1,
                'module_source': 1
            },
            {
                'question_text': 'What is the "weakest link" in most security systems?',
                'option_a': 'Firewall configuration',
                'option_b': 'Human psychology and behavior',
                'option_c': 'Password strength',
                'option_d': 'Network infrastructure',
                'correct_answer': 'b',
                'explanation': 'Human psychology and behavior is often considered the weakest link in security systems.',
                'question_set': 1,
                'module_source': 1
            },
            {
                'question_text': 'Why is social engineering considered effective against organizations?',
                'option_a': 'Because it requires expensive equipment',
                'option_b': 'Because it targets the weakest link: human psychology',
                'option_c': 'Because it only works on small companies',
                'option_d': 'Because it requires advanced technical skills',
                'correct_answer': 'b',
                'explanation': 'Social engineering targets human psychology, which is often the weakest link in security systems.',
                'question_set': 1,
                'module_source': 1
            },
            {
                'question_text': 'Which of the following is NOT a common social engineering technique?',
                'option_a': 'Building false trust',
                'option_b': 'Creating urgency',
                'option_c': 'Impersonating authority figures',
                'option_d': 'Direct network hacking',
                'correct_answer': 'd',
                'explanation': 'Direct network hacking is a technical attack method, not a social engineering technique.',
                'question_set': 1,
                'module_source': 1
            },
            
            # Module 2 Questions (4 questions)
            {
                'question_text': 'What is the most common type of social engineering attack?',
                'option_a': 'Pretexting',
                'option_b': 'Phishing',
                'option_c': 'Baiting',
                'option_d': 'Tailgating',
                'correct_answer': 'b',
                'explanation': 'Phishing is the most common type of social engineering attack, involving fraudulent emails, texts, or websites.',
                'question_set': 1,
                'module_source': 2
            },
            {
                'question_text': 'What is spear phishing?',
                'option_a': 'A general phishing attack sent to many people',
                'option_b': 'A targeted phishing attack against specific individuals or organizations',
                'option_c': 'A phishing attack using voice calls',
                'option_d': 'A phishing attack using physical media',
                'correct_answer': 'b',
                'explanation': 'Spear phishing is a targeted phishing attack against specific individuals or organizations.',
                'question_set': 1,
                'module_source': 2
            },
            {
                'question_text': 'What is pretexting?',
                'option_a': 'Creating fake websites',
                'option_b': 'Creating a fabricated scenario to obtain information',
                'option_c': 'Leaving infected USB drives',
                'option_d': 'Following someone through secure doors',
                'correct_answer': 'b',
                'explanation': 'Pretexting involves creating a fabricated scenario to obtain information by pretending to be someone else.',
                'question_set': 1,
                'module_source': 2
            },
            {
                'question_text': 'What is tailgating?',
                'option_a': 'Following someone through secure doors',
                'option_b': 'Sending fraudulent emails',
                'option_c': 'Creating fake websites',
                'option_d': 'Using infected USB drives',
                'correct_answer': 'a',
                'explanation': 'Tailgating occurs when an unauthorized person follows an authorized person into a restricted area.',
                'question_set': 1,
                'module_source': 2
            },
            
            # Module 3 Questions (4 questions)
            {
                'question_text': 'Which of the following is a red flag for email phishing?',
                'option_a': 'Professional grammar and spelling',
                'option_b': 'Urgent or threatening language',
                'option_c': 'Personal greeting with your name',
                'option_d': 'Links to official websites',
                'correct_answer': 'b',
                'explanation': 'Urgent or threatening language is a common red flag in phishing emails.',
                'question_set': 1,
                'module_source': 3
            },
            {
                'question_text': 'What should you do when you receive a suspicious email?',
                'option_a': 'Click all links to investigate',
                'option_b': 'Don\'t click links or download attachments',
                'option_c': 'Reply with your personal information',
                'option_d': 'Forward it to all your contacts',
                'correct_answer': 'b',
                'explanation': 'You should never click links or download attachments from suspicious emails.',
                'question_set': 1,
                'module_source': 3
            },
            {
                'question_text': 'How can you verify if a website is legitimate?',
                'option_a': 'Check for HTTPS and padlock icon',
                'option_b': 'Ignore the URL completely',
                'option_c': 'Click on all pop-ups',
                'option_d': 'Enter your password immediately',
                'correct_answer': 'a',
                'explanation': 'Check for HTTPS and padlock icon to verify website legitimacy.',
                'question_set': 1,
                'module_source': 3
            },
            {
                'question_text': 'What is caller ID spoofing?',
                'option_a': 'A legitimate business practice',
                'option_b': 'When phone numbers are faked to appear legitimate',
                'option_c': 'A type of email phishing',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'Caller ID spoofing is when phone numbers are faked to appear legitimate.',
                'question_set': 1,
                'module_source': 3
            },
            
            # Module 4 Questions (4 questions)
            {
                'question_text': 'What is the minimum recommended password length?',
                'option_a': '8 characters',
                'option_b': '12 characters',
                'option_c': '6 characters',
                'option_d': '16 characters',
                'correct_answer': 'b',
                'explanation': 'The minimum recommended password length is 12 characters for better security.',
                'question_set': 1,
                'module_source': 4
            },
            {
                'question_text': 'What is multi-factor authentication (MFA)?',
                'option_a': 'Using multiple passwords',
                'option_b': 'Adding an extra layer of security beyond passwords',
                'option_c': 'Using only biometric authentication',
                'option_d': 'Sharing passwords with others',
                'correct_answer': 'b',
                'explanation': 'MFA adds an extra layer of security by requiring multiple forms of verification.',
                'question_set': 1,
                'module_source': 4
            },
            {
                'question_text': 'Which of the following is a strong password?',
                'option_a': 'password123',
                'option_b': 'MyDogSpot2023!',
                'option_c': '123456789',
                'option_d': 'qwerty',
                'correct_answer': 'b',
                'explanation': 'MyDogSpot2023! is strong because it has length, complexity, and includes symbols.',
                'question_set': 1,
                'module_source': 4
            },
            {
                'question_text': 'What should you do with passwords?',
                'option_a': 'Share them with trusted friends',
                'option_b': 'Use the same password for all accounts',
                'option_c': 'Use different passwords for each account',
                'option_d': 'Write them on sticky notes',
                'correct_answer': 'c',
                'explanation': 'You should use different passwords for each account to minimize risk.',
                'question_set': 1,
                'module_source': 4
            },
            
            # Module 5 Questions (3 questions)
            {
                'question_text': 'What is a common social media security risk?',
                'option_a': 'Using strong passwords',
                'option_b': 'Oversharing personal information',
                'option_c': 'Enabling two-factor authentication',
                'option_d': 'Using privacy settings',
                'correct_answer': 'b',
                'explanation': 'Oversharing personal information is a common social media security risk.',
                'question_set': 1,
                'module_source': 5
            },
            {
                'question_text': 'What should you do with friend requests from people you don\'t know?',
                'option_a': 'Accept them immediately',
                'option_b': 'Ignore or decline them',
                'option_c': 'Share your personal information',
                'option_d': 'Send them money',
                'correct_answer': 'b',
                'explanation': 'You should ignore or decline friend requests from people you don\'t know.',
                'question_set': 1,
                'module_source': 5
            },
            {
                'question_text': 'What is a fake profile?',
                'option_a': 'A legitimate business account',
                'option_b': 'An account created by attackers to gather information',
                'option_c': 'A verified account',
                'option_d': 'A private account',
                'correct_answer': 'b',
                'explanation': 'A fake profile is an account created by attackers to gather information.',
                'question_set': 1,
                'module_source': 5
            },
            
            # Module 6 Questions (3 questions)
            {
                'question_text': 'What should you do when leaving your workstation?',
                'option_a': 'Leave it unlocked for convenience',
                'option_b': 'Lock your workstation',
                'option_c': 'Share your password with colleagues',
                'option_d': 'Ignore security warnings',
                'correct_answer': 'b',
                'explanation': 'You should always lock your workstation when stepping away.',
                'question_set': 1,
                'module_source': 6
            },
            {
                'question_text': 'What is dumpster diving?',
                'option_a': 'A recreational activity',
                'option_b': 'Searching through trash for sensitive information',
                'option_c': 'A type of password attack',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'Dumpster diving is searching through trash for sensitive information.',
                'question_set': 1,
                'module_source': 6
            },
            {
                'question_text': 'What should you do with sensitive documents?',
                'option_a': 'Leave them on your desk',
                'option_b': 'Shred them properly',
                'option_c': 'Throw them in the regular trash',
                'option_d': 'Share them with friends',
                'correct_answer': 'b',
                'explanation': 'You should shred sensitive documents properly to prevent information theft.',
                'question_set': 1,
                'module_source': 6
            },
            
            # Module 7 Questions (3 questions)
            {
                'question_text': 'What is the first step in incident response?',
                'option_a': 'Panic and call everyone',
                'option_b': 'Stay calm and document everything',
                'option_c': 'Delete all evidence',
                'option_d': 'Ignore the incident',
                'correct_answer': 'b',
                'explanation': 'The first step is to stay calm and document everything about the incident.',
                'question_set': 1,
                'module_source': 7
            },
            {
                'question_text': 'What should you do immediately after a social engineering incident?',
                'option_a': 'Delete all related emails',
                'option_b': 'Change compromised passwords',
                'option_c': 'Share the incident on social media',
                'option_d': 'Ignore it completely',
                'correct_answer': 'b',
                'explanation': 'You should change compromised passwords immediately after a social engineering incident.',
                'question_set': 1,
                'module_source': 7
            },
            {
                'question_text': 'Who should you report incidents to?',
                'option_a': 'Only your friends',
                'option_b': 'Your supervisor, IT department, or security team',
                'option_c': 'Social media followers',
                'option_d': 'No one',
                'correct_answer': 'b',
                'explanation': 'You should report incidents to your supervisor, IT department, or security team.',
                'question_set': 1,
                'module_source': 7
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Final Assessment (25 different questions)"""
        return [
            # Module 1 Questions (4 questions)
            {
                'question_text': 'What emotion do social engineers commonly exploit?',
                'option_a': 'Happiness and joy',
                'option_b': 'Fear, greed, and curiosity',
                'option_c': 'Sadness and depression',
                'option_d': 'Anger and frustration',
                'correct_answer': 'b',
                'explanation': 'Social engineers commonly exploit fear, greed, and curiosity to manipulate their targets.',
                'question_set': 2,
                'module_source': 1
            },
            {
                'question_text': 'What is the relationship between technical security and social engineering?',
                'option_a': 'Technical security prevents all social engineering attacks',
                'option_b': 'Social engineering can bypass even strong technical security',
                'option_c': 'They are completely unrelated',
                'option_d': 'Social engineering only works on weak technical security',
                'correct_answer': 'b',
                'explanation': 'Social engineering can bypass even the strongest technical security measures by manipulating human psychology.',
                'question_set': 2,
                'module_source': 1
            },
            {
                'question_text': 'What makes social engineering different from traditional hacking?',
                'option_a': 'It requires more technical skills',
                'option_b': 'It focuses on human psychology rather than technical vulnerabilities',
                'option_c': 'It only works on large organizations',
                'option_d': 'It requires expensive equipment',
                'correct_answer': 'b',
                'explanation': 'Social engineering focuses on human psychology and manipulation rather than exploiting technical vulnerabilities.',
                'question_set': 2,
                'module_source': 1
            },
            {
                'question_text': 'What should organizations do to protect against social engineering?',
                'option_a': 'Rely only on technical security measures',
                'option_b': 'Implement a combination of technical and human-focused security measures',
                'option_c': 'Ignore the threat as it only affects small companies',
                'option_d': 'Focus only on executive protection',
                'correct_answer': 'b',
                'explanation': 'Organizations should implement a combination of technical and human-focused security measures to protect against social engineering.',
                'question_set': 2,
                'module_source': 1
            },
            
            # Module 2 Questions (4 questions)
            {
                'question_text': 'What is a watering hole attack?',
                'option_a': 'Compromising frequently visited websites',
                'option_b': 'Using phone calls to trick people',
                'option_c': 'Leaving infected devices in public',
                'option_d': 'Creating fake identities',
                'correct_answer': 'a',
                'explanation': 'Watering hole attacks target websites that are likely to be visited by intended victims.',
                'question_set': 2,
                'module_source': 2
            },
            {
                'question_text': 'What is vishing?',
                'option_a': 'Voice phishing using phone calls',
                'option_b': 'SMS phishing using text messages',
                'option_c': 'Email phishing',
                'option_d': 'Website phishing',
                'correct_answer': 'a',
                'explanation': 'Vishing is voice phishing using phone calls.',
                'question_set': 2,
                'module_source': 2
            },
            {
                'question_text': 'What is whaling?',
                'option_a': 'Phishing attacks targeting high-level executives',
                'option_b': 'General phishing attacks',
                'option_c': 'SMS phishing attacks',
                'option_d': 'Voice phishing attacks',
                'correct_answer': 'a',
                'explanation': 'Whaling refers to phishing attacks specifically targeting high-level executives.',
                'question_set': 2,
                'module_source': 2
            },
            {
                'question_text': 'What is quid pro quo?',
                'option_a': 'A type of phishing attack',
                'option_b': 'Offering a service in exchange for information',
                'option_c': 'A physical security breach',
                'option_d': 'A website compromise',
                'correct_answer': 'b',
                'explanation': 'Quid pro quo involves offering a service in exchange for information or access.',
                'question_set': 2,
                'module_source': 2
            },
            
            # Module 3 Questions (4 questions)
            {
                'question_text': 'What should you do if you suspect a phishing attempt?',
                'option_a': 'Report it to your IT department',
                'option_b': 'Ignore it completely',
                'option_c': 'Share it on social media',
                'option_d': 'Reply to the sender',
                'correct_answer': 'a',
                'explanation': 'You should report suspicious phishing attempts to your IT department.',
                'question_set': 2,
                'module_source': 3
            },
            {
                'question_text': 'What should you do if you accidentally clicked a phishing link?',
                'option_a': 'Ignore it completely',
                'option_b': 'Change your passwords and monitor accounts',
                'option_c': 'Share it on social media',
                'option_d': 'Reply to the sender',
                'correct_answer': 'b',
                'explanation': 'If you accidentally clicked a phishing link, change your passwords and monitor accounts.',
                'question_set': 2,
                'module_source': 3
            },
            {
                'question_text': 'Which of the following is a legitimate request from a bank?',
                'option_a': 'Email asking for your password',
                'option_b': 'Phone call demanding immediate payment',
                'option_c': 'Letter mailed to your address',
                'option_d': 'Text message with urgent action required',
                'correct_answer': 'c',
                'explanation': 'Banks typically send official communications through regular mail, not urgent emails or calls.',
                'question_set': 2,
                'module_source': 3
            },
            {
                'question_text': 'What should you do with suspicious attachments?',
                'option_a': 'Open them immediately',
                'option_b': 'Don\'t download or open them',
                'option_c': 'Forward them to friends',
                'option_d': 'Reply to the sender',
                'correct_answer': 'b',
                'explanation': 'You should never download or open suspicious attachments.',
                'question_set': 2,
                'module_source': 3
            },
            
            # Module 4 Questions (4 questions)
            {
                'question_text': 'What is shoulder surfing?',
                'option_a': 'A type of password manager',
                'option_b': 'Watching someone type their password',
                'option_c': 'A security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'b',
                'explanation': 'Shoulder surfing is watching someone type their password to steal it.',
                'question_set': 2,
                'module_source': 4
            },
            {
                'question_text': 'What is a keylogger?',
                'option_a': 'A type of password manager',
                'option_b': 'Malware that records keystrokes',
                'option_c': 'A security feature',
                'option_d': 'A type of MFA',
                'correct_answer': 'b',
                'explanation': 'A keylogger is malware that records keystrokes to steal passwords.',
                'question_set': 2,
                'module_source': 4
            },
            {
                'question_text': 'What should you avoid in passwords?',
                'option_a': 'Uppercase letters',
                'option_b': 'Personal information like names and birthdays',
                'option_c': 'Numbers',
                'option_d': 'Symbols',
                'correct_answer': 'b',
                'explanation': 'You should avoid personal information like names and birthdays in passwords.',
                'question_set': 2,
                'module_source': 4
            },
            {
                'question_text': 'What is biometric authentication?',
                'option_a': 'Using passwords',
                'option_b': 'Using physical characteristics like fingerprints',
                'option_c': 'Using SMS codes',
                'option_d': 'Using email verification',
                'correct_answer': 'b',
                'explanation': 'Biometric authentication uses physical characteristics like fingerprints or face recognition.',
                'question_set': 2,
                'module_source': 4
            },
            
            # Module 5 Questions (3 questions)
            {
                'question_text': 'What should you do if you receive an urgent request for help on social media?',
                'option_a': 'Send money immediately',
                'option_b': 'Verify the request through other means',
                'option_c': 'Share your personal information',
                'option_d': 'Ignore it completely',
                'correct_answer': 'b',
                'explanation': 'You should verify urgent requests for help through other means before responding.',
                'question_set': 2,
                'module_source': 5
            },
            {
                'question_text': 'What is a romance scam?',
                'option_a': 'A legitimate dating service',
                'option_b': 'Building fake relationships to exploit victims',
                'option_c': 'A type of privacy setting',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'A romance scam involves building fake relationships to exploit victims.',
                'question_set': 2,
                'module_source': 5
            },
            {
                'question_text': 'What should you do with too-good-to-be-true offers on social media?',
                'option_a': 'Accept them immediately',
                'option_b': 'Be skeptical and investigate',
                'option_c': 'Share them with everyone',
                'option_d': 'Send personal information',
                'correct_answer': 'b',
                'explanation': 'You should be skeptical and investigate too-good-to-be-true offers.',
                'question_set': 2,
                'module_source': 5
            },
            
            # Module 6 Questions (3 questions)
            {
                'question_text': 'What should you do if you see a stranger in a secure area?',
                'option_a': 'Ignore them completely',
                'option_b': 'Challenge them and ask for identification',
                'option_c': 'Help them find what they\'re looking for',
                'option_d': 'Share sensitive information with them',
                'correct_answer': 'b',
                'explanation': 'You should challenge strangers and ask for identification when appropriate.',
                'question_set': 2,
                'module_source': 6
            },
            {
                'question_text': 'What is a clean desk policy?',
                'option_a': 'Keeping your desk messy',
                'option_b': 'Keeping work areas free of sensitive documents',
                'option_c': 'Sharing all documents with colleagues',
                'option_d': 'Ignoring security policies',
                'correct_answer': 'b',
                'explanation': 'A clean desk policy means keeping work areas free of sensitive documents.',
                'question_set': 2,
                'module_source': 6
            },
            {
                'question_text': 'What is eavesdropping?',
                'option_a': 'A type of exercise',
                'option_b': 'Listening to conversations in public areas',
                'option_c': 'A security feature',
                'option_d': 'A type of password',
                'correct_answer': 'b',
                'explanation': 'Eavesdropping is listening to conversations in public areas to gather information.',
                'question_set': 2,
                'module_source': 6
            },
            
            # Module 7 Questions (3 questions)
            {
                'question_text': 'What is containment in incident response?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Limiting damage and preventing further harm',
                'option_c': 'Deleting all evidence',
                'option_d': 'Sharing information with everyone',
                'correct_answer': 'b',
                'explanation': 'Containment means limiting damage and preventing further harm from the incident.',
                'question_set': 2,
                'module_source': 7
            },
            {
                'question_text': 'What should you do if you suspect a data breach?',
                'option_a': 'Ignore it completely',
                'option_b': 'Report it immediately and preserve evidence',
                'option_c': 'Delete all related files',
                'option_d': 'Share it on social media',
                'correct_answer': 'b',
                'explanation': 'You should report data breaches immediately and preserve evidence.',
                'question_set': 2,
                'module_source': 7
            },
            {
                'question_text': 'What is the purpose of post-incident activities?',
                'option_a': 'To forget about the incident',
                'option_b': 'To learn from the incident and improve security',
                'option_c': 'To blame others',
                'option_d': 'To hide the incident',
                'correct_answer': 'b',
                'explanation': 'Post-incident activities help learn from the incident and improve security.',
                'question_set': 2,
                'module_source': 7
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Final Assessment (25 different questions)"""
        return [
            # Module 1 Questions (4 questions)
            {
                'question_text': 'Which group is typically NOT a primary target of social engineering?',
                'option_a': 'IT support staff',
                'option_b': 'Customer service representatives',
                'option_c': 'Security robots',
                'option_d': 'Executives and decision-makers',
                'correct_answer': 'c',
                'explanation': 'Security robots are not human and therefore cannot be manipulated through social engineering techniques.',
                'question_set': 3,
                'module_source': 1
            },
            {
                'question_text': 'Which of the following best describes the impact of social engineering on organizations?',
                'option_a': 'Only financial losses',
                'option_b': 'Only data breaches',
                'option_c': 'Multiple impacts including financial, reputational, and operational',
                'option_d': 'No significant impact',
                'correct_answer': 'c',
                'explanation': 'Social engineering can have multiple impacts including financial losses, data breaches, reputation damage, and operational disruption.',
                'question_set': 3,
                'module_source': 1
            },
            {
                'question_text': 'What is the first step in preventing social engineering attacks?',
                'option_a': 'Installing firewalls',
                'option_b': 'Employee awareness and training',
                'option_c': 'Changing passwords regularly',
                'option_d': 'Updating software',
                'correct_answer': 'b',
                'explanation': 'Employee awareness and training is the first and most important step in preventing social engineering attacks.',
                'question_set': 3,
                'module_source': 1
            },
            {
                'question_text': 'Which prevention strategy is most effective against social engineering?',
                'option_a': 'Using complex passwords',
                'option_b': 'Regular security awareness training',
                'option_c': 'Installing antivirus software',
                'option_d': 'Using VPN connections',
                'correct_answer': 'b',
                'explanation': 'Regular security awareness training is the most effective strategy for preventing social engineering attacks.',
                'question_set': 3,
                'module_source': 1
            },
            
            # Module 2 Questions (4 questions)
            {
                'question_text': 'Which attack characteristic creates time pressure?',
                'option_a': 'Authority',
                'option_b': 'Urgency',
                'option_c': 'Scarcity',
                'option_d': 'Social proof',
                'correct_answer': 'b',
                'explanation': 'Urgency creates time pressure to bypass rational thinking.',
                'question_set': 3,
                'module_source': 2
            },
            {
                'question_text': 'What is smishing?',
                'option_a': 'Email phishing',
                'option_b': 'SMS phishing using text messages',
                'option_c': 'Voice phishing',
                'option_d': 'Website phishing',
                'correct_answer': 'b',
                'explanation': 'Smishing is SMS phishing using text messages.',
                'question_set': 3,
                'module_source': 2
            },
            {
                'question_text': 'Which attack type uses physical media?',
                'option_a': 'Phishing',
                'option_b': 'Baiting',
                'option_c': 'Pretexting',
                'option_d': 'Quid pro quo',
                'correct_answer': 'b',
                'explanation': 'Baiting uses physical media like infected USB drives to spread malware.',
                'question_set': 3,
                'module_source': 2
            },
            {
                'question_text': 'What is the main goal of watering hole attacks?',
                'option_a': 'To steal physical devices',
                'option_b': 'To infect visitors with malware',
                'option_c': 'To gain physical access',
                'option_d': 'To create fake identities',
                'correct_answer': 'b',
                'explanation': 'Watering hole attacks aim to infect visitors with malware by compromising frequently visited websites.',
                'question_set': 3,
                'module_source': 2
            },
            
            # Module 3 Questions (4 questions)
            {
                'question_text': 'What is the purpose of multi-factor authentication?',
                'option_a': 'To make logging in more difficult',
                'option_b': 'To add an extra layer of security',
                'option_c': 'To slow down internet speed',
                'option_d': 'To share passwords with others',
                'correct_answer': 'b',
                'explanation': 'Multi-factor authentication adds an extra layer of security beyond just passwords.',
                'question_set': 3,
                'module_source': 3
            },
            {
                'question_text': 'Which of the following is a sign of a phishing website?',
                'option_a': 'Professional design and branding',
                'option_b': 'HTTPS and padlock icon',
                'option_c': 'Request for unnecessary personal information',
                'option_d': 'Official company logo',
                'correct_answer': 'c',
                'explanation': 'Request for unnecessary personal information is a sign of a phishing website.',
                'question_set': 3,
                'module_source': 3
            },
            {
                'question_text': 'How often should you update your software?',
                'option_a': 'Never',
                'option_b': 'Only when forced',
                'option_c': 'Regularly to get security patches',
                'option_d': 'Once a year',
                'correct_answer': 'c',
                'explanation': 'You should update software regularly to get security patches that fix vulnerabilities.',
                'question_set': 3,
                'module_source': 3
            },
            {
                'question_text': 'What should you do if you receive a suspicious email?',
                'option_a': 'Reply immediately',
                'option_b': 'Report it to IT and don\'t click any links',
                'option_c': 'Forward it to all your contacts',
                'option_d': 'Delete it without reporting',
                'correct_answer': 'b',
                'explanation': 'You should report suspicious emails to IT and not click any links.',
                'question_set': 3,
                'module_source': 3
            },
            
            # Module 4 Questions (4 questions)
            {
                'question_text': 'What are the three factors of authentication?',
                'option_a': 'Something you know, have, and are',
                'option_b': 'Something you see, hear, and touch',
                'option_c': 'Something you want, need, and like',
                'option_d': 'Something you buy, sell, and trade',
                'correct_answer': 'a',
                'explanation': 'The three factors are something you know (password), have (phone), and are (fingerprint).',
                'question_set': 3,
                'module_source': 4
            },
            {
                'question_text': 'What is the best way to store passwords?',
                'option_a': 'On sticky notes',
                'option_b': 'In a password manager',
                'option_c': 'In a text file on your computer',
                'option_d': 'Sharing them with friends',
                'correct_answer': 'b',
                'explanation': 'A password manager is the best way to securely store passwords.',
                'question_set': 3,
                'module_source': 4
            },
            {
                'question_text': 'What should you do if your password is compromised?',
                'option_a': 'Ignore it',
                'option_b': 'Change it immediately',
                'option_c': 'Share it with others',
                'option_d': 'Write it down',
                'correct_answer': 'b',
                'explanation': 'You should change compromised passwords immediately.',
                'question_set': 3,
                'module_source': 4
            },
            {
                'question_text': 'Why is MFA important?',
                'option_a': 'It makes logging in faster',
                'option_b': 'It adds an extra layer of security',
                'option_c': 'It reduces password complexity',
                'option_d': 'It allows password sharing',
                'correct_answer': 'b',
                'explanation': 'MFA is important because it adds an extra layer of security beyond just passwords.',
                'question_set': 3,
                'module_source': 4
            },
            
            # Module 5 Questions (3 questions)
            {
                'question_text': 'What should you do if you\'re targeted by a social media scam?',
                'option_a': 'Respond to the scammer',
                'option_b': 'Block and report the account',
                'option_c': 'Share your personal information',
                'option_d': 'Send money to resolve it',
                'correct_answer': 'b',
                'explanation': 'You should block and report the account if you\'re targeted by a social media scam.',
                'question_set': 3,
                'module_source': 5
            },
            {
                'question_text': 'What information do attackers typically collect from social media?',
                'option_a': 'Only public posts',
                'option_b': 'Personal details, work information, family details, and more',
                'option_c': 'Only profile pictures',
                'option_d': 'Only usernames',
                'correct_answer': 'b',
                'explanation': 'Attackers collect personal details, work information, family details, and much more.',
                'question_set': 3,
                'module_source': 5
            },
            {
                'question_text': 'What should you do when using social media on shared devices?',
                'option_a': 'Stay logged in',
                'option_b': 'Log out when done',
                'option_c': 'Share your password',
                'option_d': 'Ignore security warnings',
                'correct_answer': 'b',
                'explanation': 'You should log out when done using social media on shared devices.',
                'question_set': 3,
                'module_source': 5
            },
            
            # Module 6 Questions (3 questions)
            {
                'question_text': 'What is piggybacking?',
                'option_a': 'A type of exercise',
                'option_b': 'Using someone else\'s access credentials',
                'option_c': 'A security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'b',
                'explanation': 'Piggybacking is using someone else\'s access credentials to gain unauthorized access.',
                'question_set': 3,
                'module_source': 6
            },
            {
                'question_text': 'What should you do with passwords at work?',
                'option_a': 'Write them on sticky notes',
                'option_b': 'Keep them secure and never share them',
                'option_c': 'Share them with trusted colleagues',
                'option_d': 'Post them on your desk',
                'correct_answer': 'b',
                'explanation': 'You should keep passwords secure and never share them with anyone.',
                'question_set': 3,
                'module_source': 6
            },
            {
                'question_text': 'What should you do with unattended mobile devices?',
                'option_a': 'Take them for yourself',
                'option_b': 'Secure them or return them to the owner',
                'option_c': 'Ignore them completely',
                'option_d': 'Share them with others',
                'correct_answer': 'b',
                'explanation': 'You should secure unattended mobile devices or return them to the owner.',
                'question_set': 3,
                'module_source': 6
            },
            
            # Module 7 Questions (3 questions)
            {
                'question_text': 'What is forensic analysis?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Investigating the root cause of an incident',
                'option_c': 'Deleting evidence',
                'option_d': 'Sharing information publicly',
                'correct_answer': 'b',
                'explanation': 'Forensic analysis involves investigating the root cause of an incident.',
                'question_set': 3,
                'module_source': 7
            },
            {
                'question_text': 'What is damage assessment?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Determining the full extent of an incident',
                'option_c': 'Deleting evidence',
                'option_d': 'Sharing information publicly',
                'correct_answer': 'b',
                'explanation': 'Damage assessment involves determining the full extent of an incident.',
                'question_set': 3,
                'module_source': 7
            },
            {
                'question_text': 'What should you do during an incident?',
                'option_a': 'Panic and run away',
                'option_b': 'Stay calm and follow incident response procedures',
                'option_c': 'Delete all evidence',
                'option_d': 'Ignore all warnings',
                'correct_answer': 'b',
                'explanation': 'You should stay calm and follow incident response procedures during an incident.',
                'question_set': 3,
                'module_source': 7
            }
        ]
