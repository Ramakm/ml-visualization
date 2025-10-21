#!/usr/bin/env python3
"""
PCA Visualization - Generated Manim Animation
"""

from manim import *
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs


class VarianceExplanation(ThreeDScene):
    """Scene: variance_explanation"""

    def construct(self):
        # Set up 3D scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)


        # Generate sample data for PCA demonstration
        rng = np.random.RandomState(42)
        n_samples = 50

        # Create correlated 3D data
        mean = [0, 0, 0]
        cov = [[2, 1.5, 0.5], [1.5, 1, 0.3], [0.5, 0.3, 0.5]]
        self.data_3d = rng.multivariate_normal(mean, cov, n_samples)

        # Perform PCA
        self.pca = PCA(n_components=3)
        self.pca.fit(self.data_3d)
        self.components = self.pca.components_
        self.explained_variance = self.pca.explained_variance_


        # variance_ellipse
        variance_ellipse = Ellipse(width=4.0, height=2.0)
        variance_ellipse.set_fill(ORANGE, opacity=0.3)
        variance_ellipse.set_stroke(ORANGE, width=2)
        variance_ellipse.rotate(30 * DEGREES)
        

        # Animation sequence
        animations = []
        
        self.wait(0.5)
        self.play(
            FadeIn(variance_ellipse),
            run_time=1.0
        )

        self.wait(2.0)
        self.play(
            FadeIn(variance_ellipse),
            run_time=2.0
        )


        # Hold for narration
        self.wait(10.0)


class PcaTransformation(ThreeDScene):
    """Scene: pca_transformation"""

    def construct(self):
        # Set up 3D scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)


        # Generate sample data for PCA demonstration
        rng = np.random.RandomState(42)
        n_samples = 50

        # Create correlated 3D data
        mean = [0, 0, 0]
        cov = [[2, 1.5, 0.5], [1.5, 1, 0.3], [0.5, 0.3, 0.5]]
        self.data_3d = rng.multivariate_normal(mean, cov, n_samples)

        # Perform PCA
        self.pca = PCA(n_components=3)
        self.pca.fit(self.data_3d)
        self.components = self.pca.components_
        self.explained_variance = self.pca.explained_variance_


        # pc1_arrow
        pc1_arrow = Arrow3D(
            start=ORIGIN,
            end=[6.00, 4.50, 1.50],
            color=BLUE,
            thickness=0.05
        )
        

        # pc2_arrow
        pc2_arrow = Arrow3D(
            start=ORIGIN,
            end=[-2.00, 2.00, 0.40],
            color=RED,
            thickness=0.04
        )
        

        # Animation sequence
        animations = []
        
        self.wait(1.0)
        self.play(
            GrowArrow(pc1_arrow),
            run_time=1.5
        )

        self.wait(2.5)
        self.play(
            GrowArrow(pc2_arrow),
            run_time=1.5
        )


        # Camera movements
        

        self.move_camera(
            phi=1.0471966666666666,
            theta=0.7853975,
            distance=5.196152422706632,
            run_time=4.0
        )
        

        # Hold for narration
        self.wait(12.0)


class Comparison(ThreeDScene):
    """Scene: comparison"""

    def construct(self):
        # Set up 3D scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)


        # Generate sample data for PCA demonstration
        rng = np.random.RandomState(42)
        n_samples = 50

        # Create correlated 3D data
        mean = [0, 0, 0]
        cov = [[2, 1.5, 0.5], [1.5, 1, 0.3], [0.5, 0.3, 0.5]]
        self.data_3d = rng.multivariate_normal(mean, cov, n_samples)

        # Perform PCA
        self.pca = PCA(n_components=3)
        self.pca.fit(self.data_3d)
        self.components = self.pca.components_
        self.explained_variance = self.pca.explained_variance_


        # Animation sequence
        animations = []
        

        # Hold for narration
        self.wait(8.0)


if __name__ == "__main__":
    """Run the PCA visualization scenes."""
    import os
    
    # Scene classes to render
    scenes = ['VarianceExplanation', 'PcaTransformation', 'Comparison']
    
    print("Available scenes:")
    for i, scene in enumerate(scenes):
        print(f"{i+1}. {scene.__name__}")
    
    # Render all scenes or specific scene
    # Example: manim -pql pca_visualization.py DataIntroduction
