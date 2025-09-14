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

    def mouse_callback(self, event, x, y, flags, param):
        """Handle mouse click events to display HSV values."""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Get HSV values at clicked position
            h, s, v = self.hsv_image[y, x]
            b, g, r = self.image[y, x]

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

            # Print to console as well
            print(f"Position: ({x}, {y}) | RGB: ({r}, {g}, {b}) | HSV: ({h}, {s}, {v})")

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

        # Set mouse callback
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

        # Create initial info display
        info_img = np.zeros((200, 400, 3), dtype=np.uint8)
        cv2.putText(info_img, "Click on the image to see", (50, 80),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(info_img, "HSV values at that point", (50, 110),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow(self.info_window, info_img)

        print(f"Loaded image: {self.image_path}")
        print(f"Image size: {self.image.shape[1]}x{self.image.shape[0]}")
        print("Instructions:")
        print("- Click on any pixel in the image to see its HSV values")
        print("- Press 'q' or ESC to quit")
        print("- Press 's' to save current HSV info")

        while True:
            cv2.imshow(self.window_name, self.image)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                break
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