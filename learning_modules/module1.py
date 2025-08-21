"""
Module 1: Introduction to Social Engineering
Content and knowledge check questions for Module 1
"""

from typing import List, Dict, Any

class Module1Content:
    """Content for Module 1: Introduction to Social Engineering"""
    
    @staticmethod
    def get_content() -> Dict[str, Any]:
        """Get module content"""
        return {
            'title': 'Introduction to Social Engineering',
            'description': 'Understanding the basics of social engineering and its impact on cybersecurity',
            'content': '''
                <h2>What is Social Engineering?</h2>
                <p>Social engineering is a psychological manipulation technique used by cybercriminals to trick individuals into revealing confidential information, performing actions, or making security mistakes. Unlike technical hacking methods, social engineering relies on human psychology and social interaction.</p>
                
                <h3>Key Concepts:</h3>
                <ul>
                    <li><strong>Psychological Manipulation:</strong> Exploiting human emotions like fear, greed, or curiosity</li>
                    <li><strong>Trust Exploitation:</strong> Building false trust to gain access to information</li>
                    <li><strong>Authority Impersonation:</strong> Pretending to be someone in authority</li>
                    <li><strong>Urgency Creation:</strong> Creating false urgency to bypass rational thinking</li>
                </ul>
                
                <h3>Why Social Engineering Works:</h3>
                <p>Social engineering is effective because it targets the weakest link in any security system: human psychology. Even the most sophisticated technical security measures can be bypassed if an attacker can manipulate a person into providing access or information.</p>
                
                <h3>Common Targets:</h3>
                <ul>
                    <li>Employees in organizations</li>
                    <li>Customer service representatives</li>
                    <li>IT support staff</li>
                    <li>Executives and decision-makers</li>
                    <li>General public</li>
                </ul>
                
                <h3>Impact on Organizations:</h3>
                <p>Social engineering attacks can result in:</p>
                <ul>
                    <li>Data breaches and information theft</li>
                    <li>Financial losses</li>
                    <li>Reputation damage</li>
                    <li>Regulatory compliance violations</li>
                    <li>Operational disruption</li>
                </ul>
                
                <h3>Prevention Strategies:</h3>
                <ul>
                    <li>Employee awareness training</li>
                    <li>Verification procedures</li>
                    <li>Incident reporting protocols</li>
                    <li>Regular security assessments</li>
                    <li>Multi-factor authentication</li>
                </ul>
            ''',
            'learning_objectives': [
                'Understand what social engineering is and how it works',
                'Identify why social engineering attacks are effective',
                'Recognize common targets and impacts',
                'Learn basic prevention strategies'
            ],
            'estimated_time': 30,  # minutes
            'difficulty_level': 'beginner'
        }

