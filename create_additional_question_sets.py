import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, KnowledgeCheckQuestion

def create_additional_question_sets():
    """Create additional question sets for each module to enable randomization on retakes"""
    with app.app_context():
        print("🔄 Creating additional question sets for randomization...")
        
        # Define additional questions for each module (Set 2 and Set 3)
        additional_questions = {
            1: [  # Module 1: Introduction to Social Engineering
                {
                    'question_text': 'Which psychological principle is most commonly exploited by social engineers?',
                    'option_a': 'Authority and trust',
                    'option_b': 'Color psychology',
                    'option_c': 'Music preferences',
                    'option_d': 'Food choices',
                    'correct_answer': 'a',
                    'explanation': 'Social engineers frequently exploit authority and trust to manipulate targets into complying with their requests.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is the primary goal of social engineering attacks?',
                    'option_a': 'To improve computer performance',
                    'option_b': 'To gain unauthorized access to information or systems',
                    'option_c': 'To create better passwords',
                    'option_d': 'To install antivirus software',
                    'correct_answer': 'b',
                    'explanation': 'The primary goal is to gain unauthorized access to information, systems, or physical locations.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which of the following is NOT a common social engineering technique?',
                    'option_a': 'Phishing',
                    'option_b': 'Pretexting',
                    'option_c': 'Baiting',
                    'option_d': 'Computer programming',
                    'correct_answer': 'd',
                    'explanation': 'Computer programming is not a social engineering technique. The others are common social engineering methods.',
                    'question_set': 2
                },
                {
                    'question_text': 'Why do social engineers target human psychology?',
                    'option_a': 'Because humans are easier to manipulate than machines',
                    'option_b': 'Because computers are too expensive',
                    'option_c': 'Because humans are always online',
                    'option_d': 'Because humans have better passwords',
                    'correct_answer': 'a',
                    'explanation': 'Humans are often the weakest link in security systems and can be manipulated through psychological tactics.',
                    'question_set': 2
                },
                {
                    'question_text': 'What makes social engineering attacks particularly dangerous?',
                    'option_a': 'They require expensive equipment',
                    'option_b': 'They can bypass technical security measures by targeting human psychology',
                    'option_c': 'They only work on old computers',
                    'option_d': 'They are always detected by antivirus software',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering can bypass technical security measures by exploiting human psychology and behavior.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'Which human behavior is most exploited by social engineers?',
                    'option_a': 'The desire to help others',
                    'option_b': 'The love of music',
                    'option_c': 'The preference for certain colors',
                    'option_d': 'The choice of clothing',
                    'correct_answer': 'a',
                    'explanation': 'Social engineers often exploit people\'s natural desire to help others and be cooperative.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the relationship between social engineering and cybersecurity?',
                    'option_a': 'They are completely unrelated',
                    'option_b': 'Social engineering is a cybersecurity threat that targets human psychology',
                    'option_c': 'Social engineering only affects physical security',
                    'option_d': 'Social engineering only works on computers',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering is a significant cybersecurity threat that targets human psychology rather than technical vulnerabilities.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which of the following best describes social engineering?',
                    'option_a': 'A type of computer virus',
                    'option_b': 'The manipulation of people to gain unauthorized access',
                    'option_c': 'A form of encryption',
                    'option_d': 'A type of firewall',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering is the manipulation of people to gain unauthorized access to information or systems.',
                    'question_set': 3
                },
                {
                    'question_text': 'Why is social engineering considered a serious security threat?',
                    'option_a': 'Because it only affects small companies',
                    'option_b': 'Because it can bypass technical security measures',
                    'option_c': 'Because it only works on weekends',
                    'option_d': 'Because it requires expensive software',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering can bypass technical security measures by exploiting human psychology and behavior.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the main difference between social engineering and technical hacking?',
                    'option_a': 'Social engineering is faster',
                    'option_b': 'Social engineering targets human psychology while technical hacking targets systems',
                    'option_c': 'Technical hacking is more expensive',
                    'option_d': 'Social engineering only works on mobile devices',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering targets human psychology and behavior, while technical hacking targets system vulnerabilities.',
                    'question_set': 3
                }
            ],
            2: [  # Module 2: Common Social Engineering Techniques
                {
                    'question_text': 'What is the main characteristic of phishing attacks?',
                    'option_a': 'They always use email',
                    'option_b': 'They impersonate trusted entities to steal information',
                    'option_c': 'They only target large companies',
                    'option_d': 'They require physical access',
                    'correct_answer': 'b',
                    'explanation': 'Phishing attacks impersonate trusted entities to trick victims into revealing sensitive information.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which technique involves creating a fake scenario to obtain information?',
                    'option_a': 'Phishing',
                    'option_b': 'Pretexting',
                    'option_c': 'Baiting',
                    'option_d': 'Quid pro quo',
                    'correct_answer': 'b',
                    'explanation': 'Pretexting involves creating a fake scenario or pretext to obtain information from the target.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is quid pro quo in social engineering?',
                    'option_a': 'A type of virus',
                    'option_b': 'Offering something in exchange for information',
                    'option_c': 'A form of encryption',
                    'option_d': 'A type of firewall',
                    'correct_answer': 'b',
                    'explanation': 'Quid pro quo involves offering something in exchange for information or access.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which attack involves leaving physical devices to tempt victims?',
                    'option_a': 'Phishing',
                    'option_b': 'Pretexting',
                    'option_c': 'Baiting',
                    'option_d': 'Tailgating',
                    'correct_answer': 'c',
                    'explanation': 'Baiting involves leaving physical devices like USB drives to tempt victims into using them.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is tailgating in social engineering?',
                    'option_a': 'Following someone through a secure door',
                    'option_b': 'Sending spam emails',
                    'option_c': 'Creating fake websites',
                    'option_d': 'Installing malware',
                    'correct_answer': 'a',
                    'explanation': 'Tailgating involves following someone through a secure door without proper authorization.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'Which social engineering technique is most commonly used in emails?',
                    'option_a': 'Baiting',
                    'option_b': 'Phishing',
                    'option_c': 'Tailgating',
                    'option_d': 'Pretexting',
                    'correct_answer': 'b',
                    'explanation': 'Phishing is the most common social engineering technique used in emails.',
                    'question_set': 3
                },
                {
                    'question_text': 'What makes pretexting effective?',
                    'option_a': 'It uses expensive equipment',
                    'option_b': 'It creates believable scenarios that seem legitimate',
                    'option_c': 'It only works on weekends',
                    'option_d': 'It requires technical skills',
                    'correct_answer': 'b',
                    'explanation': 'Pretexting is effective because it creates believable scenarios that seem legitimate to the target.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which technique exploits human curiosity?',
                    'option_a': 'Phishing',
                    'option_b': 'Baiting',
                    'option_c': 'Pretexting',
                    'option_d': 'Quid pro quo',
                    'correct_answer': 'b',
                    'explanation': 'Baiting exploits human curiosity by leaving tempting physical devices for victims to use.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the primary goal of social engineering techniques?',
                    'option_a': 'To improve computer performance',
                    'option_b': 'To gain unauthorized access or information',
                    'option_c': 'To create better passwords',
                    'option_d': 'To install security software',
                    'correct_answer': 'b',
                    'explanation': 'The primary goal of all social engineering techniques is to gain unauthorized access or information.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which technique involves offering help in exchange for access?',
                    'option_a': 'Phishing',
                    'option_b': 'Pretexting',
                    'option_c': 'Baiting',
                    'option_d': 'Quid pro quo',
                    'correct_answer': 'd',
                    'explanation': 'Quid pro quo involves offering help or services in exchange for access or information.',
                    'question_set': 3
                }
            ],
            3: [  # Module 3: Psychological Principles
                {
                    'question_text': 'Which psychological principle involves people following authority figures?',
                    'option_a': 'Reciprocity',
                    'option_b': 'Authority',
                    'option_c': 'Social proof',
                    'option_d': 'Scarcity',
                    'correct_answer': 'b',
                    'explanation': 'The authority principle involves people following instructions from authority figures.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is the principle of reciprocity?',
                    'option_a': 'People feel obligated to return favors',
                    'option_b': 'People follow authority figures',
                    'option_c': 'People want what is scarce',
                    'option_d': 'People follow the crowd',
                    'correct_answer': 'a',
                    'explanation': 'Reciprocity is the principle that people feel obligated to return favors when someone does something for them.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which principle involves people wanting what is limited?',
                    'option_a': 'Authority',
                    'option_b': 'Reciprocity',
                    'option_c': 'Scarcity',
                    'option_d': 'Social proof',
                    'correct_answer': 'c',
                    'explanation': 'The scarcity principle involves people wanting things that are limited in availability.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is social proof in psychology?',
                    'option_a': 'People following authority figures',
                    'option_b': 'People following the behavior of others',
                    'option_c': 'People wanting scarce items',
                    'option_d': 'People returning favors',
                    'correct_answer': 'b',
                    'explanation': 'Social proof is the principle that people follow the behavior of others in uncertain situations.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which principle is exploited when attackers create urgency?',
                    'option_a': 'Authority',
                    'option_b': 'Reciprocity',
                    'option_c': 'Scarcity',
                    'option_d': 'Social proof',
                    'correct_answer': 'c',
                    'explanation': 'Scarcity is exploited when attackers create urgency or limited-time offers.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'How do social engineers exploit the authority principle?',
                    'option_a': 'By pretending to be authority figures',
                    'option_b': 'By offering free gifts',
                    'option_c': 'By creating urgency',
                    'option_d': 'By showing testimonials',
                    'correct_answer': 'a',
                    'explanation': 'Social engineers exploit authority by pretending to be authority figures like IT staff or managers.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which principle involves people following the crowd?',
                    'option_a': 'Authority',
                    'option_b': 'Reciprocity',
                    'option_c': 'Social proof',
                    'option_d': 'Scarcity',
                    'correct_answer': 'c',
                    'explanation': 'Social proof involves people following the behavior of others or the crowd.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the commitment and consistency principle?',
                    'option_a': 'People want to appear consistent with their previous actions',
                    'option_b': 'People follow authority figures',
                    'option_c': 'People return favors',
                    'option_d': 'People want scarce items',
                    'correct_answer': 'a',
                    'explanation': 'The commitment and consistency principle states that people want to appear consistent with their previous actions.',
                    'question_set': 3
                },
                {
                    'question_text': 'How do attackers use the liking principle?',
                    'option_a': 'By pretending to be similar to the target',
                    'option_b': 'By creating urgency',
                    'option_c': 'By offering free gifts',
                    'option_d': 'By showing authority',
                    'correct_answer': 'a',
                    'explanation': 'Attackers use the liking principle by pretending to be similar to the target or finding common ground.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which principle involves people wanting to appear consistent?',
                    'option_a': 'Authority',
                    'option_b': 'Reciprocity',
                    'option_c': 'Commitment and consistency',
                    'option_d': 'Scarcity',
                    'correct_answer': 'c',
                    'explanation': 'The commitment and consistency principle involves people wanting to appear consistent with their previous actions.',
                    'question_set': 3
                }
            ],
            4: [  # Module 4: Real-World Examples
                {
                    'question_text': 'What was the main goal of the Target data breach?',
                    'option_a': 'To improve store security',
                    'option_b': 'To steal customer payment data',
                    'option_c': 'To test the security system',
                    'option_d': 'To update the POS system',
                    'correct_answer': 'b',
                    'explanation': 'The main goal was to steal customer payment data through social engineering.',
                    'question_set': 2
                },
                {
                    'question_text': 'How did the Target attackers gain initial access?',
                    'option_a': 'Through a direct attack on Target systems',
                    'option_b': 'Through a phishing attack on a vendor',
                    'option_c': 'Through physical break-in',
                    'option_d': 'Through a virus',
                    'correct_answer': 'b',
                    'explanation': 'Attackers gained access through a phishing attack on a Target vendor.',
                    'question_set': 2
                },
                {
                    'question_text': 'What type of social engineering was used in the Target breach?',
                    'option_a': 'Baiting',
                    'option_b': 'Phishing',
                    'option_c': 'Tailgating',
                    'option_d': 'Pretexting',
                    'correct_answer': 'b',
                    'explanation': 'Phishing was the primary social engineering technique used in the Target breach.',
                    'question_set': 2
                },
                {
                    'question_text': 'Why was the Target breach particularly significant?',
                    'option_a': 'It affected only a few customers',
                    'option_b': 'It affected millions of customers and cost millions of dollars',
                    'option_c': 'It only affected online sales',
                    'option_d': 'It was quickly resolved',
                    'correct_answer': 'b',
                    'explanation': 'The Target breach was significant because it affected millions of customers and cost millions of dollars.',
                    'question_set': 2
                },
                {
                    'question_text': 'What lesson can be learned from the Target breach?',
                    'option_a': 'Technical security is always sufficient',
                    'option_b': 'Social engineering can bypass technical security measures',
                    'option_c': 'Only large companies are targeted',
                    'option_d': 'Physical security is not important',
                    'correct_answer': 'b',
                    'explanation': 'The Target breach demonstrates that social engineering can bypass technical security measures.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'Which company was targeted in the 2013 data breach?',
                    'option_a': 'Walmart',
                    'option_b': 'Target',
                    'option_c': 'Amazon',
                    'option_d': 'Best Buy',
                    'correct_answer': 'b',
                    'explanation': 'Target was the company targeted in the 2013 data breach.',
                    'question_set': 3
                },
                {
                    'question_text': 'How many customers were affected by the Target breach?',
                    'option_a': 'Thousands',
                    'option_b': 'Millions',
                    'option_c': 'Hundreds',
                    'option_d': 'Tens of thousands',
                    'correct_answer': 'b',
                    'explanation': 'Millions of customers were affected by the Target data breach.',
                    'question_set': 3
                },
                {
                    'question_text': 'What was the financial impact of the Target breach?',
                    'option_a': 'Minimal cost',
                    'option_b': 'Millions of dollars in costs',
                    'option_c': 'No financial impact',
                    'option_d': 'Only affected online sales',
                    'correct_answer': 'b',
                    'explanation': 'The Target breach cost millions of dollars in damages and recovery costs.',
                    'question_set': 3
                },
                {
                    'question_text': 'What type of data was stolen in the Target breach?',
                    'option_a': 'Only email addresses',
                    'option_b': 'Customer payment data',
                    'option_c': 'Only passwords',
                    'option_d': 'Only names',
                    'correct_answer': 'b',
                    'explanation': 'Customer payment data was stolen in the Target breach.',
                    'question_set': 3
                },
                {
                    'question_text': 'What security lesson does the Target breach teach?',
                    'option_a': 'Only technical security matters',
                    'option_b': 'Social engineering can bypass technical defenses',
                    'option_c': 'Only small companies are at risk',
                    'option_d': 'Physical security is sufficient',
                    'correct_answer': 'b',
                    'explanation': 'The Target breach teaches that social engineering can bypass technical security defenses.',
                    'question_set': 3
                }
            ],
            5: [  # Module 5: Prevention Strategies
                {
                    'question_text': 'What is the first step in preventing social engineering attacks?',
                    'option_a': 'Installing antivirus software',
                    'option_b': 'Being aware and educated about social engineering',
                    'option_c': 'Changing passwords monthly',
                    'option_d': 'Using complex passwords',
                    'correct_answer': 'b',
                    'explanation': 'Being aware and educated about social engineering is the first step in prevention.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which verification method is most effective against social engineering?',
                    'option_a': 'Trusting the caller ID',
                    'option_b': 'Verifying requests through independent channels',
                    'option_c': 'Following email links',
                    'option_d': 'Sharing information with colleagues',
                    'correct_answer': 'b',
                    'explanation': 'Verifying requests through independent channels is most effective against social engineering.',
                    'question_set': 2
                },
                {
                    'question_text': 'What should you do with suspicious emails?',
                    'option_a': 'Reply immediately',
                    'option_b': 'Delete them without opening',
                    'option_c': 'Forward to all colleagues',
                    'option_d': 'Click on all links',
                    'correct_answer': 'b',
                    'explanation': 'Suspicious emails should be deleted without opening to prevent social engineering attacks.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which is NOT a good security practice?',
                    'option_a': 'Verifying requests independently',
                    'option_b': 'Sharing passwords with trusted colleagues',
                    'option_c': 'Being suspicious of urgent requests',
                    'option_d': 'Reporting suspicious activity',
                    'correct_answer': 'b',
                    'explanation': 'Sharing passwords with colleagues is NOT a good security practice.',
                    'question_set': 2
                },
                {
                    'question_text': 'What should you do with unexpected USB drives?',
                    'option_a': 'Use them immediately',
                    'option_b': 'Turn them in to IT or security',
                    'option_c': 'Give them to colleagues',
                    'option_d': 'Take them home',
                    'correct_answer': 'b',
                    'explanation': 'Unexpected USB drives should be turned in to IT or security personnel.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'How can you verify a suspicious request?',
                    'option_a': 'By calling the number provided in the email',
                    'option_b': 'By contacting the organization through their official website',
                    'option_c': 'By asking colleagues for their opinion',
                    'option_d': 'By responding to the email',
                    'correct_answer': 'b',
                    'explanation': 'Contact the organization through their official website to verify suspicious requests.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the best response to urgent requests for information?',
                    'option_a': 'Comply immediately',
                    'option_b': 'Be suspicious and verify independently',
                    'option_c': 'Ask colleagues for advice',
                    'option_d': 'Ignore all urgent requests',
                    'correct_answer': 'b',
                    'explanation': 'Be suspicious of urgent requests and verify them independently.',
                    'question_set': 3
                },
                {
                    'question_text': 'Which is a red flag for social engineering?',
                    'option_a': 'Requests for sensitive information',
                    'option_b': 'Urgent or threatening language',
                    'option_c': 'Both a and b',
                    'option_d': 'Professional email formatting',
                    'correct_answer': 'c',
                    'explanation': 'Both requests for sensitive information and urgent/threatening language are red flags.',
                    'question_set': 3
                },
                {
                    'question_text': 'What should you do if you suspect social engineering?',
                    'option_a': 'Handle it yourself',
                    'option_b': 'Report it to IT or security',
                    'option_c': 'Ignore it',
                    'option_d': 'Share with colleagues',
                    'correct_answer': 'b',
                    'explanation': 'Suspected social engineering should be reported to IT or security personnel.',
                    'question_set': 3
                },
                {
                    'question_text': 'Why is education important in preventing social engineering?',
                    'option_a': 'It makes computers faster',
                    'option_b': 'It helps people recognize and resist attacks',
                    'option_c': 'It reduces internet costs',
                    'option_d': 'It improves password strength',
                    'correct_answer': 'b',
                    'explanation': 'Education helps people recognize and resist social engineering attacks.',
                    'question_set': 3
                }
            ],
            6: [  # Module 6: Organizational Security
                {
                    'question_text': 'What is the purpose of security policies in organizations?',
                    'option_a': 'To make work more difficult',
                    'option_b': 'To provide clear guidelines for security practices',
                    'option_c': 'To increase costs',
                    'option_d': 'To reduce employee freedom',
                    'correct_answer': 'b',
                    'explanation': 'Security policies provide clear guidelines for security practices in organizations.',
                    'question_set': 2
                },
                {
                    'question_text': 'Why is employee training important for security?',
                    'option_a': 'It reduces IT costs',
                    'option_b': 'Employees are often the first line of defense',
                    'option_c': 'It improves computer performance',
                    'option_d': 'It makes work easier',
                    'correct_answer': 'b',
                    'explanation': 'Employees are often the first line of defense against social engineering attacks.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is the principle of least privilege?',
                    'option_a': 'Giving everyone maximum access',
                    'option_b': 'Giving users only the access they need',
                    'option_c': 'Sharing all passwords',
                    'option_d': 'Allowing unlimited access',
                    'correct_answer': 'b',
                    'explanation': 'The principle of least privilege means giving users only the access they need to perform their jobs.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which is NOT a good security practice for organizations?',
                    'option_a': 'Regular security training',
                    'option_b': 'Sharing passwords among employees',
                    'option_c': 'Incident response plans',
                    'option_d': 'Access control policies',
                    'correct_answer': 'b',
                    'explanation': 'Sharing passwords among employees is NOT a good security practice.',
                    'question_set': 2
                },
                {
                    'question_text': 'What should organizations do after a security incident?',
                    'option_a': 'Ignore it',
                    'option_b': 'Conduct a post-incident review',
                    'option_c': 'Blame employees',
                    'option_d': 'Hide the incident',
                    'correct_answer': 'b',
                    'explanation': 'Organizations should conduct a post-incident review to learn from security incidents.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'How often should security training be conducted?',
                    'option_a': 'Once every 5 years',
                    'option_b': 'Regularly and continuously',
                    'option_c': 'Only when incidents occur',
                    'option_d': 'Never',
                    'correct_answer': 'b',
                    'explanation': 'Security training should be conducted regularly and continuously.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the purpose of incident response plans?',
                    'option_a': 'To increase costs',
                    'option_b': 'To provide a structured approach to handling security incidents',
                    'option_c': 'To blame employees',
                    'option_d': 'To hide incidents',
                    'correct_answer': 'b',
                    'explanation': 'Incident response plans provide a structured approach to handling security incidents.',
                    'question_set': 3
                },
                {
                    'question_text': 'Why is access control important?',
                    'option_a': 'It makes work more difficult',
                    'option_b': 'It limits the damage from security breaches',
                    'option_c': 'It increases costs',
                    'option_d': 'It reduces employee freedom',
                    'correct_answer': 'b',
                    'explanation': 'Access control limits the damage from security breaches by restricting access.',
                    'question_set': 3
                },
                {
                    'question_text': 'What should be included in security policies?',
                    'option_a': 'Only technical procedures',
                    'option_b': 'Clear guidelines for all security practices',
                    'option_c': 'Only password requirements',
                    'option_d': 'Only email policies',
                    'correct_answer': 'b',
                    'explanation': 'Security policies should include clear guidelines for all security practices.',
                    'question_set': 3
                },
                {
                    'question_text': 'How can organizations improve security awareness?',
                    'option_a': 'By reducing training',
                    'option_b': 'By providing regular education and reminders',
                    'option_c': 'By hiding security incidents',
                    'option_d': 'By ignoring threats',
                    'correct_answer': 'b',
                    'explanation': 'Organizations can improve security awareness by providing regular education and reminders.',
                    'question_set': 3
                }
            ],
            7: [  # Module 7: Incident Response
                {
                    'question_text': 'What is the first step in incident response?',
                    'option_a': 'Blame employees',
                    'option_b': 'Identify and contain the incident',
                    'option_c': 'Hide the incident',
                    'option_d': 'Ignore the incident',
                    'correct_answer': 'b',
                    'explanation': 'The first step in incident response is to identify and contain the incident.',
                    'question_set': 2
                },
                {
                    'question_text': 'Why is documentation important in incident response?',
                    'option_a': 'To blame employees',
                    'option_b': 'To learn from the incident and improve security',
                    'option_c': 'To increase costs',
                    'option_d': 'To hide mistakes',
                    'correct_answer': 'b',
                    'explanation': 'Documentation helps learn from incidents and improve security measures.',
                    'question_set': 2
                },
                {
                    'question_text': 'What should you do if you suspect a social engineering attack?',
                    'option_a': 'Handle it yourself',
                    'option_b': 'Report it immediately to IT or security',
                    'option_c': 'Ignore it',
                    'option_d': 'Share with colleagues',
                    'correct_answer': 'b',
                    'explanation': 'Suspected social engineering attacks should be reported immediately to IT or security.',
                    'question_set': 2
                },
                {
                    'question_text': 'Which is NOT part of incident response?',
                    'option_a': 'Identification',
                    'option_b': 'Containment',
                    'option_c': 'Ignoring the incident',
                    'option_d': 'Recovery',
                    'correct_answer': 'c',
                    'explanation': 'Ignoring the incident is NOT part of proper incident response.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is the purpose of post-incident reviews?',
                    'option_a': 'To blame employees',
                    'option_b': 'To learn and improve security measures',
                    'option_c': 'To hide incidents',
                    'option_d': 'To increase costs',
                    'correct_answer': 'b',
                    'explanation': 'Post-incident reviews help learn from incidents and improve security measures.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'What is containment in incident response?',
                    'option_a': 'Ignoring the incident',
                    'option_b': 'Limiting the spread of the incident',
                    'option_c': 'Blaming employees',
                    'option_d': 'Hiding the incident',
                    'correct_answer': 'b',
                    'explanation': 'Containment involves limiting the spread of the security incident.',
                    'question_set': 3
                },
                {
                    'question_text': 'Why is quick response important in security incidents?',
                    'option_a': 'To increase costs',
                    'option_b': 'To minimize damage and prevent further spread',
                    'option_c': 'To blame employees',
                    'option_d': 'To hide the incident',
                    'correct_answer': 'b',
                    'explanation': 'Quick response minimizes damage and prevents further spread of security incidents.',
                    'question_set': 3
                },
                {
                    'question_text': 'What should be included in incident documentation?',
                    'option_a': 'Only technical details',
                    'option_b': 'All relevant details about the incident',
                    'option_c': 'Only employee names',
                    'option_d': 'Only costs',
                    'correct_answer': 'b',
                    'explanation': 'Incident documentation should include all relevant details about the incident.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is the recovery phase of incident response?',
                    'option_a': 'Ignoring the incident',
                    'option_b': 'Restoring normal operations',
                    'option_c': 'Blaming employees',
                    'option_d': 'Hiding the incident',
                    'correct_answer': 'b',
                    'explanation': 'The recovery phase involves restoring normal operations after an incident.',
                    'question_set': 3
                },
                {
                    'question_text': 'How can organizations improve incident response?',
                    'option_a': 'By ignoring incidents',
                    'option_b': 'By learning from past incidents and updating procedures',
                    'option_c': 'By blaming employees',
                    'option_d': 'By hiding incidents',
                    'correct_answer': 'b',
                    'explanation': 'Organizations can improve incident response by learning from past incidents and updating procedures.',
                    'question_set': 3
                }
            ],
            8: [  # Module 8: Future Trends
                {
                    'question_text': 'How is AI being used in social engineering?',
                    'option_a': 'To prevent attacks only',
                    'option_b': 'Both to create more sophisticated attacks and to defend against them',
                    'option_c': 'To improve computer performance',
                    'option_d': 'To reduce costs',
                    'correct_answer': 'b',
                    'explanation': 'AI is being used both to create more sophisticated attacks and to defend against them.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is deepfake technology?',
                    'option_a': 'A type of antivirus software',
                    'option_b': 'AI-generated fake audio and video content',
                    'option_c': 'A type of firewall',
                    'option_d': 'A security protocol',
                    'correct_answer': 'b',
                    'explanation': 'Deepfake technology creates AI-generated fake audio and video content.',
                    'question_set': 2
                },
                {
                    'question_text': 'Why are deepfakes a security concern?',
                    'option_a': 'They only affect entertainment',
                    'option_b': 'They can be used to impersonate trusted individuals',
                    'option_c': 'They improve security',
                    'option_d': 'They reduce costs',
                    'correct_answer': 'b',
                    'explanation': 'Deepfakes can be used to impersonate trusted individuals in social engineering attacks.',
                    'question_set': 2
                },
                {
                    'question_text': 'What is the future of social engineering?',
                    'option_a': 'It will disappear',
                    'option_b': 'It will become more sophisticated with new technologies',
                    'option_c': 'It will only affect large companies',
                    'option_d': 'It will become easier to prevent',
                    'correct_answer': 'b',
                    'explanation': 'Social engineering will become more sophisticated with new technologies like AI and deepfakes.',
                    'question_set': 2
                },
                {
                    'question_text': 'How can organizations prepare for future threats?',
                    'option_a': 'By ignoring new technologies',
                    'option_b': 'By staying informed and adapting security measures',
                    'option_c': 'By reducing security training',
                    'option_d': 'By hiding incidents',
                    'correct_answer': 'b',
                    'explanation': 'Organizations can prepare by staying informed and adapting security measures.',
                    'question_set': 2
                },
                # Set 3 questions
                {
                    'question_text': 'What technology is making social engineering more sophisticated?',
                    'option_a': 'Antivirus software',
                    'option_b': 'Artificial Intelligence',
                    'option_c': 'Firewalls',
                    'option_d': 'Password managers',
                    'correct_answer': 'b',
                    'explanation': 'Artificial Intelligence is making social engineering attacks more sophisticated.',
                    'question_set': 3
                },
                {
                    'question_text': 'What is a potential future threat from AI?',
                    'option_a': 'Improved security',
                    'option_b': 'More convincing social engineering attacks',
                    'option_c': 'Reduced costs',
                    'option_d': 'Better passwords',
                    'correct_answer': 'b',
                    'explanation': 'AI could enable more convincing social engineering attacks in the future.',
                    'question_set': 3
                },
                {
                    'question_text': 'How can deepfakes be used in social engineering?',
                    'option_a': 'To improve security',
                    'option_b': 'To impersonate trusted individuals',
                    'option_c': 'To reduce costs',
                    'option_d': 'To create better passwords',
                    'correct_answer': 'b',
                    'explanation': 'Deepfakes can be used to impersonate trusted individuals in social engineering attacks.',
                    'question_set': 3
                },
                {
                    'question_text': 'What should organizations do about future threats?',
                    'option_a': 'Ignore them',
                    'option_b': 'Stay informed and adapt security measures',
                    'option_c': 'Reduce security training',
                    'option_d': 'Hide incidents',
                    'correct_answer': 'b',
                    'explanation': 'Organizations should stay informed and adapt security measures for future threats.',
                    'question_set': 3
                },
                {
                    'question_text': 'Why is continuous learning important for security?',
                    'option_a': 'To increase costs',
                    'option_b': 'To keep up with evolving threats',
                    'option_c': 'To reduce training',
                    'option_d': 'To hide incidents',
                    'correct_answer': 'b',
                    'explanation': 'Continuous learning is important to keep up with evolving security threats.',
                    'question_set': 3
                }
            ]
        }
        
        # Create additional question sets for each module
        for module_id, questions in additional_questions.items():
            print(f"📝 Creating additional question sets for Module {module_id}...")
            
            for question_data in questions:
                # Check if this question already exists
                existing = KnowledgeCheckQuestion.query.filter_by(
                    module_id=module_id,
                    question_text=question_data['question_text'],
                    question_set=question_data['question_set']
                ).first()
                
                if not existing:
                    new_question = KnowledgeCheckQuestion(
                        module_id=module_id,
                        question_text=question_data['question_text'],
                        option_a=question_data['option_a'],
                        option_b=question_data['option_b'],
                        option_c=question_data['option_c'],
                        option_d=question_data['option_d'],
                        correct_answer=question_data['correct_answer'],
                        explanation=question_data['explanation'],
                        question_set=question_data['question_set']
                    )
                    db.session.add(new_question)
                    print(f"  ✅ Added question set {question_data['question_set']} for Module {module_id}")
                else:
                    print(f"  ⚠️  Question set {question_data['question_set']} already exists for Module {module_id}")
        
        db.session.commit()
        print("🎉 Additional question sets created successfully!")
        print("📊 Each module now has 3 sets of questions for proper randomization")

if __name__ == "__main__":
    create_additional_question_sets() 