"""
Modules package for Social Engineering Awareness Program
Contains individual module content and knowledge check questions
"""

from .module1 import Module1Content, Module1Questions
from .module2 import Module2Content, Module2Questions
from .module3 import Module3Content, Module3Questions
from .module4 import Module4Content, Module4Questions
from .module5 import Module5Content, Module5Questions
from .module6 import Module6Content, Module6Questions
from .module7 import Module7Content, Module7Questions
from .final_assessment import FinalAssessmentContent, FinalAssessmentQuestions

__all__ = [
    'Module1Content', 'Module1Questions',
    'Module2Content', 'Module2Questions',
    'Module3Content', 'Module3Questions',
    'Module4Content', 'Module4Questions',
    'Module5Content', 'Module5Questions',
    'Module6Content', 'Module6Questions',
    'Module7Content', 'Module7Questions',
    'FinalAssessmentContent', 'FinalAssessmentQuestions'
]

