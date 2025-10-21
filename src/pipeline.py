"""
Main Pipeline: Orchestrates the complete visualization generation process.
"""
from typing import List, Dict, Any, Optional
import os
from pathlib import Path

from concept_parser import ConceptParser, parse_pca_concept
from scene_planner import ScenePlanner, plan_pca_visualization
from visual_mapper import VisualMapper, map_scenes_to_visuals
from code_generator import ManimeCodeGenerator, generate_manim_code
from ai_critic import AICritic, analyze_animation


class VisualizationPipeline:
    """Complete pipeline for generating ML concept visualizations."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialize components
        self.concept_parser = ConceptParser()
        self.scene_planner = ScenePlanner()
        self.visual_mapper = VisualMapper()
        self.code_generator = ManimeCodeGenerator()
        self.ai_critic = AICritic()
        
        # Pipeline state
        self.current_concepts = []
        self.current_scenes = []
        self.current_visuals = []
        self.current_code = ""
        self.current_analysis = None
    
    def generate_visualization(self, 
                             text_input: str, 
                             topic: str = "pca",
                             max_iterations: int = 3) -> Dict[str, Any]:
        """Generate complete visualization from text input."""
        print(f"🚀 Starting visualization pipeline for: {topic}")
        
        # Step 1: Parse concepts
        print("📝 Step 1: Parsing concepts...")
        self.current_concepts = self.concept_parser.parse_text(text_input)
        print(f"   Found {len(self.current_concepts)} concepts")
        
        # Step 2: Plan scenes
        print("🎬 Step 2: Planning scenes...")
        self.current_scenes = self.scene_planner.plan_scenes(self.current_concepts, topic)
        print(f"   Planned {len(self.current_scenes)} scenes")
        
        # Step 3: Map to visuals
        print("🎨 Step 3: Mapping to visual elements...")
        self.current_visuals = self.visual_mapper.map_scenes_to_visuals(self.current_scenes)
        print(f"   Created visual mappings for {len(self.current_visuals)} scenes")
        
        # Step 4: Generate code
        print("💻 Step 4: Generating Manim code...")
        output_file = self.output_dir / f"{topic}_visualization.py"
        self.current_code = self.code_generator.generate_complete_file(
            self.current_visuals, 
            str(output_file)
        )
        print(f"   Generated code saved to: {output_file}")
        
        # Step 5: AI Critic analysis and iteration
        print("🤖 Step 5: AI Critic analysis...")
        iteration = 0
        
        while iteration < max_iterations:
            # Analyze each scene
            scene_analyses = []
            for i, scene_visual in enumerate(self.current_visuals):
                analysis = self.ai_critic.analyze_animation(
                    scene_visual, 
                    self.current_code, 
                    topic
                )
                scene_analyses.append(analysis)
                
                print(f"   Scene {i+1} ({scene_visual['name']}): {analysis.overall_score:.1f}/10 - {analysis.approval_status}")
            
            # Check if all scenes are approved
            all_approved = all(analysis.approval_status == "approved" for analysis in scene_analyses)
            
            if all_approved:
                print("✅ All scenes approved!")
                break
            
            # Apply improvements
            print(f"🔧 Iteration {iteration + 1}: Applying improvements...")
            self._apply_improvements(scene_analyses)
            
            # Regenerate code
            output_file = self.output_dir / f"{topic}_visualization_v{iteration + 2}.py"
            self.current_code = self.code_generator.generate_complete_file(
                self.current_visuals,
                str(output_file)
            )
            
            iteration += 1
        
        # Step 6: Generate final report
        print("📊 Step 6: Generating final report...")
        report = self._generate_final_report(scene_analyses, topic)
        report_file = self.output_dir / f"{topic}_analysis_report.md"
        
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"📋 Analysis report saved to: {report_file}")
        
        # Return results
        result = {
            "concepts": self.current_concepts,
            "scenes": self.current_scenes,
            "visuals": self.current_visuals,
            "code": self.current_code,
            "analyses": scene_analyses,
            "output_files": {
                "code": str(output_file),
                "report": str(report_file)
            },
            "pipeline_success": all_approved
        }
        
        print("🎉 Pipeline completed!")
        return result
    
    def _apply_improvements(self, analyses: List[Any]) -> None:
        """Apply improvements based on AI critic feedback."""
        for i, analysis in enumerate(analyses):
            if analysis.approval_status != "approved":
                scene_visual = self.current_visuals[i]
                recommendations = analysis.recommended_changes
                
                # Apply timing adjustments
                if recommendations.get("timing_adjustments"):
                    self._adjust_timing(scene_visual, recommendations["timing_adjustments"])
                
                # Apply visual improvements
                if recommendations.get("visual_improvements"):
                    self._improve_visuals(scene_visual, recommendations["visual_improvements"])
                
                # Apply educational enhancements
                if recommendations.get("educational_enhancements"):
                    self._enhance_education(scene_visual, recommendations["educational_enhancements"])
    
    def _adjust_timing(self, scene_visual: Dict[str, Any], adjustments: List[str]) -> None:
        """Apply timing adjustments to a scene."""
        current_duration = scene_visual.get("duration", 10)
        
        for adjustment in adjustments:
            if "increase" in adjustment.lower() and "duration" in adjustment.lower():
                scene_visual["duration"] = min(current_duration * 1.3, 25)  # Cap at 25 seconds
            elif "decrease" in adjustment.lower() and "duration" in adjustment.lower():
                scene_visual["duration"] = max(current_duration * 0.8, 5)   # Minimum 5 seconds
    
    def _improve_visuals(self, scene_visual: Dict[str, Any], improvements: List[str]) -> None:
        """Apply visual improvements to a scene."""
        elements = scene_visual.get("elements", [])
        
        for improvement in improvements:
            if "reduce" in improvement.lower() and "elements" in improvement.lower():
                # Remove some elements if too many
                if len(elements) > 10:
                    scene_visual["elements"] = elements[:10]
            elif "add" in improvement.lower() and ("label" in improvement.lower() or "annotation" in improvement.lower()):
                # Add text labels (simplified)
                scene_visual["needs_labels"] = True
    
    def _enhance_education(self, scene_visual: Dict[str, Any], enhancements: List[str]) -> None:
        """Apply educational enhancements to a scene."""
        for enhancement in enhancements:
            if "narration" in enhancement.lower():
                # Extend narration
                current_narration = scene_visual.get("narration", "")
                if len(current_narration) < 50:
                    scene_visual["narration"] = current_narration + " This concept is fundamental to understanding the underlying mathematical principles."
    
    def _generate_final_report(self, analyses: List[Any], topic: str) -> str:
        """Generate comprehensive final report."""
        report = f"# {topic.upper()} Visualization Pipeline Report\n\n"
        
        # Overall statistics
        total_scenes = len(analyses)
        approved_scenes = sum(1 for a in analyses if a.approval_status == "approved")
        avg_score = sum(a.overall_score for a in analyses) / len(analyses) if analyses else 0
        
        report += f"## Summary\n\n"
        report += f"- **Total Scenes:** {total_scenes}\n"
        report += f"- **Approved Scenes:** {approved_scenes}/{total_scenes}\n"
        report += f"- **Average Score:** {avg_score:.1f}/10\n"
        report += f"- **Overall Status:** {'✅ APPROVED' if approved_scenes == total_scenes else '⚠️ NEEDS REVISION'}\n\n"
        
        # Individual scene reports
        report += f"## Scene Analysis\n\n"
        for i, analysis in enumerate(analyses):
            scene_name = self.current_visuals[i]["name"]
            report += f"### Scene {i+1}: {scene_name}\n"
            report += self.ai_critic.generate_improvement_report(analysis)
            report += "\n---\n\n"
        
        # Concepts identified
        report += f"## Identified Concepts\n\n"
        for concept in self.current_concepts:
            report += f"- **{concept.name}** ({concept.concept_type.value}): {concept.description}\n"
        
        report += f"\n## Generated Files\n\n"
        report += f"- Manim Code: `{topic}_visualization.py`\n"
        report += f"- Analysis Report: `{topic}_analysis_report.md`\n\n"
        
        report += f"## Usage Instructions\n\n"
        report += f"To render the animation:\n"
        report += f"```bash\n"
        report += f"manim -pql {topic}_visualization.py\n"
        report += f"```\n\n"
        report += f"To render specific scenes:\n"
        report += f"```bash\n"
        for i, scene_visual in enumerate(self.current_visuals):
            class_name = ''.join(word.capitalize() for word in scene_visual["name"].split('_'))
            report += f"manim -pql {topic}_visualization.py {class_name}\n"
        report += f"```\n"
        
        return report
    
    def quick_demo(self, demo_text: str = None) -> Dict[str, Any]:
        """Run a quick demo of the pipeline."""
        if demo_text is None:
            demo_text = """
            PCA finds the principal components that capture the maximum variance in the data.
            We start with data points in high-dimensional space, then project them onto 
            lower-dimensional subspaces defined by the eigenvectors of the covariance matrix.
            The shadow cast by the data shows how dimensionality reduction preserves 
            the most important patterns while reducing storage requirements.
            """
        
        return self.generate_visualization(demo_text, "pca", max_iterations=2)


def run_pca_pipeline(text_input: str, output_dir: str = "output") -> Dict[str, Any]:
    """Convenience function to run the complete PCA visualization pipeline."""
    pipeline = VisualizationPipeline(output_dir)
    return pipeline.generate_visualization(text_input, "pca")
