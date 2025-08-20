# data/loader.py
"""
Data loader functions for the Financial Asset Analyzer
Fixed version without circular imports
"""

import logging
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_all_assets(language: str = "english") -> Dict[str, Any]:
    """
    Load all asset data for specified language
    
    Args:
        language: "english", "italian", "italiano", or "inglese"
        
    Returns:
        Dictionary containing all asset data
    """
    all_assets = {}
    
    # Normalize language input
    lang_lower = language.lower()
    if lang_lower in ["italiano", "italian", "it"]:
        target_language = "italian"
    elif lang_lower in ["english", "inglese", "en"]:
        target_language = "english"
    else:
        logger.error(f"Unsupported language: {language}")
        raise ValueError(f"Language '{language}' not supported. Use 'english' or 'italiano'")
    
    try:
        if target_language == "english":
            from .english.equity_assets_en import EQUITY_ASSETS_EN
            from .english.bond_assets_en import BOND_ASSETS_EN  
            from .english.alternative_assets_en import ALTERNATIVE_ASSETS_EN
            
            all_assets.update(EQUITY_ASSETS_EN)
            all_assets.update(BOND_ASSETS_EN)
            all_assets.update(ALTERNATIVE_ASSETS_EN)
            
        elif target_language == "italian":
            from .italian.equity_assets_it import EQUITY_ASSETS_IT
            from .italian.bond_assets_it import BOND_ASSETS_IT
            from .italian.alternative_assets_it import ALTERNATIVE_ASSETS_IT
            
            all_assets.update(EQUITY_ASSETS_IT)
            all_assets.update(BOND_ASSETS_IT)
            all_assets.update(ALTERNATIVE_ASSETS_IT)
            
    except ImportError as e:
        logger.error(f"Error loading data for language {target_language}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading assets: {e}")
        raise
        
    logger.info(f"Loaded {len(all_assets)} assets for language: {target_language}")
    return all_assets

def load_ui_text(language: str = "english") -> Dict[str, str]:
    """
    Load UI text for specified language
    
    Args:
        language: "english", "italian", "italiano", or "inglese"
        
    Returns:
        Dictionary containing UI text
    """
    # Normalize language input
    lang_lower = language.lower()
    if lang_lower in ["italiano", "italian", "it"]:
        target_language = "italian"
    elif lang_lower in ["english", "inglese", "en"]:
        target_language = "english"
    else:
        logger.error(f"Unsupported language: {language}")
        raise ValueError(f"Language '{language}' not supported. Use 'english' or 'italiano'")
    
    try:
        if target_language == "english":
            from .english.ui_text_en import UI_TEXT_EN
            return UI_TEXT_EN
        elif target_language == "italian":
            from .italian.ui_text_it import UI_TEXT_IT
            return UI_TEXT_IT
            
    except ImportError as e:
        logger.error(f"Error loading UI text for language {target_language}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading UI text: {e}")
        raise

def validate_asset_data(asset_data: Dict[str, Any]) -> bool:
    """
    Validate asset data structure
    
    Args:
        asset_data: Asset data dictionary to validate
        
    Returns:
        True if valid, raises exception if invalid
    """
    # Import here to avoid circular imports
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
    
    for asset_name, asset_info in asset_data.items():
        # Check required top-level fields
        for field in REQUIRED_ASSET_FIELDS:
            if field not in asset_info:
                raise ValueError(f"Asset '{asset_name}' missing required field: {field}")
        
        # Check performance data structure
        performance_data = asset_info.get("performance_storica", {})
        for field in REQUIRED_PERFORMANCE_FIELDS:
            if field not in performance_data:
                logger.warning(f"Asset '{asset_name}' missing performance field: {field}")
        
        # Validate data types
        if not isinstance(asset_info.get("punti_forza", []), list):
            raise ValueError(f"Asset '{asset_name}': punti_forza must be a list")
        
        if not isinstance(asset_info.get("punti_debolezza", []), list):
            raise ValueError(f"Asset '{asset_name}': punti_debolezza must be a list")
            
        if not isinstance(asset_info.get("scenari", {}), dict):
            raise ValueError(f"Asset '{asset_name}': scenari must be a dictionary")
    
    logger.info(f"Validation passed for {len(asset_data)} assets")
    return True

