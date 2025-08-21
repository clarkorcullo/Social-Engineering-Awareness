"""
Module 2: Types of Social Engineering Attacks
Content and knowledge check questions for Module 2
"""

from typing import List, Dict, Any

class Module2Content:
    """Content for Module 2: Types of Social Engineering Attacks"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Types of Social Engineering Attacks',
            'description': 'Understanding different types of social engineering attacks and their characteristics',
            'content': '''
                <h2>Common Types of Social Engineering Attacks</h2>
                
                <h3>1. Phishing Attacks</h3>
                <p>Phishing is the most common type of social engineering attack. Attackers send fraudulent emails, text messages, or create fake websites that appear to come from legitimate sources to steal sensitive information.</p>
                <ul>
                    <li><strong>Email Phishing:</strong> Fraudulent emails pretending to be from trusted sources</li>
                    <li><strong>Spear Phishing:</strong> Targeted phishing attacks against specific individuals or organizations</li>
                    <li><strong>Whaling:</strong> Phishing attacks targeting high-level executives</li>
                    <li><strong>Vishing:</strong> Voice phishing using phone calls</li>
                    <li><strong>Smishing:</strong> SMS phishing using text messages</li>
                </ul>
                
                <h3>2. Pretexting</h3>
                <p>Pretexting involves creating a fabricated scenario to obtain information. Attackers pretend to be someone they're not, such as a co-worker, IT support, or a trusted authority figure.</p>
                <ul>
                    <li>Creating false identities</li>
                    <li>Building trust through deception</li>
                    <li>Using authority to gain compliance</li>
                    <li>Exploiting human helpfulness</li>
                </ul>
                
                <h3>3. Baiting</h3>
                <p>Baiting uses physical media to spread malware. Attackers leave infected USB drives, CDs, or other devices in public places, hoping someone will pick them up and use them.</p>
                <ul>
                    <li>Infected USB drives</li>
                    <li>Malicious CDs or DVDs</li>
                    <li>Compromised mobile devices</li>
                    <li>Fake software downloads</li>
                </ul>
                
                <h3>4. Quid Pro Quo</h3>
                <p>Quid pro quo attacks involve offering a service in exchange for information or access. Attackers promise something valuable in return for sensitive data.</p>
                <ul>
                    <li>Fake IT support calls</li>
                    <li>Software installation offers</li>
                    <li>Free security assessments</li>
                    <li>Technical assistance scams</li>
                </ul>
                
                <h3>5. Tailgating</h3>
                <p>Tailgating occurs when an unauthorized person follows an authorized person into a restricted area. This physical social engineering technique exploits human courtesy.</p>
                <ul>
                    <li>Following someone through secure doors</li>
                    <li>Piggybacking on access cards</li>
                    <li>Exploiting human courtesy</li>
                    <li>Physical access to restricted areas</li>
                </ul>
                
                <h3>6. Watering Hole Attacks</h3>
                <p>Watering hole attacks target websites that are likely to be visited by the intended victims. Attackers compromise these sites to infect visitors with malware.</p>
                <ul>
                    <li>Compromising frequently visited websites</li>
                    <li>Targeting specific user groups</li>
                    <li>Exploiting website vulnerabilities</li>
                    <li>Distributing malware to visitors</li>
                </ul>
                
                <h3>Attack Characteristics:</h3>
                <ul>
                    <li><strong>Urgency:</strong> Creating time pressure to bypass rational thinking</li>
                    <li><strong>Authority:</strong> Impersonating someone in a position of power</li>
                    <li><strong>Scarcity:</strong> Making offers seem limited or exclusive</li>
                    <li><strong>Social Proof:</strong> Using peer pressure or group influence</li>
                    <li><strong>Reciprocity:</strong> Offering something to create obligation</li>
                </ul>
            ''',
            'learning_objectives': [
                'Identify different types of social engineering attacks',
                'Understand the characteristics and methods of each attack type',
                'Recognize common attack patterns and techniques',
                'Learn how to identify and respond to different attack types'
            ],
            'estimated_time': 35,  # minutes
            'difficulty_level': 'intermediate'
        }

class Module2Questions:
    """Knowledge check questions for Module 2"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 2"""
        return [
            {
                'question_text': 'What is the most common type of social engineering attack?',
                'option_a': 'Pretexting',
                'option_b': 'Phishing',
                'option_c': 'Baiting',
                'option_d': 'Tailgating',
                'correct_answer': 'b',
                'explanation': 'Phishing is the most common type of social engineering attack, involving fraudulent emails, texts, or websites.',
                'question_set': 1
            },
            {
                'question_text': 'What is spear phishing?',
                'option_a': 'A general phishing attack sent to many people',
                'option_b': 'A targeted phishing attack against specific individuals or organizations',
                'option_c': 'A phishing attack using voice calls',
                'option_d': 'A phishing attack using physical media',
                'correct_answer': 'b',
                'explanation': 'Spear phishing is a targeted phishing attack against specific individuals or organizations.',
                'question_set': 1
            },
            {
                'question_text': 'What is pretexting?',
                'option_a': 'Creating fake websites',
                'option_b': 'Creating a fabricated scenario to obtain information',
                'option_c': 'Leaving infected USB drives',
                'option_d': 'Following someone through secure doors',
                'correct_answer': 'b',
                'explanation': 'Pretexting involves creating a fabricated scenario to obtain information by pretending to be someone else.',
                'question_set': 1
            },
            {
                'question_text': 'What is baiting?',
                'option_a': 'Using phone calls to trick people',
                'option_b': 'Using physical media to spread malware',
                'option_c': 'Creating fake identities',
                'option_d': 'Exploiting website vulnerabilities',
                'correct_answer': 'b',
                'explanation': 'Baiting uses physical media like infected USB drives to spread malware.',
                'question_set': 1
            },
            {
                'question_text': 'What is quid pro quo?',
                'option_a': 'A type of phishing attack',
                'option_b': 'Offering a service in exchange for information',
                'option_c': 'A physical security breach',
                'option_d': 'A website compromise',
                'correct_answer': 'b',
                'explanation': 'Quid pro quo involves offering a service in exchange for information or access.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 2"""
        return [
            {
                'question_text': 'What is tailgating?',
                'option_a': 'Following someone through secure doors',
                'option_b': 'Sending fraudulent emails',
                'option_c': 'Creating fake websites',
                'option_d': 'Using infected USB drives',
                'correct_answer': 'a',
                'explanation': 'Tailgating occurs when an unauthorized person follows an authorized person into a restricted area.',
                'question_set': 2
            },
            {
                'question_text': 'What is a watering hole attack?',
                'option_a': 'Compromising frequently visited websites',
                'option_b': 'Using phone calls to trick people',
                'option_c': 'Leaving infected devices in public',
                'option_d': 'Creating fake identities',
                'correct_answer': 'a',
                'explanation': 'Watering hole attacks target websites that are likely to be visited by intended victims.',
                'question_set': 2
            },
            {
                'question_text': 'Which attack type exploits human courtesy?',
                'option_a': 'Phishing',
                'option_b': 'Pretexting',
                'option_c': 'Tailgating',
                'option_d': 'Baiting',
                'correct_answer': 'c',
                'explanation': 'Tailgating exploits human courtesy by following someone through secure doors.',
                'question_set': 2
            },
            {
                'question_text': 'What is vishing?',
                'option_a': 'Voice phishing using phone calls',
                'option_b': 'SMS phishing using text messages',
                'option_c': 'Email phishing',
                'option_d': 'Website phishing',
                'correct_answer': 'a',
                'explanation': 'Vishing is voice phishing using phone calls.',
                'question_set': 2
            },
            {
                'question_text': 'What is whaling?',
                'option_a': 'Phishing attacks targeting high-level executives',
                'option_b': 'General phishing attacks',
                'option_c': 'SMS phishing attacks',
                'option_d': 'Voice phishing attacks',
                'correct_answer': 'a',
                'explanation': 'Whaling refers to phishing attacks specifically targeting high-level executives.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 2"""
        return [
            {
                'question_text': 'Which attack characteristic creates time pressure?',
                'option_a': 'Authority',
                'option_b': 'Urgency',
                'option_c': 'Scarcity',
                'option_d': 'Social proof',
                'correct_answer': 'b',
                'explanation': 'Urgency creates time pressure to bypass rational thinking.',
                'question_set': 3
            },
            {
                'question_text': 'What is smishing?',
                'option_a': 'Email phishing',
                'option_b': 'SMS phishing using text messages',
                'option_c': 'Voice phishing',
                'option_d': 'Website phishing',
                'correct_answer': 'b',
                'explanation': 'Smishing is SMS phishing using text messages.',
                'question_set': 3
            },
            {
                'question_text': 'Which attack type uses physical media?',
                'option_a': 'Phishing',
                'option_b': 'Baiting',
                'option_c': 'Pretexting',
                'option_d': 'Quid pro quo',
                'correct_answer': 'b',
                'explanation': 'Baiting uses physical media like infected USB drives to spread malware.',
                'question_set': 3
            },
            {
                'question_text': 'What is the main goal of watering hole attacks?',
                'option_a': 'To steal physical devices',
                'option_b': 'To infect visitors with malware',
                'option_c': 'To gain physical access',
                'option_d': 'To create fake identities',
                'correct_answer': 'b',
                'explanation': 'Watering hole attacks aim to infect visitors with malware by compromising frequently visited websites.',
                'question_set': 3
            },
            {
                'question_text': 'Which attack type involves offering something in return?',
                'option_a': 'Phishing',
                'option_b': 'Baiting',
                'option_c': 'Quid pro quo',
                'option_d': 'Tailgating',
                'correct_answer': 'c',
                'explanation': 'Quid pro quo involves offering a service in exchange for information or access.',
                'question_set': 3
            }
        ]

