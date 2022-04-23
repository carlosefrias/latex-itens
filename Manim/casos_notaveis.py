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
            color=WHITE
        ).set_fill(ORANGE, opacity=0.5)
        
        label = MathTex(r"a^2").move_to(quadrado_lado_a.get_center())

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
            color=WHITE
        ).set_fill(GREEN, opacity=0.5).move_to(2*RIGHT)
        label_b = MathTex(r"b^2").move_to(quadrado_lado_b.get_center())

        self.play(Create(quadrado_lado_b))
        self.wait()
        
        label.move_to(quadrado_lado_a.get_center())
        self.play(Create(label))
        self.wait()

        self.play(Create(label_b))
        self.wait()

        self.play(FadeOut(label))
        self.play(FadeOut(label_b))
        self.wait()

        quadrado_lado_a.generate_target()
        quadrado_lado_a.target.move_to([0,0,0])
        self.play(MoveToTarget(quadrado_lado_a))
        self.wait()

        quadrado_lado_b.generate_target()
        quadrado_lado_b.target.move_to([2,-2,0])
        self.play(MoveToTarget(quadrado_lado_b))
        self.wait()

        group = VGroup(quadrado_lado_a, quadrado_lado_b)
        
        poligono_aa_bb = Polygon(
            [-a/2, -a/2, 0],
            [a/2-b, -a/2, 0],
            [a/2-b, -a/2+b, 0],
            [a/2, -a/2+b, 0],
            [a/2, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        ).set_fill(GRAY, opacity=0.5)
        
        self.play(FadeTransform(group, poligono_aa_bb))
        self.wait()

        label_aa_bb = MathTex(r"a^2-b^2").move_to(poligono_aa_bb.get_center())
        self.play(Create(label_aa_bb))
        self.wait()

        self.play(FadeOut(label_aa_bb))

        rectangulo_a_a_menos_b = Polygon(
            [-a/2, -a/2, 0],
            [a/2-b, -a/2, 0],
            [a/2-b, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        ).set_fill(BLUE, opacity=0.5)

        rectangulo_b_a_menos_b = Polygon(
            [a/2-b, -a/2+b, 0],
            [a/2, -a/2+b, 0],
            [a/2, a/2, 0],
            [a/2-b, a/2, 0],
            color=WHITE
        ).set_fill(PINK, opacity=0.5)

        group2 = VGroup(rectangulo_a_a_menos_b, rectangulo_b_a_menos_b)
        self.play(ReplacementTransform(poligono_aa_bb, group2))
        self.wait()

        label1 = MathTex(r"a\left(a-b\right)").move_to(rectangulo_a_a_menos_b.get_center())
        label2 = MathTex(r"b\left(a-b\right)").move_to(rectangulo_b_a_menos_b.get_center())

        self.play(Create(label1))
        self.play(Create(label2))
        self.wait()

        self.play(Rotate(rectangulo_a_a_menos_b,
                angle=PI/2,
                about_point=rectangulo_a_a_menos_b.get_center()))
        self.wait()

        rectangulo_b_a_menos_b.generate_target()
        rectangulo_b_a_menos_b.target.move_to([3,0,0])
        self.play(MoveToTarget(rectangulo_b_a_menos_b))

        label2.generate_target()
        label2.target.move_to(rectangulo_b_a_menos_b.get_center())
        self.play(MoveToTarget(label2))

        self.play(FadeOut(label1))
        self.play(FadeOut(label2))
        self.wait()

        pol3 = Polygon(
            [-a/2, -a/2+b, 0],
            [a/2+b, -a/2+b, 0],
            [a/2+b, a/2, 0],
            [-a/2, a/2, 0],
            color=WHITE
        ).set_fill(GOLD, opacity=0.5).move_to([0,0,0])
        
        self.play(FadeTransform(group2, pol3))
        self.wait()

        label3 = MathTex(r"\left(a-b\right)\left(a+b\right)").move_to(pol3.get_center())

        self.play(Create(label3))
        self.wait(2)

        self.play(FadeOut(label3))
        self.play(FadeOut(pol3))
        self.wait()

        step1 = MathTex(r"a^2-b^2")
        self.play(Create(step1))
        self.wait(1)

        step2 = MathTex(r"a^2-ab+ba-b^2")
        self.play(ReplacementTransform(step1,step2))
        self.wait(2)

        step3 = MathTex(r"a\left(a-b\right) + b\left(a-b\right)")
        self.play(ReplacementTransform(step2,step3))
        self.wait(2)
        
        step4 = MathTex(r"\left(a-b\right)\left(a+b\right)")
        self.play(ReplacementTransform(step3,step4))
        self.wait(2)