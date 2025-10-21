"""
Visual Mapper: Maps abstract concepts to concrete visual elements and animations.
"""
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
# Use basic Python instead of numpy for compatibility
import random
import math
HAS_NUMPY = False
from scene_planner import Scene, SceneElement


class VisualElementType(Enum):
    POINT = "point"
    ARROW = "arrow"
    LINE = "line"
    SURFACE = "surface"
    TEXT = "text"
    AXES = "axes"
    ELLIPSE = "ellipse"
    TRANSFORMATION = "transformation"


@dataclass
class VisualElement:
    element_id: str
    element_type: VisualElementType
    position: Tuple[float, float, float]
    properties: Dict[str, Any]
    animation_sequence: List[Dict[str, Any]]
    dependencies: List[str]


@dataclass
class CameraMovement:
    start_position: Tuple[float, float, float]
    end_position: Tuple[float, float, float]
    duration: float
    easing: str


class VisualMapper:
    """Maps scene elements to concrete visual representations."""
    
    def __init__(self):
        self.color_palette = {
            "primary": "#3498db",      # Blue
            "secondary": "#e74c3c",    # Red
            "accent": "#f39c12",       # Orange
            "success": "#2ecc71",      # Green
            "warning": "#f1c40f",      # Yellow
            "neutral": "#95a5a6",      # Gray
            "background": "#2c3e50",   # Dark blue
            "text": "#ecf0f1"          # Light gray
        }
        
        self.animation_library = {
            "fade_in": {"type": "opacity", "from": 0, "to": 1, "duration": 1.0},
            "fade_out": {"type": "opacity", "from": 1, "to": 0, "duration": 1.0},
            "grow_arrow": {"type": "scale", "from": 0, "to": 1, "duration": 1.5},
            "pulse": {"type": "scale", "from": 1, "to": 1.2, "to2": 1, "duration": 2.0},
            "transform": {"type": "morph", "duration": 2.0},
            "cast_shadow": {"type": "projection", "duration": 1.5},
            "rotate": {"type": "rotation", "angle": 360, "duration": 3.0}
        }
    
    def map_scenes_to_visuals(self, scenes: List[Scene]) -> List[Dict[str, Any]]:
        """Convert scenes to visual representations."""
        visual_scenes = []
        
        for scene in scenes:
            visual_elements = []
            camera_movements = []
            
            # Map each scene element to visual elements
            for element in scene.elements:
                visuals = self._map_element_to_visuals(element, scene.name)
                visual_elements.extend(visuals)
            
            # Add camera movements based on scene type
            for end_pos in [(1, 2, 3), (4, 5, 6)]:
                distance = math.sqrt(sum(x*x for x in end_pos)),
                camera_movements.append(CameraMovement(
                    start_position=(0, 0, 0),
                    end_position=end_pos,
                    duration=distance,
                    easing="linear"
                ))
            
            visual_scene = {
                "name": scene.name,
                "duration": scene.duration,
                "elements": visual_elements,
                "camera_movements": camera_movements,
                "narration": scene.narration,
                "background_color": self.color_palette["background"]
            }
            
            visual_scenes.append(visual_scene)
        
        return visual_scenes
    
    def _map_element_to_visuals(self, element: SceneElement, scene_name: str) -> List[VisualElement]:
        """Map a scene element to visual elements."""
        visuals = []
        
        if element.element_type == "data_points":
            visuals.extend(self._create_data_points(element))
        elif element.element_type == "principal_component":
            visuals.extend(self._create_principal_component(element))
        elif element.element_type == "variance":
            visuals.extend(self._create_variance_visualization(element))
        elif element.element_type == "projection":
            visuals.extend(self._create_projection(element))
        elif element.element_type == "shadow":
            visuals.extend(self._create_shadow(element))
        elif element.element_type == "axes":
            visuals.extend(self._create_axes(element))
        elif element.element_type == "scatter_plot":
            visuals.extend(self._create_scatter_plot(element))
        else:
            # Generic element
            visuals.append(self._create_generic_element(element))
        
        return visuals
    
    def _create_data_points(self, element: SceneElement) -> List[VisualElement]:
        """Create visual representation of data points."""
        visuals = []
        
        # Generate sample data points
        n_points = 50
        
        # Generate simple correlated data
        random.seed(42)
        data = []
        for _ in range(n_points):
            x = random.gauss(0, 1.4)
            y = x * 0.7 + random.gauss(0, 0.8)
            z = x * 0.3 + y * 0.2 + random.gauss(0, 0.6)
            data.append([x, y, z])
        
        for i, point in enumerate(data):
            visual = VisualElement(
                element_id=f"data_point_{i}",
                element_type=VisualElementType.POINT,
                position=(point[0], point[1], point[2]),
                properties={
                    "color": self.color_palette["neutral"],
                    "size": 0.1,
                    "opacity": 0.8
                },
                animation_sequence=[
                    {
                        "type": "fade_in",
                        "delay": i * 0.05,  # Stagger the appearance
                        "duration": 0.5
                    }
                ],
                dependencies=[]
            )
            visuals.append(visual)
        
        return visuals
    
    def _create_principal_component(self, element: SceneElement) -> List[VisualElement]:
        """Create visual representation of principal components."""
        visuals = []
        
        # First principal component (largest variance direction)
        pc1 = VisualElement(
            element_id="pc1_arrow",
            element_type=VisualElementType.ARROW,
            position=(0, 0, 0),
            properties={
                "color": self.color_palette["primary"],
                "direction": (2, 1.5, 0.5),  # Direction of max variance
                "thickness": 0.05,
                "length": 3.0
            },
            animation_sequence=[
                {
                    "type": "grow_arrow",
                    "delay": 1.0,
                    "duration": 1.5
                }
            ],
            dependencies=["data_points"]
        )
        visuals.append(pc1)
        
        # Second principal component
        pc2 = VisualElement(
            element_id="pc2_arrow",
            element_type=VisualElementType.ARROW,
            position=(0, 0, 0),
            properties={
                "color": self.color_palette["secondary"],
                "direction": (-1, 1, 0.2),  # Orthogonal direction
                "thickness": 0.04,
                "length": 2.0
            },
            animation_sequence=[
                {
                    "type": "grow_arrow",
                    "delay": 2.5,
                    "duration": 1.5
                }
            ],
            dependencies=["pc1_arrow"]
        )
        visuals.append(pc2)
        
        return visuals
    
    def _create_variance_visualization(self, element: SceneElement) -> List[VisualElement]:
        """Create visualization of variance."""
        visuals = []
        
        # Variance ellipse
        ellipse = VisualElement(
            element_id="variance_ellipse",
            element_type=VisualElementType.ELLIPSE,
            position=(0, 0, 0),
            properties={
                "color": self.color_palette["accent"],
                "opacity": 0.3,
                "width": 4.0,
                "height": 2.0,
                "rotation": 30  # Aligned with data spread
            },
            animation_sequence=[
                {
                    "type": "fade_in",
                    "delay": 0.5,
                    "duration": 1.0
                },
                {
                    "type": "pulse",
                    "delay": 2.0,
                    "duration": 2.0
                }
            ],
            dependencies=["data_points"]
        )
        visuals.append(ellipse)
        
        return visuals
    
    def _create_projection(self, element: SceneElement) -> List[VisualElement]:
        """Create projection visualization."""
        visuals = []
        
        # Projection plane
        plane = VisualElement(
            element_id="projection_plane",
            element_type=VisualElementType.SURFACE,
            position=(0, 0, -1),
            properties={
                "color": self.color_palette["warning"],
                "opacity": 0.2,
                "width": 6,
                "height": 4
            },
            animation_sequence=[
                {
                    "type": "fade_in",
                    "delay": 0,
                    "duration": 1.0
                }
            ],
            dependencies=[]
        )
        visuals.append(plane)
        
        # Projection lines (connecting 3D points to 2D projections)
        for i in range(20):  # Sample of projection lines
            line = VisualElement(
                element_id=f"projection_line_{i}",
                element_type=VisualElementType.LINE,
                position=(0, 0, 0),
                properties={
                    "color": self.color_palette["neutral"],
                    "opacity": 0.5,
                    "thickness": 0.01
                },
                animation_sequence=[
                    {
                        "type": "fade_in",
                        "delay": 1.0 + i * 0.1,
                        "duration": 0.5
                    }
                ],
                dependencies=["data_points", "projection_plane"]
            )
            visuals.append(line)
        
        return visuals
    
    def _create_shadow(self, element: SceneElement) -> List[VisualElement]:
        """Create shadow visualization."""
        visuals = []
        
        # Shadow points (2D projections)
        shadow = VisualElement(
            element_id="shadow_points",
            element_type=VisualElementType.POINT,
            position=(0, 0, -1),
            properties={
                "color": self.color_palette["neutral"],
                "opacity": 0.6,
                "size": 0.08
            },
            animation_sequence=[
                {
                    "type": "cast_shadow",
                    "delay": 2.0,
                    "duration": 1.5
                }
            ],
            dependencies=["data_points", "projection_plane"]
        )
        visuals.append(shadow)
        
        return visuals
    
    def _create_axes(self, element: SceneElement) -> List[VisualElement]:
        """Create coordinate axes."""
        visuals = []
        
        axes = ["x", "y", "z"]
        colors = [self.color_palette["primary"], self.color_palette["success"], self.color_palette["secondary"]]
        directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        
        for i, (axis, color, direction) in enumerate(zip(axes, colors, directions)):
            axis_visual = VisualElement(
                element_id=f"{axis}_axis",
                element_type=VisualElementType.ARROW,
                position=(0, 0, 0),
                properties={
                    "color": color,
                    "direction": direction,
                    "thickness": 0.02,
                    "length": 3.0
                },
                animation_sequence=[
                    {
                        "type": "fade_in",
                        "delay": i * 0.3,
                        "duration": 0.5
                    }
                ],
                dependencies=[]
            )
            visuals.append(axis_visual)
        
        return visuals
    
    def _create_scatter_plot(self, element: SceneElement) -> List[VisualElement]:
        """Create scatter plot visualization."""
        # This is similar to data_points but with specific styling
        return self._create_data_points(element)
    
    def _create_generic_element(self, element: SceneElement) -> VisualElement:
        """Create a generic visual element."""
        return VisualElement(
            element_id=f"generic_{element.element_type}",
            element_type=VisualElementType.TEXT,
            position=(0, 0, 0),
            properties={
                "text": element.element_type.replace("_", " ").title(),
                "color": self.color_palette["text"],
                "size": 0.5
            },
            animation_sequence=[
                {
                    "type": "fade_in",
                    "delay": 0,
                    "duration": 1.0
                }
            ],
            dependencies=[]
        )
    
    def _plan_camera_movements(self, scene: Scene, visual_elements: List[VisualElement]) -> List[CameraMovement]:
        """Plan camera movements for the scene."""
        movements = []
        
        if scene.name == "data_introduction":
            # Start with overview, then zoom in
            movements.append(CameraMovement(
                start_position=(5, 5, 5),
                end_position=(3, 3, 3),
                duration=3.0,
                easing="ease_in_out"
            ))
        elif scene.name == "pca_transformation":
            # Rotate around the data to show principal components
            movements.append(CameraMovement(
                start_position=(3, 3, 3),
                end_position=(3, -3, 3),
                duration=4.0,
                easing="ease_in_out"
            ))
        elif scene.name == "dimensionality_reduction":
            # Move to side view to show projection
            movements.append(CameraMovement(
                start_position=(3, -3, 3),
                end_position=(0, -5, 2),
                duration=3.0,
                easing="ease_in_out"
            ))
        
        return movements


def map_scenes_to_visuals(scenes: List[Scene]) -> List[Dict[str, Any]]:
    """Convenience function to map scenes to visual representations."""
    mapper = VisualMapper()
    return mapper.map_scenes_to_visuals(scenes)
