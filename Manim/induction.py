"""
Latex equations:
Prove que:    
    \[\left(1+2+3+...+n\right)^2 = 1^3+2^3+3^3+...+n^3,~\forall n \in \mathbb{N}\]
    
    Demonstração por indução:
    
    Passo básico:
    
    n=1:
    \[1^2=1=1^3\]
    
    n=2:
    
    \[\left(1+2\right)^2=3^2=9=1+8=1^3+2^3\]
    
    n=3:
    \[\left(1+2+3\right)^2=6^2=36=1+8+27=1^3+2^3+3^3\]
    
    Passo indutivo:
    
    Hipótese de indução: 
    \[\left(\sum_{i=1}^{n} i\right)^2=\sum_{i=1}^{n} i^3\]
    
    Tese: 
    \[\left(\sum_{i=1}^{n+1} i\right)^2=\sum_{i=1}^{n+1} i^3\]
    
    \[\left(\sum_{i=1}^{n+1} i\right)^2=\left(\sum_{i=1}^n i + n+1\right)^2=\]
    
    \[=\left(\sum_{i=1}^n i\right)^2+2\left(\sum_{i=1}^n i\right)\times\left(n+1\right)+\left(n+1\right)^2=\]
    
    \[=\sum_{i=1}^n i^3 + 2\times\dfrac{n}{2}\times\left(n+1\right)\times\left(n+1\right) + \left(n+1\right)^2=\]
    
    \[=\sum_{i=1}^n i^3 + {n}\times\left(n+1\right)^2 + \left(n+1\right)^2=\]
    
    \[=\sum_{i=1}^n i^3 + \left(n+1\right)^2\times\left(n+1\right)=\]
    
    \[=\sum_{i=1}^n i^3 + \left(n+1\right)^3=\]
    
    \[=1^3+2^3+...+n^3+\left(n+1\right)^3=\]
    
    \[=\sum_{i=1}^{n+1} i^3\]
"""

from manim import *

class Induction(Scene):
    def construct(self):
        text = Text("Provar que:", font_size=80)
        equation = MathTex(r"\left(1+2+3+...+n\right)^2 = 1^3+2^3+3^3+...+n^3,~\forall n \in \mathbb{N}", font_size=40) 
        self.play(Create(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)
        self.play(Create(equation))
        self.wait(3)
        self.play(FadeOut(equation))
        self.wait(1)
        
        text1 = Text("Demonstração por indução:", font_size=60)
        self.play(Create(text1))

        passoBasico = Text("passo básico:")
        self.play(Transform(text1, passoBasico))
        self.wait(1)
        self.play(FadeOut(passoBasico))
        
        text2 = Text(r"n=1:")
        self.play(FadeTransform(text1, text2))
        self.wait(1)
        tex = MathTex(r"1^2=1=1^3")
        self.play(FadeTransform(text2,tex))
        self.wait(1)
        self.play(FadeOut(tex))

        text3 = Text(r"n=2:")
        self.play(Create(text3))
        self.wait(1)
        tex1 = MathTex(r"\left(1+2\right)^2=3^2=9=1+8=1^3+2^3")
        self.play(FadeTransform(text3,tex1))
        self.wait(3)
        self.play(FadeOut(tex1))

        text4 = Text(r"n=3:")
        self.play(Create(text4))
        self.wait(1)
        tex4 = MathTex(r"\left(1+2+3\right)^2=6^2=36=1+8+27=1^3+2^3+3^3")
        self.play(FadeTransform(text4,tex4))
        self.wait(3)
        
        text5 = Text("Passo indutivo:", font_size=60)
        self.play(FadeTransform(tex4, text5))
        self.wait(1)
        self.play(FadeOut(text5))
        text6 = Text("Hipótese:", font_size=60)
        self.play(Create(text6))
        self.wait(1)

        hip = MathTex(r"\left(\sum_{i=1}^{n} i\right)^2=\sum_{i=1}^{n} i^3")
        self.play(FadeTransform(text6, hip))
        self.wait(2)
        self.play(FadeOut(hip))

        tese = Text("Tese:", font_size=60)
        self.play(Create(tese))
        self.wait(1)
        teseTex = MathTex(r"\left(\sum_{i=1}^{n+1} i\right)^2=\sum_{i=1}^{n+1} i^3")
        self.play(FadeTransform(tese, teseTex))
        self.wait(2)
        self.play(FadeOut(teseTex))

        step1 = MathTex(r"\left(\sum_{i=1}^{n+1} i\right)^2")
        self.play(FadeTransform(teseTex, step1))
        self.wait(1)

        step2 = MathTex(r"=\left(\sum_{i=1}^n i + n+1\right)^2")
        self.play(FadeTransform(step1,step2))
        self.wait(2)

        step3 = MathTex(r"=\left(\sum_{i=1}^n i\right)^2+2\left(\sum_{i=1}^n i\right)\times\left(n+1\right)+\left(n+1\right)^2")
        self.play(FadeTransform(step2,step3))
        self.wait(2)

        step4 = MathTex(r"=\sum_{i=1}^n i^3 + 2\times\dfrac{n}{2}\times\left(n+1\right)\times\left(n+1\right) + \left(n+1\right)^2")
        self.play(FadeTransform(step3,step4))
        self.wait(2)

        step5 = MathTex(r"=\sum_{i=1}^n i^3 + {n}\times\left(n+1\right)^2 + \left(n+1\right)^2")
        self.play(FadeTransform(step4,step5))
        self.wait(2)

        step6 = MathTex(r"=\sum_{i=1}^n i^3 + \left(n+1\right)^2\times\left(n+1\right)")
        self.play(FadeTransform(step5,step6))
        self.wait(2)

        step7 = MathTex(r"=\sum_{i=1}^n i^3 + \left(n+1\right)^3")
        self.play(FadeTransform(step6,step7))
        self.wait(2)

        step8 = MathTex(r"=1^3+2^3+...+n^3+\left(n+1\right)^3")
        self.play(FadeTransform(step7,step8))
        self.wait(2)

        step9 = MathTex(r"=\sum_{i=1}^{n+1} i^3")
        self.play(FadeTransform(step8,step9))
        self.wait(2)
        self.play(FadeOut(step9))

        cqp = Text("Como queriamos provar.", font_size=30)
        self.play(Create(cqp))
        self.wait(1)