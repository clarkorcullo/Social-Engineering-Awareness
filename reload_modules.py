"""
Script to reload modules with proper content from modules folder
"""

from app import app, db
from data_models.content_models import Module, KnowledgeCheckQuestion

def reload_modules():
    """Reload modules with proper content"""
    
    with app.app_context():
        print("🔄 Reloading Modules with Proper Content")
        print("=" * 50)
        
        try:
            # Clear existing modules and questions
            print("🗑️  Clearing existing modules and questions...")
            KnowledgeCheckQuestion.query.delete()
            Module.query.delete()
            db.session.commit()
            print("✅ Cleared existing data")
            
            # Import module content classes
            print("\n📚 Importing module content...")
            from learning_modules import (
                Module1Content, Module2Content, Module3Content, Module4Content,
                Module5Content, Module6Content, Module7Content, FinalAssessmentContent
            )
            
            # Module content classes
            module_classes = [
                Module1Content, Module2Content, Module3Content, Module4Content,
                Module5Content, Module6Content, Module7Content, FinalAssessmentContent
            ]
            
            print("📝 Creating modules with content...")
            for i, module_class in enumerate(module_classes, 1):
                # Get content from module class
                content_data = module_class.get_content()
                
                # Create module data
                module_data = {
                    'name': content_data['title'],
                    'description': content_data['description'],
                    'content': content_data['content'],
                    'order': i,
                    'has_simulation': i in [2, 3, 4, 5],  # Modules 2-5 have simulations
                    'simulation_type': 'phishing' if i == 3 else 'pretexting' if i == 4 else 'baiting' if i == 5 else None
                }
                
                # Create and save module
                module = Module(**module_data)
                if module.save():
                    print(f"✅ Created module {i}: {content_data['title']}")
                else:
                    print(f"❌ Failed to create module {i}")
            
            # Import and create questions
            print("\n❓ Creating knowledge check questions...")
            from learning_modules import (
                Module1Questions, Module2Questions, Module3Questions, Module4Questions,
                Module5Questions, Module6Questions, Module7Questions, FinalAssessmentQuestions
            )
            
            # Module question classes
            question_classes = [
                Module1Questions, Module2Questions, Module3Questions, Module4Questions,
                Module5Questions, Module6Questions, Module7Questions, FinalAssessmentQuestions
            ]
            
            for module_id, question_class in enumerate(question_classes, 1):
                # Get questions from module class
                questions_data = question_class.get_question_set_1()
                
                for question_data in questions_data:
                    # Add module_id to question data
                    question_data['module_id'] = module_id
                    
                    # Remove any fields that are not in the KnowledgeCheckQuestion model
                    if 'module_source' in question_data:
                        del question_data['module_source']
                    
                    # Create and save question
                    question = KnowledgeCheckQuestion(**question_data)
                    if question.save():
                        print(f"✅ Created question for module {module_id}")
                    else:
                        print(f"❌ Failed to create question for module {module_id}")
            
            print("\n🎉 Module reload completed successfully!")
            print(f"📊 Total modules created: {Module.count()}")
            print(f"❓ Total questions created: {KnowledgeCheckQuestion.count()}")
            
        except Exception as e:
            print(f"❌ Error reloading modules: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    reload_modules()
