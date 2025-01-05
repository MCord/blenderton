from manim import *

config.pixel_height = 400
config.pixel_width = 800
config.frame_height = 6
config.frame_width = 20


class square(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        square = Square(side_length=5, color=BLUE)

        t = "width = 5"
        side_label_top = Tex(t, font_size=36, color=BLACK)
        side_label_bottom = Tex(t, font_size=36, color=BLACK)
        side_label_left = Tex(t, font_size=36, color=BLACK)
        side_label_right = Tex(t, font_size=36, color=BLACK)

        # Position the labels near each side
        side_label_top.next_to(square.get_top(), UP, buff=0.1)
        side_label_bottom.next_to(square.get_bottom(), DOWN, buff=0.1)
        side_label_left.next_to(square.get_left(), LEFT, buff=0.1)
        side_label_right.next_to(square.get_right(), RIGHT, buff=0.1)

        side_label_left.rotate(PI / 2)
        side_label_right.rotate(-PI / 2)

        # Add the square and labels to the scene
        self.play(
            Create(square),
            Write(side_label_top),
            Write(side_label_bottom),
            Write(side_label_left),
            Write(side_label_right),
        )

        self.wait(5)


class rectangle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rectangle = Rectangle(width=10, height=5, color=BLACK)

        w = "width = 10"
        h = "height = 5"
        side_label_top = Tex(w, font_size=36, color=RED)
        side_label_bottom = Tex(w, font_size=36, color=RED)
        side_label_left = Tex(h, font_size=36, color=BLUE)
        side_label_right = Tex(h, font_size=36, color=BLUE)

        # Position the labels near each side
        side_label_top.next_to(rectangle.get_top(), UP, buff=0.1)
        side_label_bottom.next_to(rectangle.get_bottom(), DOWN, buff=0.1)
        side_label_left.next_to(rectangle.get_left(), LEFT, buff=0.1)
        side_label_right.next_to(rectangle.get_right(), RIGHT, buff=0.1)

        side_label_left.rotate(PI / 2)
        side_label_right.rotate(-PI / 2)

        # Add the square and labels to the scene
        self.play(
            Create(rectangle),
            Write(side_label_top),
            Write(side_label_bottom),
            Write(side_label_left),
            Write(side_label_right),
        )

        self.wait(5)
