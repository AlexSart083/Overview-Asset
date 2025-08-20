# data/__init__.py
"""
Financial Asset Analyzer - Data Package
Modular data structure for asset information and UI text
"""

__version__ = "1.2.0"
__author__ = "Financial Asset Analyzer Team"

# Package metadata
SUPPORTED_LANGUAGES = ["english", "italian"]
ASSET_CATEGORIES = ["equity", "bonds", "alternative"]

# Data validation constants
REQUIRED_ASSET_FIELDS = [
    "descrizione",
    "performance_storica", 
    "punti_forza",
    "punti_debolezza",
    "scenari",
    "allocazione_range",
    "correlazioni"
]

REQUIRED_PERFORMANCE_FIELDS = [
    "20_anni",
    "10_anni", 
    "5_anni",
    "1_anno",
    "indice_riferimento"
]

# Import main loader functions
from .loader import load_all_assets, load_ui_text, validate_asset_data

__all__ = [
    "load_all_assets",
    "load_ui_text", 
    "validate_asset_data",
    "SUPPORTED_LANGUAGES",
    "ASSET_CATEGORIES"
]
