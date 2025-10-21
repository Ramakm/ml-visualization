#!/usr/bin/env python3
"""
PCA Visualization - Generated Manim Animation
"""

from manim import *
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs


class DataIntroduction(ThreeDScene):
    """Scene: data_introduction"""

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


        # Data point data_point_0
        data_point_0 = Sphere(radius=0.1).move_to([-0.20, -0.28, -0.18])
        data_point_0.set_color(GRAY)
        data_point_0.set_opacity(0.8)
        

        # Data point data_point_1
        data_point_1 = Sphere(radius=0.1).move_to([0.98, 0.59, -0.49])
        data_point_1.set_color(GRAY)
        data_point_1.set_opacity(0.8)
        

        # Data point data_point_2
        data_point_2 = Sphere(radius=0.1).move_to([0.47, 0.11, 0.03])
        data_point_2.set_color(GRAY)
        data_point_2.set_opacity(0.8)
        

        # Data point data_point_3
        data_point_3 = Sphere(radius=0.1).move_to([0.16, 0.30, 0.81])
        data_point_3.set_color(GRAY)
        data_point_3.set_opacity(0.8)
        

        # Data point data_point_4
        data_point_4 = Sphere(radius=0.1).move_to([0.92, 0.73, -0.02])
        data_point_4.set_color(GRAY)
        data_point_4.set_opacity(0.8)
        

        # Data point data_point_5
        data_point_5 = Sphere(radius=0.1).move_to([-1.42, -0.80, 0.20])
        data_point_5.set_color(GRAY)
        data_point_5.set_opacity(0.8)
        

        # Data point data_point_6
        data_point_6 = Sphere(radius=0.1).move_to([0.06, -0.04, 0.33])
        data_point_6.set_color(GRAY)
        data_point_6.set_opacity(0.8)
        

        # Data point data_point_7
        data_point_7 = Sphere(radius=0.1).move_to([-2.03, -1.67, -0.65])
        data_point_7.set_color(GRAY)
        data_point_7.set_opacity(0.8)
        

        # Data point data_point_8
        data_point_8 = Sphere(radius=0.1).move_to([1.22, 0.66, 0.73])
        data_point_8.set_color(GRAY)
        data_point_8.set_opacity(0.8)
        

        # Data point data_point_9
        data_point_9 = Sphere(radius=0.1).move_to([0.35, 0.87, -0.39])
        data_point_9.set_color(GRAY)
        data_point_9.set_opacity(0.8)
        

        # Animation sequence
        animations = []
        
        self.play(
            FadeIn(data_point_0),
            run_time=0.5
        )

        self.wait(0.05)
        self.play(
            FadeIn(data_point_1),
            run_time=0.5
        )

        self.wait(0.1)
        self.play(
            FadeIn(data_point_2),
            run_time=0.5
        )

        self.wait(0.15000000000000002)
        self.play(
            FadeIn(data_point_3),
            run_time=0.5
        )

        self.wait(0.2)
        self.play(
            FadeIn(data_point_4),
            run_time=0.5
        )

        self.wait(0.25)
        self.play(
            FadeIn(data_point_5),
            run_time=0.5
        )

        self.wait(0.30000000000000004)
        self.play(
            FadeIn(data_point_6),
            run_time=0.5
        )

        self.wait(0.35000000000000003)
        self.play(
            FadeIn(data_point_7),
            run_time=0.5
        )

        self.wait(0.4)
        self.play(
            FadeIn(data_point_8),
            run_time=0.5
        )

        self.wait(0.45)
        self.play(
            FadeIn(data_point_9),
            run_time=0.5
        )


        # Camera movements
        

        self.move_camera(
            phi=1.0471966666666666,
            theta=0.7853975,
            distance=5.196152422706632,
            run_time=3.0
        )
        

        # Hold for narration
        self.wait(8.0)


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


        # Data point data_point_0
        data_point_0 = Sphere(radius=0.1).move_to([-0.20, -0.28, -0.18])
        data_point_0.set_color(GRAY)
        data_point_0.set_opacity(0.8)
        

        # Data point data_point_1
        data_point_1 = Sphere(radius=0.1).move_to([0.98, 0.59, -0.49])
        data_point_1.set_color(GRAY)
        data_point_1.set_opacity(0.8)
        

        # Data point data_point_2
        data_point_2 = Sphere(radius=0.1).move_to([0.47, 0.11, 0.03])
        data_point_2.set_color(GRAY)
        data_point_2.set_opacity(0.8)
        

        # Data point data_point_3
        data_point_3 = Sphere(radius=0.1).move_to([0.16, 0.30, 0.81])
        data_point_3.set_color(GRAY)
        data_point_3.set_opacity(0.8)
        

        # Data point data_point_4
        data_point_4 = Sphere(radius=0.1).move_to([0.92, 0.73, -0.02])
        data_point_4.set_color(GRAY)
        data_point_4.set_opacity(0.8)
        

        # Data point data_point_5
        data_point_5 = Sphere(radius=0.1).move_to([-1.42, -0.80, 0.20])
        data_point_5.set_color(GRAY)
        data_point_5.set_opacity(0.8)
        

        # Data point data_point_6
        data_point_6 = Sphere(radius=0.1).move_to([0.06, -0.04, 0.33])
        data_point_6.set_color(GRAY)
        data_point_6.set_opacity(0.8)
        

        # Data point data_point_7
        data_point_7 = Sphere(radius=0.1).move_to([-2.03, -1.67, -0.65])
        data_point_7.set_color(GRAY)
        data_point_7.set_opacity(0.8)
        

        # Data point data_point_8
        data_point_8 = Sphere(radius=0.1).move_to([1.22, 0.66, 0.73])
        data_point_8.set_color(GRAY)
        data_point_8.set_opacity(0.8)
        

        # Data point data_point_9
        data_point_9 = Sphere(radius=0.1).move_to([0.35, 0.87, -0.39])
        data_point_9.set_color(GRAY)
        data_point_9.set_opacity(0.8)
        

        # Animation sequence
        animations = []
        
        self.play(
            FadeIn(data_point_0),
            run_time=0.5
        )

        self.wait(0.05)
        self.play(
            FadeIn(data_point_1),
            run_time=0.5
        )

        self.wait(0.1)
        self.play(
            FadeIn(data_point_2),
            run_time=0.5
        )

        self.wait(0.15000000000000002)
        self.play(
            FadeIn(data_point_3),
            run_time=0.5
        )

        self.wait(0.2)
        self.play(
            FadeIn(data_point_4),
            run_time=0.5
        )

        self.wait(0.25)
        self.play(
            FadeIn(data_point_5),
            run_time=0.5
        )

        self.wait(0.30000000000000004)
        self.play(
            FadeIn(data_point_6),
            run_time=0.5
        )

        self.wait(0.35000000000000003)
        self.play(
            FadeIn(data_point_7),
            run_time=0.5
        )

        self.wait(0.4)
        self.play(
            FadeIn(data_point_8),
            run_time=0.5
        )

        self.wait(0.45)
        self.play(
            FadeIn(data_point_9),
            run_time=0.5
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
        

        # projection_plane
        projection_plane = Rectangle(width=6, height=4)
        projection_plane.set_fill(YELLOW, opacity=0.2)
        projection_plane.set_stroke(YELLOW, width=2)
        projection_plane.move_to([0, 0, -1])
        

        # projection_line_0 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 0:
            point_3d = self.data_3d[0]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_0 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_0.set_opacity(0.5)
        

        # projection_line_1 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 1:
            point_3d = self.data_3d[1]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_1 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_1.set_opacity(0.5)
        

        # projection_line_2 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 2:
            point_3d = self.data_3d[2]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_2 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_2.set_opacity(0.5)
        

        # projection_line_3 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 3:
            point_3d = self.data_3d[3]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_3 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_3.set_opacity(0.5)
        

        # projection_line_4 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 4:
            point_3d = self.data_3d[4]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_4 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_4.set_opacity(0.5)
        

        # projection_line_5 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 5:
            point_3d = self.data_3d[5]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_5 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_5.set_opacity(0.5)
        

        # projection_line_6 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 6:
            point_3d = self.data_3d[6]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_6 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_6.set_opacity(0.5)
        

        # Animation sequence
        animations = []
        
        self.play(
            FadeIn(projection_plane),
            run_time=1.0
        )

        self.wait(1.0)
        self.play(
            GrowArrow(pc1_arrow),
            FadeIn(projection_line_0),
            run_time=0.5
        )

        self.wait(1.1)
        self.play(
            FadeIn(projection_line_1),
            run_time=0.5
        )

        self.wait(1.2)
        self.play(
            FadeIn(projection_line_2),
            run_time=0.5
        )

        self.wait(1.3)
        self.play(
            FadeIn(projection_line_3),
            run_time=0.5
        )

        self.wait(1.4)
        self.play(
            FadeIn(projection_line_4),
            run_time=0.5
        )

        self.wait(1.5)
        self.play(
            FadeIn(projection_line_5),
            run_time=0.5
        )

        self.wait(1.6)
        self.play(
            FadeIn(projection_line_6),
            run_time=0.5
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


class DimensionalityReduction(ThreeDScene):
    """Scene: dimensionality_reduction"""

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


        # projection_plane
        projection_plane = Rectangle(width=6, height=4)
        projection_plane.set_fill(YELLOW, opacity=0.2)
        projection_plane.set_stroke(YELLOW, width=2)
        projection_plane.move_to([0, 0, -1])
        

        # projection_line_0 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 0:
            point_3d = self.data_3d[0]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_0 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_0.set_opacity(0.5)
        

        # projection_line_1 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 1:
            point_3d = self.data_3d[1]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_1 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_1.set_opacity(0.5)
        

        # projection_line_2 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 2:
            point_3d = self.data_3d[2]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_2 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_2.set_opacity(0.5)
        

        # projection_line_3 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 3:
            point_3d = self.data_3d[3]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_3 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_3.set_opacity(0.5)
        

        # projection_line_4 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 4:
            point_3d = self.data_3d[4]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_4 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_4.set_opacity(0.5)
        

        # projection_line_5 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 5:
            point_3d = self.data_3d[5]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_5 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_5.set_opacity(0.5)
        

        # projection_line_6 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 6:
            point_3d = self.data_3d[6]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_6 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_6.set_opacity(0.5)
        

        # projection_line_7 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 7:
            point_3d = self.data_3d[7]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_7 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_7.set_opacity(0.5)
        

        # projection_line_8 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 8:
            point_3d = self.data_3d[8]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_8 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_8.set_opacity(0.5)
        

        # Animation sequence
        animations = []
        
        self.play(
            FadeIn(projection_plane),
            run_time=1.0
        )

        self.wait(1.0)
        self.play(
            FadeIn(projection_line_0),
            run_time=0.5
        )

        self.wait(1.1)
        self.play(
            FadeIn(projection_line_1),
            run_time=0.5
        )

        self.wait(1.2)
        self.play(
            FadeIn(projection_line_2),
            run_time=0.5
        )

        self.wait(1.3)
        self.play(
            FadeIn(projection_line_3),
            run_time=0.5
        )

        self.wait(1.4)
        self.play(
            FadeIn(projection_line_4),
            run_time=0.5
        )

        self.wait(1.5)
        self.play(
            FadeIn(projection_line_5),
            run_time=0.5
        )

        self.wait(1.6)
        self.play(
            FadeIn(projection_line_6),
            run_time=0.5
        )

        self.wait(1.7000000000000002)
        self.play(
            FadeIn(projection_line_7),
            run_time=0.5
        )

        self.wait(1.8)
        self.play(
            FadeIn(projection_line_8),
            run_time=0.5
        )


        # Camera movements
        

        self.move_camera(
            phi=1.0471966666666666,
            theta=0.7853975,
            distance=5.385164807134504,
            run_time=3.0
        )
        

        # Hold for narration
        self.wait(10.0)


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
    scenes = ['DataIntroduction', 'VarianceExplanation', 'PcaTransformation', 'DimensionalityReduction', 'Comparison']
    
    print("Available scenes:")
    for i, scene in enumerate(scenes):
        print(f"{i+1}. {scene.__name__}")
    
    # Render all scenes or specific scene
    # Example: manim -pql pca_visualization.py DataIntroduction
