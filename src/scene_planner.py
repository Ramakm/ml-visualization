"""
Scene Planner: Breaks down concepts into structured scenes for animation.
"""
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from concept_parser import ParsedConcept, ConceptType


class SceneType(Enum):
    INTRODUCTION = "introduction"
    CONCEPT_EXPLANATION = "concept_explanation"
    TRANSFORMATION = "transformation"
    COMPARISON = "comparison"
    CONCLUSION = "conclusion"


@dataclass
class SceneElement:
    element_type: str
    properties: Dict[str, Any]
    animation_type: str
    duration: float
    dependencies: List[str]


@dataclass
class Scene:
    name: str
    scene_type: SceneType
    description: str
    elements: List[SceneElement]
    duration: float
    narration: str
    transitions: Dict[str, Any]


class ScenePlanner:
    """Plans and structures scenes for ML concept visualization."""
    
    def __init__(self):
        self.pca_scene_templates = {
            "data_introduction": {
                "type": SceneType.INTRODUCTION,
                "elements": ["data_points", "scatter_plot", "axes"],
                "duration": 8.0,
                "narration_template": "Here we have a dataset with {n_dimensions} dimensions..."
            },
            "variance_explanation": {
                "type": SceneType.CONCEPT_EXPLANATION,
                "elements": ["data_points", "variance", "spread_indicator"],
                "duration": 10.0,
                "narration_template": "Notice how the data spreads in different directions..."
            },
            "pca_transformation": {
                "type": SceneType.TRANSFORMATION,
                "elements": ["principal_component", "rotation", "projection"],
                "duration": 12.0,
                "narration_template": "PCA finds the directions of maximum variance..."
            },
            "dimensionality_reduction": {
                "type": SceneType.TRANSFORMATION,
                "elements": ["projection", "shadow", "reduced_data"],
                "duration": 10.0,
                "narration_template": "We can project the data onto fewer dimensions..."
            },
            "comparison": {
                "type": SceneType.COMPARISON,
                "elements": ["original_data", "reduced_data", "information_loss"],
                "duration": 8.0,
                "narration_template": "Comparing original vs reduced data..."
            }
        }
    
    def plan_scenes(self, concepts: List[ParsedConcept], topic: str = "pca") -> List[Scene]:
        """Plan scenes based on parsed concepts."""
        scenes = []
        
        if topic.lower() == "pca":
            scenes = self._plan_pca_scenes(concepts)
        else:
            scenes = self._plan_generic_scenes(concepts)
        
        return self._optimize_scene_flow(scenes)
    
    def _plan_pca_scenes(self, concepts: List[ParsedConcept]) -> List[Scene]:
        """Plan PCA-specific scenes."""
        scenes = []
        concept_names = [c.name for c in concepts]
        
        # Scene 1: Data Introduction
        if any(name in concept_names for name in ["data_points", "dataset", "scatter_plot"]):
            scenes.append(self._create_scene(
                "data_introduction",
                concepts,
                "Introduction to the dataset and its structure"
            ))
        
        # Scene 2: Variance Explanation
        if "variance" in concept_names:
            scenes.append(self._create_scene(
                "variance_explanation",
                concepts,
                "Understanding variance and data spread"
            ))
        
        # Scene 3: PCA Transformation
        if "principal_component" in concept_names:
            scenes.append(self._create_scene(
                "pca_transformation",
                concepts,
                "Finding principal components"
            ))
        
        # Scene 4: Dimensionality Reduction
        if any(name in concept_names for name in ["projection", "shadow", "reduction"]):
            scenes.append(self._create_scene(
                "dimensionality_reduction",
                concepts,
                "Projecting data to lower dimensions"
            ))
        
        # Scene 5: Comparison
        scenes.append(self._create_scene(
            "comparison",
            concepts,
            "Comparing original and reduced representations"
        ))
        
        return scenes
    
    def _create_scene(self, template_name: str, concepts: List[ParsedConcept], description: str) -> Scene:
        """Create a scene from template and concepts."""
        template = self.pca_scene_templates[template_name]
        elements = []
        
        # Create scene elements based on available concepts
        for element_name in template["elements"]:
            matching_concepts = [c for c in concepts if c.name == element_name]
            if matching_concepts:
                concept = matching_concepts[0]
                element = SceneElement(
                    element_type=element_name,
                    properties=concept.visual_properties,
                    animation_type=concept.visual_properties.get("animation", "fade_in"),
                    duration=template["duration"] / len(template["elements"]),
                    dependencies=concept.relationships
                )
                elements.append(element)
        
        # Generate narration
        narration = self._generate_narration(template_name, concepts)
        
        scene = Scene(
            name=template_name,
            scene_type=template["type"],
            description=description,
            elements=elements,
            duration=template["duration"],
            narration=narration,
            transitions={"fade_in": 1.0, "fade_out": 1.0}
        )
        
        return scene
    
    def _generate_narration(self, template_name: str, concepts: List[ParsedConcept]) -> str:
        """Generate narration for a scene."""
        template = self.pca_scene_templates[template_name]
        base_narration = template["narration_template"]
        
        # Customize based on concepts
        narrations = {
            "data_introduction": "Let's start with a dataset containing multiple features. Each point represents one observation.",
            "variance_explanation": "The data spreads differently in each direction. Some directions show more variance than others.",
            "pca_transformation": "PCA identifies the principal components - the directions where data varies the most.",
            "dimensionality_reduction": "We can project our high-dimensional data onto these principal components.",
            "comparison": "Notice how the reduced representation preserves the main patterns while using fewer dimensions."
        }
        
        return narrations.get(template_name, base_narration)
    
    def _plan_generic_scenes(self, concepts: List[ParsedConcept]) -> List[Scene]:
        """Plan generic scenes for non-PCA topics."""
        scenes = []
        
        # Group concepts by type
        math_concepts = [c for c in concepts if c.concept_type == ConceptType.MATHEMATICAL_ENTITY]
        visual_concepts = [c for c in concepts if c.concept_type == ConceptType.VISUAL_ELEMENT]
        process_concepts = [c for c in concepts if c.concept_type == ConceptType.PROCESS_STEP]
        
        if math_concepts:
            scenes.append(self._create_generic_scene("Mathematical Concepts", math_concepts))
        if visual_concepts:
            scenes.append(self._create_generic_scene("Visual Elements", visual_concepts))
        if process_concepts:
            scenes.append(self._create_generic_scene("Process Steps", process_concepts))
        
        return scenes
    
    def _create_generic_scene(self, name: str, concepts: List[ParsedConcept]) -> Scene:
        """Create a generic scene from concepts."""
        elements = []
        total_duration = 0
        
        for concept in concepts:
            duration = 3.0 + concept.importance_score * 5.0
            element = SceneElement(
                element_type=concept.name,
                properties=concept.visual_properties,
                animation_type=concept.visual_properties.get("animation", "fade_in"),
                duration=duration,
                dependencies=concept.relationships
            )
            elements.append(element)
            total_duration += duration
        
        return Scene(
            name=name.lower().replace(" ", "_"),
            scene_type=SceneType.CONCEPT_EXPLANATION,
            description=f"Explanation of {name.lower()}",
            elements=elements,
            duration=total_duration,
            narration=f"Let's explore {name.lower()} in detail.",
            transitions={"fade_in": 1.0, "fade_out": 1.0}
        )
    
    def _optimize_scene_flow(self, scenes: List[Scene]) -> List[Scene]:
        """Optimize the flow and transitions between scenes."""
        if len(scenes) <= 1:
            return scenes
        
        # Add smooth transitions
        for i in range(len(scenes) - 1):
            current_scene = scenes[i]
            next_scene = scenes[i + 1]
            
            # Find common elements for smooth transitions
            current_elements = {e.element_type for e in current_scene.elements}
            next_elements = {e.element_type for e in next_scene.elements}
            common_elements = current_elements.intersection(next_elements)
            
            if common_elements:
                current_scene.transitions["fade_out"] = 0.5
                next_scene.transitions["fade_in"] = 0.5
        
        return scenes


def plan_pca_visualization(concepts: List[ParsedConcept]) -> List[Scene]:
    """Convenience function to plan PCA visualization scenes."""
    planner = ScenePlanner()
    return planner.plan_scenes(concepts, "pca")
