"""
Baiting simulation scenarios for Social Engineering Awareness Program
Contains realistic baiting scenarios and decision points
"""

from typing import List, Dict, Any
from .base_simulation import BaseSimulation

class BaitingSimulation(BaseSimulation):
    """Baiting simulation scenarios"""
    
    def get_simulation_type(self) -> str:
        """Get the simulation type identifier"""
        return "baiting"
    
    def get_scenarios(self) -> List[Dict[str, Any]]:
        """Get list of baiting scenarios"""
        return [
            {
                'id': 1,
                'type': 'baiting',
                'title': 'USB Drive Found',
                'description': 'You find a USB drive in the office parking lot.',
                'scenario': '''You find a USB drive labeled "Employee Salaries 2024" in the parking lot. It looks like someone dropped it.''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Plug it into your computer to find the owner', 
                        'correct': False, 
                        'explanation': 'Never plug unknown USB drives into your computer. They may contain malware.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Turn it in to IT security', 
                        'correct': True, 
                        'explanation': 'Turn unknown devices over to IT security for safe handling.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Leave it where you found it', 
                        'correct': False, 
                        'explanation': 'Leaving it could allow others to pick it up and plug it in.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Take it to lost and found', 
                        'correct': False, 
                        'explanation': 'Lost and found may not have proper security protocols for unknown devices.'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'baiting',
                'title': 'Free Software Download',
                'description': 'You see an advertisement for free software.',
                'scenario': '''You see an ad for "Free Office Suite 2024" that claims to be a free alternative to Microsoft Office.''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Download and install it', 
                        'correct': False, 
                        'explanation': 'Free software from unknown sources may contain malware.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Research the software first', 
                        'correct': True, 
                        'explanation': 'Always research software before downloading, especially free alternatives.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Ask IT department', 
                        'correct': True, 
                        'explanation': 'Consult IT department before installing any software on work computers.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Download on personal computer first', 
                        'correct': False, 
                        'explanation': 'Don\'t risk your personal computer either. Research first.'
                    }
                ]
            },
            {
                'id': 3,
                'type': 'baiting',
                'title': 'Conference Giveaway',
                'description': 'You receive a free device at a conference.',
                'scenario': '''At a conference, a vendor gives you a free USB drive with their company logo and some promotional materials.''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Use it immediately to store files', 
                        'correct': False, 
                        'explanation': 'Even branded USB drives from vendors can contain malware.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Scan it with antivirus first', 
                        'correct': True, 
                        'explanation': 'Always scan unknown devices before using them.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Give it to IT for inspection', 
                        'correct': True, 
                        'explanation': 'IT can properly inspect and test the device before use.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Use it only on personal computer', 
                        'correct': False, 
                        'explanation': 'Don\'t risk any computer. Scan or have IT inspect first.'
                    }
                ]
            },
            {
                'id': 4,
                'type': 'baiting',
                'title': 'Email Attachment',
                'description': 'You receive an email with an interesting attachment.',
                'scenario': '''You receive an email with the subject "Free Movie Tickets" and an attachment called "tickets.pdf.exe".''',
                'options': [
                    {
                        'id': 'a', 
                        'text': 'Open the attachment', 
                        'correct': False, 
                        'explanation': 'Never open suspicious attachments, especially .exe files disguised as documents.'
                    },
                    {
                        'id': 'b', 
                        'text': 'Delete the email', 
                        'correct': True, 
                        'explanation': 'Delete suspicious emails with unexpected attachments.'
                    },
                    {
                        'id': 'c', 
                        'text': 'Forward to IT security', 
                        'correct': True, 
                        'explanation': 'Forward suspicious emails to IT security for analysis.'
                    },
                    {
                        'id': 'd', 
                        'text': 'Scan with antivirus first', 
                        'correct': False, 
                        'explanation': 'Don\'t even download suspicious attachments for scanning.'
                    }
                ]
            }
        ]
