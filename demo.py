#!/usr/bin/env python3
"""
Demo script for the ML Visualization Pipeline
Demonstrates the complete process: Text → Concepts → Scenes → Visuals → Code → Analysis
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.pipeline import VisualizationPipeline


def demo_pca_explanation():
    """Demo: Generate PCA explanation visualization."""
    print("=" * 60)
    print("🎓 PCA EXPLANATION VISUALIZATION DEMO")
    print("=" * 60)
    
    # Input text explaining PCA
    pca_explanation = """
    Principal Component Analysis (PCA) is a dimensionality reduction technique that finds 
    the directions of maximum variance in high-dimensional data. 
    
    Starting with a dataset of data points scattered in 3D space, PCA identifies the 
    principal components - the axes along which the data varies the most. The first 
    principal component captures the direction of maximum variance, while subsequent 
    components capture decreasing amounts of variance and are orthogonal to previous ones.
    
    The key insight is that we can project our high-dimensional data onto these principal 
    components to create a lower-dimensional representation. This projection is like 
    casting a shadow of the 3D data onto a 2D plane, preserving the most important 
    patterns while reducing storage requirements and computational complexity.
    
    The eigenvalues tell us how much variance each component captures, helping us decide 
    how many dimensions to keep. This transformation allows us to visualize and analyze 
    high-dimensional data more effectively.
    """
    
    # Initialize pipeline
    pipeline = VisualizationPipeline(output_dir="demo_output")
    
    # Run the complete pipeline
    result = pipeline.generate_visualization(
        text_input=pca_explanation,
        topic="pca",
        max_iterations=2
    )
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 PIPELINE RESULTS")
    print("=" * 60)
    
    print(f"\n✨ Concepts Identified: {len(result['concepts'])}")
    for concept in result['concepts'][:5]:  # Show top 5
        print(f"   • {concept.name} ({concept.concept_type.value}) - Score: {concept.importance_score:.2f}")
    
    print(f"\n🎬 Scenes Planned: {len(result['scenes'])}")
    for scene in result['scenes']:
        print(f"   • {scene.name} ({scene.duration}s) - {len(scene.elements)} elements")
    
    print(f"\n🎨 Visual Scenes: {len(result['visuals'])}")
    for visual in result['visuals']:
        print(f"   • {visual['name']} - {len(visual['elements'])} visual elements")
    
    print(f"\n🤖 AI Analysis:")
    for i, analysis in enumerate(result['analyses']):
        scene_name = result['visuals'][i]['name']
        print(f"   • {scene_name}: {analysis.overall_score:.1f}/10 ({analysis.approval_status})")
    
    print(f"\n📁 Output Files:")
    for file_type, file_path in result['output_files'].items():
        if file_type == 'scene_videos' and file_path:
            print(f"   • {file_type}: {len(file_path)} videos")
        elif file_path:
            print(f"   • {file_type}: {file_path}")
    
    success = "✅ SUCCESS" if result['pipeline_success'] else "⚠️ NEEDS IMPROVEMENT"
    print(f"\n🎯 Pipeline Status: {success}")
    
    if result['output_files'].get('final_video'):
        print(f"\n🎥 Final Video: {result['output_files']['final_video']}")
        print(f"   Watch your complete PCA explanation animation!")
    
    return result


def demo_quick_test():
    """Demo: Quick test with minimal input."""
    print("\n" + "=" * 60)
    print("⚡ QUICK TEST DEMO")
    print("=" * 60)
    
    pipeline = VisualizationPipeline(output_dir="quick_test_output")
    
    # Simple input
    simple_text = "PCA reduces dimensionality by finding principal components with maximum variance."
    
    result = pipeline.generate_visualization(
        text_input=simple_text,
        topic="pca",
        max_iterations=1
    )
    
    print(f"\n📝 Input: {simple_text}")
    print(f"🔍 Concepts found: {len(result['concepts'])}")
    print(f"🎬 Scenes created: {len(result['scenes'])}")
    print(f"💻 Code generated: {len(result['code'])} characters")
    
    return result


def show_generated_code_sample(result):
    """Show a sample of the generated Manim code."""
    print("\n" + "=" * 60)
    print("💻 GENERATED CODE SAMPLE")
    print("=" * 60)
    
    code_lines = result['code'].split('\n')
    
    # Find the first class definition
    class_start = None
    for i, line in enumerate(code_lines):
        if line.strip().startswith('class ') and 'Scene' in line:
            class_start = i
            break
    
    if class_start:
        # Show first 30 lines of the first scene class
        sample_lines = code_lines[class_start:class_start + 30]
        print("```python")
        for line in sample_lines:
            print(line)
        print("...")
        print("```")
    else:
        print("No scene class found in generated code.")


def main():
    """Run all demos."""
    print("🚀 ML VISUALIZATION PIPELINE DEMO")
    print("Generating educational animations from text descriptions")
    
    try:
        # Run main PCA demo
        pca_result = demo_pca_explanation()
        
        # Show code sample
        show_generated_code_sample(pca_result)
        
        # Run quick test
        quick_result = demo_quick_test()
        
        print("\n" + "=" * 60)
        print("🎉 DEMO COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Install Manim: pip install manim")
        print("2. Run generated code: manim -pql demo_output/pca_visualization.py")
        print("3. Check output videos in media/ folder")
        print("4. Review analysis reports in demo_output/")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
