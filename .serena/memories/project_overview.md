# HSV Image Viewer Project Overview

## Project Purpose
This is a simple Python application that allows users to view HSV (Hue, Saturation, Value) color values of pixels in images using OpenCV. The tool provides an interactive GUI where users can click on image pixels to see their HSV values, track statistics across multiple clicks, and analyze color ranges.

## Key Features
- Interactive image viewer with HSV value display
- Click-based pixel analysis
- Statistics tracking (min/max/average HSV values)
- Real-time statistics display
- Color sample visualization
- Image resizing for large images
- Keyboard shortcuts for resetting and managing statistics

## Tech Stack
- **Language**: Python 3
- **Main Dependencies**: 
  - OpenCV (cv2) >= 4.5.0 for image processing and GUI
  - NumPy >= 1.19.0 for array operations
  - argparse (built-in) for command line interface
- **Environment Management**: direnv with python layout
- **Version Control**: Git

## Project Structure
```
.
├── hsv_viewer.py          # Main application file
├── requirements.txt       # Python dependencies
├── .envrc                # direnv configuration
├── .gitignore            # Git ignore rules
└── .serena/              # Serena configuration directory
```

The project is a single-file application with the main `HSVViewer` class containing all functionality.