def get_asset_categories(language: str = "english") -> Dict[str, list]:
    """
    Get asset categories for navigation with Government/Corporate separation
    
    Args:
        language: "english", "italian", "italiano", or "inglese"
        
    Returns:
        Dictionary with asset categories
    """
    # Normalize language input
    lang_lower = language.lower()
    if lang_lower in ["italiano", "italian", "it"]:
        target_language = "italian"
    elif lang_lower in ["english", "inglese", "en"]:
        target_language = "english"
    else:
        target_language = "english"  # Default fallback
    
    if target_language == "english":
        return {
            "📈 Equity Strategies": [
                "Global Equities (Market Cap)", "Momentum Equities", "Quality Equities", 
                "Value Equities", "Minimum Volatility Equities", "Small Cap Equities", 
                "Emerging Markets", "High Dividend Equities"
            ],
            "🏛️ Government Bonds": [
                "Government Bonds 0-1 Years", "Government Bonds 1-3 Years", "Government Bonds 3-7 Years", 
                "Government Bonds 7-10 Years", "Government Bonds >10 Years"
            ],
            "🏢 Corporate Bonds": [
                "Corporate Bonds 0-1 Years", "Corporate Bonds 1-3 Years", "Corporate Bonds 3-7 Years", 
                "Corporate Bonds 7-10 Years", "Corporate Bonds >10 Years"
            ],
            "🔸 Specialized Bonds": [
                "High Yield Bonds", "Inflation Linked Bonds", "Convertible Bonds", 
                "Subordinated Bonds"
            ],
            "🥇 Precious Metals": ["Gold", "Silver"],
            "🏗️ Alternative Assets": ["Commodities", "REITs"]
        }
    else:  # Italian
        return {
            "📈 Strategie Azionarie": [
                "Azioni Globali (Market Cap)", "Azioni Momentum", "Azioni Quality", 
                "Azioni Value", "Azioni Minimum Volatility", "Azioni Small Cap", 
                "Mercati Emergenti", "Azionario High Dividend"
            ],
            "🏛️ Obbligazioni Governative": [
                "Bond Governativi 0-1 anni", "Bond Governativi 1-3 anni", "Bond Governativi 3-7 anni", 
                "Bond Governativi 7-10 anni", "Bond Governativi >10 anni"
            ],
            "🏢 Obbligazioni Corporate": [
                "Bond Corporate 0-1 anni", "Bond Corporate 1-3 anni", "Bond Corporate 3-7 anni", 
                "Bond Corporate 7-10 anni", "Bond Corporate >10 anni"
            ],
            "🔸 Obbligazioni Specializzate": [
                "Bond High Yield", "Bond Inflation Linked", "Bond Convertibili", 
                "Obbligazioni Subordinate"
            ],
            "🥇 Metalli Preziosi": ["Oro", "Argento"],
            "🏗️ Asset Alternativi": ["Materie Prime", "REIT"]
        }

# Language mapping for debugging
LANGUAGE_MAPPING = {
    "english": "english",
    "inglese": "english", 
    "en": "english",
    "italiano": "italian",
    "italian": "italian",
    "it": "italian"
}

def normalize_language(language: str) -> str:
    """
    Normalize language input to standard format
    
    Args:
        language: Input language string
        
    Returns:
        Normalized language string
    """
    lang_lower = language.lower().strip()
    return LANGUAGE_MAPPING.get(lang_lower, "english")

def debug_language_loading(language: str) -> Dict[str, Any]:
    """
    Debug function to check language loading
    
    Args:
        language: Input language
        
    Returns:
        Debug information
    """
    normalized = normalize_language(language)
    
    debug_info = {
        "input_language": language,
        "normalized_language": normalized,
        "supported_languages": list(LANGUAGE_MAPPING.keys()),
        "available_modules": []
    }
    
    # Check available modules
    try:
        if normalized == "english":
            from .english.equity_assets_en import EQUITY_ASSETS_EN
            from .english.bond_assets_en import BOND_ASSETS_EN
            from .english.alternative_assets_en import ALTERNATIVE_ASSETS_EN
            from .english.ui_text_en import UI_TEXT_EN
            debug_info["available_modules"].extend([
                "english.equity_assets_en", "english.bond_assets_en", 
                "english.alternative_assets_en", "english.ui_text_en"
            ])
            debug_info["assets_count"] = len(EQUITY_ASSETS_EN) + len(BOND_ASSETS_EN) + len(ALTERNATIVE_ASSETS_EN)
        elif normalized == "italian":
            from .italian.equity_assets_it import EQUITY_ASSETS_IT
            from .italian.bond_assets_it import BOND_ASSETS_IT
            from .italian.alternative_assets_it import ALTERNATIVE_ASSETS_IT
            from .italian.ui_text_it import UI_TEXT_IT
            debug_info["available_modules"].extend([
                "italian.equity_assets_it", "italian.bond_assets_it", 
                "italian.alternative_assets_it", "italian.ui_text_it"
            ])
            debug_info["assets_count"] = len(EQUITY_ASSETS_IT) + len(BOND_ASSETS_IT) + len(ALTERNATIVE_ASSETS_IT)
    except ImportError as e:
        debug_info["import_error"] = str(e)
    
    return debug_info
