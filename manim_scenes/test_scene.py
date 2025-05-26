from manim import *

class TestScene(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        
        # Create a square
        square = Square(side_length=3, color=RED)
        
        # Create text
        text = Text("Test Animation", color=WHITE)
        
        # Add animations
        self.play(Create(circle))
        self.wait(1)
        
        self.play(Transform(circle, square))
        self.wait(1)
        
        self.play(Write(text))
        self.wait(2) 