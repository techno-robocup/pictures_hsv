# Code Style and Conventions

## General Style
- **Python Version**: Python 3 (shebang: `#!/usr/bin/env python3`)
- **Code Organization**: Single-file application with class-based structure
- **Naming Convention**: 
  - snake_case for variables, functions, and methods
  - PascalCase for class names (e.g., `HSVViewer`)
  - Descriptive variable names (e.g., `clicked_pixels`, `stats_window`)

## Documentation Style
- **Module Docstring**: Triple-quoted docstring at file start with description
- **Method Docstrings**: Triple-quoted docstrings for all methods explaining purpose
- **Comments**: Inline comments for complex logic and explanations

## Code Structure Patterns
- **Class Design**: Single main class (`HSVViewer`) with clear separation of concerns
- **Method Organization**: Logical grouping of related functionality
  - Initialization and setup methods
  - Statistics and data management methods  
  - Display and UI methods
  - Event handling methods
  - Main execution method

## Import Organization
- Standard library imports first (argparse, sys, os)
- Third-party imports second (cv2, numpy)
- Clean, single-line imports

## Variable Naming Patterns
- UI elements use descriptive names: `window_name`, `info_window`, `stats_window`
- Data tracking uses clear names: `clicked_pixels`, `min_H`, `max_H`
- OpenCV/image data: `image`, `hsv_image`

## Error Handling
- File existence checks with clear error messages
- Try-catch for OpenCV availability checking
- Graceful handling of image loading failures