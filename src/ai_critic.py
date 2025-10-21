"""
AI Critic: Analyzes generated animations and provides feedback for improvements.
"""
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import json
import os
from pathlib import Path


class CriticAspect(Enum):
    TIMING = "timing"
    VISUAL_CLARITY = "visual_clarity"
    EDUCATIONAL_VALUE = "educational_value"
    ANIMATION_FLOW = "animation_flow"
    TECHNICAL_ACCURACY = "technical_accuracy"


@dataclass
class CriticFeedback:
    aspect: CriticAspect
    score: float  # 0-10 scale
    feedback: str
    suggestions: List[str]
    severity: str  # "low", "medium", "high"


@dataclass
class AnimationAnalysis:
    overall_score: float
    feedback_items: List[CriticFeedback]
    recommended_changes: Dict[str, Any]
    approval_status: str  # "approved", "needs_revision", "rejected"


class AICritic:
    """AI-powered critic for analyzing and improving animations."""
    
    def __init__(self, openai_api_key: Optional[str] = None):
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.quality_thresholds = {
            "excellent": 8.5,
            "good": 7.0,
            "acceptable": 5.5,
            "needs_improvement": 3.0
        }
        
        self.pca_educational_criteria = {
            "concept_clarity": "Does the animation clearly show what PCA does?",
            "variance_visualization": "Is data variance effectively visualized?",
            "component_identification": "Are principal components clearly identified?",
            "dimensionality_reduction": "Is the reduction process well demonstrated?",
            "mathematical_accuracy": "Are the mathematical concepts correctly represented?"
        }
    
    def analyze_animation(self, 
                         scene_data: Dict[str, Any], 
                         generated_code: str,
                         topic: str = "pca") -> AnimationAnalysis:
        """Analyze an animation and provide comprehensive feedback."""
        feedback_items = []
        
        # Analyze different aspects
        feedback_items.extend(self._analyze_timing(scene_data))
        feedback_items.extend(self._analyze_visual_clarity(scene_data))
        feedback_items.extend(self._analyze_educational_value(scene_data, topic))
        feedback_items.extend(self._analyze_animation_flow(scene_data))
        feedback_items.extend(self._analyze_code_quality(generated_code))
        
        # Calculate overall score
        overall_score = self._calculate_overall_score(feedback_items)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(feedback_items, scene_data)
        
        # Determine approval status
        approval_status = self._determine_approval_status(overall_score, feedback_items)
        
        return AnimationAnalysis(
            overall_score=overall_score,
            feedback_items=feedback_items,
            recommended_changes=recommendations,
            approval_status=approval_status
        )
    
    def _analyze_timing(self, scene_data: Dict[str, Any]) -> List[CriticFeedback]:
        """Analyze animation timing."""
        feedback = []
        duration = scene_data.get("duration", 0)
        elements = scene_data.get("elements", [])
        
        # Check overall duration
        if duration < 5:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TIMING,
                score=4.0,
                feedback="Scene duration is too short for effective learning",
                suggestions=["Increase scene duration to at least 8-10 seconds",
                           "Add more time for concept absorption"],
                severity="medium"
            ))
        elif duration > 30:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TIMING,
                score=5.0,
                feedback="Scene duration might be too long, risking viewer attention",
                suggestions=["Consider breaking into multiple shorter scenes",
                           "Add more dynamic elements to maintain engagement"],
                severity="low"
            ))
        else:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TIMING,
                score=8.0,
                feedback="Scene duration is appropriate for the content",
                suggestions=[],
                severity="low"
            ))
        
        # Analyze element timing distribution
        if len(elements) > 0:
            avg_element_time = duration / len(elements)
            if avg_element_time < 1.0:
                feedback.append(CriticFeedback(
                    aspect=CriticAspect.TIMING,
                    score=5.0,
                    feedback="Elements appear too quickly for comprehension",
                    suggestions=["Increase time between element appearances",
                               "Add pauses for concept processing"],
                    severity="medium"
                ))
        
        return feedback
    
    def _analyze_visual_clarity(self, scene_data: Dict[str, Any]) -> List[CriticFeedback]:
        """Analyze visual clarity and aesthetics."""
        feedback = []
        elements = scene_data.get("elements", [])
        
        # Check element count
        if len(elements) > 15:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.VISUAL_CLARITY,
                score=4.0,
                feedback="Too many visual elements may cause cognitive overload",
                suggestions=["Reduce number of simultaneous elements",
                           "Group related elements together",
                           "Use progressive disclosure"],
                severity="high"
            ))
        elif len(elements) < 3:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.VISUAL_CLARITY,
                score=6.0,
                feedback="Scene might benefit from more visual elements",
                suggestions=["Add supporting visual elements",
                           "Include labels or annotations"],
                severity="low"
            ))
        else:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.VISUAL_CLARITY,
                score=8.5,
                feedback="Good balance of visual elements",
                suggestions=[],
                severity="low"
            ))
        
        # Check color usage
        colors_used = set()
        for element in elements:
            if hasattr(element, 'properties') and 'color' in element.properties:
                colors_used.add(element.properties['color'])
        
        if len(colors_used) > 6:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.VISUAL_CLARITY,
                score=5.0,
                feedback="Too many colors may reduce visual clarity",
                suggestions=["Limit color palette to 4-5 colors",
                           "Use color consistently for similar concepts"],
                severity="medium"
            ))
        
        return feedback
    
    def _analyze_educational_value(self, scene_data: Dict[str, Any], topic: str) -> List[CriticFeedback]:
        """Analyze educational effectiveness."""
        feedback = []
        
        if topic.lower() == "pca":
            feedback.extend(self._analyze_pca_educational_value(scene_data))
        else:
            feedback.extend(self._analyze_generic_educational_value(scene_data))
        
        return feedback
    
    def _analyze_pca_educational_value(self, scene_data: Dict[str, Any]) -> List[CriticFeedback]:
        """Analyze PCA-specific educational value."""
        feedback = []
        scene_name = scene_data.get("name", "")
        elements = scene_data.get("elements", [])
        element_types = [getattr(e, 'element_type', str(e)) for e in elements]
        
        # Check for key PCA concepts
        if "data_introduction" in scene_name:
            has_data_points = any("data_point" in str(e) or "point" in str(e) for e in element_types)
            has_axes = any("axis" in str(e) for e in element_types)
            
            if has_data_points and has_axes:
                feedback.append(CriticFeedback(
                    aspect=CriticAspect.EDUCATIONAL_VALUE,
                    score=9.0,
                    feedback="Excellent foundation - shows data in coordinate system",
                    suggestions=[],
                    severity="low"
                ))
            else:
                feedback.append(CriticFeedback(
                    aspect=CriticAspect.EDUCATIONAL_VALUE,
                    score=5.0,
                    feedback="Missing key elements for data introduction",
                    suggestions=["Add coordinate axes", "Ensure data points are visible"],
                    severity="high"
                ))
        
        elif "variance" in scene_name:
            has_variance_viz = any("ellipse" in str(e) or "variance" in str(e) for e in element_types)
            if not has_variance_viz:
                feedback.append(CriticFeedback(
                    aspect=CriticAspect.EDUCATIONAL_VALUE,
                    score=4.0,
                    feedback="Variance concept not clearly visualized",
                    suggestions=["Add variance ellipse or spread indicator",
                               "Show data distribution visually"],
                    severity="high"
                ))
        
        elif "pca_transformation" in scene_name:
            has_components = any("arrow" in str(e) or "component" in str(e) for e in element_types)
            if not has_components:
                feedback.append(CriticFeedback(
                    aspect=CriticAspect.EDUCATIONAL_VALUE,
                    score=3.0,
                    feedback="Principal components not shown",
                    suggestions=["Add arrows showing principal component directions",
                               "Highlight maximum variance directions"],
                    severity="high"
                ))
        
        return feedback
    
    def _analyze_generic_educational_value(self, scene_data: Dict[str, Any]) -> List[CriticFeedback]:
        """Analyze generic educational value."""
        feedback = []
        
        narration = scene_data.get("narration", "")
        if len(narration) < 20:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.EDUCATIONAL_VALUE,
                score=5.0,
                feedback="Narration is too brief for effective learning",
                suggestions=["Expand narration with more explanation",
                           "Add context and examples"],
                severity="medium"
            ))
        
        return feedback
    
    def _analyze_animation_flow(self, scene_data: Dict[str, Any]) -> List[CriticFeedback]:
        """Analyze animation flow and transitions."""
        feedback = []
        elements = scene_data.get("elements", [])
        
        # Check for animation variety
        animation_types = set()
        for element in elements:
            if hasattr(element, 'animation_sequence'):
                for anim in element.animation_sequence:
                    animation_types.add(anim.get('type', 'fade_in'))
        
        if len(animation_types) < 2:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.ANIMATION_FLOW,
                score=5.0,
                feedback="Limited animation variety may reduce engagement",
                suggestions=["Add more animation types",
                           "Use different entrances for different elements"],
                severity="medium"
            ))
        else:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.ANIMATION_FLOW,
                score=8.0,
                feedback="Good variety in animations",
                suggestions=[],
                severity="low"
            ))
        
        return feedback
    
    def _analyze_code_quality(self, generated_code: str) -> List[CriticFeedback]:
        """Analyze the quality of generated Manim code."""
        feedback = []
        
        # Check code length (rough proxy for complexity)
        lines = generated_code.split('\n')
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        if len(code_lines) > 200:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TECHNICAL_ACCURACY,
                score=5.0,
                feedback="Generated code is quite complex",
                suggestions=["Consider breaking into smaller functions",
                           "Simplify animation logic where possible"],
                severity="low"
            ))
        
        # Check for common Manim patterns
        has_construct = "def construct(self):" in generated_code
        has_animations = "self.play(" in generated_code
        has_3d_setup = "ThreeDScene" in generated_code or "set_camera_orientation" in generated_code
        
        if not has_construct:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TECHNICAL_ACCURACY,
                score=2.0,
                feedback="Missing construct method",
                suggestions=["Add proper construct method"],
                severity="high"
            ))
        
        if not has_animations:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TECHNICAL_ACCURACY,
                score=3.0,
                feedback="No animations found in code",
                suggestions=["Add self.play() calls for animations"],
                severity="high"
            ))
        
        if has_3d_setup:
            feedback.append(CriticFeedback(
                aspect=CriticAspect.TECHNICAL_ACCURACY,
                score=8.0,
                feedback="Proper 3D scene setup detected",
                suggestions=[],
                severity="low"
            ))
        
        return feedback
    
    def _calculate_overall_score(self, feedback_items: List[CriticFeedback]) -> float:
        """Calculate overall score from individual feedback items."""
        if not feedback_items:
            return 5.0
        
        # Weight different aspects
        weights = {
            CriticAspect.EDUCATIONAL_VALUE: 0.3,
            CriticAspect.VISUAL_CLARITY: 0.25,
            CriticAspect.TIMING: 0.2,
            CriticAspect.ANIMATION_FLOW: 0.15,
            CriticAspect.TECHNICAL_ACCURACY: 0.1
        }
        
        weighted_score = 0
        total_weight = 0
        
        for feedback in feedback_items:
            weight = weights.get(feedback.aspect, 0.1)
            weighted_score += feedback.score * weight
            total_weight += weight
        
        return weighted_score / total_weight if total_weight > 0 else 5.0
    
    def _generate_recommendations(self, 
                                feedback_items: List[CriticFeedback], 
                                scene_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate specific recommendations for improvement."""
        recommendations = {
            "timing_adjustments": [],
            "visual_improvements": [],
            "educational_enhancements": [],
            "technical_fixes": []
        }
        
        for feedback in feedback_items:
            if feedback.severity in ["medium", "high"]:
                if feedback.aspect == CriticAspect.TIMING:
                    recommendations["timing_adjustments"].extend(feedback.suggestions)
                elif feedback.aspect == CriticAspect.VISUAL_CLARITY:
                    recommendations["visual_improvements"].extend(feedback.suggestions)
                elif feedback.aspect == CriticAspect.EDUCATIONAL_VALUE:
                    recommendations["educational_enhancements"].extend(feedback.suggestions)
                elif feedback.aspect == CriticAspect.TECHNICAL_ACCURACY:
                    recommendations["technical_fixes"].extend(feedback.suggestions)
        
        return recommendations
    
    def _determine_approval_status(self, 
                                 overall_score: float, 
                                 feedback_items: List[CriticFeedback]) -> str:
        """Determine if the animation is approved for use."""
        high_severity_issues = [f for f in feedback_items if f.severity == "high"]
        
        if overall_score >= self.quality_thresholds["excellent"] and not high_severity_issues:
            return "approved"
        elif overall_score >= self.quality_thresholds["acceptable"] and len(high_severity_issues) <= 1:
            return "needs_revision"
        else:
            return "rejected"
    
    def generate_improvement_report(self, analysis: AnimationAnalysis) -> str:
        """Generate a human-readable improvement report."""
        report = f"# Animation Analysis Report\n\n"
        report += f"**Overall Score:** {analysis.overall_score:.1f}/10\n"
        report += f"**Status:** {analysis.approval_status.upper()}\n\n"
        
        report += "## Feedback by Aspect\n\n"
        
        for aspect in CriticAspect:
            aspect_feedback = [f for f in analysis.feedback_items if f.aspect == aspect]
            if aspect_feedback:
                report += f"### {aspect.value.replace('_', ' ').title()}\n"
                for feedback in aspect_feedback:
                    report += f"- **Score:** {feedback.score}/10\n"
                    report += f"- **Feedback:** {feedback.feedback}\n"
                    if feedback.suggestions:
                        report += f"- **Suggestions:**\n"
                        for suggestion in feedback.suggestions:
                            report += f"  - {suggestion}\n"
                    report += "\n"
        
        if analysis.recommended_changes:
            report += "## Recommended Changes\n\n"
            for category, changes in analysis.recommended_changes.items():
                if changes:
                    report += f"### {category.replace('_', ' ').title()}\n"
                    for change in changes:
                        report += f"- {change}\n"
                    report += "\n"
        
        return report


def analyze_animation(scene_data: Dict[str, Any], 
                     generated_code: str, 
                     topic: str = "pca") -> AnimationAnalysis:
    """Convenience function to analyze an animation."""
    critic = AICritic()
    return critic.analyze_animation(scene_data, generated_code, topic)
