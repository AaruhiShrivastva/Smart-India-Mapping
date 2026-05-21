from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
import random
import os
from ai_models.satellite_analysis import SatelliteAnalyzer

router = APIRouter(prefix="/geospatial", tags=["Geospatial"])
analyzer = SatelliteAnalyzer()

@router.get("/states-data")
async def get_states_summary():
    """Returns dummy demographic and environmental data for Indian states"""
    states = ["Maharashtra", "Karnataka", "Delhi", "Tamil Nadu", "Uttar Pradesh", "West Bengal", "Gujarat"]
    data = []
    for state in states:
        data.append({
            "name": state,
            "population_density": random.randint(300, 1200),
            "pollution_index": random.randint(50, 350),
            "forest_cover": random.randint(5, 30),
            "traffic_congestion": random.uniform(0.1, 0.9),
            "healthcare_index": random.randint(40, 95)
        })
    return data

@router.get("/alerts")
async def get_active_alerts():
    """Returns simulated real-time alerts for disasters or traffic"""
    alerts = [
        {"type": "Traffic", "location": "Mumbai - Western Express Highway", "severity": "High", "message": "Heavy congestion due to waterlogging"},
        {"type": "Pollution", "location": "Delhi - NCR", "severity": "Critical", "message": "AQI crossed 400. Mask advisory in effect."},
        {"type": "Weather", "location": "Odisha Coast", "severity": "Medium", "message": "Cyclone warning - Level 2"}
    ]
    return alerts

@router.get("/satellite/urban-detection")
async def analyze_urban_expansion(image_type: str = "urban"):
    """Analyzes satellite imagery for urban expansion detection"""
    image_path = f"data/images/{image_type}_sample.jpg"
    
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail=f"Image not found: {image_path}")
    
    result = analyzer.detect_urban_areas(image_path)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    
    return {
        "analysis_type": "Urban Expansion Detection",
        "image_analyzed": image_type,
        "results": result,
        "timestamp": "2026-05-20T12:00:00Z"
    }

@router.get("/satellite/crop-health")
async def analyze_crop_health(image_type: str = "rural"):
    """Analyzes satellite imagery for crop health using NDVI proxy"""
    image_path = f"data/images/{image_type}_sample.jpg"
    
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail=f"Image not found: {image_path}")
    
    result = analyzer.analyze_crop_health(image_path)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    
    return {
        "analysis_type": "Agricultural Health (NDVI)",
        "image_analyzed": image_type,
        "results": result,
        "timestamp": "2026-05-20T12:00:00Z"
    }

@router.get("/satellite/batch-analysis")
async def batch_satellite_analysis():
    """Performs batch analysis on all available satellite images"""
    results = {
        "urban_analysis": analyzer.detect_urban_areas("data/images/urban_sample.jpg"),
        "crop_analysis": analyzer.analyze_crop_health("data/images/rural_sample.jpg"),
        "analysis_count": 2,
        "timestamp": "2026-05-20T12:00:00Z"
    }
    return results
