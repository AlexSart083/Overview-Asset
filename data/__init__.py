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

# Import main loader functions with error handling
try:
    from .loader import (
        load_all_assets, 
        load_ui_text, 
        validate_asset_data,
        get_asset_categories,
        normalize_language,
        debug_language_loading
    )
    
    __all__ = [
        "load_all_assets",
        "load_ui_text", 
        "validate_asset_data",
        "get_asset_categories",
        "normalize_language",
        "debug_language_loading",
        "SUPPORTED_LANGUAGES",
        "ASSET_CATEGORIES",
        "REQUIRED_ASSET_FIELDS",
        "REQUIRED_PERFORMANCE_FIELDS"
    ]
    
except ImportError as e:
    # Fallback if loader has issues
    print(f"Warning: Could not import from loader: {e}")
    
    def load_all_assets(language="english"):
        """Fallback function"""
        return {}
    
    def load_ui_text(language="english"):
        """Fallback function"""
        return {}
    
    def validate_asset_data(asset_data):
        """Fallback function"""
        return True
    
    def get_asset_categories(language="english"):
        """Fallback function"""
        return {}
    
    def normalize_language(language):
        """Fallback function"""
        return "english"
    
    def debug_language_loading(language):
        """Fallback function"""
        return {"error": "Loader not available"}
    
    __all__ = [
        "load_all_assets",
        "load_ui_text", 
        "validate_asset_data",
        "get_asset_categories",
        "normalize_language",
        "debug_language_loading",
        "SUPPORTED_LANGUAGES",
        "ASSET_CATEGORIES"
    ]
