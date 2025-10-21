# ML Visualization Pipeline

An automated system for generating educational ML concept animations from text descriptions using Manim.

## Pipeline Architecture

```
Text input → ConceptParser → Scene Planner → Visual Mapper → Code Generator → Render + AI Critic → Final Animation
```

### Components

1. **ConceptParser**: Identifies key entities (variance, principal components, data points, etc.)
2. **Scene Planner**: Breaks concepts into structured scenes ("Data Intro", "PCA Transformation", etc.)
3. **Visual Mapper**: Maps abstract concepts to concrete visual elements (arrows, surfaces, dots)
4. **Code Generator**: Writes executable Manim scene code
5. **Render + AI Critic**: Analyzes and improves timing, clarity, and educational value

## Features

- 🎓 **Educational Focus**: Optimized for learning with clear narration and pacing
- 🎨 **Automatic Visualization**: Converts text to 3D animations without manual design
- 🤖 **AI-Powered Quality Control**: Iterative improvement based on educational criteria
- 🔧 **Extensible**: Easy to add new ML concepts beyond PCA
- 📊 **Comprehensive Analysis**: Detailed reports on animation quality and suggestions

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run Demo

```bash
python demo.py
```

This generates a complete PCA explanation animation from text input.

### Custom Usage

```python
from src.pipeline import VisualizationPipeline

pipeline = VisualizationPipeline()
result = pipeline.generate_visualization(
    text_input="Your ML concept explanation here...",
    topic="pca",
    max_iterations=3
)
```

## Example Output

The pipeline generates:
- **Manim code**: Executable Python files for animation
- **Analysis reports**: Detailed feedback on educational effectiveness
- **Scene breakdowns**: Structured visualization plans

## Supported Concepts

Currently optimized for **PCA (Principal Component Analysis)**:
- Data visualization in 3D space
- Variance and spread demonstration
- Principal component identification
- Dimensionality reduction projection
- Shadow/projection analogies

## Architecture Details

### ConceptParser
- Identifies mathematical entities, visual elements, and process steps
- Assigns importance scores and visual properties
- Maps relationships between concepts

### Scene Planner
- Creates educational narrative flow
- Optimizes timing and transitions
- Generates contextual narration

### Visual Mapper
- Converts abstract concepts to 3D visual elements
- Plans camera movements and animations
- Manages color schemes and styling

### Code Generator
- Produces clean, executable Manim code
- Handles 3D scene setup and animations
- Generates proper class structures

### AI Critic
- Analyzes timing, visual clarity, and educational value
- Provides specific improvement suggestions
- Iteratively refines animations

## File Structure

```
ml-visualization/
├── src/
│   ├── concept_parser.py    # Entity identification
│   ├── scene_planner.py     # Scene structuring
│   ├── visual_mapper.py     # Visual element mapping
│   ├── code_generator.py    # Manim code generation
│   ├── ai_critic.py         # Quality analysis
│   └── pipeline.py          # Main orchestrator
├── demo.py                  # Demo script
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Contributing

To add support for new ML concepts:

1. Extend `ConceptParser` with new entity mappings
2. Add scene templates in `ScenePlanner`
3. Create visual mappings in `VisualMapper`
4. Update educational criteria in `AICritic`

## License

MIT License - see LICENSE file for details.
