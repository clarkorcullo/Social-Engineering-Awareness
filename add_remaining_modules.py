#!/usr/bin/env python3
"""
Script to add remaining modules (3-8) with comprehensive content
"""

from app import app, db, Module, KnowledgeCheckQuestion

def add_remaining_modules():
    """Add modules 3-8 with comprehensive content"""
    
    modules_data = [
        {
            'name': 'Phishing Attacks',
            'description': 'Understanding and identifying phishing attempts',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-fish"></i> Phishing Attacks</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Key Learning Objectives</h5>
                    <ul>
                        <li>Identify different types of phishing attacks</li>
                        <li>Recognize red flags in suspicious emails</li>
                        <li>Understand spear phishing and whaling</li>
                        <li>Learn defense strategies against phishing</li>
                    </ul>
                </div>

                <h4><i class="fas fa-envelope"></i> What is Phishing?</h4>
                <p>Phishing is a type of social engineering attack where attackers impersonate legitimate organizations to steal sensitive information like passwords, credit card numbers, and personal data.</p>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-primary text-white">
                                <i class="fas fa-exclamation-triangle"></i> Common Red Flags
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>Urgent requests for action</li>
                                    <li>Poor grammar or spelling</li>
                                    <li>Suspicious sender addresses</li>
                                    <li>Requests for sensitive information</li>
                                    <li>Unusual links or attachments</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-warning text-dark">
                                <i class="fas fa-shield-alt"></i> Defense Strategies
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>Verify sender addresses carefully</li>
                                    <li>Hover over links before clicking</li>
                                    <li>Never share passwords via email</li>
                                    <li>Report suspicious emails to IT</li>
                                    <li>Use multi-factor authentication</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <h4><i class="fas fa-user-tie"></i> Types of Phishing</h4>
                
                <div class="card mb-3">
                    <div class="card-header bg-info text-white">
                        <i class="fas fa-bullseye"></i> Spear Phishing
                    </div>
                    <div class="card-body">
                        <p><strong>Definition:</strong> Targeted attacks against specific individuals using personalized information.</p>
                        <p><strong>Characteristics:</strong> Uses personal details, appears more legitimate, higher success rate.</p>
                    </div>
                </div>

                <div class="card mb-3">
                    <div class="card-header bg-warning text-dark">
                        <i class="fas fa-crown"></i> Whaling
                    </div>
                    <div class="card-body">
                        <p><strong>Definition:</strong> Phishing attacks targeting high-level executives and decision-makers.</p>
                        <p><strong>Characteristics:</strong> Sophisticated, uses executive authority, targets sensitive business information.</p>
                    </div>
                </div>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Module Summary</h5>
                    <p>You now understand phishing attacks and how to identify and defend against them. In the next module, you'll learn about pretexting and impersonation techniques.</p>
                </div>
            </div>
            ''',
            'order': 3,
            'has_simulation': True,
            'simulation_type': 'phishing'
        },
        {
            'name': 'Pretexting and Impersonation',
            'description': 'Learning about pretexting techniques and impersonation',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-mask"></i> Pretexting and Impersonation</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Key Learning Objectives</h5>
                    <ul>
                        <li>Understand pretexting techniques</li>
                        <li>Recognize impersonation attempts</li>
                        <li>Learn verification procedures</li>
                        <li>Develop defense strategies</li>
                    </ul>
                </div>

                <h4><i class="fas fa-theater-masks"></i> What is Pretexting?</h4>
                <p>Pretexting involves creating fabricated scenarios or pretexts to obtain sensitive information. Attackers build trust by impersonating legitimate authority figures or creating believable situations.</p>

                <div class="card bg-light">
                    <div class="card-body">
                        <h5><i class="fas fa-example"></i> Common Pretexting Scenarios</h5>
                        <ul>
                            <li><strong>IT Support:</strong> "I need to verify your account for security purposes"</li>
                            <li><strong>Bank Representative:</strong> "We've detected suspicious activity on your account"</li>
                            <li><strong>Government Official:</strong> "This is an official investigation requiring your cooperation"</li>
                            <li><strong>Colleague:</strong> "I'm working on a project and need your password to access shared files"</li>
                        </ul>
                    </div>
                </div>

                <h4><i class="fas fa-phone"></i> Caller ID Spoofing</h4>
                <p>Attackers can fake caller ID information to appear as legitimate organizations. This makes it harder to identify fraudulent calls.</p>

                <div class="alert alert-warning">
                    <h5><i class="fas fa-exclamation-triangle"></i> Verification Procedures</h5>
                    <ul>
                        <li>Always hang up and call back using a known number</li>
                        <li>Never trust caller ID information</li>
                        <li>Verify identity through official channels</li>
                        <li>Ask for official identification</li>
                    </ul>
                </div>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Module Summary</h5>
                    <p>You now understand pretexting and impersonation techniques. In the next module, you'll learn about baiting and quid pro quo attacks.</p>
                </div>
            </div>
            ''',
            'order': 4,
            'has_simulation': True,
            'simulation_type': 'pretexting'
        },
        {
            'name': 'Baiting and Quid Pro Quo',
            'description': 'Understanding baiting and quid pro quo attacks',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-bait"></i> Baiting and Quid Pro Quo</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Key Learning Objectives</h5>
                    <ul>
                        <li>Understand baiting techniques</li>
                        <li>Recognize quid pro quo scenarios</li>
                        <li>Learn physical security awareness</li>
                        <li>Develop defense strategies</li>
                    </ul>
                </div>

                <h4><i class="fas fa-usb"></i> Physical Baiting</h4>
                <p>Baiting uses physical media or digital lures to entice victims into taking harmful actions. Attackers leave malicious devices in public places hoping someone will use them.</p>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-danger text-white">
                                <i class="fas fa-exclamation-triangle"></i> Common Baiting Items
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>USB drives left in public places</li>
                                    <li>CDs or DVDs with "confidential" labels</li>
                                    <li>Fake company badges or IDs</li>
                                    <li>Malicious QR codes</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-success text-white">
                                <i class="fas fa-shield-alt"></i> Defense Strategies
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>Never plug unknown USB devices</li>
                                    <li>Scan all media before use</li>
                                    <li>Use virtual machines for testing</li>
                                    <li>Report suspicious items to security</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <h4><i class="fas fa-handshake"></i> Quid Pro Quo</h4>
                <p>Quid pro quo involves offering a service or benefit in exchange for sensitive information or access. Attackers exploit the human tendency to reciprocate favors.</p>

                <div class="alert alert-warning">
                    <h5><i class="fas fa-exclamation-triangle"></i> Common Quid Pro Quo Scenarios</h5>
                    <ul>
                        <li><strong>Tech Support:</strong> "I'll help you fix your computer if you give me your password"</li>
                        <li><strong>Free Services:</strong> "Get free antivirus software by completing this survey"</li>
                        <li><strong>Job Offers:</strong> "We'll hire you if you provide your social security number"</li>
                        <li><strong>Prizes:</strong> "You've won! Just provide your bank details to claim your prize"</li>
                    </ul>
                </div>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Module Summary</h5>
                    <p>You now understand baiting and quid pro quo attacks. In the next module, you'll learn about advanced social engineering techniques.</p>
                </div>
            </div>
            ''',
            'order': 5,
            'has_simulation': True,
            'simulation_type': 'baiting'
        },
        {
            'name': 'Advanced Techniques',
            'description': 'Advanced social engineering methods and countermeasures',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-chess"></i> Advanced Techniques</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Key Learning Objectives</h5>
                    <ul>
                        <li>Understand advanced social engineering techniques</li>
                        <li>Learn about deepfake and AI-based attacks</li>
                        <li>Recognize sophisticated manipulation methods</li>
                        <li>Develop advanced defense strategies</li>
                    </ul>
                </div>

                <h4><i class="fas fa-robot"></i> AI-Powered Attacks</h4>
                <p>Modern attackers use artificial intelligence and machine learning to create more convincing and targeted social engineering attacks.</p>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-primary text-white">
                                <i class="fas fa-microphone"></i> Deepfake Voice
                            </div>
                            <div class="card-body">
                                <p>Attackers can clone voices using AI to impersonate executives and authority figures in phone calls.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-warning text-dark">
                                <i class="fas fa-video"></i> Deepfake Video
                            </div>
                            <div class="card-body">
                                <p>AI-generated videos can impersonate real people for sophisticated social engineering attacks.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <h4><i class="fas fa-network-wired"></i> Social Media Intelligence</h4>
                <p>Attackers gather extensive information from social media profiles to create highly personalized and convincing attacks.</p>

                <div class="alert alert-warning">
                    <h5><i class="fas fa-exclamation-triangle"></i> Information Gathering Techniques</h5>
                    <ul>
                        <li>Analyzing public social media posts</li>
                        <li>Mapping personal and professional relationships</li>
                        <li>Identifying personal interests and vulnerabilities</li>
                        <li>Tracking location and activity patterns</li>
                    </ul>
                </div>

                <h4><i class="fas fa-tint"></i> Watering Hole Attacks</h4>
                <p>Attackers compromise websites that are frequently visited by their target audience, infecting visitors with malware.</p>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Module Summary</h5>
                    <p>You now understand advanced social engineering techniques. In the next module, you'll learn about incident response procedures.</p>
                </div>
            </div>
            ''',
            'order': 6,
            'has_simulation': True,
            'simulation_type': 'advanced'
        },
        {
            'name': 'Incident Response',
            'description': 'How to respond to social engineering incidents',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-ambulance"></i> Incident Response</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Key Learning Objectives</h5>
                    <ul>
                        <li>Learn proper incident response procedures</li>
                        <li>Understand documentation requirements</li>
                        <li>Know when and how to report incidents</li>
                        <li>Develop recovery strategies</li>
                    </ul>
                </div>

                <h4><i class="fas fa-stop-circle"></i> Immediate Response</h4>
                <p>When you suspect a social engineering attack, your first priority is to stop providing any information and disengage safely.</p>

                <div class="card bg-light">
                    <div class="card-body">
                        <h5><i class="fas fa-list-ol"></i> Response Steps</h5>
                        <ol>
                            <li><strong>Stop:</strong> Don't provide any more information</li>
                            <li><strong>Disconnect:</strong> End the communication safely</li>
                            <li><strong>Document:</strong> Record all details immediately</li>
                            <li><strong>Report:</strong> Contact security or IT immediately</li>
                            <li><strong>Secure:</strong> Change passwords and enable 2FA</li>
                        </ol>
                    </div>
                </div>

                <h4><i class="fas fa-clipboard-list"></i> Documentation</h4>
                <p>Proper documentation is crucial for incident response and prevention of future attacks.</p>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-primary text-white">
                                <i class="fas fa-info-circle"></i> What to Document
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>Date and time of incident</li>
                                    <li>Method of contact (phone, email, etc.)</li>
                                    <li>Information requested</li>
                                    <li>Attacker's claimed identity</li>
                                    <li>Any information provided</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-warning text-dark">
                                <i class="fas fa-shield-alt"></i> Evidence Preservation
                            </div>
                            <div class="card-body">
                                <ul>
                                    <li>Save suspicious emails</li>
                                    <li>Take screenshots of fake websites</li>
                                    <li>Record phone call details</li>
                                    <li>Preserve any physical evidence</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <h4><i class="fas fa-undo"></i> Recovery Procedures</h4>
                <p>After a social engineering incident, take immediate steps to secure your accounts and prevent further damage.</p>

                <div class="alert alert-warning">
                    <h5><i class="fas fa-exclamation-triangle"></i> Recovery Steps</h5>
                    <ul>
                        <li>Change all passwords immediately</li>
                        <li>Enable two-factor authentication</li>
                        <li>Monitor accounts for suspicious activity</li>
                        <li>Contact financial institutions if needed</li>
                        <li>Learn from the incident to prevent future attacks</li>
                    </ul>
                </div>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Module Summary</h5>
                    <p>You now understand proper incident response procedures. In the final module, you'll take a comprehensive assessment of all your learning.</p>
                </div>
            </div>
            ''',
            'order': 7,
            'has_simulation': False
        },
        {
            'name': 'Final Assessment',
            'description': 'Comprehensive evaluation of all learning outcomes',
            'content': '''
            <div class="module-content">
                <h3><i class="fas fa-graduation-cap"></i> Final Assessment</h3>
                
                <div class="alert alert-info">
                    <h5><i class="fas fa-lightbulb"></i> Assessment Overview</h5>
                    <p>This final assessment will evaluate your understanding of all social engineering concepts covered in the previous modules.</p>
                </div>

                <h4><i class="fas fa-clipboard-check"></i> What to Expect</h4>
                <p>The final assessment includes questions from all modules and tests your ability to apply knowledge in real-world scenarios.</p>

                <div class="card bg-light">
                    <div class="card-body">
                        <h5><i class="fas fa-list"></i> Assessment Topics</h5>
                        <ul>
                            <li>Social engineering fundamentals and psychology</li>
                            <li>Types of attacks and their characteristics</li>
                            <li>Phishing identification and defense</li>
                            <li>Pretexting and impersonation recognition</li>
                            <li>Baiting and quid pro quo scenarios</li>
                            <li>Advanced techniques and countermeasures</li>
                            <li>Incident response procedures</li>
                        </ul>
                    </div>
                </div>

                <h4><i class="fas fa-trophy"></i> Success Criteria</h4>
                <p>To pass the final assessment, you must demonstrate comprehensive understanding of social engineering concepts and practical application skills.</p>

                <div class="alert alert-success">
                    <h5><i class="fas fa-check-circle"></i> Ready for Assessment</h5>
                    <p>You have completed all learning modules and are now ready to take the final comprehensive assessment. Good luck!</p>
                </div>
            </div>
            ''',
            'order': 8,
            'has_simulation': False
        }
    ]
    
    for module_data in modules_data:
        module = Module(**module_data)
        db.session.add(module)
    
    print("✅ Added remaining modules (3-8)")

def add_questions_for_remaining_modules():
    """Add questions for modules 3-8"""
    
    # Module 3: Phishing Attacks
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
            'module_id': 3,
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
            'module_id': 3,
            'question_text': 'What is whaling in social engineering?',
            'option_a': 'Phishing attacks targeting fish',
            'option_b': 'Phishing attacks targeting high-level executives',
            'option_c': 'Phishing attacks in the ocean',
            'option_d': 'Phishing attacks using whale sounds',
            'correct_answer': 'b',
            'explanation': 'Whaling refers to phishing attacks specifically targeting high-level executives and decision-makers.',
            'question_set': 1
        },
        {
            'module_id': 3,
            'question_text': 'What is the best defense against phishing?',
            'option_a': 'Using antivirus software only',
            'option_b': 'Awareness and verification procedures',
            'option_c': 'Ignoring all emails',
            'option_d': 'Using the same password everywhere',
            'correct_answer': 'b',
            'explanation': 'Awareness and verification procedures are the best defense against phishing attacks.',
            'question_set': 1
        }
    ]
    
    # Module 4: Pretexting and Impersonation
    module4_questions = [
        {
            'module_id': 4,
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
            'module_id': 4,
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
            'module_id': 4,
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
            'question_text': 'What is a common pretexting scenario?',
            'option_a': 'Sending spam emails',
            'option_b': 'IT support claiming to need password verification',
            'option_c': 'Hacking into systems',
            'option_d': 'Creating fake websites',
            'correct_answer': 'b',
            'explanation': 'IT support claiming to need password verification is a common pretexting scenario.',
            'question_set': 1
        }
    ]
    
    # Module 5: Baiting and Quid Pro Quo
    module5_questions = [
        {
            'module_id': 5,
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
            'module_id': 5,
            'question_text': 'What should you do with unknown USB devices?',
            'option_a': 'Plug them into your computer immediately',
            'option_b': 'Never plug unknown USB devices into your computer',
            'option_c': 'Format them and use them',
            'option_d': 'Give them to IT without checking',
            'correct_answer': 'b',
            'explanation': 'Never plug unknown USB devices into your computer as they may contain malware.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What is quid pro quo in social engineering?',
            'option_a': 'Offering a service in exchange for information or access',
            'option_b': 'Sending threatening messages',
            'option_c': 'Creating fake websites',
            'option_d': 'Hacking into systems',
            'correct_answer': 'a',
            'explanation': 'Quid pro quo involves offering a service or benefit in exchange for sensitive information or access.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What is a common quid pro quo scenario?',
            'option_a': 'Sending spam emails',
            'option_b': 'Tech support offering help in exchange for passwords',
            'option_c': 'Hacking into systems',
            'option_d': 'Creating fake websites',
            'correct_answer': 'b',
            'explanation': 'Tech support offering help in exchange for passwords is a common quid pro quo scenario.',
            'question_set': 1
        },
        {
            'module_id': 5,
            'question_text': 'What is the best defense against baiting attacks?',
            'option_a': 'Using antivirus software only',
            'option_b': 'Never using unknown physical media',
            'option_c': 'Ignoring all physical items',
            'option_d': 'Using the same password everywhere',
            'correct_answer': 'b',
            'explanation': 'Never using unknown physical media is the best defense against baiting attacks.',
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
    
    # Module 8: Final Assessment (comprehensive questions)
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
    
    # Add all questions
    all_questions = (module3_questions + module4_questions + module5_questions + 
                    module6_questions + module7_questions + module8_questions)
    
    for question_data in all_questions:
        question = KnowledgeCheckQuestion(**question_data)
        db.session.add(question)
    
    print("✅ Added questions for remaining modules")

def main():
    with app.app_context():
        # Add remaining modules and questions
        add_remaining_modules()
        add_questions_for_remaining_modules()
        
        # Commit changes
        db.session.commit()
        
        print("✅ Successfully added all remaining modules and questions!")
        print(f"Total modules: {Module.query.count()}")
        print(f"Total questions: {KnowledgeCheckQuestion.query.count()}")

if __name__ == '__main__':
    main() 