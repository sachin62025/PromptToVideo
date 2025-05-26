import google.generativeai as genai
from app.utils.logger import get_logger

logger = get_logger(__name__)

# Configure the Gemini API
genai.configure(api_key='GEMINI_API_KEY')

def generate_code(user_prompt: str) -> str:
    logger.info(f"Generating Manim code for prompt: {user_prompt}")
    
    # Simple template for a basic circle animation
    template = """from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        
        # Create a square
        square = Square(side_length=3, color=RED)
        
        # Add animations
        self.play(Create(circle))
        self.wait(1)
        
        self.play(Transform(circle, square))
        self.wait(2)
"""
    
    try:
        # Try to use the new recommended model
        model_name = 'gemini-1.5-flash'
        try:
            model = genai.GenerativeModel(model_name)
        except Exception as e:
            logger.warning(f"Could not use {model_name}: {e}. Trying available models.")
            models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            if not models:
                logger.error("No suitable models found")
                return template
            model = genai.GenerativeModel(models[0].name)
        
        # Create a more specific prompt
        prompt = f"""Generate Manim code for this animation: {user_prompt}
        Requirements:
        1. The code must be a complete, valid Python file
        2. The class must be named 'GeneratedScene' and inherit from Scene
        3. The code must be properly indented
        4. The code must be enclosed in triple backticks (```python ... ```)
        5. Use this template as a base:
        {template}
        """
        
        # Generate response
        response = model.generate_content(prompt)
        
        if not response.text:
            logger.warning("Empty response from Gemini, using template")
            return template
            
        generated_code = response.text
        
        # Extract code from markdown if present
        if "```python" in generated_code:
            code_blocks = generated_code.split("```python")
            if len(code_blocks) > 1:
                code = code_blocks[1].split("```")[0].strip()
                generated_code = code
        
        # Validate that we have a GeneratedScene class
        if "class GeneratedScene" not in generated_code:
            logger.warning("Generated code does not contain GeneratedScene class, using template")
            return template
            
        logger.info("Successfully generated Manim code")
        logger.debug(f"Generated code: {generated_code}")
        return generated_code
    except Exception as e:
        logger.error(f"Error generating code: {str(e)}")
        logger.info("Using fallback template")
        return template
