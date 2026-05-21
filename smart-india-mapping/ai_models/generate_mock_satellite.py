import cv2
import numpy as np
import random
import os

def generate_mock_satellite_image(output_path, image_type="urban"):
    """Generates a synthetic satellite image for testing CV module"""
    width, height = 512, 512
    img = np.zeros((height, width, 3), np.uint8)

    if image_type == "urban":
        # Base color (Grey/Concrete)
        img[:] = (180, 180, 180)
        # Add "roads" (Darker grey lines)
        for _ in range(5):
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            cv2.line(img, (x1, y1), (x2, y2), (100, 100, 100), 10)
        # Add "buildings" (Rectangles)
        for _ in range(50):
            x, y = random.randint(0, width-20), random.randint(0, height-20)
            cv2.rectangle(img, (x, y), (x+15, y+15), (150, 150, 150), -1)
    
    elif image_type == "rural":
        # Base color (Green/Soil)
        img[:] = (50, 150, 50)
        # Add "fields" (Different shades of green)
        for _ in range(20):
            x, y = random.randint(0, width-100), random.randint(0, height-100)
            cv2.rectangle(img, (x, y), (x+80, y+80), (40, random.randint(100, 200), 40), -1)
        # Add a "river" (Blue)
        points = np.array([[random.randint(0, 100), 0], [random.randint(200, 300), 250], [random.randint(400, 500), 512]])
        cv2.polylines(img, [points], False, (200, 100, 50), 20)

    cv2.imwrite(output_path, img)
    print(f"Mock satellite image saved to {output_path}")

if __name__ == "__main__":
    os.makedirs("data/images", exist_ok=True)
    generate_mock_satellite_image("data/images/urban_sample.jpg", "urban")
    generate_mock_satellite_image("data/images/rural_sample.jpg", "rural")
