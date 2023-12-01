PROMPT1 = """

from manim import *

class BasicIndefiniteIntegral(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int x^2 \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for the integration rule
        explanation1 = Text("Using the power rule of integration:", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Demonstrating the power rule
        power_rule = MathTex(r"\int x^n \,dx = \frac{x^{n+1}}{n+1} + C")
        self.play(Write(power_rule))
        self.wait(2)

        # Performing the integration step
        solution1 = MathTex(r"= \frac{x^{2+1}}{3}")
        self.play(ReplacementTransform(problem.copy(), solution1))
        self.wait(1)

        # Explanation for simplifying the expression
        explanation2 = Text("Simplify the expression", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= \frac{1}{3}x^3 + C")
        self.play(ReplacementTransform(solution1, final_solution))
        self.wait(1)

        # Clear the scene
        self.clear()
        self.wait(1)

        # Conclude with the final solution
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT2 = """

from manim import *

class DefiniteIntegralExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int_0^4 2x \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for setting up the integral
        explanation1 = Text("Evaluate the integral from 0 to 4", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Performing the integration
        integration_step = MathTex(r"= [x^2]_0^4")
        self.play(ReplacementTransform(problem.copy(), integration_step))
        self.wait(1)

        # Explanation for evaluating the integral
        explanation2 = Text("Evaluate the expression at the upper and lower bounds", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= 4^2 - 0^2", r"= 16")
        self.play(ReplacementTransform(integration_step, final_solution))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT3 = """

from manim import *

class IntegrationByPartsExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int x e^x \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for integration by parts
        explanation1 = Text("Apply integration by parts: \n"
                            "Integrate udv = uv - ∫vdu", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Choosing u and dv
        uv_selection = MathTex(r"u = x, \quad dv = e^x dx")
        self.play(Write(uv_selection))
        self.wait(2)

        # Performing the integration step
        integration_step = MathTex(r"= x e^x - \int e^x \,dx")
        self.play(ReplacementTransform(problem.copy(), integration_step))
        self.wait(1)

        # Explanation for further integration
        explanation2 = Text("Integrate the remaining integral", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= x e^x - e^x + C")
        self.play(ReplacementTransform(integration_step, final_solution))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT4 = """

from manim import *

class TrigIntegrationExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int \sin(x) \cos(x) \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for using a trigonometric identity
        explanation1 = Text("Use trigonometric identities", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Trig identity step
        trig_step = MathTex(r"\int \frac{1}{2} \sin(2x) \,dx")
        self.play(ReplacementTransform(problem.copy(), trig_step))
        self.wait(1)

        # Explanation for integration
        explanation2 = Text("Integrate using the power rule", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= -\frac{1}{4}\cos(2x) + C")
        self.play(ReplacementTransform(trig_step, final_solution))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT5 = """

from manim import *

class ImproperIntegralExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int_1^\infty \frac{1}{x^2} \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for setting up the improper integral
        explanation1 = Text("Convert to a limit problem for improper integral", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Setting up the limit
        limit_setup = MathTex(r"= \lim_{b \to \infty} \int_1^b \frac{1}{x^2} \,dx")
        self.play(ReplacementTransform(problem.copy(), limit_setup))
        self.wait(1)

        # Integration step
        integration_step = MathTex(r"= \lim_{b \to \infty} [-\frac{1}{x}]_1^b")
        self.play(ReplacementTransform(limit_setup, integration_step))
        self.wait(1)

        # Explanation for evaluating the limit
        explanation2 = Text("Evaluate the limit as b approaches infinity", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= 1")
        self.play(ReplacementTransform(integration_step, final_solution))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT6 = """

from manim import *

class DoubleIntegralExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int_{0}^{1} \int_{0}^{2} xy \,dx\,dy")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for inner integral
        explanation1 = Text("First, integrate with respect to x", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Inner integral step
        inner_integral = MathTex(r"= \int_{0}^{1} [\frac{1}{2}x^2y]_{0}^{2} \,dy")
        self.play(ReplacementTransform(problem.copy(), inner_integral))
        self.wait(1)

        # Explanation for outer integral
        explanation2 = Text("Next, integrate the result with respect to y", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Outer integral step and final solution
        final_solution = MathTex(r"= \int_{0}^{1} 2y \,dy", r"= [y^2]_{0}^{1}", r"= 1")
        self.play(ReplacementTransform(inner_integral, final_solution))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_solution))
        self.wait(1)
"""

PROMPT7 = """from manim import *

class PartialDifferentialEquationExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\frac{\partial u}{\partial x} + \frac{\partial u}{\partial y} = 0")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for approach
        explanation1 = Text("This is a first-order linear PDE.", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # General solution explanation
        explanation2 = Text("The general solution is of the form u(x, y) = f(x - y)", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Displaying the general solution
        general_solution = MathTex(r"u(x, y) = f(x - y)")
        self.play(ReplacementTransform(problem, general_solution))
        self.wait(1)

        # Explanation for specific solution
        explanation3 = Text("Specific solutions depend on boundary conditions or additional information.", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation3))
        self.wait(2)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(general_solution))
        self.wait(1)
"""

PROMPT8 = """

from manim import *

class SecondOrderODEExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"y'' + 2y' + y = 0")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for characteristic equation
        explanation1 = Text("Form the characteristic equation", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Characteristic equation step
        char_eq = MathTex(r"r^2 + 2r + 1 = 0")
        self.play(ReplacementTransform(problem.copy(), char_eq))
        self.wait(1)

        # Explanation for solving the characteristic equation
        explanation2 = Text("Solve for r", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Solving the characteristic equation
        roots = MathTex(r"r = -1")
        self.play(ReplacementTransform(char_eq, roots))
        self.wait(1)

        # General solution
        general_solution = MathTex(r"y = C_1 e^{-x} + C_2 x e^{-x}")
        self.play(Write(general_solution))
        self.wait(1)

        # Explanation for general solution
        explanation3 = Text("General solution of the ODE", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation3))
        self.wait(2)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(general_solution))
        self.wait(1)
"""

PROMPT9 = """

from manim import *

class TripleIntegralCylindricalExample(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int_{0}^{2\pi} \int_{0}^{1} \int_{0}^{r} r dz\,dr\,d\theta")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for inner integral
        explanation1 = Text("Integrate with respect to z first", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Inner integral step
        inner_integral = MathTex(r"= \int_{0}^{2\pi} \int_{0}^{1} [rz]_{0}^{r} dr\,d\theta")
        self.play(ReplacementTransform(problem.copy(), inner_integral))
        self.wait(1)

        # Middle integral step
        middle_integral = MathTex(r"= \int_{0}^{2\pi} \int_{0}^{1} r^2 dr\,d\theta")
        self.play(ReplacementTransform(inner_integral, middle_integral))
        self.wait(1)

        # Explanation for middle integral
        explanation2 = Text("Now integrate with respect to r", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Final integral step
        final_integral = MathTex(r"= \int_{0}^{2\pi} [\frac{1}{3}r^3]_{0}^{1} d\theta")
        self.play(ReplacementTransform(middle_integral, final_integral))
        self.wait(1)

        # Explanation for final integral
        explanation3 = Text("Finally, integrate with respect to \(\theta\)", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation3))
        self.wait(2)

        # Final solution
        final_solution = MathTex(r"= \int_{0}^{2\pi
"""
