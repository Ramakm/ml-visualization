# Rendering & Video Concatenation Guide

## Overview

The ML Visualization Pipeline now automatically renders all generated scenes and concatenates them into a single final video. This eliminates the need for manual rendering and video editing.

## Pipeline Workflow

### Step 7: Automatic Rendering

After generating the Manim code, the pipeline automatically:

1. **Checks for Manim**: Verifies Manim is installed
2. **Renders each scene**: Uses `manim -ql` for quick low-quality renders
3. **Saves individual videos**: Each scene is rendered separately
4. **Tracks progress**: Shows real-time rendering status

**Example output:**
```
🎬 Step 7: Rendering scenes with Manim...
   Rendering scene 1/5: DataIntroduction...
   ✅ Rendered: DataIntroduction_ManimCE_v0.19.0.mp4
   Rendering scene 2/5: VarianceExplanation...
   ✅ Rendered: VarianceExplanation_ManimCE_v0.19.0.mp4
   ...
```

### Step 8: Video Concatenation

After all scenes are rendered:

1. **Checks for ffmpeg**: Verifies ffmpeg is available
2. **Creates concat list**: Generates a file list for ffmpeg
3. **Concatenates videos**: Combines all scenes in order
4. **Saves final video**: Creates `{topic}_final.mp4`

**Example output:**
```
🎞️  Step 8: Concatenating videos into final output...
   Concatenating 5 videos...
✅ Final video saved to: demo_output/pca_final.mp4
```

## Requirements

### Manim

The pipeline uses Manim Community Edition to render scenes.

**Installation:**
```bash
pip install manim
```

**What happens if Manim is missing?**
- Pipeline continues without rendering
- Generated Manim code is still saved
- Warning message displayed
- You can manually render later

### ffmpeg

ffmpeg is used to concatenate multiple video files into one.

**Installation:**

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org) and add to PATH

**What happens if ffmpeg is missing?**
- Individual scene videos are still available
- No concatenation performed
- Warning message displayed
- Videos can be manually concatenated later

### scikit-learn

Required for PCA computations in generated code.

**Installation:**
```bash
pip install scikit-learn
```

**What happens if scikit-learn is missing?**
- Rendering will fail
- Error message shows missing dependency
- Code generation still completes successfully

## Output Structure

After running the pipeline with rendering enabled, you'll get:

```
output_directory/
├── pca_visualization.py          # Generated Manim code
├── pca_analysis_report.md        # Quality analysis report
├── pca_final.mp4                 # ✨ Final concatenated video
└── media/
    └── videos/
        └── pca_visualization/
            └── 480p15/
                ├── DataIntroduction_*.mp4
                ├── VarianceExplanation_*.mp4
                ├── PcaTransformation_*.mp4
                ├── DimensionalityReduction_*.mp4
                └── Comparison_*.mp4
```

## Video Quality Settings

By default, the pipeline uses `-ql` (quick, low quality) for faster rendering:
- **Resolution**: 480p (854x480)
- **Frame rate**: 15 fps
- **File size**: Small
- **Render time**: Fast (~10-30 seconds per scene)

### Customizing Quality

To change video quality, modify the rendering command in `pipeline.py`:

```python
# Quick low quality (default)
["manim", "-ql", ...]

# Medium quality
["manim", "-qm", ...]

# High quality
["manim", "-qh", ...]

# Production quality (4K)
["manim", "-qk", ...]
```

**Note:** Higher quality = longer render times (minutes per scene)

## Troubleshooting

### Rendering Takes Too Long

**Problem:** Scene rendering exceeds timeout

**Solution:**
- Timeout is set to 120 seconds per scene
- Increase in `pipeline.py`: `timeout=300` (5 minutes)
- Or use lower quality: `-ql` instead of `-qh`

### Video Files Not Found

**Problem:** Rendered video not located after successful render

**Possible causes:**
- Different Manim version changes output path
- Media directory structure differs

