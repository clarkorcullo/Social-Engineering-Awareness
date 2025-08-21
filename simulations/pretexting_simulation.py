"""
Pretexting simulation scenarios for Social Engineering Awareness Program
Contains realistic pretexting scenarios and decision points
"""

from typing import List, Dict, Any
from .base_simulation import BaseSimulation

class PretextingSimulation(BaseSimulation):
    """Pretexting simulation scenarios"""
    
    def get_simulation_type(self) -> str:
        """Get the simulation type identifier"""
        return "pretexting"
    
    def get_scenarios(self) -> List[Dict[str, Any]]:
        """Get list of pretexting scenarios"""
        return [
            {
                'id': 1,
                'type': 'pretexting',
                'title': 'IT Support Call',
                'description': 'Someone calls claiming to be from IT support.',
                'caller_info': 'IT Support Department',
                'scenario': '''The caller says: "Hello, this is IT Support. We've detected a virus on your computer and need to verify your account for security purposes. Can you please provide your username and password?"''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide your password', 
                        'correct': False, 
                        'explanation': 'Never give passwords over the phone. IT support should never ask for passwords.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their employee ID', 
                        'correct': True, 
                        'explanation': 'Always verify the caller\'s identity before providing any information.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Hang up immediately', 
                        'correct': False, 
                        'explanation': 'While safe, it\'s better to verify first and then report if suspicious.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Transfer to your supervisor', 
                        'correct': True, 
                        'explanation': 'Escalating to supervisor is a good practice for suspicious calls.'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'pretexting',
                'title': 'Vendor Verification',
                'description': 'Someone calls claiming to be from a vendor company.',
                'caller_info': 'ABC Supplies Inc.',
                'scenario': '''The caller says: "Hello, I'm calling from ABC Supplies. We need to verify your account information for our records. Can you confirm your company's billing address and account number?"''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide the information', 
                        'correct': False, 
                        'explanation': 'Never provide account information to unsolicited callers.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask them to send a written request', 
                        'correct': True, 
                        'explanation': 'Legitimate vendors will send written requests for verification.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Call them back using known number', 
                        'correct': True, 
                        'explanation': 'Call back using the official number from your records.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Transfer to purchasing department', 
                        'correct': True, 
                        'explanation': 'Forwarding to the appropriate department is correct.'
                    }
                ]
            },
            {
                'id': 3,
                'type': 'pretexting',
                'title': 'Social Security Call',
                'description': 'Someone calls claiming to be from Social Security Administration.',
                'caller_info': 'Social Security Administration',
                'scenario': '''The caller says: "This is the Social Security Administration. We need to verify your Social Security number due to suspicious activity. Can you please provide your full SSN and date of birth?"''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide your SSN', 
                        'correct': False, 
                        'explanation': 'Never provide SSN over the phone. Government agencies don\'t call asking for SSN.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their badge number', 
                        'correct': True, 
                        'explanation': 'Always ask for official identification from government callers.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Hang up and call SSA directly', 
                        'correct': True, 
                        'explanation': 'Call the official SSA number to verify if there\'s an issue.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Provide partial information', 
                        'correct': False, 
                        'explanation': 'Don\'t provide any personal information to unsolicited callers.'
                    }
                ]
            },
            {
                'id': 4,
                'type': 'pretexting',
                'title': 'Bank Security Alert',
                'description': 'Someone calls claiming to be from your bank\'s security department.',
                'caller_info': 'Bank Security Department',
                'scenario': '''The caller says: "This is Bank Security. We've detected fraudulent activity on your account. To protect your account, we need to verify your identity. Can you provide your account number and PIN?"''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide account information', 
                        'correct': False, 
                        'explanation': 'Banks never call asking for account numbers or PINs.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their employee ID', 
                        'correct': True, 
                        'explanation': 'Always verify the caller\'s identity before providing any information.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Call the bank directly', 
                        'correct': True, 
                        'explanation': 'Call the official bank number to verify if there\'s an issue.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Provide partial account number', 
                        'correct': False, 
                        'explanation': 'Don\'t provide any account information to unsolicited callers.'
                    }
                ]
            }
        ]
