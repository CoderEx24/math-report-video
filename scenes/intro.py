from manim import *

# this is the intro scene
# it should display the title "Digital Image" for 3 seconds
# then it may include and introduction into the topic

class Intro(Scene):
    def construct(self):
        title = Tex("Digital Image")

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        self.wait(1)

        title   = Tex("Topic Points")
        point_1 = Tex("- Representing Images as Matrices")
        point_2 = Tex("- Types of Image Compression")
        point_3 = Tex("- JPEG")
        
        point_1.align_to(3 * UP)
        point_2.next_to(point_1, DOWN).align_to(point_1, LEFT)
        point_3.next_to(point_2, DOWN).align_to(point_1, LEFT)

        self.play(Write(title))
        self.wait(3)
        self.play(title.animate.align_on_border(UP))
        self.wait(3)
        self.play(Write(point_1))
        self.wait(3)
        self.play(Write(point_2))
        self.wait(3)
        self.play(Write(point_3))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(point_1), FadeOut(point_2), FadeOut(point_3))
        self.wait(3)
