#!/usr/bin/env python3
"""
HSV Image Viewer
A simple application to view HSV values of pixels in an image using OpenCV.
Click on any pixel to see its HSV values.
"""

import cv2
import numpy as np
import argparse
import sys
import os

class HSVViewer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.hsv_image = None
        self.window_name = "HSV Image Viewer"
        self.info_window = "HSV Info"
        self.stats_window = "HSV Statistics"

        # Track clicked pixels
        self.clicked_pixels = []

        # Initialize min/max values
        self.min_H = 179
        self.max_H = 0
        self.min_S = 255
        self.max_S = 0
        self.min_V = 255
        self.max_V = 0

    def load_image(self):
        """Load and validate the image file."""
        if not os.path.exists(self.image_path):
            print(f"Error: Image file '{self.image_path}' not found.")
            return False

        self.image = cv2.imread(self.image_path)
        if self.image is None:
            print(f"Error: Could not load image '{self.image_path}'. Please check if it's a valid image file.")
            return False

        # Convert to HSV
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return True

    def update_statistics(self, h, s, v):
        """Update min/max statistics and add pixel to tracked list."""
        # Add to clicked pixels list
        self.clicked_pixels.append((h, s, v))

        # Update min/max values
        if len(self.clicked_pixels) == 1:
            # First pixel - initialize min/max with actual values
            self.min_H = self.max_H = h
            self.min_S = self.max_S = s
            self.min_V = self.max_V = v
        else:
            # Subsequent pixels - update min/max
            self.min_H = min(self.min_H, h)
            self.max_H = max(self.max_H, h)
            self.min_S = min(self.min_S, s)
            self.max_S = max(self.max_S, s)
            self.min_V = min(self.min_V, v)
            self.max_V = max(self.max_V, v)

    def get_average_hsv(self):
        """Calculate average HSV values from all clicked pixels."""
        if not self.clicked_pixels:
            return 0, 0, 0

        h_values = [int(pixel[0]) for pixel in self.clicked_pixels]
        s_values = [int(pixel[1]) for pixel in self.clicked_pixels]
        v_values = [int(pixel[2]) for pixel in self.clicked_pixels]

        avg_h = sum(h_values) / len(h_values)
        avg_s = sum(s_values) / len(s_values)
        avg_v = sum(v_values) / len(v_values)

        return int(avg_h), int(avg_s), int(avg_v)

    def display_statistics(self):
        """Create and display statistics window."""
        stats_img = np.zeros((300, 500, 3), dtype=np.uint8)

        if not self.clicked_pixels:
            cv2.putText(stats_img, "No pixels clicked yet", (50, 150),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow(self.stats_window, stats_img)
            return

        # Get statistics
        avg_h, avg_s, avg_v = self.get_average_hsv()
        num_pixels = len(self.clicked_pixels)

        # Display title
        cv2.putText(stats_img, f"Statistics ({num_pixels} pixels)", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Display averages
        cv2.putText(stats_img, "AVERAGES:", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 100), 2)
        cv2.putText(stats_img, f"H: {avg_h}", (20, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"S: {avg_s}", (20, 120),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"V: {avg_v}", (20, 140),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display minimums
        cv2.putText(stats_img, "MINIMUMS:", (150, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 255), 2)
        cv2.putText(stats_img, f"H: {self.min_H}", (160, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"S: {self.min_S}", (160, 120),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"V: {self.min_V}", (160, 140),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display maximums
        cv2.putText(stats_img, "MAXIMUMS:", (290, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 100, 100), 2)
        cv2.putText(stats_img, f"H: {self.max_H}", (300, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"S: {self.max_S}", (300, 120),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"V: {self.max_V}", (300, 140),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display ranges
        cv2.putText(stats_img, "RANGES:", (10, 190),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 100), 2)
        cv2.putText(stats_img, f"H: {self.max_H - self.min_H}", (20, 220),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"S: {self.max_S - self.min_S}", (20, 240),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(stats_img, f"V: {self.max_V - self.min_V}", (20, 260),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Instructions
        cv2.putText(stats_img, "Press 'r' to reset statistics", (150, 220),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
        cv2.putText(stats_img, "Press 'c' to clear last click", (150, 240),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

        cv2.imshow(self.stats_window, stats_img)

    def reset_statistics(self):
        """Reset all statistics and pixel tracking."""
        self.clicked_pixels = []
        self.min_H = 179
        self.max_H = 0
        self.min_S = 255
        self.max_S = 0
        self.min_V = 255
        self.max_V = 0
        print("Statistics reset!")

    def remove_last_pixel(self):
        """Remove the last clicked pixel from statistics."""
        if self.clicked_pixels:
            removed = self.clicked_pixels.pop()
            print(f"Removed last pixel: HSV({removed[0]}, {removed[1]}, {removed[2]})")

            # Recalculate min/max values
            if self.clicked_pixels:
                h_values = [pixel[0] for pixel in self.clicked_pixels]
                s_values = [pixel[1] for pixel in self.clicked_pixels]
                v_values = [pixel[2] for pixel in self.clicked_pixels]

                self.min_H = min(h_values)
                self.max_H = max(h_values)
                self.min_S = min(s_values)
                self.max_S = max(s_values)
                self.min_V = min(v_values)
                self.max_V = max(v_values)
            else:
                self.reset_statistics()
        else:
            print("No pixels to remove!")

    def mouse_callback(self, event, x, y, flags, param):
        """Handle mouse click events to display HSV values."""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Get HSV values at clicked position
            h, s, v = self.hsv_image[y, x]
            b, g, r = self.image[y, x]

            # Update statistics
            self.update_statistics(h, s, v)

            # Create info display
            info_img = np.zeros((200, 400, 3), dtype=np.uint8)

            # Display RGB values
            cv2.putText(info_img, f"Position: ({x}, {y})", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(info_img, f"RGB: ({r}, {g}, {b})", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(info_img, f"HSV: ({h}, {s}, {v})", (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # Display HSV explanation
            cv2.putText(info_img, f"Hue: {h} (0-179)", (10, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 100), 1)
            cv2.putText(info_img, f"Saturation: {s} (0-255)", (10, 140),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 100), 1)
            cv2.putText(info_img, f"Value: {v} (0-255)", (10, 160),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 100), 1)

            # Show color sample
            color_sample = np.full((50, 100, 3), (b, g, r), dtype=np.uint8)
            info_img[120:170, 250:350] = color_sample

            cv2.imshow(self.info_window, info_img)

            # Update statistics display
            self.display_statistics()

            # Print to console as well
            avg_h, avg_s, avg_v = self.get_average_hsv()
            print(f"Position: ({x}, {y}) | RGB: ({r}, {g}, {b}) | HSV: ({h}, {s}, {v})")
            print(f"Pixels clicked: {len(self.clicked_pixels)} | Average HSV: ({avg_h}, {avg_s}, {avg_v})")
            print(f"All S values: {[pixel[1] for pixel in self.clicked_pixels]}")
            print(f"All V values: {[pixel[2] for pixel in self.clicked_pixels]}")

    def run(self):
        """Main application loop."""
        if not self.load_image():
            return False

        # Resize image if too large
        height, width = self.image.shape[:2]
        max_width, max_height = 1200, 800

        if width > max_width or height > max_height:
            scale = min(max_width/width, max_height/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            self.image = cv2.resize(self.image, (new_width, new_height))
            self.hsv_image = cv2.resize(self.hsv_image, (new_width, new_height))

        # Create windows
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.info_window, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.stats_window, cv2.WINDOW_AUTOSIZE)

        # Set mouse callback
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

        # Create initial info display
        info_img = np.zeros((200, 400, 3), dtype=np.uint8)
        cv2.putText(info_img, "Click on the image to see", (50, 80),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(info_img, "HSV values at that point", (50, 110),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow(self.info_window, info_img)

        # Create initial statistics display
        self.display_statistics()

        print(f"Loaded image: {self.image_path}")
        print(f"Image size: {self.image.shape[1]}x{self.image.shape[0]}")
        print("Instructions:")
        print("- Click on any pixel in the image to see its HSV values")
        print("- Press 'q' or ESC to quit")
        print("- Press 'r' to reset statistics")
        print("- Press 'c' to clear last clicked pixel")
        print("- Press 's' to save current HSV info")

        while True:
            cv2.imshow(self.window_name, self.image)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                break
            elif key == ord('r'):
                self.reset_statistics()
                self.display_statistics()
            elif key == ord('c'):
                self.remove_last_pixel()
                self.display_statistics()
            elif key == ord('s'):
                print("Saving functionality not implemented yet")

        cv2.destroyAllWindows()
        return True

def main():
    parser = argparse.ArgumentParser(description='HSV Image Viewer - View HSV values of image pixels')
    parser.add_argument('image', help='Path to the image file')
    parser.add_argument('--version', action='version', version='HSV Viewer 1.0')

    args = parser.parse_args()

    # Check if OpenCV is available
    try:
        cv2_version = cv2.__version__
        print(f"OpenCV version: {cv2_version}")
    except:
        print("Error: OpenCV (cv2) is not installed. Please install it with: pip install opencv-python")
        sys.exit(1)

    viewer = HSVViewer(args.image)
    if not viewer.run():
        sys.exit(1)

if __name__ == "__main__":
    main()