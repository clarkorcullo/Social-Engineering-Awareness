"""
Phishing simulation scenarios for Social Engineering Awareness Program
Contains realistic phishing email scenarios and decision points
"""

from typing import List, Dict, Any
from .base_simulation import BaseSimulation

class PhishingSimulation(BaseSimulation):
    """Phishing simulation scenarios"""
    
    def get_simulation_type(self) -> str:
        """Get the simulation type identifier"""
        return "phishing"
    
    def get_scenarios(self) -> List[Dict[str, Any]]:
        """Get list of phishing scenarios"""
        return [
            {
                'id': 1,
                'type': 'phishing',
                'title': 'Suspicious Email from Bank',
                'description': 'You receive an email claiming to be from your bank asking for account verification.',
                'email_subject': 'URGENT: Account Verification Required',
                'email_sender': 'security@yourbank.com',
                'email_content': '''Dear Valued Customer,

We have detected suspicious activity on your account and need to verify your identity immediately.

Please click the link below to verify your account details:
[VERIFY ACCOUNT]

If you do not verify within 24 hours, your account will be suspended.

Thank you,
Bank Security Team''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Click the link and provide information', 
                        'correct': False, 
                        'explanation': 'Never click links in suspicious emails. Banks never ask for account verification via email.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Forward to IT department', 
                        'correct': True, 
                        'explanation': 'Forwarding suspicious emails to IT is the correct action for security threats.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Reply with your account details', 
                        'correct': False, 
                        'explanation': 'Never provide account details via email. This is a common phishing tactic.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Delete the email', 
                        'correct': False, 
                        'explanation': 'While deleting is okay, reporting to IT is better for security awareness.'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'phishing',
                'title': 'Prize Notification',
                'description': 'You receive an email claiming you won a prize.',
                'email_subject': 'CONGRATULATIONS! You Won $10,000!',
                'email_sender': 'prizes@lottery.com',
                'email_content': '''Congratulations!

You have been selected as a winner in our annual lottery!
Your prize: $10,000 USD

To claim your prize, please click the link below and provide your banking information:
[CLAIM PRIZE]

This offer expires in 24 hours.

Best regards,
Lottery Commission''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Click to claim your prize', 
                        'correct': False, 
                        'explanation': 'This is likely a scam. Legitimate lotteries don\'t contact winners via email.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Delete the email', 
                        'correct': True, 
                        'explanation': 'Delete suspicious prize emails. If you didn\'t enter a lottery, you didn\'t win.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Reply asking for more details', 
                        'correct': False, 
                        'explanation': 'Don\'t engage with suspicious emails. This confirms your email is active.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Forward to friends', 
                        'correct': False, 
                        'explanation': 'Don\'t spread potential scams to others.'
                    }
                ]
            },
            {
                'id': 3,
                'type': 'phishing',
                'title': 'Password Reset Request',
                'description': 'You receive an email about a password reset you didn\'t request.',
                'email_subject': 'Password Reset Request',
                'email_sender': 'noreply@company.com',
                'email_content': '''Hello,

We received a request to reset your password for your account.

If you made this request, click the link below to reset your password:
[RESET PASSWORD]

If you did not make this request, please ignore this email.

Best regards,
IT Support Team''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Click the reset link', 
                        'correct': False, 
                        'explanation': 'If you didn\'t request a reset, this could be a phishing attempt.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Go directly to the company website', 
                        'correct': True, 
                        'explanation': 'Always go directly to the official website, never click email links.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Reply to the email', 
                        'correct': False, 
                        'explanation': 'Don\'t reply to suspicious emails. Contact IT directly if needed.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Forward to IT security', 
                        'correct': True, 
                        'explanation': 'Forwarding suspicious emails to IT security is a good practice.'
                    }
                ]
            },
            {
                'id': 4,
                'type': 'phishing',
                'title': 'Invoice Payment',
                'description': 'You receive an email with an urgent invoice payment request.',
                'email_subject': 'URGENT: Invoice Payment Overdue',
                'email_sender': 'billing@supplier.com',
                'email_content': '''Dear Customer,

Your invoice #INV-2024-001 is overdue.
Amount: $2,500.00
Due Date: Yesterday

Please click the link below to make immediate payment:
[PAY INVOICE]

Failure to pay may result in legal action.

Thank you,
Billing Department''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Click the payment link', 
                        'correct': False, 
                        'explanation': 'Never click payment links in emails. Verify the invoice first.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Contact the company directly', 
                        'correct': True, 
                        'explanation': 'Contact the company directly using known contact information.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Reply asking for invoice details', 
                        'correct': False, 
                        'explanation': 'Don\'t engage with suspicious emails. Contact the company directly.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Forward to accounting department', 
                        'correct': True, 
                        'explanation': 'Forwarding to accounting for verification is appropriate.'
                    }
                ]
            }
        ]
