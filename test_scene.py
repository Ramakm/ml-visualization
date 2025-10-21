#!/usr/bin/env python3
"""
Simple test scene to verify Manim code generation
"""

from manim import *


class SimpleTestScene(ThreeDScene):
    """Simple 3D scene with data points and arrows"""

    def construct(self):
        # Set up 3D scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Create some simple data points
        points = VGroup()
        for i in range(10):
            x = (i % 3 - 1) * 2
            y = (i % 4 - 1.5) * 1.5
            z = (i % 2 - 0.5) * 1
            point = Sphere(radius=0.1).move_to([x, y, z])
            point.set_color(BLUE)
            points.add(point)

        # Create principal component arrows
        pc1 = Arrow3D(
            start=ORIGIN,
            end=[2, 1.5, 0.5],
            color=RED,
            thickness=0.05
        )

        pc2 = Arrow3D(
            start=ORIGIN,
            end=[-1, 1, 0.2],
            color=GREEN,
            thickness=0.04
        )

        # Add title
        title = Text("PCA Visualization Demo", font_size=36)
        title.to_edge(UP)

        # Animate
        self.play(FadeIn(title))
        self.wait(0.5)
        
        self.play(*[FadeIn(point) for point in points], run_time=2)
        self.wait(0.5)
        
        self.play(GrowArrow(pc1))
        self.wait(0.5)
        
        self.play(GrowArrow(pc2))
        self.wait(1)
        
        # Rotate camera
        self.move_camera(phi=70 * DEGREES, theta=60 * DEGREES, run_time=2)
        self.wait(1)


if __name__ == "__main__":
    # Render with: manim -pql test_scene.py SimpleTestScene
    pass