class Module1Questions:
    """Knowledge check questions for Module 1"""
    
    @staticmethod
    def get_question_set_1() -> List[Dict[str, Any]]:
        """Get question set 1 for Module 1"""
        return [
            {
                'question_text': 'What is the primary method used in social engineering attacks?',
                'option_a': 'Technical hacking and coding',
                'option_b': 'Psychological manipulation and human interaction',
                'option_c': 'Physical security breaches',
                'option_d': 'Network infrastructure attacks',
                'correct_answer': 'b',
                'explanation': 'Social engineering primarily relies on psychological manipulation and human interaction rather than technical methods.',
                'question_set': 1
            },
            {
                'question_text': 'Why is social engineering considered effective against organizations?',
                'option_a': 'Because it requires expensive equipment',
                'option_b': 'Because it targets the weakest link: human psychology',
                'option_c': 'Because it only works on small companies',
                'option_d': 'Because it requires advanced technical skills',
                'correct_answer': 'b',
                'explanation': 'Social engineering targets human psychology, which is often the weakest link in security systems.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is NOT a common social engineering technique?',
                'option_a': 'Building false trust',
                'option_b': 'Creating urgency',
                'option_c': 'Impersonating authority figures',
                'option_d': 'Direct network hacking',
                'correct_answer': 'd',
                'explanation': 'Direct network hacking is a technical attack method, not a social engineering technique.',
                'question_set': 1
            },
            {
                'question_text': 'What is the main goal of social engineering attacks?',
                'option_a': 'To damage computer hardware',
                'option_b': 'To trick people into revealing information or performing actions',
                'option_c': 'To improve network security',
                'option_d': 'To create new software programs',
                'correct_answer': 'b',
                'explanation': 'The main goal is to manipulate people into revealing confidential information or performing security-compromising actions.',
                'question_set': 1
            },
            {
                'question_text': 'Which of the following is an effective prevention strategy against social engineering?',
                'option_a': 'Ignoring suspicious emails',
                'option_b': 'Employee awareness training',
                'option_c': 'Using only strong passwords',
                'option_d': 'Installing antivirus software',
                'correct_answer': 'b',
                'explanation': 'Employee awareness training is crucial for preventing social engineering attacks by educating staff about common tactics.',
                'question_set': 1
            }
        ]
    
    @staticmethod
    def get_question_set_2() -> List[Dict[str, Any]]:
        """Get question set 2 for Module 1"""
        return [
            {
                'question_text': 'What emotion do social engineers commonly exploit?',
                'option_a': 'Happiness and joy',
                'option_b': 'Fear, greed, and curiosity',
                'option_c': 'Sadness and depression',
                'option_d': 'Anger and frustration',
                'correct_answer': 'b',
                'explanation': 'Social engineers commonly exploit fear, greed, and curiosity to manipulate their targets.',
                'question_set': 2
            },
            {
                'question_text': 'Which group is typically NOT a primary target of social engineering?',
                'option_a': 'IT support staff',
                'option_b': 'Customer service representatives',
                'option_c': 'Security robots',
                'option_d': 'Executives and decision-makers',
                'correct_answer': 'c',
                'explanation': 'Security robots are not human and therefore cannot be manipulated through social engineering techniques.',
                'question_set': 2
            },
            {
                'question_text': 'What is the relationship between technical security and social engineering?',
                'option_a': 'Technical security prevents all social engineering attacks',
                'option_b': 'Social engineering can bypass even strong technical security',
                'option_c': 'They are completely unrelated',
                'option_d': 'Social engineering only works on weak technical security',
                'correct_answer': 'b',
                'explanation': 'Social engineering can bypass even the strongest technical security measures by manipulating human psychology.',
                'question_set': 2
            },
            {
                'question_text': 'Which of the following best describes the impact of social engineering on organizations?',
                'option_a': 'Only financial losses',
                'option_b': 'Only data breaches',
                'option_c': 'Multiple impacts including financial, reputational, and operational',
                'option_d': 'No significant impact',
                'correct_answer': 'c',
                'explanation': 'Social engineering can have multiple impacts including financial losses, data breaches, reputation damage, and operational disruption.',
                'question_set': 2
            },
            {
                'question_text': 'What is the first step in preventing social engineering attacks?',
                'option_a': 'Installing firewalls',
                'option_b': 'Employee awareness and training',
                'option_c': 'Changing passwords regularly',
                'option_d': 'Updating software',
                'correct_answer': 'b',
                'explanation': 'Employee awareness and training is the first and most important step in preventing social engineering attacks.',
                'question_set': 2
            }
        ]
    
    @staticmethod
    def get_question_set_3() -> List[Dict[str, Any]]:
        """Get question set 3 for Module 1"""
        return [
            {
                'question_text': 'What makes social engineering different from traditional hacking?',
                'option_a': 'It requires more technical skills',
                'option_b': 'It focuses on human psychology rather than technical vulnerabilities',
                'option_c': 'It only works on large organizations',
                'option_d': 'It requires expensive equipment',
                'correct_answer': 'b',
                'explanation': 'Social engineering focuses on human psychology and manipulation rather than exploiting technical vulnerabilities.',
                'question_set': 3
            },
            {
                'question_text': 'Which of the following is a key characteristic of social engineering attacks?',
                'option_a': 'They always involve malware',
                'option_b': 'They rely on building trust or creating urgency',
                'option_c': 'They require physical access to systems',
                'option_d': 'They only target high-level executives',
                'correct_answer': 'b',
                'explanation': 'Social engineering attacks rely on building false trust or creating urgency to manipulate targets.',
                'question_set': 3
            },
            {
                'question_text': 'What is the "weakest link" in most security systems?',
                'option_a': 'Firewall configuration',
                'option_b': 'Human psychology and behavior',
                'option_c': 'Password strength',
                'option_d': 'Network infrastructure',
                'correct_answer': 'b',
                'explanation': 'Human psychology and behavior is often considered the weakest link in security systems.',
                'question_set': 3
            },
            {
                'question_text': 'Which prevention strategy is most effective against social engineering?',
                'option_a': 'Using complex passwords',
                'option_b': 'Regular security awareness training',
                'option_c': 'Installing antivirus software',
                'option_d': 'Using VPN connections',
                'correct_answer': 'b',
                'explanation': 'Regular security awareness training is the most effective strategy for preventing social engineering attacks.',
                'question_set': 3
            },
            {
                'question_text': 'What should organizations do to protect against social engineering?',
                'option_a': 'Rely only on technical security measures',
                'option_b': 'Implement a combination of technical and human-focused security measures',
                'option_c': 'Ignore the threat as it only affects small companies',
                'option_d': 'Focus only on executive protection',
                'correct_answer': 'b',
                'explanation': 'Organizations should implement a combination of technical and human-focused security measures to protect against social engineering.',
                'question_set': 3
            }
        ]

