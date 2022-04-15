from manimlib import *

class QuadraticEquation(Scene):
    def construct(self):
        lines = VGroup(
            Tex("x^2-x-6=0"),
            Tex("x=\\dfrac{1\\pm\\sqrt{(-1)^2-4\\times 1\\times (-6)}}{2\\times 1}"),
            Tex("x=\\dfrac{1\\pm5}{2}"),
            Tex("x=3\\lor x=-2")
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2],
            path_arc=145 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(lines[2].copy(), lines[3]),
            **play_kw
        )
        self.wait()

class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(circle))
        self.wait()