**Solution:**
Check the actual output location:
```bash
find demo_output/media -name "*.mp4"
```

### Concatenation Fails

**Problem:** ffmpeg concatenation produces errors

**Common issues:**
1. **Codec mismatch**: Videos have different codecs
   - Solution: Re-render all scenes with same quality
   
2. **Resolution mismatch**: Videos have different resolutions
   - Solution: Use consistent quality settings

3. **File path issues**: Absolute paths not found
   - Solution: Check `concat_list.txt` for correct paths

### Memory Issues

**Problem:** System runs out of memory during rendering

**Solutions:**
- Render fewer scenes at once
- Use lower quality settings
- Close other applications
- Reduce number of data points in visualization

## Manual Rendering

If automatic rendering fails, you can render manually:

### Individual Scene

```bash
manim -pql demo_output/pca_visualization.py DataIntroduction
```

### All Scenes

```bash
manim -ql demo_output/pca_visualization.py
```

### Manual Concatenation

Create `concat_list.txt`:
```
file '/path/to/video1.mp4'
file '/path/to/video2.mp4'
file '/path/to/video3.mp4'
```

Run ffmpeg:
```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy output.mp4
```

## Performance Tips

### Speed Up Rendering

1. **Use low quality**: `-ql` renders 5-10x faster than `-qh`
2. **Reduce data points**: Fewer objects = faster rendering
3. **Simplify animations**: Complex transformations take longer
4. **Disable anti-aliasing**: Add `--disable_caching` flag

### Optimize Video Size

1. **Compress after concatenation**:
```bash
ffmpeg -i pca_final.mp4 -vcodec h264 -acodec aac -b:v 1M pca_final_compressed.mp4
```

2. **Convert to web-friendly format**:
```bash
ffmpeg -i pca_final.mp4 -c:v libvpx-vp9 -crf 30 pca_final.webm
```

## Advanced Configuration

### Custom Media Directory

Change where videos are saved:

```python
pipeline = VisualizationPipeline(output_dir="custom_output")
```

### Disable Rendering

Skip automatic rendering but still generate code:

Modify `pipeline.py` or create a parameter:
```python
def generate_visualization(self, ..., auto_render=False):
    # ...
    if auto_render:
        rendered_videos = self._render_scenes(output_file, topic)
```

### Parallel Rendering

For faster processing, render scenes in parallel (advanced):

```python
from concurrent.futures import ProcessPoolExecutor

def _render_scenes_parallel(self, code_file, topic):
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(render_scene, scene) for scene in scenes]
        # Collect results...
```

## Best Practices

1. **Test with low quality first**: Verify animations before high-quality render
2. **Keep scenes short**: 5-15 seconds per scene works best
3. **Check dependencies**: Run `manim --version` and `ffmpeg -version` before starting
4. **Monitor disk space**: Videos can be large (100MB-1GB for full pipeline)
5. **Use version control**: Don't commit large video files to git

## Integration with Other Tools

### YouTube Upload

After generating the final video:

```bash
# Add metadata
ffmpeg -i pca_final.mp4 -metadata title="PCA Explained" \
       -metadata description="Educational PCA animation" \
       -c copy pca_final_with_metadata.mp4
```

### Social Media

Create clips from specific scenes:

```bash
# Extract first 10 seconds
ffmpeg -i pca_final.mp4 -t 10 -c copy pca_clip.mp4

# Create GIF preview
ffmpeg -i pca_final.mp4 -t 5 -vf "scale=640:-1" preview.gif
```

## Summary

The automatic rendering and concatenation feature:
- ✅ Saves time by automating the entire process
- ✅ Produces a single, shareable final video
- ✅ Maintains high quality with configurable settings
- ✅ Gracefully handles missing dependencies
- ✅ Provides detailed progress and error messages

For most users, simply running `python demo.py` is enough to get a complete, rendered video explanation of PCA!
