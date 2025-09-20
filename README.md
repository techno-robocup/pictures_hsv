# HSV Image Viewer

A simple Python application to view HSV (Hue, Saturation, Value) values of pixels in an image using OpenCV. Click on any pixel to see its HSV values and track statistics across multiple clicks.

## Features

- **Interactive HSV Analysis**: Click on any pixel to view its HSV and RGB values
- **Real-time Statistics**: Track minimum, maximum, and average HSV values across clicked pixels
- **Multiple Display Windows**:
  - Main image viewer
  - HSV info panel showing clicked pixel details
  - Statistics panel showing aggregated data
- **Statistical Analysis**: View ranges and averages for all clicked pixels
- **Undo/Reset Functionality**: Remove last clicked pixel or reset all statistics
- **Auto-resize**: Large images are automatically resized to fit screen

## Requirements

- Python 3.6+
- OpenCV 4.5.0+
- NumPy 1.19.0+

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python hsv_viewer.py <image_path>
```

### Example
```bash
python hsv_viewer.py my_image.jpg
```

### Controls

- **Left Click**: View HSV values at clicked position
- **'q' or ESC**: Quit application
- **'r'**: Reset all statistics
- **'c'**: Clear last clicked pixel
- **'s'**: Save current HSV info (not yet implemented)

### Command Line Options

- `--version`: Show version information
- `-h, --help`: Show help message

## Output Information

For each clicked pixel, the application displays:

- **Position**: X, Y coordinates
- **RGB Values**: Red, Green, Blue values (0-255)
- **HSV Values**:
  - Hue (0-179)
  - Saturation (0-255)
  - Value/Brightness (0-255)

### Statistics Panel

The statistics window shows:
- **Averages**: Mean HSV values across all clicked pixels
- **Minimums**: Lowest HSV values encountered
- **Maximums**: Highest HSV values encountered
- **Ranges**: Difference between max and min values

## Version

HSV Viewer 1.0
