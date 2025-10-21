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
        

        # Data point data_point_10
        data_point_10 = Sphere(radius=0.1).move_to([0.80, -0.65, -1.46])
        data_point_10.set_color(GRAY)
        data_point_10.set_opacity(0.8)
        

        # Data point data_point_11
        data_point_11 = Sphere(radius=0.1).move_to([-0.85, -1.33, 0.01])
        data_point_11.set_color(GRAY)
        data_point_11.set_opacity(0.8)
        

        # Data point data_point_12
        data_point_12 = Sphere(radius=0.1).move_to([0.93, -0.32, 0.72])
        data_point_12.set_color(GRAY)
        data_point_12.set_opacity(0.8)
        

        # Data point data_point_13
        data_point_13 = Sphere(radius=0.1).move_to([-1.40, -1.05, -0.81])
        data_point_13.set_color(GRAY)
        data_point_13.set_opacity(0.8)
        

        # Data point data_point_14
        data_point_14 = Sphere(radius=0.1).move_to([0.16, 0.77, 0.58])
        data_point_14.set_color(GRAY)
        data_point_14.set_opacity(0.8)
        

        # Data point data_point_15
        data_point_15 = Sphere(radius=0.1).move_to([0.49, 0.86, 0.61])
        data_point_15.set_color(GRAY)
        data_point_15.set_opacity(0.8)
        

        # Data point data_point_16
        data_point_16 = Sphere(radius=0.1).move_to([-0.88, -1.19, -0.78])
        data_point_16.set_color(GRAY)
        data_point_16.set_opacity(0.8)
        

        # Data point data_point_17
        data_point_17 = Sphere(radius=0.1).move_to([0.70, 0.29, 1.67])
        data_point_17.set_color(GRAY)
        data_point_17.set_opacity(0.8)
        

        # Data point data_point_18
        data_point_18 = Sphere(radius=0.1).move_to([-1.15, -1.68, -0.22])
        data_point_18.set_color(GRAY)
        data_point_18.set_opacity(0.8)
        

        # Data point data_point_19
        data_point_19 = Sphere(radius=0.1).move_to([1.99, 1.80, 1.46])
        data_point_19.set_color(GRAY)
        data_point_19.set_opacity(0.8)
        

        # Data point data_point_20
        data_point_20 = Sphere(radius=0.1).move_to([2.00, 1.32, 0.01])
        data_point_20.set_color(GRAY)
        data_point_20.set_opacity(0.8)
        

        # Data point data_point_21
        data_point_21 = Sphere(radius=0.1).move_to([-0.74, 0.24, -1.04])
        data_point_21.set_color(GRAY)
        data_point_21.set_opacity(0.8)
        

        # Data point data_point_22
        data_point_22 = Sphere(radius=0.1).move_to([0.05, 0.24, -0.13])
        data_point_22.set_color(GRAY)
        data_point_22.set_opacity(0.8)
        

        # Data point data_point_23
        data_point_23 = Sphere(radius=0.1).move_to([1.01, 1.17, 1.93])
        data_point_23.set_color(GRAY)
        data_point_23.set_opacity(0.8)
        

        # Data point data_point_24
        data_point_24 = Sphere(radius=0.1).move_to([0.87, 0.12, -0.05])
        data_point_24.set_color(GRAY)
        data_point_24.set_opacity(0.8)
        

        # Data point data_point_25
        data_point_25 = Sphere(radius=0.1).move_to([-1.16, -0.05, -0.70])
        data_point_25.set_color(GRAY)
        data_point_25.set_opacity(0.8)
        

        # Data point data_point_26
        data_point_26 = Sphere(radius=0.1).move_to([-0.10, 0.53, -0.36])
        data_point_26.set_color(GRAY)
        data_point_26.set_opacity(0.8)
        

        # Data point data_point_27
        data_point_27 = Sphere(radius=0.1).move_to([-0.41, -1.76, -1.12])
        data_point_27.set_color(GRAY)
        data_point_27.set_opacity(0.8)
        

        # Data point data_point_28
        data_point_28 = Sphere(radius=0.1).move_to([-0.79, -0.22, 0.43])
        data_point_28.set_color(GRAY)
        data_point_28.set_opacity(0.8)
        

        # Data point data_point_29
        data_point_29 = Sphere(radius=0.1).move_to([-0.03, 0.19, 0.13])
        data_point_29.set_color(GRAY)
        data_point_29.set_opacity(0.8)
        

        # Data point data_point_30
        data_point_30 = Sphere(radius=0.1).move_to([1.52, 1.78, 0.98])
        data_point_30.set_color(GRAY)
        data_point_30.set_opacity(0.8)
        

        # Data point data_point_31
        data_point_31 = Sphere(radius=0.1).move_to([-1.42, -0.27, -0.25])
        data_point_31.set_color(GRAY)
        data_point_31.set_opacity(0.8)
        

        # Data point data_point_32
        data_point_32 = Sphere(radius=0.1).move_to([1.72, 1.18, 1.92])
        data_point_32.set_color(GRAY)
        data_point_32.set_opacity(0.8)
        

        # Data point data_point_33
        data_point_33 = Sphere(radius=0.1).move_to([-0.50, 0.92, 0.10])
        data_point_33.set_color(GRAY)
        data_point_33.set_opacity(0.8)
        

        # Data point data_point_34
        data_point_34 = Sphere(radius=0.1).move_to([-0.72, -1.41, -0.59])
        data_point_34.set_color(GRAY)
        data_point_34.set_opacity(0.8)
        

        # Data point data_point_35
        data_point_35 = Sphere(radius=0.1).move_to([1.99, 2.05, 1.42])
        data_point_35.set_color(GRAY)
        data_point_35.set_opacity(0.8)
        

        # Data point data_point_36
        data_point_36 = Sphere(radius=0.1).move_to([-3.33, -1.76, -1.02])
        data_point_36.set_color(GRAY)
        data_point_36.set_opacity(0.8)
        

        # Data point data_point_37
        data_point_37 = Sphere(radius=0.1).move_to([-0.77, -1.04, -0.44])
        data_point_37.set_color(GRAY)
        data_point_37.set_opacity(0.8)
        

        # Data point data_point_38
        data_point_38 = Sphere(radius=0.1).move_to([2.41, 0.85, 0.64])
        data_point_38.set_color(GRAY)
        data_point_38.set_opacity(0.8)
        

        # Data point data_point_39
        data_point_39 = Sphere(radius=0.1).move_to([1.91, 0.98, 0.55])
        data_point_39.set_color(GRAY)
        data_point_39.set_opacity(0.8)
        

        # Data point data_point_40
        data_point_40 = Sphere(radius=0.1).move_to([0.14, -0.90, -0.01])
        data_point_40.set_color(GRAY)
        data_point_40.set_opacity(0.8)
        

        # Data point data_point_41
        data_point_41 = Sphere(radius=0.1).move_to([-1.69, -0.48, -0.60])
        data_point_41.set_color(GRAY)
        data_point_41.set_opacity(0.8)
        

        # Data point data_point_42
        data_point_42 = Sphere(radius=0.1).move_to([3.20, 2.46, 2.27])
        data_point_42.set_color(GRAY)
        data_point_42.set_opacity(0.8)
        

        # Data point data_point_43
        data_point_43 = Sphere(radius=0.1).move_to([-1.82, -1.37, -0.63])
        data_point_43.set_color(GRAY)
        data_point_43.set_opacity(0.8)
        

        # Data point data_point_44
        data_point_44 = Sphere(radius=0.1).move_to([2.44, 0.37, 1.40])
        data_point_44.set_color(GRAY)
        data_point_44.set_opacity(0.8)
        

        # Data point data_point_45
        data_point_45 = Sphere(radius=0.1).move_to([0.83, 1.81, 1.04])
        data_point_45.set_color(GRAY)
        data_point_45.set_opacity(0.8)
        

        # Data point data_point_46
        data_point_46 = Sphere(radius=0.1).move_to([0.07, -0.37, -0.80])
        data_point_46.set_color(GRAY)
        data_point_46.set_opacity(0.8)
        

        # Data point data_point_47
        data_point_47 = Sphere(radius=0.1).move_to([0.27, 0.04, 1.30])
        data_point_47.set_color(GRAY)
        data_point_47.set_opacity(0.8)
        

        # Data point data_point_48
        data_point_48 = Sphere(radius=0.1).move_to([-0.86, -0.34, -1.27])
        data_point_48.set_color(GRAY)
        data_point_48.set_opacity(0.8)
        

        # Data point data_point_49
        data_point_49 = Sphere(radius=0.1).move_to([-0.55, -0.18, 0.29])
        data_point_49.set_color(GRAY)
        data_point_49.set_opacity(0.8)
        

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

        self.wait(0.5)
        self.play(
            FadeIn(data_point_10),
            run_time=0.5
        )

        self.wait(0.55)
        self.play(
            FadeIn(data_point_11),
            run_time=0.5
        )

        self.wait(0.6000000000000001)
        self.play(
            FadeIn(data_point_12),
            run_time=0.5
        )

        self.wait(0.65)
        self.play(
            FadeIn(data_point_13),
            run_time=0.5
        )

        self.wait(0.7000000000000001)
        self.play(
            FadeIn(data_point_14),
            run_time=0.5
        )

        self.wait(0.75)
        self.play(
            FadeIn(data_point_15),
            run_time=0.5
        )

        self.wait(0.8)
        self.play(
            FadeIn(data_point_16),
            run_time=0.5
        )

        self.wait(0.8500000000000001)
        self.play(
            FadeIn(data_point_17),
            run_time=0.5
        )

        self.wait(0.9)
        self.play(
            FadeIn(data_point_18),
            run_time=0.5
        )

        self.wait(0.9500000000000001)
        self.play(
            FadeIn(data_point_19),
            run_time=0.5
        )

        self.wait(1.0)
        self.play(
            FadeIn(data_point_20),
            run_time=0.5
        )

        self.wait(1.05)
        self.play(
            FadeIn(data_point_21),
            run_time=0.5
        )

        self.wait(1.1)
        self.play(
            FadeIn(data_point_22),
            run_time=0.5
        )

        self.wait(1.1500000000000001)
        self.play(
            FadeIn(data_point_23),
            run_time=0.5
        )

        self.wait(1.2000000000000002)
        self.play(
            FadeIn(data_point_24),
            run_time=0.5
        )

        self.wait(1.25)
        self.play(
            FadeIn(data_point_25),
            run_time=0.5
        )

        self.wait(1.3)
        self.play(
            FadeIn(data_point_26),
            run_time=0.5
        )

        self.wait(1.35)
        self.play(
            FadeIn(data_point_27),
            run_time=0.5
        )

        self.wait(1.4000000000000001)
        self.play(
            FadeIn(data_point_28),
            run_time=0.5
        )

        self.wait(1.4500000000000002)
        self.play(
            FadeIn(data_point_29),
            run_time=0.5
        )

        self.wait(1.5)
        self.play(
            FadeIn(data_point_30),
            run_time=0.5
        )

        self.wait(1.55)
        self.play(
            FadeIn(data_point_31),
            run_time=0.5
        )

        self.wait(1.6)
        self.play(
            FadeIn(data_point_32),
            run_time=0.5
        )

        self.wait(1.6500000000000001)
        self.play(
            FadeIn(data_point_33),
            run_time=0.5
        )

        self.wait(1.7000000000000002)
        self.play(
            FadeIn(data_point_34),
            run_time=0.5
        )

        self.wait(1.75)
        self.play(
            FadeIn(data_point_35),
            run_time=0.5
        )

        self.wait(1.8)
        self.play(
            FadeIn(data_point_36),
            run_time=0.5
        )

        self.wait(1.85)
        self.play(
            FadeIn(data_point_37),
            run_time=0.5
        )

        self.wait(1.9000000000000001)
        self.play(
            FadeIn(data_point_38),
            run_time=0.5
        )

        self.wait(1.9500000000000002)
        self.play(
            FadeIn(data_point_39),
            run_time=0.5
        )

        self.wait(2.0)
        self.play(
            FadeIn(data_point_40),
            run_time=0.5
        )

        self.wait(2.0500000000000003)
        self.play(
            FadeIn(data_point_41),
            run_time=0.5
        )

        self.wait(2.1)
        self.play(
            FadeIn(data_point_42),
            run_time=0.5
        )

        self.wait(2.15)
        self.play(
            FadeIn(data_point_43),
            run_time=0.5
        )

        self.wait(2.2)
        self.play(
            FadeIn(data_point_44),
            run_time=0.5
        )

        self.wait(2.25)
        self.play(
            FadeIn(data_point_45),
            run_time=0.5
        )

        self.wait(2.3000000000000003)
        self.play(
            FadeIn(data_point_46),
            run_time=0.5
        )

        self.wait(2.35)
        self.play(
            FadeIn(data_point_47),
            run_time=0.5
        )

        self.wait(2.4000000000000004)
        self.play(
            FadeIn(data_point_48),
            run_time=0.5
        )

        self.wait(2.45)
        self.play(
            FadeIn(data_point_49),
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
        

        # Data point data_point_10
        data_point_10 = Sphere(radius=0.1).move_to([0.80, -0.65, -1.46])
        data_point_10.set_color(GRAY)
        data_point_10.set_opacity(0.8)
        

        # Data point data_point_11
        data_point_11 = Sphere(radius=0.1).move_to([-0.85, -1.33, 0.01])
        data_point_11.set_color(GRAY)
        data_point_11.set_opacity(0.8)
        

        # Data point data_point_12
        data_point_12 = Sphere(radius=0.1).move_to([0.93, -0.32, 0.72])
        data_point_12.set_color(GRAY)
        data_point_12.set_opacity(0.8)
        

        # Data point data_point_13
        data_point_13 = Sphere(radius=0.1).move_to([-1.40, -1.05, -0.81])
        data_point_13.set_color(GRAY)
        data_point_13.set_opacity(0.8)
        

        # Data point data_point_14
        data_point_14 = Sphere(radius=0.1).move_to([0.16, 0.77, 0.58])
        data_point_14.set_color(GRAY)
        data_point_14.set_opacity(0.8)
        

        # Data point data_point_15
        data_point_15 = Sphere(radius=0.1).move_to([0.49, 0.86, 0.61])
        data_point_15.set_color(GRAY)
        data_point_15.set_opacity(0.8)
        

        # Data point data_point_16
        data_point_16 = Sphere(radius=0.1).move_to([-0.88, -1.19, -0.78])
        data_point_16.set_color(GRAY)
        data_point_16.set_opacity(0.8)
        

        # Data point data_point_17
        data_point_17 = Sphere(radius=0.1).move_to([0.70, 0.29, 1.67])
        data_point_17.set_color(GRAY)
        data_point_17.set_opacity(0.8)
        

        # Data point data_point_18
        data_point_18 = Sphere(radius=0.1).move_to([-1.15, -1.68, -0.22])
        data_point_18.set_color(GRAY)
        data_point_18.set_opacity(0.8)
        

        # Data point data_point_19
        data_point_19 = Sphere(radius=0.1).move_to([1.99, 1.80, 1.46])
        data_point_19.set_color(GRAY)
        data_point_19.set_opacity(0.8)
        

        # Data point data_point_20
        data_point_20 = Sphere(radius=0.1).move_to([2.00, 1.32, 0.01])
        data_point_20.set_color(GRAY)
        data_point_20.set_opacity(0.8)
        

        # Data point data_point_21
        data_point_21 = Sphere(radius=0.1).move_to([-0.74, 0.24, -1.04])
        data_point_21.set_color(GRAY)
        data_point_21.set_opacity(0.8)
        

        # Data point data_point_22
        data_point_22 = Sphere(radius=0.1).move_to([0.05, 0.24, -0.13])
        data_point_22.set_color(GRAY)
        data_point_22.set_opacity(0.8)
        

        # Data point data_point_23
        data_point_23 = Sphere(radius=0.1).move_to([1.01, 1.17, 1.93])
        data_point_23.set_color(GRAY)
        data_point_23.set_opacity(0.8)
        

        # Data point data_point_24
        data_point_24 = Sphere(radius=0.1).move_to([0.87, 0.12, -0.05])
        data_point_24.set_color(GRAY)
        data_point_24.set_opacity(0.8)
        

        # Data point data_point_25
        data_point_25 = Sphere(radius=0.1).move_to([-1.16, -0.05, -0.70])
        data_point_25.set_color(GRAY)
        data_point_25.set_opacity(0.8)
        

        # Data point data_point_26
        data_point_26 = Sphere(radius=0.1).move_to([-0.10, 0.53, -0.36])
        data_point_26.set_color(GRAY)
        data_point_26.set_opacity(0.8)
        

        # Data point data_point_27
        data_point_27 = Sphere(radius=0.1).move_to([-0.41, -1.76, -1.12])
        data_point_27.set_color(GRAY)
        data_point_27.set_opacity(0.8)
        

        # Data point data_point_28
        data_point_28 = Sphere(radius=0.1).move_to([-0.79, -0.22, 0.43])
        data_point_28.set_color(GRAY)
        data_point_28.set_opacity(0.8)
        

        # Data point data_point_29
        data_point_29 = Sphere(radius=0.1).move_to([-0.03, 0.19, 0.13])
        data_point_29.set_color(GRAY)
        data_point_29.set_opacity(0.8)
        

        # Data point data_point_30
        data_point_30 = Sphere(radius=0.1).move_to([1.52, 1.78, 0.98])
        data_point_30.set_color(GRAY)
        data_point_30.set_opacity(0.8)
        

        # Data point data_point_31
        data_point_31 = Sphere(radius=0.1).move_to([-1.42, -0.27, -0.25])
        data_point_31.set_color(GRAY)
        data_point_31.set_opacity(0.8)
        

        # Data point data_point_32
        data_point_32 = Sphere(radius=0.1).move_to([1.72, 1.18, 1.92])
        data_point_32.set_color(GRAY)
        data_point_32.set_opacity(0.8)
        

        # Data point data_point_33
        data_point_33 = Sphere(radius=0.1).move_to([-0.50, 0.92, 0.10])
        data_point_33.set_color(GRAY)
        data_point_33.set_opacity(0.8)
        

        # Data point data_point_34
        data_point_34 = Sphere(radius=0.1).move_to([-0.72, -1.41, -0.59])
        data_point_34.set_color(GRAY)
        data_point_34.set_opacity(0.8)
        

        # Data point data_point_35
        data_point_35 = Sphere(radius=0.1).move_to([1.99, 2.05, 1.42])
        data_point_35.set_color(GRAY)
        data_point_35.set_opacity(0.8)
        

        # Data point data_point_36
        data_point_36 = Sphere(radius=0.1).move_to([-3.33, -1.76, -1.02])
        data_point_36.set_color(GRAY)
        data_point_36.set_opacity(0.8)
        

        # Data point data_point_37
        data_point_37 = Sphere(radius=0.1).move_to([-0.77, -1.04, -0.44])
        data_point_37.set_color(GRAY)
        data_point_37.set_opacity(0.8)
        

        # Data point data_point_38
        data_point_38 = Sphere(radius=0.1).move_to([2.41, 0.85, 0.64])
        data_point_38.set_color(GRAY)
        data_point_38.set_opacity(0.8)
        

        # Data point data_point_39
        data_point_39 = Sphere(radius=0.1).move_to([1.91, 0.98, 0.55])
        data_point_39.set_color(GRAY)
        data_point_39.set_opacity(0.8)
        

        # Data point data_point_40
        data_point_40 = Sphere(radius=0.1).move_to([0.14, -0.90, -0.01])
        data_point_40.set_color(GRAY)
        data_point_40.set_opacity(0.8)
        

        # Data point data_point_41
        data_point_41 = Sphere(radius=0.1).move_to([-1.69, -0.48, -0.60])
        data_point_41.set_color(GRAY)
        data_point_41.set_opacity(0.8)
        

        # Data point data_point_42
        data_point_42 = Sphere(radius=0.1).move_to([3.20, 2.46, 2.27])
        data_point_42.set_color(GRAY)
        data_point_42.set_opacity(0.8)
        

        # Data point data_point_43
        data_point_43 = Sphere(radius=0.1).move_to([-1.82, -1.37, -0.63])
        data_point_43.set_color(GRAY)
        data_point_43.set_opacity(0.8)
        

        # Data point data_point_44
        data_point_44 = Sphere(radius=0.1).move_to([2.44, 0.37, 1.40])
        data_point_44.set_color(GRAY)
        data_point_44.set_opacity(0.8)
        

        # Data point data_point_45
        data_point_45 = Sphere(radius=0.1).move_to([0.83, 1.81, 1.04])
        data_point_45.set_color(GRAY)
        data_point_45.set_opacity(0.8)
        

        # Data point data_point_46
        data_point_46 = Sphere(radius=0.1).move_to([0.07, -0.37, -0.80])
        data_point_46.set_color(GRAY)
        data_point_46.set_opacity(0.8)
        

        # Data point data_point_47
        data_point_47 = Sphere(radius=0.1).move_to([0.27, 0.04, 1.30])
        data_point_47.set_color(GRAY)
        data_point_47.set_opacity(0.8)
        

        # Data point data_point_48
        data_point_48 = Sphere(radius=0.1).move_to([-0.86, -0.34, -1.27])
        data_point_48.set_color(GRAY)
        data_point_48.set_opacity(0.8)
        

        # Data point data_point_49
        data_point_49 = Sphere(radius=0.1).move_to([-0.55, -0.18, 0.29])
        data_point_49.set_color(GRAY)
        data_point_49.set_opacity(0.8)
        

        # variance_ellipse
        variance_ellipse = Ellipse(width=4.0, height=2.0)
        variance_ellipse.set_fill(ORANGE, opacity=0.3)
        variance_ellipse.set_stroke(ORANGE, width=2)
        variance_ellipse.rotate(30 * DEGREES)
        

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

        self.wait(0.5)
        self.play(
            FadeIn(data_point_10),
            FadeIn(variance_ellipse),
            run_time=1.0
        )

        self.wait(0.55)
        self.play(
            FadeIn(data_point_11),
            run_time=0.5
        )

        self.wait(0.6000000000000001)
        self.play(
            FadeIn(data_point_12),
            run_time=0.5
        )

        self.wait(0.65)
        self.play(
            FadeIn(data_point_13),
            run_time=0.5
        )

        self.wait(0.7000000000000001)
        self.play(
            FadeIn(data_point_14),
            run_time=0.5
        )

        self.wait(0.75)
        self.play(
            FadeIn(data_point_15),
            run_time=0.5
        )

        self.wait(0.8)
        self.play(
            FadeIn(data_point_16),
            run_time=0.5
        )

        self.wait(0.8500000000000001)
        self.play(
            FadeIn(data_point_17),
            run_time=0.5
        )

        self.wait(0.9)
        self.play(
            FadeIn(data_point_18),
            run_time=0.5
        )

        self.wait(0.9500000000000001)
        self.play(
            FadeIn(data_point_19),
            run_time=0.5
        )

        self.wait(1.0)
        self.play(
            FadeIn(data_point_20),
            run_time=0.5
        )

        self.wait(1.05)
        self.play(
            FadeIn(data_point_21),
            run_time=0.5
        )

        self.wait(1.1)
        self.play(
            FadeIn(data_point_22),
            run_time=0.5
        )

        self.wait(1.1500000000000001)
        self.play(
            FadeIn(data_point_23),
            run_time=0.5
        )

        self.wait(1.2000000000000002)
        self.play(
            FadeIn(data_point_24),
            run_time=0.5
        )

        self.wait(1.25)
        self.play(
            FadeIn(data_point_25),
            run_time=0.5
        )

        self.wait(1.3)
        self.play(
            FadeIn(data_point_26),
            run_time=0.5
        )

        self.wait(1.35)
        self.play(
            FadeIn(data_point_27),
            run_time=0.5
        )

        self.wait(1.4000000000000001)
        self.play(
            FadeIn(data_point_28),
            run_time=0.5
        )

        self.wait(1.4500000000000002)
        self.play(
            FadeIn(data_point_29),
            run_time=0.5
        )

        self.wait(1.5)
        self.play(
            FadeIn(data_point_30),
            run_time=0.5
        )

        self.wait(1.55)
        self.play(
            FadeIn(data_point_31),
            run_time=0.5
        )

        self.wait(1.6)
        self.play(
            FadeIn(data_point_32),
            run_time=0.5
        )

        self.wait(1.6500000000000001)
        self.play(
            FadeIn(data_point_33),
            run_time=0.5
        )

        self.wait(1.7000000000000002)
        self.play(
            FadeIn(data_point_34),
            run_time=0.5
        )

        self.wait(1.75)
        self.play(
            FadeIn(data_point_35),
            run_time=0.5
        )

        self.wait(1.8)
        self.play(
            FadeIn(data_point_36),
            run_time=0.5
        )

        self.wait(1.85)
        self.play(
            FadeIn(data_point_37),
            run_time=0.5
        )

        self.wait(1.9000000000000001)
        self.play(
            FadeIn(data_point_38),
            run_time=0.5
        )

        self.wait(1.9500000000000002)
        self.play(
            FadeIn(data_point_39),
            run_time=0.5
        )

        self.wait(2.0)
        self.play(
            FadeIn(data_point_40),
            FadeIn(variance_ellipse),
            run_time=2.0
        )

        self.wait(2.0500000000000003)
        self.play(
            FadeIn(data_point_41),
            run_time=0.5
        )

        self.wait(2.1)
        self.play(
            FadeIn(data_point_42),
            run_time=0.5
        )

        self.wait(2.15)
        self.play(
            FadeIn(data_point_43),
            run_time=0.5
        )

        self.wait(2.2)
        self.play(
            FadeIn(data_point_44),
            run_time=0.5
        )

        self.wait(2.25)
        self.play(
            FadeIn(data_point_45),
            run_time=0.5
        )

        self.wait(2.3000000000000003)
        self.play(
            FadeIn(data_point_46),
            run_time=0.5
        )

        self.wait(2.35)
        self.play(
            FadeIn(data_point_47),
            run_time=0.5
        )

        self.wait(2.4000000000000004)
        self.play(
            FadeIn(data_point_48),
            run_time=0.5
        )

        self.wait(2.45)
        self.play(
            FadeIn(data_point_49),
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
        

        # projection_line_9 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 9:
            point_3d = self.data_3d[9]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_9 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_9.set_opacity(0.5)
        

        # projection_line_10 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 10:
            point_3d = self.data_3d[10]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_10 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_10.set_opacity(0.5)
        

        # projection_line_11 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 11:
            point_3d = self.data_3d[11]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_11 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_11.set_opacity(0.5)
        

        # projection_line_12 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 12:
            point_3d = self.data_3d[12]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_12 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_12.set_opacity(0.5)
        

        # projection_line_13 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 13:
            point_3d = self.data_3d[13]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_13 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_13.set_opacity(0.5)
        

        # projection_line_14 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 14:
            point_3d = self.data_3d[14]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_14 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_14.set_opacity(0.5)
        

        # projection_line_15 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 15:
            point_3d = self.data_3d[15]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_15 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_15.set_opacity(0.5)
        

        # projection_line_16 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 16:
            point_3d = self.data_3d[16]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_16 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_16.set_opacity(0.5)
        

        # projection_line_17 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 17:
            point_3d = self.data_3d[17]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_17 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_17.set_opacity(0.5)
        

        # projection_line_18 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 18:
            point_3d = self.data_3d[18]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_18 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_18.set_opacity(0.5)
        

        # projection_line_19 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 19:
            point_3d = self.data_3d[19]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_19 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_19.set_opacity(0.5)
        

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

        self.wait(1.9)
        self.play(
            FadeIn(projection_line_9),
            run_time=0.5
        )

        self.wait(2.0)
        self.play(
            FadeIn(projection_line_10),
            run_time=0.5
        )

        self.wait(2.1)
        self.play(
            FadeIn(projection_line_11),
            run_time=0.5
        )

        self.wait(2.2)
        self.play(
            FadeIn(projection_line_12),
            run_time=0.5
        )

        self.wait(2.3)
        self.play(
            FadeIn(projection_line_13),
            run_time=0.5
        )

        self.wait(2.4000000000000004)
        self.play(
            FadeIn(projection_line_14),
            run_time=0.5
        )

        self.wait(2.5)
        self.play(
            GrowArrow(pc2_arrow),
            FadeIn(projection_line_15),
            run_time=0.5
        )

        self.wait(2.6)
        self.play(
            FadeIn(projection_line_16),
            run_time=0.5
        )

        self.wait(2.7)
        self.play(
            FadeIn(projection_line_17),
            run_time=0.5
        )

        self.wait(2.8)
        self.play(
            FadeIn(projection_line_18),
            run_time=0.5
        )

        self.wait(2.9000000000000004)
        self.play(
            FadeIn(projection_line_19),
            run_time=0.5
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
        

        # projection_line_9 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 9:
            point_3d = self.data_3d[9]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_9 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_9.set_opacity(0.5)
        

        # projection_line_10 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 10:
            point_3d = self.data_3d[10]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_10 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_10.set_opacity(0.5)
        

        # projection_line_11 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 11:
            point_3d = self.data_3d[11]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_11 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_11.set_opacity(0.5)
        

        # projection_line_12 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 12:
            point_3d = self.data_3d[12]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_12 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_12.set_opacity(0.5)
        

        # projection_line_13 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 13:
            point_3d = self.data_3d[13]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_13 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_13.set_opacity(0.5)
        

        # projection_line_14 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 14:
            point_3d = self.data_3d[14]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_14 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_14.set_opacity(0.5)
        

        # projection_line_15 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 15:
            point_3d = self.data_3d[15]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_15 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_15.set_opacity(0.5)
        

        # projection_line_16 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 16:
            point_3d = self.data_3d[16]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_16 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_16.set_opacity(0.5)
        

        # projection_line_17 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 17:
            point_3d = self.data_3d[17]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_17 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_17.set_opacity(0.5)
        

        # projection_line_18 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 18:
            point_3d = self.data_3d[18]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_18 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_18.set_opacity(0.5)
        

        # projection_line_19 - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > 19:
            point_3d = self.data_3d[19]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            projection_line_19 = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color=GRAY,
                thickness=0.01
            )
            projection_line_19.set_opacity(0.5)
        

        # Create data points
        self.data_points = VGroup()
        for i, point in enumerate(self.data_3d):
            sphere = Sphere(radius=0.08).move_to([point[0], point[1], point[2]])
            sphere.set_color(GRAY)
            sphere.set_opacity(0.6)
            self.data_points.add(sphere)
        

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

        self.wait(1.9)
        self.play(
            FadeIn(projection_line_9),
            run_time=0.5
        )

        self.wait(2.0)
        self.play(
            FadeIn(projection_line_10),
            Transform(shadow_points, shadow_points),
            run_time=1.5
        )

        self.wait(2.1)
        self.play(
            FadeIn(projection_line_11),
            run_time=0.5
        )

        self.wait(2.2)
        self.play(
            FadeIn(projection_line_12),
            run_time=0.5
        )

        self.wait(2.3)
        self.play(
            FadeIn(projection_line_13),
            run_time=0.5
        )

        self.wait(2.4000000000000004)
        self.play(
            FadeIn(projection_line_14),
            run_time=0.5
        )

        self.wait(2.5)
        self.play(
            FadeIn(projection_line_15),
            run_time=0.5
        )

        self.wait(2.6)
        self.play(
            FadeIn(projection_line_16),
            run_time=0.5
        )

        self.wait(2.7)
        self.play(
            FadeIn(projection_line_17),
            run_time=0.5
        )

        self.wait(2.8)
        self.play(
            FadeIn(projection_line_18),
            run_time=0.5
        )

        self.wait(2.9000000000000004)
        self.play(
            FadeIn(projection_line_19),
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
