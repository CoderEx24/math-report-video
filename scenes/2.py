from manim import *

class ImageCompression(Scene):
    def construct(self):
        section_title = Tex("Image Compression")
        
        self.play(Write(section_title));   self.wait(3)
        self.play(FadeOut(section_title)); self.wait(1)

        lossless_compression_title = Tex("Lossless Compression")
        run_length_encoding        = Tex("Run Length Encoding")
        long_run_1                 = Tex("aaaaaaabbbbbbbbcccccc")
        long_run_2                 = Tex("abcd")
        compressed_run_1           = Tex("7a8b6c")
        compressed_run_2           = Tex("1a1b1c1d")
        huffman_coding_title       = Tex("Huffman Coding")
        reducible_video            = ImageMobject("assets/reducible_video.png") 

        lossless_compression_title.align_on_border(UP)
        run_length_encoding.next_to(lossless_compression_title, DOWN)
        huffman_coding_title.next_to(lossless_compression_title, DOWN)

        self.play(Write(lossless_compression_title));       self.wait(3)
        self.play(Write(run_length_encoding));              self.wait(1)
        self.play(Write(long_run_1));                       self.wait(1)
        self.play(Transform(long_run_1, compressed_run_1)); self.wait(3)
        self.play(FadeOut(long_run_1));                     self.wait(3)
        self.play(Write(long_run_2));                       self.wait(2)
        self.play(Transform(long_run_2, compressed_run_2)); self.wait(2)
        self.play(FadeOut(long_run_2), \
                FadeOut(run_length_encoding));              self.wait(2)
        self.play(Write(huffman_coding_title));             self.wait(2)
        self.play(FadeIn(reducible_video));                 self.wait(2)
        self.play(FadeOut(huffman_coding_title), \
                FadeOut(reducible_video));                  self.wait(2)
