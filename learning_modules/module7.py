"""
Module 7: Incident Response and Reporting
Content and knowledge check questions for Module 7
"""

from typing import List, Dict, Any

class Module7Content:
    """Content for Module 7: Incident Response and Reporting"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Incident Response and Reporting',
            'description': 'Learning how to respond to and report social engineering incidents',
            'content': '''
                <h2>Incident Response Framework</h2>
                
                <h3>What is an Incident?</h3>
                <p>A security incident is any event that compromises the confidentiality, integrity, or availability of information or systems. Social engineering incidents can include:</p>
                <ul>
                    <li><strong>Successful phishing attacks:</strong> When someone falls for a phishing attempt</li>
                    <li><strong>Unauthorized access:</strong> When someone gains access through social engineering</li>
                    <li><strong>Data breaches:</strong> When sensitive information is stolen</li>
                    <li><strong>Malware infections:</strong> When malicious software is installed</li>
                    <li><strong>Financial fraud:</strong> When money is stolen through deception</li>
                </ul>
                
                <h3>Incident Response Steps:</h3>
                <ol>
                    <li><strong>Preparation:</strong> Having plans and procedures in place</li>
                    <li><strong>Identification:</strong> Recognizing that an incident has occurred</li>
                    <li><strong>Containment:</strong> Limiting the damage and preventing further harm</li>
                    <li><strong>Eradication:</strong> Removing the threat and fixing vulnerabilities</li>
                    <li><strong>Recovery:</strong> Restoring normal operations</li>
                    <li><strong>Lessons Learned:</strong> Improving security based on the incident</li>
                </ol>
                
                <h3>Immediate Response Actions:</h3>
                <ul>
                    <li><strong>Don't panic:</strong> Stay calm and think clearly</li>
                    <li><strong>Document everything:</strong> Take screenshots, save emails, record details</li>
                    <li><strong>Don't delete evidence:</strong> Preserve all information related to the incident</li>
                    <li><strong>Isolate affected systems:</strong> Disconnect from network if necessary</li>
                    <li><strong>Change passwords:</strong> Update compromised accounts immediately</li>
                    <li><strong>Report immediately:</strong> Contact appropriate authorities or IT department</li>
                </ul>
                
                <h3>What Information to Document:</h3>
                <ul>
                    <li><strong>Date and time:</strong> When the incident occurred</li>
                    <li><strong>Description:</strong> What happened in detail</li>
                    <li><strong>Source:</strong> Where the attack came from (email, phone, person)</li>
                    <li><strong>Impact:</strong> What was affected or compromised</li>
                    <li><strong>Actions taken:</strong> What you did in response</li>
                    <li><strong>Evidence:</strong> Screenshots, emails, documents, etc.</li>
                </ul>
                
                <h3>Reporting Procedures:</h3>
                <ul>
                    <li><strong>Internal reporting:</strong> Notify your supervisor, IT department, or security team</li>
                    <li><strong>External reporting:</strong> Contact law enforcement if necessary</li>
                    <li><strong>Regulatory reporting:</strong> Report to relevant authorities if required</li>
                    <li><strong>Vendor reporting:</strong> Notify affected service providers</li>
                    <li><strong>Customer notification:</strong> Inform affected customers if required</li>
                </ul>
                
                <h3>Communication During Incidents:</h3>
                <ul>
                    <li><strong>Internal communication:</strong> Keep management and team informed</li>
                    <li><strong>External communication:</strong> Coordinate with public relations</li>
                    <li><strong>Customer communication:</strong> Provide clear, accurate information</li>
                    <li><strong>Media communication:</strong> Designate a spokesperson</li>
                    <li><strong>Legal communication:</strong> Consult with legal counsel</li>
                </ul>
                
                <h3>Post-Incident Activities:</h3>
                <ul>
                    <li><strong>Forensic analysis:</strong> Investigate the root cause</li>
                    <li><strong>Damage assessment:</strong> Determine the full extent of the incident</li>
                    <li><strong>Security improvements:</strong> Implement lessons learned</li>
                    <li><strong>Training updates:</strong> Enhance security awareness programs</li>
                    <li><strong>Policy review:</strong> Update security policies and procedures</li>
                    <li><strong>Monitoring enhancement:</strong> Improve detection capabilities</li>
                </ul>
                
                <h3>Prevention Through Reporting:</h3>
                <p>Reporting incidents helps prevent future attacks by:</p>
                <ul>
                    <li><strong>Identifying patterns:</strong> Recognizing common attack methods</li>
                    <li><strong>Improving defenses:</strong> Strengthening security measures</li>
                    <li><strong>Training others:</strong> Educating staff about new threats</li>
                    <li><strong>Collaborating:</strong> Sharing information with other organizations</li>
                    <li><strong>Legal action:</strong> Pursuing attackers through legal channels</li>
                </ul>
            ''',
            'learning_objectives': [
                'Understand incident response frameworks and procedures',
                'Learn how to document and report security incidents',
                'Develop skills for immediate response to social engineering attacks',
                'Understand post-incident activities and prevention strategies'
            ],
            'estimated_time': 40,  # minutes
            'difficulty_level': 'advanced'
        }

class Module7Questions:
    """Knowledge check questions for Module 7"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 7"""
        return [
            {
                'question_text': 'What is the first step in incident response?',
                'option_a': 'Panic and call everyone',
                'option_b': 'Stay calm and document everything',
                'option_c': 'Delete all evidence',
                'option_d': 'Ignore the incident',
                'correct_answer': 'b',
                'explanation': 'The first step is to stay calm and document everything about the incident.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do immediately after a social engineering incident?',
                'option_a': 'Delete all related emails',
                'option_b': 'Change compromised passwords',
                'option_c': 'Share the incident on social media',
                'option_d': 'Ignore it completely',
                'correct_answer': 'b',
                'explanation': 'You should change compromised passwords immediately after a social engineering incident.',
                'question_set': 1
            },
            {
                'question_text': 'What is containment in incident response?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Limiting damage and preventing further harm',
                'option_c': 'Deleting all evidence',
                'option_d': 'Sharing information with everyone',
                'correct_answer': 'b',
                'explanation': 'Containment means limiting damage and preventing further harm from the incident.',
                'question_set': 1
            },
            {
                'question_text': 'What should you document during an incident?',
                'option_a': 'Only the date',
                'option_b': 'Date, time, description, source, impact, and actions taken',
                'option_c': 'Only what you remember',
                'option_d': 'Nothing at all',
                'correct_answer': 'b',
                'explanation': 'You should document date, time, description, source, impact, and actions taken.',
                'question_set': 1
            },
            {
                'question_text': 'What should you do with evidence from an incident?',
                'option_a': 'Delete it immediately',
                'option_b': 'Preserve it for investigation',
                'option_c': 'Share it on social media',
                'option_d': 'Ignore it completely',
                'correct_answer': 'b',
                'explanation': 'You should preserve evidence for investigation and documentation.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 7"""
        return [
            {
                'question_text': 'Who should you report incidents to?',
                'option_a': 'Only your friends',
                'option_b': 'Your supervisor, IT department, or security team',
                'option_c': 'Social media followers',
                'option_d': 'No one',
                'correct_answer': 'b',
                'explanation': 'You should report incidents to your supervisor, IT department, or security team.',
                'question_set': 2
            },
            {
                'question_text': 'What is the purpose of post-incident activities?',
                'option_a': 'To forget about the incident',
                'option_b': 'To learn from the incident and improve security',
                'option_c': 'To blame others',
                'option_d': 'To hide the incident',
                'correct_answer': 'b',
                'explanation': 'Post-incident activities help learn from the incident and improve security.',
                'question_set': 2
            },
            {
                'question_text': 'What should you do if you suspect a data breach?',
                'option_a': 'Ignore it completely',
                'option_b': 'Report it immediately and preserve evidence',
                'option_c': 'Delete all related files',
                'option_d': 'Share it on social media',
                'correct_answer': 'b',
                'explanation': 'You should report data breaches immediately and preserve evidence.',
                'question_set': 2
            },
            {
                'question_text': 'What is forensic analysis?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Investigating the root cause of an incident',
                'option_c': 'Deleting evidence',
                'option_d': 'Sharing information publicly',
                'correct_answer': 'b',
                'explanation': 'Forensic analysis involves investigating the root cause of an incident.',
                'question_set': 2
            },
            {
                'question_text': 'Why is reporting incidents important?',
                'option_a': 'To get attention',
                'option_b': 'To help prevent future attacks and improve security',
                'option_c': 'To blame others',
                'option_d': 'To waste time',
                'correct_answer': 'b',
                'explanation': 'Reporting incidents helps prevent future attacks and improve security.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 7"""
        return [
            {
                'question_text': 'What should you do if you receive a suspicious email?',
                'option_a': 'Reply immediately',
                'option_b': 'Report it to IT and don\'t click any links',
                'option_c': 'Forward it to all your contacts',
                'option_d': 'Delete it without reporting',
                'correct_answer': 'b',
                'explanation': 'You should report suspicious emails to IT and not click any links.',
                'question_set': 3
            },
            {
                'question_text': 'What is the "lessons learned" phase?',
                'option_a': 'Forgetting about the incident',
                'option_b': 'Improving security based on the incident',
                'option_c': 'Blaming others',
                'option_d': 'Hiding the incident',
                'correct_answer': 'b',
                'explanation': 'The lessons learned phase involves improving security based on the incident.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do if you accidentally clicked a phishing link?',
                'option_a': 'Ignore it completely',
                'option_b': 'Report it immediately and change passwords',
                'option_c': 'Click more links',
                'option_d': 'Share it with friends',
                'correct_answer': 'b',
                'explanation': 'You should report it immediately and change passwords if you clicked a phishing link.',
                'question_set': 3
            },
            {
                'question_text': 'What is damage assessment?',
                'option_a': 'Ignoring the problem',
                'option_b': 'Determining the full extent of an incident',
                'option_c': 'Deleting evidence',
                'option_d': 'Sharing information publicly',
                'correct_answer': 'b',
                'explanation': 'Damage assessment involves determining the full extent of an incident.',
                'question_set': 3
            },
            {
                'question_text': 'What should you do during an incident?',
                'option_a': 'Panic and run away',
                'option_b': 'Stay calm and follow incident response procedures',
                'option_c': 'Delete all evidence',
                'option_d': 'Ignore all warnings',
                'correct_answer': 'b',
                'explanation': 'You should stay calm and follow incident response procedures during an incident.',
                'question_set': 3
            }
        ]

