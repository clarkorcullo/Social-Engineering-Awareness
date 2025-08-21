"""
Module 5: Social Media Security
Content and knowledge check questions for Module 5
"""

from typing import List, Dict, Any

class Module5Content:
    """Content for Module 5: Social Media Security"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Social Media Security',
            'description': 'Protecting yourself from social engineering attacks on social media',
            'content': '''
                <h2>Social Media Security Risks</h2>
                
                <h3>Common Social Media Threats:</h3>
                <ul>
                    <li><strong>Fake profiles:</strong> Attackers create fake accounts to gather information</li>
                    <li><strong>Oversharing:</strong> Revealing too much personal information</li>
                    <li><strong>Location sharing:</strong> Revealing your whereabouts and routines</li>
                    <li><strong>Fake contests and surveys:</strong> Collecting personal data</li>
                    <li><strong>Malicious links:</strong> Clicking on harmful content</li>
                    <li><strong>Social engineering scams:</strong> Manipulation through social connections</li>
                </ul>
                
                <h3>Information Attackers Collect:</h3>
                <ul>
                    <li><strong>Personal details:</strong> Full name, birth date, address, phone number</li>
                    <li><strong>Work information:</strong> Company, job title, colleagues</li>
                    <li><strong>Family details:</strong> Spouse, children, relatives</li>
                    <li><strong>Hobbies and interests:</strong> Used for targeted attacks</li>
                    <li><strong>Travel plans:</strong> When you'll be away from home</li>
                    <li><strong>Financial information:</strong> Income, purchases, lifestyle</li>
                </ul>
                
                <h3>Privacy Settings Best Practices:</h3>
                <ul>
                    <li><strong>Review regularly:</strong> Check privacy settings monthly</li>
                    <li><strong>Limit audience:</strong> Use "Friends only" or "Private" settings</li>
                    <li><strong>Control tagging:</strong> Approve tags before they appear</li>
                    <li><strong>Location services:</strong> Disable when not needed</li>
                    <li><strong>Third-party apps:</strong> Limit access to your data</li>
                    <li><strong>Search visibility:</strong> Control who can find your profile</li>
                </ul>
                
                <h3>Safe Social Media Practices:</h3>
                <ul>
                    <li><strong>Think before posting:</strong> Consider what information you're sharing</li>
                    <li><strong>Verify friend requests:</strong> Only accept from people you know</li>
                    <li><strong>Be cautious with links:</strong> Don't click suspicious URLs</li>
                    <li><strong>Use strong passwords:</strong> Different passwords for each platform</li>
                    <li><strong>Enable two-factor authentication:</strong> Add extra security</li>
                    <li><strong>Log out when done:</strong> Especially on shared devices</li>
                </ul>
                
                <h3>Social Engineering on Social Media:</h3>
                <p>Attackers use social media for various social engineering tactics:</p>
                <ul>
                    <li><strong>Impersonation:</strong> Creating fake profiles of people you know</li>
                    <li><strong>Fake emergencies:</strong> Claiming to need urgent help</li>
                    <li><strong>Fake contests:</strong> Offering prizes in exchange for information</li>
                    <li><strong>Romance scams:</strong> Building fake relationships to exploit</li>
                    <li><strong>Job scams:</strong> Fake job offers to collect information</li>
                </ul>
                
                <h3>Red Flags to Watch For:</h3>
                <ul>
                    <li><strong>Unsolicited friend requests:</strong> From people you don't know</li>
                    <li><strong>Urgent requests for help:</strong> Especially involving money</li>
                    <li><strong>Too-good-to-be-true offers:</strong> Free prizes, job opportunities</li>
                    <li><strong>Requests for personal information:</strong> Via private messages</li>
                    <li><strong>Pressure tactics:</strong> "Act now or miss out"</li>
                    <li><strong>Inconsistent stories:</strong> Details that don't add up</li>
                </ul>
                
                <h3>What to Do If You're Targeted:</h3>
                <ol>
                    <li><strong>Don't respond:</strong> Ignore suspicious messages</li>
                    <li><strong>Block and report:</strong> Use platform reporting tools</li>
                    <li><strong>Document everything:</strong> Screenshots of suspicious activity</li>
                    <li><strong>Warn others:</strong> Alert friends and family</li>
                    <li><strong>Change passwords:</strong> If you suspect compromise</li>
                    <li><strong>Contact authorities:</strong> For serious threats or fraud</li>
                </ol>
            ''',
            'learning_objectives': [
                'Understand social media security risks and threats',
                'Learn privacy settings and safe practices',
                'Identify social engineering tactics on social media',
                'Develop strategies to protect personal information online'
            ],
            'estimated_time': 30,  # minutes
            'difficulty_level': 'intermediate'
        }

class Module5Questions:
    """Knowledge check questions for Module 5"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 5"""
        return [
            {
                'question_text': 'What is a common social media security risk?',
                'option_a': 'Using strong passwords',
                'option_b': 'Oversharing personal information',
                'option_c': 'Enabling two-factor authentication',
                'option_d': 'Using privacy settings',
                'correct_answer': 'b',
                'explanation': 'Oversharing personal information is a common social media security risk.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do with friend requests from people you don\'t know?',
                'option_a': 'Accept them immediately',
                'option_b': 'Ignore or decline them',
                'option_c': 'Share your personal information',
                'option_d': 'Send them money',
                'correct_answer': 'b',
                'explanation': 'You should ignore or decline friend requests from people you don\'t know.',
                'question_set': 1
            },
            {
                'question_text': 'How often should you review your privacy settings?',
                'option_a': 'Never',
                'option_b': 'Monthly',
                'option_c': 'Once a year',
                'option_d': 'Only when forced',
                'correct_answer': 'b',
                'explanation': 'You should review your privacy settings monthly to ensure they\'re still appropriate.',
                'question_set': 1
            },
            {
                'question_text': 'What is location sharing?',
                'option_a': 'A security feature',
                'option_b': 'Revealing your whereabouts and routines',
                'option_c': 'A type of password',
                'option_d': 'A social media app',
                'correct_answer': 'b',
                'explanation': 'Location sharing reveals your whereabouts and routines, which can be a security risk.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do with suspicious links on social media?',
                'option_a': 'Click them immediately',
                'option_b': 'Share them with friends',
                'option_c': 'Don\'t click them',
                'option_d': 'Reply to the sender',
                'correct_answer': 'c',
                'explanation': 'You should not click suspicious links on social media.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 5"""
        return [
            {
                'question_text': 'What is a fake profile?',
                'option_a': 'A legitimate business account',
                'option_b': 'An account created by attackers to gather information',
                'option_c': 'A verified account',
                'option_d': 'A private account',
                'correct_answer': 'b',
                'explanation': 'A fake profile is an account created by attackers to gather information.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do if you receive an urgent request for help on social media?',
                'option_a': 'Send money immediately',
                'option_b': 'Verify the request through other means',
                'option_c': 'Share your personal information',
                'option_d': 'Ignore it completely',
                'correct_answer': 'b',
                'explanation': 'You should verify urgent requests for help through other means before responding.',
                'question_set': 2
            },
            {
                'question_text': 'What is a romance scam?',
                'option_a': 'A legitimate dating service',
                'option_b': 'Building fake relationships to exploit victims',
                'option_c': 'A type of privacy setting',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'A romance scam involves building fake relationships to exploit victims.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do with too-good-to-be-true offers on social media?',
                'option_a': 'Accept them immediately',
                'option_b': 'Be skeptical and investigate',
                'option_c': 'Share them with everyone',
                'option_d': 'Send personal information',
                'correct_answer': 'b',
                'explanation': 'You should be skeptical and investigate too-good-to-be-true offers.',
                'question_set': 2
            },
            {
                'question_text': 'What is the best practice for social media passwords?',
                'option_a': 'Use the same password for all platforms',
                'option_b': 'Use different passwords for each platform',
                'option_c': 'Share passwords with friends',
                'option_d': 'Never change passwords',
                'correct_answer': 'b',
                'explanation': 'You should use different passwords for each social media platform.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 5"""
        return [
            {
                'question_text': 'What should you do if you\'re targeted by a social media scam?',
                'option_a': 'Respond to the scammer',
                'option_b': 'Block and report the account',
                'option_c': 'Share your personal information',
                'option_d': 'Send money to resolve it',
                'correct_answer': 'b',
                'explanation': 'You should block and report the account if you\'re targeted by a social media scam.',
                'question_set': 3
            },
            {
                'question_text': 'What information do attackers typically collect from social media?',
                'option_a': 'Only public posts',
                'option_b': 'Personal details, work information, family details, and more',
                'option_c': 'Only profile pictures',
                'option_d': 'Only usernames',
                'correct_answer': 'b',
                'explanation': 'Attackers collect personal details, work information, family details, and much more.',
                'question_set': 3
            },
            {
                'question_text': 'What is a job scam on social media?',
                'option_a': 'A legitimate job posting',
                'option_b': 'Fake job offers to collect information',
                'option_c': 'A type of privacy setting',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'A job scam involves fake job offers designed to collect personal information.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do when using social media on shared devices?',
                'option_a': 'Stay logged in',
                'option_b': 'Log out when done',
                'option_c': 'Share your password',
                'option_d': 'Ignore security warnings',
                'correct_answer': 'b',
                'explanation': 'You should log out when done using social media on shared devices.',
                'question_set': 3
            },
            {
                'question_text': 'What is the "think before posting" rule?',
                'option_a': 'Post everything immediately',
                'option_b': 'Consider what information you\'re sharing before posting',
                'option_c': 'Ignore privacy concerns',
                'option_d': 'Share everything with everyone',
                'correct_answer': 'b',
                'explanation': 'The "think before posting" rule means considering what information you\'re sharing before posting.',
                'question_set': 3
            }
        ]

