import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from satellite_analysis import SatelliteAnalyzer

def test():
    # Change to project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    
    analyzer = SatelliteAnalyzer()
    
    print("Testing Urban Analysis...")
    urban_res = analyzer.detect_urban_areas("data/images/urban_sample.jpg")
    print(f"Result: {urban_res}")
    
    print("\nTesting Rural Analysis...")
    rural_res = analyzer.analyze_crop_health("data/images/rural_sample.jpg")
    print(f"Result: {rural_res}")

if __name__ == "__main__":
    test()
