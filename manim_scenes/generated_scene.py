from manim import *

class GeneratedScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True},
        )

        # Sine wave
        sine_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_label = MathTex(r"\sin(x)").next_to(sine_graph, UP, buff=0.2)

        # Cosine wave
        cosine_graph = axes.plot(lambda x: np.cos(x), color=RED)
        cosine_label = MathTex(r"\cos(x)").next_to(cosine_graph, UP, buff=0.2)


        self.play(Create(axes))
        self.play(Create(sine_graph), Create(sine_label))
        self.play(Create(cosine_graph), Create(cosine_label))

        self.wait(2)

        # Animate the graphs growing (optional)
        # You can modify the range to control the animation speed and extent.

        sine_graph_anim = axes.plot(lambda x: np.sin(x), color=BLUE)
        cosine_graph_anim = axes.plot(lambda x: np.cos(x), color=RED)


        #This section is commented out because the animation is quite slow and doesn't add much value
        # self.play(
        #     Transform(sine_graph, sine_graph_anim),
        #     Transform(cosine_graph, cosine_graph_anim),
        #     run_time=5
        # )

        self.wait(2)