#!/usr/bin/env python3
"""
Script to update Module 2 content with missing statistics
"""

import os
import sys
from datetime import datetime

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Module

def update_module2_statistics():
    """Update Module 2 content with missing statistics"""
    with app.app_context():
        print("🔄 Updating Module 2 with missing statistics...")
        
        # Get Module 2
        module2 = Module.query.filter_by(id=2).first()
        if not module2:
            print("❌ Module 2 not found!")
            return
        
        # Updated Module 2 content with statistics
        updated_content = """
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
                <h3><i class="fas fa-chart-pie"></i> Social Engineering Attack Statistics</h3>
                
                <div class="statistics-highlight">
                    <div class="stat-card">
                        <div class="stat-number">65%</div>
                        <div class="stat-label">of social engineering attacks are phishing attacks</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">20%</div>
                        <div class="stat-label">of social engineering attacks are pretexting</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">15%</div>
                        <div class="stat-label">of social engineering attacks are other methods</div>
                    </div>
                </div>
                
                <div class="alert alert-info">
                    <div class="alert-icon">
                        <i class="fas fa-info-circle"></i>
                    </div>
                    <div class="alert-content">
                        <h4>Key Insight</h4>
                        <p>Phishing accounts for the majority of social engineering attacks (65%), making it the most common and dangerous technique. Pretexting represents 20% of attacks, while other methods like baiting, quid pro quo, and vishing make up the remaining 15%.</p>
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
                        <p>Phishing is the most common social engineering attack, accounting for <strong>65% of all social engineering attacks</strong>. Attackers send fraudulent messages designed to trick people into revealing sensitive information or downloading malicious software.</p>
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
                            <p><strong>Description:</strong> Targeted attacks against specific individuals or organizations using personalized information.</p>
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
                        <p>Pretexting involves creating a fabricated scenario to obtain information from a target. Attackers build trust by pretending to be someone they're not. <strong>Pretexting accounts for 20% of social engineering attacks</strong>.</p>
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
                        <p>65% of social engineering attacks are phishing attacks, making them the most frequent method.</p>
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
                        <p>20% of social engineering attacks use pretexting to create believable scenarios.</p>
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
        
        # Update Module 2 content
        module2.content = updated_content
        db.session.commit()
        
        print("✅ Module 2 updated with statistics!")
        print("📊 Added statistics:")
        print("   - 65% of social engineering attacks are phishing attacks")
        print("   - 20% of social engineering attacks are pretexting")
        print("   - 15% of social engineering attacks are other methods")

if __name__ == "__main__":
    update_module2_statistics()



