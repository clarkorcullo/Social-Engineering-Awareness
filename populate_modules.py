#!/usr/bin/env python3
"""
Script to populate the database with default modules
"""

from app import app, db, Module

def populate_modules():
    """Populate the database with default modules"""
    
    modules = [
        {
            'name': 'Introduction to Social Engineering',
            'description': 'Understanding the fundamentals of social engineering and human psychology.',
            'content': '<h3>What is Social Engineering?</h3><p>Social engineering is the art of manipulating people so they give up confidential information. The types of information these criminals are seeking can vary, but when individuals are targeted, the criminals are usually trying to trick you into giving them your passwords or bank information, or access your computer to secretly install malicious software.</p>',
            'order': 1,
            'has_simulation': False,
            'simulation_type': None
        },
        {
            'name': 'Types of Social Engineering Attacks',
            'description': 'Exploring different attack vectors and manipulation techniques.',
            'content': '<h3>Common Attack Types</h3><ul><li>Phishing</li><li>Pretexting</li><li>Baiting</li><li>Quid Pro Quo</li></ul>',
            'order': 2,
            'has_simulation': True,
            'simulation_type': 'phishing'
        },
        {
            'name': 'Phishing Detection and Prevention',
            'description': 'Identifying and defending against phishing attacks.',
            'content': '<h3>Phishing</h3><p>Phishing is a method of trying to gather personal information using deceptive e-mails and websites.</p>',
            'order': 3,
            'has_simulation': True,
            'simulation_type': 'phishing'
        },
        {
            'name': 'Vishing and Voice-Based Attacks',
            'description': 'Understanding and defending against voice-based social engineering.',
            'content': '<h3>Vishing</h3><p>Vishing is the act of using the telephone in an attempt to scam the user into surrendering private information that will be used for identity theft.</p>',
            'order': 4,
            'has_simulation': False,
            'simulation_type': None
        },
        {
            'name': 'Physical Social Engineering',
            'description': 'Defending against in-person manipulation techniques.',
            'content': '<h3>Physical Social Engineering</h3><p>Physical social engineering involves manipulating people in person to gain unauthorized access to buildings, systems, or data.</p>',
            'order': 5,
            'has_simulation': False,
            'simulation_type': None
        },
        {
            'name': 'Advanced Defense Strategies',
            'description': 'Implementing comprehensive social engineering defenses.',
            'content': '<h3>Defense Strategies</h3><ul><li>Security Awareness Training</li><li>Multi-factor Authentication</li><li>Incident Response Planning</li></ul>',
            'order': 6,
            'has_simulation': False,
            'simulation_type': None
        },
        {
            'name': 'Incident Response and Recovery',
            'description': 'Responding to and recovering from social engineering attacks.',
            'content': '<h3>Incident Response</h3><p>Incident response is a well-organized approach to addressing and managing the aftermath of a security breach or cyberattack.</p>',
            'order': 7,
            'has_simulation': False,
            'simulation_type': None
        }
    ]
    
    with app.app_context():
        # Clear existing modules
        Module.query.delete()
        
        # Add new modules
        for m in modules:
            module = Module(**m)
            db.session.add(module)
        
        db.session.commit()
        print(f"✅ Successfully populated database with {len(modules)} modules!")

if __name__ == '__main__':
    populate_modules() 