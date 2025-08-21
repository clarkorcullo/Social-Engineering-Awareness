"""
Base simulation class for Social Engineering Awareness Program
Provides common functionality for all simulation types
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import random

class BaseSimulation(ABC):
    """Abstract base class for all simulation types"""
    
    def __init__(self):
        """Initialize base simulation"""
        self.simulation_type = self.get_simulation_type()
        self.scenarios = self.get_scenarios()
    
    @abstractmethod
    def get_simulation_type(self) -> str:
        """Get the simulation type identifier"""
        pass
    
    @abstractmethod
    def get_scenarios(self) -> List[Dict[str, Any]]:
        """Get list of scenarios for this simulation type"""
        pass
    
    def get_random_scenario(self) -> Dict[str, Any]:
        """Get a random scenario from the available scenarios"""
        if not self.scenarios:
            raise ValueError(f"No scenarios available for {self.simulation_type}")
        return random.choice(self.scenarios)
    
    def get_scenario_by_id(self, scenario_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific scenario by ID"""
        for scenario in self.scenarios:
            if scenario.get('id') == scenario_id:
                return scenario
        return None
    
    def get_all_scenarios(self) -> List[Dict[str, Any]]:
        """Get all scenarios for this simulation type"""
        return self.scenarios
    
    def validate_scenario(self, scenario: Dict[str, Any]) -> bool:
        """Validate that a scenario has all required fields"""
        required_fields = ['id', 'type', 'title', 'description', 'options']
        
        for field in required_fields:
            if field not in scenario:
                return False
        
        # Validate options
        options = scenario.get('options', [])
        if not options:
            return False
        
        for option in options:
            if not all(key in option for key in ['id', 'text', 'correct', 'explanation']):
                return False
        
        return True
    
    def get_correct_answers(self, scenario: Dict[str, Any]) -> List[str]:
        """Get list of correct answer IDs for a scenario"""
        correct_answers = []
        for option in scenario.get('options', []):
            if option.get('correct', False):
                correct_answers.append(option['id'])
        return correct_answers
    
    def calculate_score(self, scenario: Dict[str, Any], user_answers: Dict[str, str]) -> Dict[str, Any]:
        """Calculate score for user answers"""
        score = 0
        total_questions = len(scenario.get('options', []))
        detailed_results = []
        
        for option in scenario.get('options', []):
            user_answer = user_answers.get(str(option['id']), '').lower()
            is_correct = user_answer == option['id'].lower() and option['correct']
            
            if is_correct:
                score += 1
            
            detailed_results.append({
                'question_id': option['id'],
                'user_answer': user_answer,
                'correct_answer': option['id'] if option['correct'] else 'N/A',
                'is_correct': is_correct,
                'explanation': option['explanation']
            })
        
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0
        
        return {
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage,
            'detailed_results': detailed_results,
            'passed': percentage >= 70  # 70% passing threshold
        }
