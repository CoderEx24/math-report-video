from manim import *

class RepresentImageAsMatrix(Scene):
    def construct(self):
        title = Tex("Image Representation")

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        self.wait(3)

        vector_image_title = Tex("Vector Image")

        self.play(Write(vector_image_title))
        self.play(vector_image_title.animate.align_on_border(UP))
        self.wait(3)

        line, circle, square = Line(RIGHT + UP, LEFT + DOWN), Circle(color=RED, fill_opacity=0.3), Square(color=BLUE, fill_opacity=0.3)
        
        circle.shift(2 * LEFT)
        square.shift(    LEFT)
        
        self.play(Create(line))
        self.wait(3)
        self.play(Create(circle))
        self.wait(3)
        self.play(Create(square))
        self.wait(3)
        self.play(FadeOut(line), FadeOut(circle), FadeOut(square), FadeOut(vector_image_title))
        self.wait(5)


        raster_image_title           = Tex("Raster Image")
        image_matrix                 = MathTex(r"I_{m\times n} = \begin{bmatrix} \vec{i}_{11} & \vec{i}_{12} & \hdots & \vec{i}_{1n} \\ \vec{i}_21 & \vec{i}_{22} & \hdots & \vec{i}_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \vec{i}_{m1} & \vec{i}_{m2} & \hdots & \vec{i}_{mn} \end{bmatrix}") 
        vector_belong_to_color_space = MathTex(r"\vec{i}_{ij} \in C")
        c_is_color_space_text        = Tex("C is a color space")

        vector_belong_to_color_space.next_to(image_matrix, DOWN)
        c_is_color_space_text.next_to(vector_belong_to_color_space, DOWN)

        self.play(Write(raster_image_title))
        self.play(raster_image_title.animate.align_on_border(UP))
        self.wait(3)
        self.play(Write(image_matrix))
        self.wait(3)
        self.play(Write(vector_belong_to_color_space))
        self.play(Write(c_is_color_space_text))
        self.wait(3)
        self.play(FadeOut(raster_image_title), FadeOut(image_matrix), FadeOut(vector_belong_to_color_space), FadeOut(c_is_color_space_text))
        self.wait(1)

        rgb_title                                                 = Tex("RGB")
        cmyk_title                                                = Tex("CMYK")
        rgb_vector                                                = MathTex(r"\vec{i} = \begin{bmatrix} R \\ G \\ B \end{bmatrix}")
        cmyk_vector                                               = MathTex(r"\vec{i} = \begin{bmatrix} C \\ M \\ Y \\ K \end{bmatrix}")
        red_circle, green_circle, blue_circle                     = Circle(1, fill_opacity=0.6), Circle(1, fill_color=GREEN, fill_opacity=0.6), Circle(1, fill_color=BLUE, fill_opacity=0.6)
        cyan_circle, magenta_circle, yellow_circle, black_circle  = Circle(1, fill_opacity=0.6, fill_color=rgb_to_color((1, 1, 0))), Circle(1, fill_opacity=0.6, fill_color=rgb_to_color((1, 0, 1))), Circle(1, fill_opacity=0.6, fill_color=YELLOW), Circle(1, fill_opacity=0.6, fill_color=BLACK)

        rgb_title.shift(3 * UP + 4 * LEFT)
        cmyk_title.shift(3 * UP + 4 * RIGHT)

        rgb_vector.next_to(rgb_title, DOWN)
        cmyk_vector.next_to(cmyk_title, DOWN)
        
        red_circle.next_to(rgb_vector, DOWN)
        green_circle.next_to(rgb_vector, DOWN).shift(DOWN + 0.8 * LEFT)
        blue_circle.next_to(rgb_vector, DOWN).shift(DOWN + 0.8 * RIGHT)

        cyan_circle.next_to(cmyk_vector, DOWN)
        magenta_circle.next_to(cmyk_vector, DOWN).shift(0.5 * DOWN + 0.5 * LEFT)
        yellow_circle.next_to(cmyk_vector, DOWN).shift(0.5 * DOWN + 0.5 * RIGHT)
        black_circle.next_to(cmyk_vector, DOWN).shift(DOWN)

        self.play(Write(rgb_title))
        self.wait(1)
        self.play(Write(rgb_vector))
        self.wait(1)
        self.play(Create(red_circle), Create(green_circle), Create(blue_circle))
        self.wait(5)
        self.play(Write(cmyk_title))
        self.wait(3) 
        self.play(Write(cmyk_vector))
        self.wait(3)
        self.play(Create(cyan_circle), Create(magenta_circle), Create(yellow_circle), Create(black_circle))
        self.wait(5)
        self.play(FadeOut(rgb_title), FadeOut(rgb_vector), FadeOut(red_circle), FadeOut(green_circle), FadeOut(blue_circle), \
                FadeOut(cmyk_title), FadeOut(cmyk_vector), FadeOut(cyan_circle), FadeOut(magenta_circle), FadeOut(yellow_circle), FadeOut(black_circle))
        self.wait(1)
