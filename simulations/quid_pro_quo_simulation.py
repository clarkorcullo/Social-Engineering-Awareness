"""
Quid Pro Quo simulation scenarios for Social Engineering Awareness Program
Contains realistic quid pro quo scenarios and decision points
"""

from typing import List, Dict, Any
from .base_simulation import BaseSimulation

class QuidProQuoSimulation(BaseSimulation):
    """Quid Pro Quo simulation scenarios"""
    
    def get_simulation_type(self) -> str:
        """Get the simulation type identifier"""
        return "quid_pro_quo"
    
    def get_scenarios(self) -> List[Dict[str, Any]]:
        """Get list of quid pro quo scenarios"""
        return [
            {
                'id': 1,
                'type': 'quid_pro_quo',
                'title': 'IT Support Exchange',
                'description': 'Someone offers IT support in exchange for information.',
                'scenario': '''A caller says: "I can help you fix your computer issues right now, but I need your login credentials to access the system. In return, I'll give you free tech support for a month."''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide your credentials', 
                        'correct': False, 
                        'explanation': 'Never provide login credentials in exchange for services.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their official ID', 
                        'correct': True, 
                        'explanation': 'Always verify the identity of anyone offering services.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Decline the offer', 
                        'correct': True, 
                        'explanation': 'Decline suspicious offers that require sensitive information.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Ask your supervisor first', 
                        'correct': True, 
                        'explanation': 'Consult with supervisor before accepting any external services.'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'quid_pro_quo',
                'title': 'Software License Offer',
                'description': 'Someone offers free software in exchange for access.',
                'scenario': '''A vendor says: "I can give you a free license for our premium software, but I need temporary access to your system to install it properly."''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Grant them access', 
                        'correct': False, 
                        'explanation': 'Never grant system access to external parties without proper procedures.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask IT department to handle it', 
                        'correct': True, 
                        'explanation': 'Let IT department handle all software installations and licensing.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Ask for written documentation', 
                        'correct': True, 
                        'explanation': 'Request proper documentation before accepting any software.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Decline the offer', 
                        'correct': True, 
                        'explanation': 'Decline offers that require system access from external parties.'
                    }
                ]
            },
            {
                'id': 3,
                'type': 'quid_pro_quo',
                'title': 'Training Exchange',
                'description': 'Someone offers training in exchange for company information.',
                'scenario': '''A consultant says: "I'll provide free cybersecurity training for your team, but I need some information about your current security setup to customize the training."''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Provide security details', 
                        'correct': False, 
                        'explanation': 'Don\'t share security information with external parties without proper authorization.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their credentials', 
                        'correct': True, 
                        'explanation': 'Verify the consultant\'s credentials and authorization.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Contact HR/management', 
                        'correct': True, 
                        'explanation': 'Consult with HR or management before accepting external training offers.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Use generic training materials', 
                        'correct': True, 
                        'explanation': 'Use generic training materials that don\'t require sensitive information.'
                    }
                ]
            },
            {
                'id': 4,
                'type': 'quid_pro_quo',
                'title': 'Discount for Information',
                'description': 'Someone offers a discount in exchange for customer data.',
                'scenario': '''A vendor says: "I can give you a 50% discount on our services if you can share some information about your customer base and their needs."''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Share customer information', 
                        'correct': False, 
                        'explanation': 'Never share customer information in exchange for discounts.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Ask for their privacy policy', 
                        'correct': True, 
                        'explanation': 'Request their privacy policy and data handling procedures.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Consult legal department', 
                        'correct': True, 
                        'explanation': 'Consult with legal department before sharing any customer data.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Decline the offer', 
                        'correct': True, 
                        'explanation': 'Decline offers that require sharing sensitive customer information.'
                    }
                ]
            }
        ]
