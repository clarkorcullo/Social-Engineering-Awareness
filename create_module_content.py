#!/usr/bin/env python3
"""
Script to create comprehensive module content with questions and simulations
"""

import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Module, KnowledgeCheckQuestion

def create_module_content():
    with app.app_context():
        # Module 1: Introduction to Social Engineering
        module1_content = """
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-brain"></i> Understanding Social Engineering</h2>
                    <p class="lead">Learn the fundamentals of social engineering and why it's the most effective cyber attack method.</p>
                </div>
                
                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Define social engineering and its core principles</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand why social engineering is so effective</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Identify common human vulnerabilities</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize psychological principles exploited by attackers</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-question-circle"></i> What is Social Engineering?</h3>
                
                <div class="definition-card">
                    <div class="card-header">
                        <i class="fas fa-book"></i> Definition
                    </div>
                    <div class="card-body">
                        <p><strong>Social Engineering</strong> is the art of manipulating people into performing actions or divulging confidential information. Unlike technical hacking, social engineering targets the human element - often the weakest link in any security system.</p>
                        <p>Cybercriminals use social engineering techniques to trick people into making security mistakes or giving away sensitive information through psychological manipulation rather than technical exploits.</p>
                    </div>
                </div>

                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">98%</div>
                        <div class="stat-label">of cyberattacks rely on social engineering</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">85%</div>
                        <div class="stat-label">of data breaches involve human error</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">$6.9B</div>
                        <div class="stat-label">annual cost of social engineering attacks</div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-psychology"></i> Why Social Engineering Works</h3>
                
                <p>Social engineering is effective because it exploits natural human behaviors and psychological tendencies. Attackers understand that people are generally:</p>
                
                <div class="psychology-grid">
                    <div class="psychology-card helpful">
                        <div class="card-icon">
                            <i class="fas fa-heart"></i>
                        </div>
                        <h4>Helpful by Nature</h4>
                        <p>Most people want to be helpful and cooperative, especially when someone appears to be in need.</p>
                    </div>
                    
                    <div class="psychology-card trusting">
                        <div class="card-icon">
                            <i class="fas fa-handshake"></i>
                        </div>
                        <h4>Trusting of Authority</h4>
                        <p>People naturally trust authority figures and are more likely to comply with requests from perceived experts.</p>
                    </div>
                    
                    <div class="psychology-card curious">
                        <div class="card-icon">
                            <i class="fas fa-search"></i>
                        </div>
                        <h4>Naturally Curious</h4>
                        <p>Human curiosity can lead people to click on suspicious links or open unexpected attachments.</p>
                    </div>
                    
                    <div class="psychology-card fearful">
                        <div class="card-icon">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        <h4>Fearful of Consequences</h4>
                        <p>Fear of getting in trouble or missing deadlines can cause people to act quickly without thinking.</p>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-shield-alt"></i> The Human Factor in Cybersecurity</h3>
                
                <div class="alert alert-warning">
                    <div class="alert-icon">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <div class="alert-content">
                        <h4>Key Insight</h4>
                        <p>Even the most sophisticated technical defenses can be bypassed by manipulating the people who use them. This means that understanding and defending against social engineering is crucial for cybersecurity.</p>
                    </div>
                </div>
                
                <p>Traditional cybersecurity focuses on protecting systems and networks, but social engineering attacks target the human element. No matter how strong your technical defenses are, they can be compromised if someone is tricked into providing access.</p>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-chart-line"></i> The Social Engineering Attack Process</h3>
                
                <p>Social engineering attacks typically follow a structured process that exploits human psychology:</p>
                
                <div class="process-timeline">
                    <div class="timeline-item">
                        <div class="timeline-marker">
                            <span>1</span>
                        </div>
                        <div class="timeline-content">
                            <h4>Information Gathering</h4>
                            <p>Attackers research their targets to understand vulnerabilities and create convincing scenarios. They gather information from social media, company websites, and other public sources.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-marker">
                            <span>2</span>
                        </div>
                        <div class="timeline-content">
                            <h4>Building Trust</h4>
                            <p>Attackers establish credibility and rapport with their targets. They may impersonate trusted individuals or create scenarios that seem legitimate.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-marker">
                            <span>3</span>
                        </div>
                        <div class="timeline-content">
                            <h4>Exploiting Vulnerabilities</h4>
                            <p>Attackers manipulate targets into taking desired actions, such as clicking malicious links, providing passwords, or transferring money.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-marker">
                            <span>4</span>
                        </div>
                        <div class="timeline-content">
                            <h4>Maintaining Access</h4>
                            <p>Attackers ensure continued access and cover their tracks to avoid detection while maximizing their gains.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-graduation-cap"></i> Real-World Examples</h3>
                
                <p>Understanding real-world examples helps you recognize patterns and develop better defenses:</p>
                
                <div class="example-cards">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-building"></i>
                            <h4>Corporate Impersonation</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>An attacker calls an employee pretending to be from IT support, saying there's an urgent security issue that requires immediate password reset.</p>
                            
                            <h5>Psychological Triggers:</h5>
                            <ul>
                                <li><strong>Authority:</strong> IT support (trusted authority figure)</li>
                                <li><strong>Urgency:</strong> Security issue requiring immediate action</li>
                                <li><strong>Fear:</strong> Getting in trouble for not cooperating</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-envelope"></i>
                            <h4>Phishing Email</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>An employee receives an email appearing to be from their bank, claiming their account has been compromised and requiring immediate verification.</p>
                            
                            <h5>Psychological Triggers:</h5>
                            <ul>
                                <li><strong>Fear:</strong> Financial loss and account compromise</li>
                                <li><strong>Urgency:</strong> Immediate action required</li>
                                <li><strong>Trust:</strong> Appears to come from trusted institution</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <h4>People are the Target</h4>
                        <p>Social engineering attacks target human psychology, not technical systems.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-chart-pie"></i>
                        </div>
                        <h4>Most Common Attack Method</h4>
                        <p>98% of cyberattacks rely on social engineering techniques.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-virus"></i>
                        </div>
                        <h4>Defense is Possible</h4>
                        <p>Understanding these techniques is the first step in defending against them.</p>
                    </div>
                </div>
            </div>
        </div>
        """

        # Module 2: Types of Social Engineering Attacks
        module2_content = """
        <div class="learning-module">
            <div class="module-intro">
                <div class="intro-header">
                    <h2><i class="fas fa-mask"></i> Types of Social Engineering Attacks</h2>
                    <p class="lead">Explore the various techniques attackers use to manipulate people and gain unauthorized access.</p>
                </div>
                
                <div class="learning-objectives">
                    <h3><i class="fas fa-target"></i> Learning Objectives</h3>
                    <div class="objectives-grid">
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Identify different types of social engineering attacks</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Understand the psychology behind each attack type</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Recognize warning signs and red flags</span>
                        </div>
                        <div class="objective-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Learn defensive strategies for each attack type</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-envelope"></i> Phishing Attacks</h3>
                
                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-fish"></i>
                            <h4>What is Phishing?</h4>
                        </div>
                        <p>Phishing is the most common social engineering attack, where attackers send fraudulent messages designed to trick people into revealing sensitive information or downloading malicious software.</p>
                    </div>
                </div>

                <div class="phishing-types">
                    <div class="type-card">
                        <div class="type-header email">
                            <i class="fas fa-envelope"></i>
                            <h4>Email Phishing</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Fraudulent emails that appear to come from legitimate sources.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Urgent requests for action</li>
                                    <li>Requests for sensitive information</li>
                                    <li>Suspicious sender addresses</li>
                                    <li>Poor grammar or spelling</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="type-card">
                        <div class="type-header spear">
                            <i class="fas fa-crosshairs"></i>
                            <h4>Spear Phishing</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Targeted attacks against specific individuals or organizations.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Personalized information about you</li>
                                    <li>References to recent events</li>
                                    <li>Appears to come from known contacts</li>
                                    <li>Requests for unusual actions</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="type-card">
                        <div class="type-header whaling">
                            <i class="fas fa-crown"></i>
                            <h4>Whaling</h4>
                        </div>
                        <div class="type-content">
                            <p><strong>Description:</strong> Phishing attacks targeting high-level executives and decision-makers.</p>
                            <div class="warning-signs">
                                <h5><i class="fas fa-exclamation-triangle"></i> Warning Signs:</h5>
                                <ul>
                                    <li>Targets senior management</li>
                                    <li>Requests for financial transfers</li>
                                    <li>Confidential business matters</li>
                                    <li>Urgent executive decisions</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-phone"></i> Vishing (Voice Phishing)</h3>
                
                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-phone-alt"></i>
                            <h4>Voice-Based Social Engineering</h4>
                        </div>
                        <p>Vishing attacks use phone calls to manipulate victims into providing sensitive information or performing actions that benefit the attacker.</p>
                    </div>
                </div>

                <div class="vishing-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-bank"></i>
                            <h4>Bank Impersonation</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from your bank's security department, reporting suspicious activity on your account.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Requests for account verification</li>
                                <li>Asks for PIN or password</li>
                                <li>Creates sense of urgency</li>
                                <li>Won't let you call back</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-tools"></i>
                            <h4>Technical Support Scam</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from Microsoft or Apple support, saying your computer has been infected with viruses.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Claims to detect problems remotely</li>
                                <li>Requests remote access to your computer</li>
                                <li>Asks for payment for "services"</li>
                                <li>Creates fear about data loss</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-user-tie"></i> Pretexting</h3>
                
                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-theater-masks"></i>
                            <h4>Creating False Scenarios</h4>
                        </div>
                        <p>Pretexting involves creating a fabricated scenario to obtain information from a target. Attackers build trust by pretending to be someone they're not.</p>
                    </div>
                </div>

                <div class="pretexting-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-id-card"></i>
                            <h4>Identity Verification</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be from HR or IT, needing to verify employee information for "system updates."</p>
                            
                            <h5>Information Sought:</h5>
                            <ul>
                                <li>Employee ID numbers</li>
                                <li>Date of birth</li>
                                <li>Social Security numbers</li>
                                <li>Password resets</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-clipboard-list"></i>
                            <h4>Survey Scams</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be conducting a legitimate survey or research study, asking for personal information.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Asks for sensitive personal data</li>
                                <li>Offers rewards for participation</li>
                                <li>Refuses to provide company details</li>
                                <li>Creates pressure to participate</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-handshake"></i> Baiting</h3>
                
                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-bait"></i>
                            <h4>Physical and Digital Lures</h4>
                        </div>
                        <p>Baiting attacks use physical or digital "bait" to lure victims into a trap. The bait is designed to trigger human curiosity and greed.</p>
                    </div>
                </div>

                <div class="baiting-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-usb"></i>
                            <h4>USB Drop Attack</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Attackers leave infected USB drives in public places, hoping someone will plug them into a computer.</p>
                            
                            <h5>Defense Strategy:</h5>
                            <ul>
                                <li>Never plug in unknown USB devices</li>
                                <li>Disable autorun on computers</li>
                                <li>Use USB security policies</li>
                                <li>Train employees on risks</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-gift"></i>
                            <h4>Digital Baiting</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Attackers offer free software, games, or other digital content that contains malware.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Too good to be true offers</li>
                                <li>Requests for personal information</li>
                                <li>Unknown or suspicious sources</li>
                                <li>Pressure to act quickly</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-users"></i> Quid Pro Quo</h3>
                
                <div class="attack-overview">
                    <div class="overview-card">
                        <div class="overview-header">
                            <i class="fas fa-exchange-alt"></i>
                            <h4>Something for Something</h4>
                        </div>
                        <p>Quid pro quo attacks promise a benefit in exchange for information or access. Attackers exploit the human tendency to reciprocate favors.</p>
                    </div>
                </div>

                <div class="quid-pro-quo-examples">
                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-laptop"></i>
                            <h4>IT Support Scam</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims to be IT support offering to "fix" your computer problems in exchange for remote access.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Unsolicited support calls</li>
                                <li>Requests for remote access</li>
                                <li>Claims to detect problems you haven't noticed</li>
                                <li>Demands immediate action</li>
                            </ul>
                        </div>
                    </div>

                    <div class="example-card">
                        <div class="example-header">
                            <i class="fas fa-ticket-alt"></i>
                            <h4>Prize Scams</h4>
                        </div>
                        <div class="example-content">
                            <h5>Scenario:</h5>
                            <p>Caller claims you've won a prize or lottery, but requires personal information to claim it.</p>
                            
                            <h5>Red Flags:</h5>
                            <ul>
                                <li>Unsolicited prize notifications</li>
                                <li>Requests for bank account information</li>
                                <li>Demands for upfront fees</li>
                                <li>Pressure to act immediately</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <h3><i class="fas fa-lightbulb"></i> Key Takeaways</h3>
                
                <div class="takeaways-grid">
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <h4>Phishing is Most Common</h4>
                        <p>Email-based attacks are the most frequent social engineering method.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <h4>Voice Attacks are Effective</h4>
                        <p>Vishing can be more convincing than email due to human voice interaction.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-mask"></i>
                        </div>
                        <h4>Pretexting Builds Trust</h4>
                        <p>Attackers create believable scenarios to establish credibility.</p>
                    </div>
                    
                    <div class="takeaway-item">
                        <div class="takeaway-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h4>Defense is Multi-Layered</h4>
                        <p>Protection requires awareness, training, and technical controls.</p>
                    </div>
                </div>
            </div>
        </div>
        """

        # Update Module 1
        module1 = Module.query.filter_by(id=1).first()
        if module1:
            module1.content = module1_content
            print("✅ Updated Module 1 content")

        # Update Module 2
        module2 = Module.query.filter_by(id=2).first()
        if module2:
            module2.content = module2_content
            print("✅ Updated Module 2 content")

        # Update Knowledge Check Questions - Remove module references
        questions_to_update = [
            {
                'id': 1,
                'question_text': 'What percentage of cyberattacks rely on social engineering?',
                'explanation': '98% of cyberattacks rely on social engineering, making it crucial for cybersecurity.'
            },
            {
                'id': 2,
                'question_text': 'Which of the following is NOT listed as a natural human behavior exploited by social engineers?',
                'explanation': 'Advanced technical knowledge is not a vulnerability - it\'s actually a defense. The other options are natural human behaviors that can be exploited.'
            },
            {
                'id': 3,
                'question_text': 'What is the "human factor" in cybersecurity?',
                'explanation': 'The "human factor" refers to how human behavior and psychology often represent the weakest link in security systems.'
            },
            {
                'id': 4,
                'question_text': 'What is the first step in the social engineering attack process?',
                'explanation': 'The attack process begins with information gathering, where attackers research their targets to understand vulnerabilities.'
            },
            {
                'id': 5,
                'question_text': 'Which psychological principle involves people feeling obligated to return favors?',
                'explanation': 'Reciprocity involves feeling obligated to return favors, which social engineers exploit.'
            },
            {
                'id': 6,
                'question_text': 'What percentage of social engineering attacks are phishing attacks?',
                'explanation': 'Phishing accounts for 65% of social engineering attacks, making it the most common type.'
            },
            {
                'id': 7,
                'question_text': 'What is the key difference between regular phishing and spear phishing?',
                'explanation': 'Spear phishing involves targeted attacks against specific individuals using personalized information.'
            },
            {
                'id': 8,
                'question_text': 'Which of the following is NOT listed as a common pretexting scenario?',
                'explanation': 'Fake lottery winner notifications are not listed as common pretexting scenarios in the module.'
            },
            {
                'id': 9,
                'question_text': 'What percentage of social engineering attacks are pretexting?',
                'explanation': 'Pretexting accounts for 20% of social engineering attacks.'
            },
            {
                'id': 10,
                'question_text': 'What is the main characteristic of baiting attacks?',
                'explanation': 'Baiting is defined as using physical media or digital lures to entice victims into taking harmful actions.'
            }
        ]

        for question_data in questions_to_update:
            question = KnowledgeCheckQuestion.query.filter_by(id=question_data['id']).first()
            if question:
                question.question_text = question_data['question_text']
                question.explanation = question_data['explanation']
                print(f"✅ Updated question {question_data['id']}")

        db.session.commit()
        print("✅ All module content and questions updated successfully!")

if __name__ == "__main__":
    create_module_content() 