"""
Module 4: Password Security and Authentication
Content and knowledge check questions for Module 4
"""

from typing import List, Dict, Any

class Module4Content:
    """Content for Module 4: Password Security and Authentication"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Password Security and Authentication',
            'description': 'Understanding password security and authentication methods',
            'content': '''
                <h2>Password Security Best Practices</h2>
                
                <h3>Creating Strong Passwords:</h3>
                <ul>
                    <li><strong>Length:</strong> Use at least 12 characters</li>
                    <li><strong>Complexity:</strong> Include uppercase, lowercase, numbers, and symbols</li>
                    <li><strong>Uniqueness:</strong> Use different passwords for each account</li>
                    <li><strong>Avoid common patterns:</strong> Don't use "123456" or "password"</li>
                    <li><strong>No personal information:</strong> Avoid names, birthdays, or addresses</li>
                </ul>
                
                <h3>Password Management:</h3>
                <ul>
                    <li><strong>Use a password manager:</strong> Securely store and generate passwords</li>
                    <li><strong>Regular updates:</strong> Change passwords periodically</li>
                    <li><strong>Secure storage:</strong> Never write passwords on paper or share them</li>
                    <li><strong>Backup recovery:</strong> Have a secure way to recover accounts</li>
                </ul>
                
                <h3>Multi-Factor Authentication (MFA):</h3>
                <p>MFA adds an extra layer of security by requiring multiple forms of verification:</p>
                <ul>
                    <li><strong>Something you know:</strong> Password or PIN</li>
                    <li><strong>Something you have:</strong> Phone, security key, or token</li>
                    <li><strong>Something you are:</strong> Fingerprint, face recognition, or voice</li>
                </ul>
                
                <h3>Types of MFA:</h3>
                <ul>
                    <li><strong>SMS/Text messages:</strong> Codes sent to your phone</li>
                    <li><strong>Authenticator apps:</strong> Time-based codes (Google Authenticator, Authy)</li>
                    <li><strong>Hardware tokens:</strong> Physical devices that generate codes</li>
                    <li><strong>Biometric authentication:</strong> Fingerprint, face, or voice recognition</li>
                    <li><strong>Email verification:</strong> Codes sent to your email</li>
                </ul>
                
                <h3>Common Password Mistakes:</h3>
                <ul>
                    <li><strong>Using weak passwords:</strong> "password", "123456", "qwerty"</li>
                    <li><strong>Reusing passwords:</strong> Same password for multiple accounts</li>
                    <li><strong>Sharing passwords:</strong> Giving passwords to others</li>
                    <li><strong>Storing insecurely:</strong> Writing passwords on sticky notes</li>
                    <li><strong>Not updating:</strong> Using the same password for years</li>
                </ul>
                
                <h3>Password Recovery Security:</h3>
                <ul>
                    <li><strong>Security questions:</strong> Use answers that aren't easily guessable</li>
                    <li><strong>Recovery email:</strong> Use a secure, separate email account</li>
                    <li><strong>Backup codes:</strong> Store recovery codes securely</li>
                    <li><strong>Account monitoring:</strong> Watch for suspicious activity</li>
                </ul>
                
                <h3>Social Engineering and Passwords:</h3>
                <p>Attackers use various techniques to steal passwords:</p>
                <ul>
                    <li><strong>Phishing:</strong> Fake login pages to capture passwords</li>
                    <li><strong>Shoulder surfing:</strong> Watching you type passwords</li>
                    <li><strong>Keyloggers:</strong> Malware that records keystrokes</li>
                    <li><strong>Social manipulation:</strong> Tricking you into revealing passwords</li>
                </ul>
            ''',
            'learning_objectives': [
                'Understand password security best practices',
                'Learn about multi-factor authentication methods',
                'Identify common password security mistakes',
                'Develop strategies to protect against password-based attacks'
            ],
            'estimated_time': 35,  # minutes
            'difficulty_level': 'intermediate'
        }

class Module4Questions:
    """Knowledge check questions for Module 4"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 4"""
        return [
            {
                'question_text': 'What is the minimum recommended password length?',
                'option_a': '8 characters',
                'option_b': '12 characters',
                'option_c': '6 characters',
                'option_d': '16 characters',
                'correct_answer': 'b',
                'explanation': 'The minimum recommended password length is 12 characters for better security.',
                'question_set': 1
            },
            {
                'question_text': 'What is multi-factor authentication (MFA)?',
                'option_a': 'Using multiple passwords',
                'option_b': 'Adding an extra layer of security beyond passwords',
                'option_c': 'Using only biometric authentication',
                'option_d': 'Sharing passwords with others',
                'correct_answer': 'b',
                'explanation': 'MFA adds an extra layer of security by requiring multiple forms of verification.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is a strong password?',
                'option_a': 'password123',
                'option_b': 'MyDogSpot2023!',
                'option_c': '123456789',
                'option_d': 'qwerty',
                'correct_answer': 'b',
                'explanation': 'MyDogSpot2023! is strong because it has length, complexity, and includes symbols.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do with passwords?',
                'option_a': 'Share them with trusted friends',
                'option_b': 'Use the same password for all accounts',
                'option_c': 'Use different passwords for each account',
                'option_d': 'Write them on sticky notes',
                'correct_answer': 'c',
                'explanation': 'You should use different passwords for each account to minimize risk.',
                'question_set': 1
            },
            {
                'question_text': 'What is a password manager?',
                'option_a': 'A person who remembers your passwords',
                'option_b': 'Software that securely stores and generates passwords',
                'option_c': 'A notebook for writing passwords',
                'option_d': 'A website that shares passwords',
                'correct_answer': 'b',
                'explanation': 'A password manager is software that securely stores and generates passwords.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 4"""
        return [
            {
                'question_text': 'Which of the following is NOT a type of MFA?',
                'option_a': 'SMS text messages',
                'option_b': 'Authenticator apps',
                'option_c': 'Using the same password twice',
                'option_d': 'Biometric authentication',
                'correct_answer': 'c',
                'explanation': 'Using the same password twice is not a form of multi-factor authentication.',
                'question_set': 2
            },
            {
                'question_text': 'What is shoulder surfing?',
                'option_a': 'A type of password manager',
                'option_b': 'Watching someone type their password',
                'option_c': 'A security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'b',
                'explanation': 'Shoulder surfing is watching someone type their password to steal it.',
                'question_set': 2
            },
            {
                'question_text': 'How often should you change your passwords?',
                'option_a': 'Never',
                'option_b': 'Only when forced',
                'option_c': 'Periodically and when compromised',
                'option_d': 'Every day',
                'correct_answer': 'c',
                'explanation': 'You should change passwords periodically and immediately when compromised.',
                'question_set': 2
            },
            {
                'question_text': 'What is a keylogger?',
                'option_a': 'A type of password manager',
                'option_b': 'Malware that records keystrokes',
                'option_c': 'A security feature',
                'option_d': 'A type of MFA',
                'correct_answer': 'b',
                'explanation': 'A keylogger is malware that records keystrokes to steal passwords.',
                'question_set': 2
            },
            {
                'question_text': 'What should you avoid in passwords?',
                'option_a': 'Uppercase letters',
                'option_b': 'Personal information like names and birthdays',
                'option_c': 'Numbers',
                'option_d': 'Symbols',
                'correct_answer': 'b',
                'explanation': 'You should avoid personal information like names and birthdays in passwords.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 4"""
        return [
            {
                'question_text': 'What are the three factors of authentication?',
                'option_a': 'Something you know, have, and are',
                'option_b': 'Something you see, hear, and touch',
                'option_c': 'Something you want, need, and like',
                'option_d': 'Something you buy, sell, and trade',
                'correct_answer': 'a',
                'explanation': 'The three factors are something you know (password), have (phone), and are (fingerprint).',
                'question_set': 3
            },
            {
                'question_text': 'What is the best way to store passwords?',
                'option_a': 'On sticky notes',
                'option_b': 'In a password manager',
                'option_c': 'In a text file on your computer',
                'option_d': 'Sharing them with friends',
                'correct_answer': 'b',
                'explanation': 'A password manager is the best way to securely store passwords.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do if your password is compromised?',
                'option_a': 'Ignore it',
                'option_b': 'Change it immediately',
                'option_c': 'Share it with others',
                'option_d': 'Write it down',
                'correct_answer': 'b',
                'explanation': 'You should change compromised passwords immediately.',
                'question_set': 3
            },
            {
                'question_text': 'What is biometric authentication?',
                'option_a': 'Using passwords',
                'option_b': 'Using physical characteristics like fingerprints',
                'option_c': 'Using SMS codes',
                'option_d': 'Using email verification',
                'correct_answer': 'b',
                'explanation': 'Biometric authentication uses physical characteristics like fingerprints or face recognition.',
                'question_set': 3
            },
            {
                'question_text': 'Why is MFA important?',
                'option_a': 'It makes logging in faster',
                'option_b': 'It adds an extra layer of security',
                'option_c': 'It reduces password complexity',
                'option_d': 'It allows password sharing',
                'correct_answer': 'b',
                'explanation': 'MFA is important because it adds an extra layer of security beyond just passwords.',
                'question_set': 3
            }
        ]

