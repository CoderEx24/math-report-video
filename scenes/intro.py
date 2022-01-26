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
