"""
Module 6: Physical Security and Social Engineering
Content and knowledge check questions for Module 6
"""

from typing import List, Dict, Any

class Module6Content:
    """Content for Module 6: Physical Security and Social Engineering"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Physical Security and Social Engineering',
            'description': 'Understanding physical security threats and social engineering in the real world',
            'content': '''
                <h2>Physical Security Threats</h2>
                
                <h3>Common Physical Social Engineering Attacks:</h3>
                <ul>
                    <li><strong>Tailgating:</strong> Following someone through secure doors</li>
                    <li><strong>Piggybacking:</strong> Using someone else's access credentials</li>
                    <li><strong>Dumpster diving:</strong> Searching through trash for sensitive information</li>
                    <li><strong>Shoulder surfing:</strong> Watching someone enter passwords or PINs</li>
                    <li><strong>Impersonation:</strong> Pretending to be authorized personnel</li>
                    <li><strong>Baiting:</strong> Leaving infected devices in public places</li>
                </ul>
                
                <h3>Workplace Security Risks:</h3>
                <ul>
                    <li><strong>Unsecured workstations:</strong> Leaving computers unlocked</li>
                    <li><strong>Visible passwords:</strong> Writing passwords on sticky notes</li>
                    <li><strong>Unattended documents:</strong> Leaving sensitive papers on desks</li>
                    <li><strong>Unlocked filing cabinets:</strong> Easy access to confidential files</li>
                    <li><strong>Unsecured printers:</strong> Sensitive documents left in trays</li>
                    <li><strong>Unattended mobile devices:</strong> Phones and tablets left unlocked</li>
                </ul>
                
                <h3>Physical Security Best Practices:</h3>
                <ul>
                    <li><strong>Lock your workstation:</strong> Always lock when stepping away</li>
                    <li><strong>Secure your desk:</strong> Lock drawers and cabinets</li>
                    <li><strong>Shred documents:</strong> Properly dispose of sensitive papers</li>
                    <li><strong>Be aware of surroundings:</strong> Notice who's around when entering passwords</li>
                    <li><strong>Challenge strangers:</strong> Ask for identification when appropriate</li>
                    <li><strong>Report suspicious activity:</strong> Alert security or management</li>
                </ul>
                
                <h3>Impersonation Tactics:</h3>
                <p>Attackers use various methods to impersonate legitimate personnel:</p>
                <ul>
                    <li><strong>Fake ID badges:</strong> Counterfeit or stolen identification</li>
                    <li><strong>Uniforms and clothing:</strong> Dressing like maintenance or delivery staff</li>
                    <li><strong>Authority claims:</strong> Pretending to be from management or IT</li>
                    <li><strong>Emergency scenarios:</strong> Creating false urgency to bypass security</li>
                    <li><strong>Social proof:</strong> Using names of real employees</li>
                </ul>
                
                <h3>Information Gathering Techniques:</h3>
                <ul>
                    <li><strong>Eavesdropping:</strong> Listening to conversations in public areas</li>
                    <li><strong>Visual observation:</strong> Watching people work or enter passwords</li>
                    <li><strong>Social interaction:</strong> Engaging in casual conversation to gather information</li>
                    <li><strong>Document theft:</strong> Taking papers from desks or printers</li>
                    <li><strong>Photography:</strong> Taking pictures of sensitive information</li>
                </ul>
                
                <h3>Prevention Strategies:</h3>
                <ul>
                    <li><strong>Employee training:</strong> Regular security awareness programs</li>
                    <li><strong>Access control:</strong> Proper badge and key management</li>
                    <li><strong>Visitor management:</strong> Escorting and monitoring guests</li>
                    <li><strong>Clean desk policy:</strong> Keeping work areas free of sensitive documents</li>
                    <li><strong>Incident reporting:</strong> Clear procedures for reporting suspicious activity</li>
                    <li><strong>Security audits:</strong> Regular assessments of physical security</li>
                </ul>
                
                <h3>What to Do If You Suspect an Attack:</h3>
                <ol>
                    <li><strong>Stay calm:</strong> Don't panic or confront the attacker</li>
                    <li><strong>Observe and remember:</strong> Note details about the person and situation</li>
                    <li><strong>Don't provide information:</strong> Be cautious about what you share</li>
                    <li><strong>Report immediately:</strong> Contact security or management</li>
                    <li><strong>Document everything:</strong> Write down what happened</li>
                    <li><strong>Follow up:</strong> Ensure the incident is properly investigated</li>
                </ol>
            ''',
            'learning_objectives': [
                'Understand physical security threats and social engineering tactics',
                'Learn workplace security best practices',
                'Identify impersonation and information gathering techniques',
                'Develop strategies to prevent physical security breaches'
            ],
            'estimated_time': 35,  # minutes
            'difficulty_level': 'intermediate'
        }

class Module6Questions:
    """Knowledge check questions for Module 6"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 6"""
        return [
            {
                'question_text': 'What is tailgating?',
                'option_a': 'Following someone through secure doors',
                'option_b': 'A type of email attack',
                'option_c': 'A password security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'a',
                'explanation': 'Tailgating is following someone through secure doors without proper authorization.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do when leaving your workstation?',
                'option_a': 'Leave it unlocked for convenience',
                'option_b': 'Lock your workstation',
                'option_c': 'Share your password with colleagues',
                'option_d': 'Ignore security warnings',
                'correct_answer': 'b',
                'explanation': 'You should always lock your workstation when stepping away.',
                'question_set': 1
            },
            {
                'question_text': 'What is dumpster diving?',
                'option_a': 'A recreational activity',
                'option_b': 'Searching through trash for sensitive information',
                'option_c': 'A type of password attack',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'Dumpster diving is searching through trash for sensitive information.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do with sensitive documents?',
                'option_a': 'Leave them on your desk',
                'option_b': 'Shred them properly',
                'option_c': 'Throw them in the regular trash',
                'option_d': 'Share them with friends',
                'correct_answer': 'b',
                'explanation': 'You should shred sensitive documents properly to prevent information theft.',
                'question_set': 1
            },
            {
                'question_text': 'What is shoulder surfing?',
                'option_a': 'A type of exercise',
                'option_b': 'Watching someone enter passwords or PINs',
                'option_c': 'A security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'b',
                'explanation': 'Shoulder surfing is watching someone enter passwords or PINs to steal them.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 6"""
        return [
            {
                'question_text': 'What should you do if you see a stranger in a secure area?',
                'option_a': 'Ignore them completely',
                'option_b': 'Challenge them and ask for identification',
                'option_c': 'Help them find what they\'re looking for',
                'option_d': 'Share sensitive information with them',
                'correct_answer': 'b',
                'explanation': 'You should challenge strangers and ask for identification when appropriate.',
                'question_set': 2
            },
            {
                'question_text': 'What is impersonation in physical security?',
                'option_a': 'A legitimate business practice',
                'option_b': 'Pretending to be authorized personnel',
                'option_c': 'A type of password',
                'option_d': 'A security feature',
                'correct_answer': 'b',
                'explanation': 'Impersonation is pretending to be authorized personnel to gain access.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do with unattended documents?',
                'option_a': 'Leave them where they are',
                'option_b': 'Secure them properly',
                'option_c': 'Share them with others',
                'option_d': 'Throw them away',
                'correct_answer': 'b',
                'explanation': 'You should secure unattended documents properly to prevent information theft.',
                'question_set': 2
            },
            {
                'question_text': 'What is a clean desk policy?',
                'option_a': 'Keeping your desk messy',
                'option_b': 'Keeping work areas free of sensitive documents',
                'option_c': 'Sharing all documents with colleagues',
                'option_d': 'Ignoring security policies',
                'correct_answer': 'b',
                'explanation': 'A clean desk policy means keeping work areas free of sensitive documents.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do if you suspect a physical security attack?',
                'option_a': 'Confront the attacker directly',
                'option_b': 'Report it immediately to security or management',
                'option_c': 'Ignore it completely',
                'option_d': 'Share the information on social media',
                'correct_answer': 'b',
                'explanation': 'You should report suspected physical security attacks immediately to security or management.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 6"""
        return [
            {
                'question_text': 'What is piggybacking?',
                'option_a': 'A type of exercise',
                'option_b': 'Using someone else\'s access credentials',
                'option_c': 'A security feature',
                'option_d': 'A type of malware',
                'correct_answer': 'b',
                'explanation': 'Piggybacking is using someone else\'s access credentials to gain unauthorized access.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do with passwords at work?',
                'option_a': 'Write them on sticky notes',
                'option_b': 'Keep them secure and never share them',
                'option_c': 'Share them with trusted colleagues',
                'option_d': 'Post them on your desk',
                'correct_answer': 'b',
                'explanation': 'You should keep passwords secure and never share them with anyone.',
                'question_set': 3
            },
            {
                'question_text': 'What is eavesdropping?',
                'option_a': 'A type of exercise',
                'option_b': 'Listening to conversations in public areas',
                'option_c': 'A security feature',
                'option_d': 'A type of password',
                'correct_answer': 'b',
                'explanation': 'Eavesdropping is listening to conversations in public areas to gather information.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do with unattended mobile devices?',
                'option_a': 'Take them for yourself',
                'option_b': 'Secure them or return them to the owner',
                'option_c': 'Ignore them completely',
                'option_d': 'Share them with others',
                'correct_answer': 'b',
                'explanation': 'You should secure unattended mobile devices or return them to the owner.',
                'question_set': 3
            },
            {
                'question_text': 'What is the first step when you suspect a physical security attack?',
                'option_a': 'Panic and run away',
                'option_b': 'Stay calm and observe',
                'option_c': 'Confront the attacker',
                'option_d': 'Ignore the situation',
                'correct_answer': 'b',
                'explanation': 'The first step is to stay calm and observe the situation carefully.',
                'question_set': 3
            }
        ]

