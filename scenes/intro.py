from manim import *

# this is the intro scene
# it should display the title "Digital Image" for 3 seconds
# then it may include and introduction into the topic

class Intro(Scene):
    def construct(self):
        title = Text("Digital Image")

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        self.wait(1)

        title   = Text("Topic Points")
        point_1 = Text("- Representing Images as Matrices")
        point_2 = Text("- Types of Image Compression")
        point_3 = Text("- JPEG")
       
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.align_on_border(UP))
        self.wait(1)
        self.play(Write(point_1))
        self.wait()
        self.play(point_1.animate.next_to(title, DOWN))
        self.wait(1)
        self.play(Write(point_2))
        self.wait()
        self.play(point_2.animate.next_to(point_1, DOWN))
        self.wait(1)
        self.play(Write(point_3))
        self.wait()
        self.play(point_3.animate.next_to(point_2, DOWN))
        self.wait(1)
