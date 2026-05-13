import os
import sys
from pathlib import Path

def get_base_dir():
    """Get the base directory whether running as script or exe"""
    if getattr(sys, 'frozen', False):
        if sys.platform == 'darwin':
            return os.path.dirname(os.path.dirname(os.path.dirname(sys.executable)))
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

_BASE_DIR = get_base_dir()

# Create data directories
DATA_DIR = Path(_BASE_DIR) / "data"
COORDINATES = DATA_DIR / "coordinates"
LABEL_CSV = DATA_DIR / "labels.csv"
MASKS = DATA_DIR / "masks"
POLYGONS = DATA_DIR / "polygons"

def ensure_data_dirs():
    """Ensure all required data directories exist."""
    COORDINATES.mkdir(parents=True, exist_ok=True)
    MASKS.mkdir(parents=True, exist_ok=True)
    POLYGONS.mkdir(parents=True, exist_ok=True)
    
    if not LABEL_CSV.exists():
        import csv
        with open(LABEL_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['image', 'polygon', 'point', 'x', 'y'])