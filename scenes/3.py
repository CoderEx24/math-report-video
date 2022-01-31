from manim import *

class Jpeg(Scene):
    def construct(self):
        jpeg_title = Tex("JPEG")

        self.play(Write(jpeg_title));   self.wait(2)
        self.play(FadeOut(jpeg_title)); self.wait(2)

        color_space_transform_title = Tex("Color Space Transformation")
        rgb_vector                  = MathTex(r"\vec{i}_{rgb} = \begin{bmatrix} R \\ G \\ B \end{bmatrix}")
        ycc_vector                  = MathTex(r"\vec{i}_{ycc} = \begin{bmatrix} Y \\ C_B \\ C_R \end{bmatrix}")
        y_text                      = Tex("$Y$ is luminance")
        cc_text                     = Tex("$C_B$ and $C_R$ are chrominance")

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


        chroma_subsampling_title = Tex("Chroma Subsampling")
        unsampled_squares        = ImageMobject("assets/unsampled.png")
        sampled_squares          = ImageMobject("assets/sampled.png")

        chroma_subsampling_title.align_on_border(UP)

        self.play(Write(chroma_subsampling_title)); self.wait(3)
        self.play(FadeIn(unsampled_squares));       self.wait(3)
        self.play(Transform(unsampled_squares, \
                sampled_squares));                  self.wait(3)
        self.play(FadeOut(chroma_subsampling_title), \
                FadeOut(unsampled_squares));        self.wait(3)
        
        y_matrix  = MathTex(r"Y_{m \times n} = \begin{bmatrix} y_{11} & y_{12} & \hdots & y_{1n} \\ y_{21} & y_{22} & \hdots & y_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ y_{m1} & y_{m2} & \hdots & y_{mn} \end{bmatrix}", font_size=27)
        cb_matrix = MathTex(r"C_{B_{m \times n}} = \begin{bmatrix} c_{b_{11}} & c_{b_{12}} & \hdots & c_{b_{1n}} \\ c_{b_{21}} & c_{b_{22}} & \hdots & c_{b_{2n}} \\ \vdots & \vdots & \ddots & \vdots \\ c_{b_{m1}} & c_{b_{m2}} & \hdots & c_{b_{mn}} \end{bmatrix}", font_size=27)
        cr_matrix = MathTex(r"C_{R_{m \times n}} = \begin{bmatrix} c_{r_{11}} & c_{r_{12}} & \hdots & c_{r_{1n}} \\ c_{r_{21}} & c_{r_{22}} & \hdots & c_{r_{2n}} \\ \vdots & \vdots & \ddots & \vdots \\ c_{r_{m1}} & c_{r_{m2}} & \hdots & c_{r_{mn}} \end{bmatrix}", font_size=27)
        y_block   = MathTex(r"B_{Y_{8 \times 8}} = \begin{bmatrix} b_{y_{11}} & b_{y_{12}} & \hdots & b_{y_{18}} \\ b_{y_{21}} & b_{y_{22}} & \hdots & b_{y_{28}} \\ \vdots & \vdots & \ddots & \vdots \\ b_{y_{81}} & b_{y_{82}} & \hdots & b_{y_{88}} \end{bmatrix}", font_size=27)
        cb_block  = MathTex(r"B_{C_{B_{8 \times 8}}} = \begin{bmatrix} b_{c_{b_{11}}} & b_{c_{b_{12}}} & \hdots & b_{c_{b_{18}}} \\ b_{c_{b_{21}}} & b_{c_{b_{22}}} & \hdots & b_{c_{b_{28}}} \\ \vdots & \vdots & \ddots & \vdots \\ b_{c_{b_{81}}} & b_{c_{b_{82}}} & \hdots & b_{c_{b_{88}}} \end{bmatrix}", font_size=27)
        cr_block  = MathTex(r"B_{C_{R_{8 \times 8}}} = \begin{bmatrix} b_{c_{r_{11}}} & b_{c_{r_{12}}} & \hdots & b_{c_{r_{18}}} \\ b_{c_{r_{21}}} & b_{c_{r_{22}}} & \hdots & b_{c_{r_{28}}} \\ \vdots & \vdots & \ddots & \vdots \\ b_{c_{r_{81}}} & b_{c_{r_{82}}} & \hdots & b_{c_{r_{88}}} \end{bmatrix}", font_size=27)
        
        y_matrix.align_on_border(LEFT)
        cb_matrix.next_to(y_matrix)
        cr_matrix.next_to(cb_matrix)
        y_block.align_on_border(LEFT)
        cb_block.next_to(y_block)
        cr_block.next_to(cb_block)

        self.play(Write(y_matrix), \
                Write(cb_matrix),  \
                Write(cr_matrix));                  self.wait(3)
        self.play(Transform(y_matrix, y_block), \
                Transform(cb_matrix, cb_block), \
                Transform(cr_matrix, cr_block));    self.wait(3)
        self.play(FadeOut(y_matrix), \
                FadeOut(cb_matrix),  \
                FadeOut(cr_matrix));                self.wait(0.1)

