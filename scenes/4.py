from manim import *

class Outro(Scene):
    def construct(self):
        digital_image_title = Tex("Digital Image")
        group_members_list  = Tex(r"Kareem Hassanein Hassan \\ --REDACTED--")
        credits_text        = Tex(r"This Video was made by Manim, check it out at the link below \\ https://github.com/ManimCommunity/manim")
        video_repo_text     = Tex(r"check out this video's code repository at \\ https://github.com/CoderEx24/math-report-video")

        digital_image_title.align_on_border(UP)
        credits_text.shift(UP)
        video_repo_text.next_to(credits_text, DOWN);

        self.play(Write(digital_image_title), \
                Write(group_members_list));       self.wait(3)
        self.play(FadeOut(group_members_list));   self.wait(3)
        self.play(Write(credits_text), \
                Write(video_repo_text));          self.wait(3)
        self.play(FadeOut(digital_image_title), \
                FadeOut(credits_text),          \
                FadeOut(video_repo_text))

