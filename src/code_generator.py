"""
Code Generator: Converts visual representations to executable Manim code.
"""
from typing import List, Dict, Any, Optional
import textwrap
import math
from visual_mapper import VisualElement, VisualElementType


class ManimeCodeGenerator:
    """Generates Manim code from visual scene descriptions."""
    
    def __init__(self):
        self.imports = [
            "from manim import *",
            "import numpy as np",
            "from sklearn.decomposition import PCA",
            "from sklearn.datasets import make_blobs"
        ]
        
        self.color_mapping = {
            "#3498db": "BLUE",
            "#e74c3c": "RED", 
            "#f39c12": "ORANGE",
            "#2ecc71": "GREEN",
            "#f1c40f": "YELLOW",
            "#95a5a6": "GRAY",
            "#2c3e50": "DARK_BLUE",
            "#ecf0f1": "LIGHT_GRAY"
        }
    
    def generate_scene_class(self, scene_data: Dict[str, Any]) -> str:
        """Generate a complete Manim scene class."""
        class_name = self._to_class_name(scene_data["name"])
        
        # Generate class header
        code = f"class {class_name}(ThreeDScene):\n"
        code += '    """' + f'Scene: {scene_data["name"]}' + '"""\n\n'
        
        # Generate construct method
        code += "    def construct(self):\n"
        code += "        # Set up 3D scene\n"
        code += "        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)\n\n"
        
        # Generate data setup
        code += self._generate_data_setup()
        
        # Generate visual elements
        for element in scene_data["elements"]:
            code += self._generate_element_code(element)
        
        # Generate animations
        code += self._generate_animation_sequence(scene_data["elements"])
        
        # Generate camera movements
        if scene_data.get("camera_movements"):
            code += self._generate_camera_movements(scene_data["camera_movements"])
        
        # Add narration timing
        code += f"\n        # Hold for narration\n"
        code += f"        self.wait({scene_data['duration']})\n"
        
        return code
    
    def generate_complete_file(self, visual_scenes: List[Dict[str, Any]], output_path: str = None) -> str:
        """Generate a complete Manim file with all scenes."""
        code = "#!/usr/bin/env python3\n"
        code += '"""\nPCA Visualization - Generated Manim Animation\n"""\n\n'
        
        # Add imports
        for import_line in self.imports:
            code += import_line + "\n"
        code += "\n\n"
        
        # Generate each scene class
        for scene_data in visual_scenes:
            code += self.generate_scene_class(scene_data)
            code += "\n\n"
        
        # Generate main execution
        code += self._generate_main_execution(visual_scenes)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(code)
        
        return code
    
    def _to_class_name(self, scene_name: str) -> str:
        """Convert scene name to valid class name."""
        return ''.join(word.capitalize() for word in scene_name.split('_'))
    
    def _generate_data_setup(self) -> str:
        """Generate data setup code."""
        code = textwrap.dedent("""
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
        
        """)
        return textwrap.indent(code, "        ")
    
    def _generate_element_code(self, element: VisualElement) -> str:
        """Generate code for a visual element."""
        code = ""
        
        if element.element_type == VisualElementType.POINT:
            code += self._generate_points_code(element)
        elif element.element_type == VisualElementType.ARROW:
            code += self._generate_arrow_code(element)
        elif element.element_type == VisualElementType.SURFACE:
            code += self._generate_surface_code(element)
        elif element.element_type == VisualElementType.ELLIPSE:
            code += self._generate_ellipse_code(element)
        elif element.element_type == VisualElementType.LINE:
            code += self._generate_line_code(element)
        elif element.element_type == VisualElementType.TEXT:
            code += self._generate_text_code(element)
        
        return code
    
    def _generate_points_code(self, element: VisualElement) -> str:
        """Generate code for data points."""
        if "data_point" in element.element_id:
            # Individual data point
            x, y, z = element.position
            color = self._get_manim_color(element.properties.get("color", "#95a5a6"))
            size = element.properties.get("size", 0.1)
            
            code = f"""
        # Data point {element.element_id}
        {element.element_id} = Sphere(radius={size}).move_to([{x:.2f}, {y:.2f}, {z:.2f}])
        {element.element_id}.set_color({color})
        {element.element_id}.set_opacity({element.properties.get("opacity", 1.0)})
        
"""
        else:
            # Collection of data points
            color = self._get_manim_color(element.properties.get("color", "#95a5a6"))
            size = element.properties.get("size", 0.1)
            
            code = f"""
        # Create data points
        self.data_points = VGroup()
        for i, point in enumerate(self.data_3d):
            sphere = Sphere(radius={size}).move_to([point[0], point[1], point[2]])
            sphere.set_color({color})
            sphere.set_opacity({element.properties.get("opacity", 0.8)})
            self.data_points.add(sphere)
        
"""
        
        return code
    
    def _generate_arrow_code(self, element: VisualElement) -> str:
        """Generate code for arrows (principal components)."""
        color = self._get_manim_color(element.properties.get("color", "#3498db"))
        direction = element.properties.get("direction", (1, 0, 0))
        length = element.properties.get("length", 2.0)
        thickness = element.properties.get("thickness", 0.05)
        
        code = f"""
        # {element.element_id}
        {element.element_id} = Arrow3D(
            start=ORIGIN,
            end=[{direction[0] * length:.2f}, {direction[1] * length:.2f}, {direction[2] * length:.2f}],
            color={color},
            thickness={thickness}
        )
        
"""
        
        return code
    
    def _generate_surface_code(self, element: VisualElement) -> str:
        """Generate code for surfaces (projection planes)."""
        color = self._get_manim_color(element.properties.get("color", "#f39c12"))
        width = element.properties.get("width", 4)
        height = element.properties.get("height", 3)
        opacity = element.properties.get("opacity", 0.3)
        
        code = f"""
        # {element.element_id}
        {element.element_id} = Rectangle(width={width}, height={height})
        {element.element_id}.set_fill({color}, opacity={opacity})
        {element.element_id}.set_stroke({color}, width=2)
        {element.element_id}.move_to([{element.position[0]}, {element.position[1]}, {element.position[2]}])
        
"""
        
        return code
    
    def _generate_ellipse_code(self, element: VisualElement) -> str:
        """Generate code for ellipses (variance visualization)."""
        color = self._get_manim_color(element.properties.get("color", "#f39c12"))
        width = element.properties.get("width", 2)
        height = element.properties.get("height", 1)
        opacity = element.properties.get("opacity", 0.3)
        
        code = f"""
        # {element.element_id}
        {element.element_id} = Ellipse(width={width}, height={height})
        {element.element_id}.set_fill({color}, opacity={opacity})
        {element.element_id}.set_stroke({color}, width=2)
        {element.element_id}.rotate({element.properties.get("rotation", 0)} * DEGREES)
        
"""
        
        return code
    
    def _generate_line_code(self, element: VisualElement) -> str:
        """Generate code for lines (projection lines)."""
        color = self._get_manim_color(element.properties.get("color", "#95a5a6"))
        thickness = element.properties.get("thickness", 0.02)
        
        code = f"""
        # {element.element_id} - projection line
        if hasattr(self, 'data_points') and len(self.data_points) > {element.element_id.split('_')[-1] if element.element_id.split('_')[-1].isdigit() else '0'}:
            point_3d = self.data_3d[{element.element_id.split('_')[-1] if element.element_id.split('_')[-1].isdigit() else '0'}]
            point_2d = [point_3d[0], point_3d[1], -1]  # Project to z=-1 plane
            {element.element_id} = Line3D(
                start=[point_3d[0], point_3d[1], point_3d[2]],
                end=point_2d,
                color={color},
                thickness={thickness}
            )
            {element.element_id}.set_opacity({element.properties.get("opacity", 0.5)})
        
"""
        
        return code
    
    def _generate_text_code(self, element: VisualElement) -> str:
        """Generate code for text elements."""
        text = element.properties.get("text", "Text")
        color = self._get_manim_color(element.properties.get("color", "#ecf0f1"))
        size = element.properties.get("size", 0.5)
        
        code = f"""
        # {element.element_id}
        {element.element_id} = Text("{text}", font_size={size * 48})
        {element.element_id}.set_color({color})
        {element.element_id}.move_to([{element.position[0]}, {element.position[1]}, {element.position[2]}])
        
"""
        
        return code
    
    def _generate_animation_sequence(self, elements: List[VisualElement]) -> str:
        """Generate animation sequence for all elements."""
        code = """
        # Animation sequence
        animations = []
        
"""
        
        # Group animations by timing
        animation_groups = {}
        
        for element in elements:
            for animation in element.animation_sequence:
                delay = animation.get("delay", 0)
                if delay not in animation_groups:
                    animation_groups[delay] = []
                animation_groups[delay].append((element.element_id, animation))
        
        # Generate animations in order
        for delay in sorted(animation_groups.keys()):
            if delay > 0:
                code += f"        self.wait({delay})\n"
            
            animations = animation_groups[delay]
            anim_code = "        self.play(\n"
            
            for element_id, animation in animations:
                anim_type = animation.get("type", "fade_in")
                duration = animation.get("duration", 1.0)
                
                if anim_type == "fade_in":
                    anim_code += f"            FadeIn({element_id}),\n"
                elif anim_type == "grow_arrow":
                    anim_code += f"            GrowArrow({element_id}),\n"
                elif anim_type == "scale":
                    scale_to = animation.get("to", 1.2)
                    anim_code += f"            {element_id}.animate.scale({scale_to}),\n"
                elif anim_type == "cast_shadow":
                    anim_code += f"            Transform({element_id}, {element_id}),\n"
                else:
                    anim_code += f"            FadeIn({element_id}),\n"
            
            anim_code += f"            run_time={duration}\n"
            anim_code += "        )\n\n"
            
            code += anim_code
        
        return code
    
    def _generate_camera_movements(self, movements: List[Dict[str, Any]]) -> str:
        """Generate camera movement code."""
        code = """
        # Camera movements
        
"""
        
        for i, movement in enumerate(movements):
            start_pos = movement.start_position
            end_pos = movement.end_position
            duration = movement.duration
            
            code += f"""
        self.move_camera(
            phi={60 * 3.14159 / 180},
            theta={45 * 3.14159 / 180},
            distance={math.sqrt(sum(x*x for x in end_pos))},
            run_time={duration}
        )
        
"""
        
        return code
    
    def _generate_main_execution(self, visual_scenes: List[Dict[str, Any]]) -> str:
        """Generate main execution code."""
        scene_classes = [self._to_class_name(scene["name"]) for scene in visual_scenes]
        
        code = 'if __name__ == "__main__":\n'
        code += '    """Run the PCA visualization scenes."""\n'
        code += '    import os\n'
        code += '    \n'
        code += '    # Scene classes to render\n'
        code += f'    scenes = {scene_classes}\n'
        code += '    \n'
        code += '    print("Available scenes:")\n'
        code += '    for i, scene in enumerate(scenes):\n'
        code += '        print(f"{i+1}. {scene.__name__}")\n'
        code += '    \n'
        code += '    # Render all scenes or specific scene\n'
        code += '    # Example: manim -pql pca_visualization.py DataIntroduction\n'
        
        return code
    
    def _get_manim_color(self, hex_color: str) -> str:
        """Convert hex color to Manim color constant."""
        return self.color_mapping.get(hex_color, f'"{hex_color}"')


def generate_manim_code(visual_scenes: List[Dict[str, Any]], output_path: str = None) -> str:
    """Convenience function to generate Manim code from visual scenes."""
    generator = ManimeCodeGenerator()
    return generator.generate_complete_file(visual_scenes, output_path)
