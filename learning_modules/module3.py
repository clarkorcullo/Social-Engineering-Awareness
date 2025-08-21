"""
Module 3: Phishing Detection and Prevention
Content and knowledge check questions for Module 3
"""

from typing import List, Dict, Any

class Module3Content:
    """Content for Module 3: Phishing Detection and Prevention"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Phishing Detection and Prevention',
            'description': 'Learning how to identify and prevent phishing attacks',
            'content': '''
                <h2>How to Detect Phishing Attacks</h2>
                
                <h3>Email Phishing Red Flags:</h3>
                <ul>
                    <li><strong>Urgent or threatening language:</strong> "Your account will be suspended"</li>
                    <li><strong>Requests for sensitive information:</strong> Passwords, credit card numbers, SSN</li>
                    <li><strong>Suspicious sender addresses:</strong> Slight variations in domain names</li>
                    <li><strong>Generic greetings:</strong> "Dear Customer" instead of your name</li>
                    <li><strong>Poor grammar and spelling:</strong> Professional companies rarely make these mistakes</li>
                    <li><strong>Suspicious links:</strong> Hover over links to see actual URLs</li>
                    <li><strong>Unexpected attachments:</strong> Files you weren't expecting</li>
                </ul>
                
                <h3>Website Phishing Indicators:</h3>
                <ul>
                    <li><strong>URL inconsistencies:</strong> Check the actual domain name</li>
                    <li><strong>Missing security indicators:</strong> No HTTPS or padlock icon</li>
                    <li><strong>Poor design quality:</strong> Unprofessional appearance</li>
                    <li><strong>Request for unnecessary information:</strong> Banks don't ask for passwords via email</li>
                    <li><strong>Pop-up forms:</strong> Legitimate sites rarely use pop-ups for login</li>
                </ul>
                
                <h3>Phone Phishing (Vishing) Signs:</h3>
                <ul>
                    <li><strong>Caller ID spoofing:</strong> Numbers can be faked</li>
                    <li><strong>Pressure tactics:</strong> "Act now or lose access"</li>
                    <li><strong>Requests for remote access:</strong> Never give control of your computer</li>
                    <li><strong>Payment demands:</strong> Government agencies don't demand immediate payment</li>
                    <li><strong>Threats of legal action:</strong> Scare tactics to create urgency</li>
                </ul>
                
                <h3>Prevention Strategies:</h3>
                <ul>
                    <li><strong>Verify sender identity:</strong> Contact the organization directly</li>
                    <li><strong>Check URLs carefully:</strong> Look for misspellings or extra characters</li>
                    <li><strong>Use multi-factor authentication:</strong> Adds an extra layer of security</li>
                    <li><strong>Keep software updated:</strong> Patches fix security vulnerabilities</li>
                    <li><strong>Use security software:</strong> Antivirus and anti-phishing tools</li>
                    <li><strong>Report suspicious emails:</strong> Help protect others</li>
                    <li><strong>Educate yourself and others:</strong> Stay informed about new tactics</li>
                </ul>
                
                <h3>What to Do If You Suspect Phishing:</h3>
                <ol>
                    <li><strong>Don't click links or download attachments</strong></li>
                    <li><strong>Don't provide personal information</strong></li>
                    <li><strong>Report the incident to your IT department</strong></li>
                    <li><strong>Forward suspicious emails to your security team</strong></li>
                    <li><strong>Change passwords if you suspect compromise</strong></li>
                    <li><strong>Monitor accounts for suspicious activity</strong></li>
                </ol>
            ''',
            'learning_objectives': [
                'Identify common phishing red flags in emails, websites, and phone calls',
                'Understand prevention strategies for different types of phishing',
                'Learn proper response procedures when encountering phishing attempts',
                'Develop skills to protect personal and organizational information'
            ],
            'estimated_time': 40,  # minutes
            'difficulty_level': 'intermediate'
        }

class Module3Questions:
    """Knowledge check questions for Module 3"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 3"""
        return [
            {
                'question_text': 'Which of the following is a red flag for email phishing?',
                'option_a': 'Professional grammar and spelling',
                'option_b': 'Urgent or threatening language',
                'option_c': 'Personal greeting with your name',
                'option_d': 'Links to official websites',
                'correct_answer': 'b',
                'explanation': 'Urgent or threatening language is a common red flag in phishing emails.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do when you receive a suspicious email?',
                'option_a': 'Click all links to investigate',
                'option_b': 'Reply with your personal information',
                'option_c': 'Don\'t click links or download attachments',
                'option_d': 'Forward it to all your contacts',
                'correct_answer': 'c',
                'explanation': 'You should never click links or download attachments from suspicious emails.',
                'question_set': 1
            },
            {
                'question_text': 'How can you verify if a website is legitimate?',
                'option_a': 'Check for HTTPS and padlock icon',
                'option_b': 'Ignore the URL completely',
                'option_c': 'Click on all pop-ups',
                'option_d': 'Enter your password immediately',
                'correct_answer': 'a',
                'explanation': 'Check for HTTPS and padlock icon to verify website legitimacy.',
                'question_set': 1
            },
            {
                'question_text': 'What is caller ID spoofing?',
                'option_a': 'A legitimate business practice',
                'option_b': 'When phone numbers are faked to appear legitimate',
                'option_c': 'A type of email phishing',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'Caller ID spoofing is when phone numbers are faked to appear legitimate.',
                'question_set': 1
            },
            {
                'question_text': 'Which prevention strategy is most effective?',
                'option_a': 'Using only strong passwords',
                'option_b': 'Multi-factor authentication',
                'option_c': 'Ignoring all emails',
                'option_d': 'Sharing passwords with colleagues',
                'correct_answer': 'b',
                'explanation': 'Multi-factor authentication adds an extra layer of security.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 3"""
        return [
            {
                'question_text': 'What should you do if you suspect a phishing attempt?',
                'option_a': 'Report it to your IT department',
                'option_b': 'Ignore it completely',
                'option_c': 'Share it on social media',
                'option_d': 'Reply to the sender',
                'correct_answer': 'a',
                'explanation': 'You should report suspicious phishing attempts to your IT department.',
                'question_set': 2
            },
            {
                'question_text': 'Which of the following is NOT a phishing red flag?',
                'option_a': 'Generic greetings like "Dear Customer"',
                'option_b': 'Requests for sensitive information',
                'option_c': 'Professional design and branding',
                'option_d': 'Urgent or threatening language',
                'correct_answer': 'c',
                'explanation': 'Professional design and branding is typically a sign of legitimacy, not phishing.',
                'question_set': 2
            },
            {
                'question_text': 'What is vishing?',
                'option_a': 'Email phishing',
                'option_b': 'Voice phishing using phone calls',
                'option_c': 'Website phishing',
                'option_d': 'SMS phishing',
                'correct_answer': 'b',
                'explanation': 'Vishing is voice phishing using phone calls.',
                'question_set': 2
            },
            {
                'question_text': 'How can you check if a link is legitimate?',
                'option_a': 'Click it immediately',
                'option_b': 'Hover over the link to see the actual URL',
                'option_c': 'Ignore the link completely',
                'option_d': 'Share it with friends',
                'correct_answer': 'b',
                'explanation': 'Hover over the link to see the actual URL before clicking.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do if you accidentally clicked a phishing link?',
                'option_a': 'Ignore it completely',
                'option_b': 'Change your passwords and monitor accounts',
                'option_c': 'Share it on social media',
                'option_d': 'Reply to the sender',
                'correct_answer': 'b',
                'explanation': 'If you accidentally clicked a phishing link, change your passwords and monitor accounts.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 3"""
        return [
            {
                'question_text': 'Which of the following is a legitimate request from a bank?',
                'option_a': 'Email asking for your password',
                'option_b': 'Phone call demanding immediate payment',
                'option_c': 'Letter mailed to your address',
                'option_d': 'Text message with urgent action required',
                'correct_answer': 'c',
                'explanation': 'Banks typically send official communications through regular mail, not urgent emails or calls.',
                'question_set': 3
            },
            {
                'question_text': 'What is the purpose of multi-factor authentication?',
                'option_a': 'To make logging in more difficult',
                'option_b': 'To add an extra layer of security',
                'option_c': 'To slow down internet speed',
                'option_d': 'To share passwords with others',
                'correct_answer': 'b',
                'explanation': 'Multi-factor authentication adds an extra layer of security beyond just passwords.',
                'question_set': 3
            },
            {
                'question_text': 'Which of the following is a sign of a phishing website?',
                'option_a': 'Professional design and branding',
                'option_b': 'HTTPS and padlock icon',
                'option_c': 'Request for unnecessary personal information',
                'option_d': 'Official company logo',
                'correct_answer': 'c',
                'explanation': 'Request for unnecessary personal information is a sign of a phishing website.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do with suspicious attachments?',
                'option_a': 'Open them immediately',
                'option_b': 'Don\'t download or open them',
                'option_c': 'Forward them to friends',
                'option_d': 'Reply to the sender',
                'correct_answer': 'b',
                'explanation': 'You should never download or open suspicious attachments.',
                'question_set': 3
            },
            {
                'question_text': 'How often should you update your software?',
                'option_a': 'Never',
                'option_b': 'Only when forced',
                'option_c': 'Regularly to get security patches',
                'option_d': 'Once a year',
                'correct_answer': 'c',
                'explanation': 'You should update software regularly to get security patches that fix vulnerabilities.',
                'question_set': 3
            }
        ]

