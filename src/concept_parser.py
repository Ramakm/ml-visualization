"""
ConceptParser: Identifies key entities and concepts from text input for ML visualization.
"""
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import re


class ConceptType(Enum):
    MATHEMATICAL_ENTITY = "mathematical_entity"
    VISUAL_ELEMENT = "visual_element"
    PROCESS_STEP = "process_step"
    DATA_STRUCTURE = "data_structure"


@dataclass
class ParsedConcept:
    name: str
    concept_type: ConceptType
    description: str
    visual_properties: Dict[str, Any]
    relationships: List[str]
    importance_score: float


class ConceptParser:
    """Parses text input to identify key concepts for visualization."""
    
    def __init__(self):
        self.pca_entities = {
            # Mathematical entities
            "variance": ConceptType.MATHEMATICAL_ENTITY,
            "eigenvalue": ConceptType.MATHEMATICAL_ENTITY,
            "eigenvector": ConceptType.MATHEMATICAL_ENTITY,
            "principal_component": ConceptType.MATHEMATICAL_ENTITY,
            "covariance_matrix": ConceptType.MATHEMATICAL_ENTITY,
            "projection": ConceptType.MATHEMATICAL_ENTITY,
            "dimensionality": ConceptType.MATHEMATICAL_ENTITY,
            
            # Visual elements
            "data_points": ConceptType.VISUAL_ELEMENT,
            "scatter_plot": ConceptType.VISUAL_ELEMENT,
            "arrow": ConceptType.VISUAL_ELEMENT,
            "axis": ConceptType.VISUAL_ELEMENT,
            "cloud": ConceptType.VISUAL_ELEMENT,
            "surface": ConceptType.VISUAL_ELEMENT,
            "shadow": ConceptType.VISUAL_ELEMENT,
            
            # Process steps
            "transformation": ConceptType.PROCESS_STEP,
            "rotation": ConceptType.PROCESS_STEP,
            "reduction": ConceptType.PROCESS_STEP,
            "decomposition": ConceptType.PROCESS_STEP,
            
            # Data structures
            "dataset": ConceptType.DATA_STRUCTURE,
            "matrix": ConceptType.DATA_STRUCTURE,
            "vector": ConceptType.DATA_STRUCTURE,
        }
        
        self.visual_mappings = {
            "variance": {"color": "BLUE", "animation": "pulse", "shape": "ellipse"},
            "data_points": {"color": "WHITE", "animation": "fade_in", "shape": "dot"},
            "principal_component": {"color": "RED", "animation": "grow_arrow", "shape": "arrow"},
            "projection": {"color": "YELLOW", "animation": "transform", "shape": "line"},
            "shadow": {"color": "GRAY", "animation": "cast_shadow", "shape": "silhouette"},
        }
    
    def parse_text(self, text: str) -> List[ParsedConcept]:
        """Parse input text and extract relevant concepts."""
        concepts = []
        text_lower = text.lower()
        
        # Find entities in text
        for entity, concept_type in self.pca_entities.items():
            if entity.replace("_", " ") in text_lower or entity in text_lower:
                visual_props = self.visual_mappings.get(entity, {})
                importance = self._calculate_importance(entity, text_lower)
                
                concept = ParsedConcept(
                    name=entity,
                    concept_type=concept_type,
                    description=self._get_description(entity),
                    visual_properties=visual_props,
                    relationships=self._find_relationships(entity, text_lower),
                    importance_score=importance
                )
                concepts.append(concept)
        
        # Sort by importance
        concepts.sort(key=lambda x: x.importance_score, reverse=True)
        return concepts
    
    def _calculate_importance(self, entity: str, text: str) -> float:
        """Calculate importance score based on frequency and context."""
        count = text.count(entity.replace("_", " "))
        count += text.count(entity)
        
        # Boost score for key PCA concepts
        key_concepts = ["principal_component", "variance", "data_points", "projection"]
        if entity in key_concepts:
            count *= 2
        
        return min(count / len(text.split()) * 100, 1.0)
    
    def _get_description(self, entity: str) -> str:
        """Get description for entity."""
        descriptions = {
            "variance": "Measure of data spread",
            "principal_component": "Direction of maximum variance",
            "data_points": "Individual observations in dataset",
            "projection": "Mapping to lower dimensional space",
            "shadow": "2D representation of 3D data",
            "eigenvalue": "Importance of principal component",
            "eigenvector": "Direction of principal component",
        }
        return descriptions.get(entity, f"Concept: {entity}")
    
    def _find_relationships(self, entity: str, text: str) -> List[str]:
        """Find related concepts mentioned near this entity."""
        relationships = {
            "variance": ["data_points", "principal_component"],
            "principal_component": ["variance", "eigenvalue", "eigenvector"],
            "data_points": ["variance", "scatter_plot", "cloud"],
            "projection": ["shadow", "dimensionality", "transformation"],
        }
        return relationships.get(entity, [])


def parse_pca_concept(text: str) -> List[ParsedConcept]:
    """Convenience function to parse PCA-related text."""
    parser = ConceptParser()
    return parser.parse_text(text)
