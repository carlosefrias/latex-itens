from manim import *

a = 6
b = 2

class DiferencaQuadrados(Scene):
    def construct(self):
        quadrado_lado_a = Polygon(
                [-a/2, -a/2, 0],
                [a/2, -a/2, 0],
                [a/2, a/2, 0],
                [-a/2, a/2, 0],
                color=WHITE)
        quadrado_lado_a.set_fill(ORANGE, opacity=0.5)
        centro = quadrado_lado_a.get_center()
        label = MathTex(r"a^2").move_to(centro)

        self.play(Create(quadrado_lado_a))
        self.wait()

        self.play(Create(label))
        self.wait()
        self.play(FadeOut(label))
        self.wait()
        
        self.play(MoveAlongPath(quadrado_lado_a, Line(LEFT, 3*LEFT)), rate_func=linear)

        quadrado_lado_b = Polygon(
                [-b/2, -b/2, 0],
                [b/2, -b/2, 0],
                [b/2, b/2, 0],
                [-b/2, b/2, 0],
                color=WHITE)

        quadrado_lado_b.set_fill(GREEN, opacity=0.5)
        quadrado_lado_b.move_to(2*RIGHT)
        centro_b = quadrado_lado_b.get_center()
        label_b = MathTex(r"b^2").move_to(centro_b)

        self.play(Create(quadrado_lado_b))
        self.wait()
        
        centro = quadrado_lado_a.get_center()
        label.move_to(centro)
        self.play(Create(label))
        self.wait()

        self.play(Create(label_b))
        self.wait()

        self.play(FadeOut(label))
        self.play(FadeOut(label_b))
        self.play(FadeOut(quadrado_lado_a))
        self.play(FadeOut(quadrado_lado_b))
        self.wait()

        group = VGroup(quadrado_lado_a, quadrado_lado_b)
        
        poligono_aa_bb = Polygon(
                [-a/2, -a/2, 0],
                [a/2-b, -a/2, 0],
                [a/2-b, -a/2+b, 0],
                [a/2, -a/2+b, 0],
                [a/2, a/2, 0],
                [-a/2, a/2, 0],
                color=WHITE)
        poligono_aa_bb.set_fill(GRAY, opacity=0.5)
        self.play(Transform(group, poligono_aa_bb))
        self.wait()

        centro_pol = poligono_aa_bb.get_center()
        label_aa_bb = MathTex(r"a^2-b^2")
        label_aa_bb.move_to(centro_pol)
        self.play(Create(label_aa_bb))
        self.wait()

        self.play(FadeOut(label_aa_bb))

        rectangulo_a_a_menos_b = Polygon(
            [-a/2, -a/2, 0],
            [a/2-b, -a/2, 0],
            [a/2-b, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        )
        rectangulo_a_a_menos_b.set_fill(BLUE, opacity=0.5)

        rectangulo_b_a_menos_b = Polygon(
            [a/2-b, -a/2+b, 0],
            [a/2, -a/2+b, 0],
            [a/2, a/2, 0],
            [a/2-b, a/2, 0],
            color=WHITE
        )
        rectangulo_b_a_menos_b.set_fill(PINK, opacity=0.5)

        group2 = VGroup(rectangulo_a_a_menos_b, rectangulo_b_a_menos_b)
        self.play(Transform(group, group2))
        self.wait()

        centro1 = rectangulo_a_a_menos_b.get_center()
        label1 = MathTex(r"a\left(a-b\right)")
        label1.move_to(centro1)

        centro2 = rectangulo_b_a_menos_b.get_center()
        label2 = MathTex(r"b\left(a-b\right)")
        label2.move_to(centro2)

        self.play(Create(label1))
        self.play(Create(label2))
        self.wait()

        pol1 = Polygon(
            [-a/2, -a/2+b, 0],
            [a/2, -a/2+b, 0],
            [a/2, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        )
        pol1.set_fill(BLUE, opacity=0.5)

        pol2 = Polygon(
            [a/2, -a/2+b, 0],
            [a/2+b, -a/2+b, 0],
            [a/2+b, a/2, 0],
            [a/2, a/2, 0],
            color=WHITE
        )
        pol2.set_fill(PINK, opacity=0.5)
        
        self.play(FadeOut(label1))
        self.play(FadeOut(label2))
        self.play(FadeOut(group))
        self.wait()

        group3 = VGroup(pol1, pol2)
        self.play(FadeTransform(group2, group3))
        self.wait()

        centro3 = pol1.get_center()
        centro4 = pol2.get_center()
        label1.move_to(centro3)
        label2.move_to(centro4)

        self.play(Create(label1))
        self.play(Create(label2))
        self.wait()

        self.play(FadeOut(label1))
        self.play(FadeOut(label2))
        self.wait()

        pol3 = Polygon(
            [-a/2, -a/2+b, 0],
            [a/2+b, -a/2+b, 0],
            [a/2+b, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        )
        pol3.set_fill(GOLD, opacity=0.5)
        self.play(FadeOut(group3))
        self.play(FadeTransform(group3, pol3))
        self.wait()

        label3 = MathTex(r"\left(a-b\right)\left(a+b\right)")
        label3.move_to(pol3.get_center())

        self.play(Create(label3))
        self.wait(2)

        self.play(FadeOut(label3))
        self.play(FadeOut(pol3))
        self.wait()


        step1 = MathTex(r"a^2-b^2")
        self.play(Create(step1))
        self.wait(1)

        step2 = MathTex(r"=a^2-ab+ba-b^2")
        self.play(FadeTransform(step1,step2))
        self.wait(2)

        step3 = MathTex(r"=a\left(a-b\right) + b\left(a-b\right)")
        self.play(FadeTransform(step2,step3))
        self.wait(2)
        
        step4 = MathTex(r"=\left(a-b\right)\left(a+b\right)")
        self.play(FadeTransform(step3,step4))
        self.wait(2)