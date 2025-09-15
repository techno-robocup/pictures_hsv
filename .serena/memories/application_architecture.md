# Application Architecture

## Main Components

### HSVViewer Class
The core class that handles all application functionality:

#### Key Attributes
- `image_path`: Path to the image file
- `image`: Original BGR image from OpenCV
- `hsv_image`: Converted HSV version of the image
- `clicked_pixels`: List tracking all clicked pixel HSV values
- `min_H/max_H`, `min_S/max_S`, `min_V/max_V`: Statistics tracking
- Window names: `window_name`, `info_window`, `stats_window`

#### Key Methods
- `load_image()`: Loads and validates image file, converts to HSV
- `update_statistics()`: Tracks clicked pixels and updates min/max values
- `get_average_hsv()`: Calculates average HSV from all clicked pixels
- `display_statistics()`: Creates and shows statistics window
- `reset_statistics()`: Clears all tracked data
- `remove_last_pixel()`: Removes last clicked pixel and recalculates stats
- `mouse_callback()`: Handles mouse click events on image
- `run()`: Main application loop with event handling

### Application Flow
1. Parse command line arguments (image path)
2. Check OpenCV availability
3. Create HSVViewer instance
4. Load and validate image
5. Resize if necessary
6. Create three windows (main image, info, statistics)
7. Set up mouse callback for clicks
8. Enter main event loop handling keyboard input
9. Clean up and exit

### UI Windows
- **Main Window**: Displays the image, handles mouse clicks
- **Info Window**: Shows clicked pixel position, RGB/HSV values, color sample
- **Statistics Window**: Displays aggregate statistics (averages, min/max, ranges)

### Key Libraries Usage
- **OpenCV**: Image loading, color conversion, GUI windows, event handling
- **NumPy**: Array operations for image data and statistics calculations
- **argparse**: Command line interface
- **sys/os**: System operations and file validation