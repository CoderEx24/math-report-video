from manim import *

class Jpeg(Scene):
    def construct(self):
        jpeg_title = Tex("JPEG")

        self.play(Write(jpeg_title));   self.wait(2)
        self.play(FadeOut(jpeg_title)); self.wait(2)

        color_space_transform_title = Tex("Color Space Transformation")
        rgb_vector                  = MathTex(r"\vec{i}_{rgb} = \begin{bmatrix} R \\ G \\ B \end{bmatrix}")
        ycc_vector                  = MathTex(r"\vec{i}_{ycc} = \begin{bmatrix} Y \\ C_r \\ C_b \end{bmatrix}")
        y_text                      = Tex("$Y$ is luminance")
        cc_text                     = Tex("$C_r$ and $C_b$ are chrominance")

        color_space_transform_title.align_on_border(UP)
        y_text.next_to(ycc_vector, DOWN)
        cc_text.next_to(y_text, DOWN)

        self.play(Write(color_space_transform_title));  self.wait(3)
        self.play(Write(rgb_vector));                   self.wait(3)
        self.play(Transform(rgb_vector, ycc_vector));   self.wait(3)
        self.play(Write(y_text), \
                Write(cc_text));                        self.wait(3)
        self.play(FadeOut(color_space_transform_title), \
                FadeOut(rgb_vector),                    \
                FadeOut(y_text),                        \
                FadeOut(cc_text));                      self.wait(3)


