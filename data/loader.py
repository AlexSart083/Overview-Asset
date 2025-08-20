# data/loader.py
"""
Data loader functions for the Financial Asset Analyzer
Combines modular data files into complete datasets
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
        language: "english" or "italian"
        
    Returns:
        Dictionary containing all asset data
    """
    all_assets = {}
    
    try:
        if language.lower() == "english":
            from .english.equity_assets_en import EQUITY_ASSETS_EN
            from .english.bond_assets_en import BOND_ASSETS_EN  
            from .english.alternative_assets_en import ALTERNATIVE_ASSETS_EN
            
            all_assets.update(EQUITY_ASSETS_EN)
            all_assets.update(BOND_ASSETS_EN)
            all_assets.update(ALTERNATIVE_ASSETS_EN)
            
        elif language.lower() == "italian":
            from .italian.equity_assets_it import EQUITY_ASSETS_IT
            from .italian.bond_assets_it import BOND_ASSETS_IT
            from .italian.alternative_assets_it import ALTERNATIVE_ASSETS_IT
            
            all_assets.update(EQUITY_ASSETS_IT)
            all_assets.update(BOND_ASSETS_IT)
            all_assets.update(ALTERNATIVE_ASSETS_IT)
            
        else:
            logger.error(f"Unsupported language: {language}")
            raise ValueError(f"Language '{language}' not supported")
            
    except ImportError as e:
        logger.error(f"Error loading data for language {language}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading assets: {e}")
        raise
        
    logger.info(f"Loaded {len(all_assets)} assets for language: {language}")
    return all_assets

def load_ui_text(language: str = "english") -> Dict[str, str]:
    """
    Load UI text for specified language
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary containing UI text
    """
    try:
        if language.lower() == "english":
            from .english.ui_text_en import UI_TEXT_EN
            return UI_TEXT_EN
        elif language.lower() == "italian":
            from .italian.ui_text_it import UI_TEXT_IT
            return UI_TEXT_IT
        else:
            logger.error(f"Unsupported language: {language}")
            raise ValueError(f"Language '{language}' not supported")
            
    except ImportError as e:
        logger.error(f"Error loading UI text for language {language}: {e}")
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
    from . import REQUIRED_ASSET_FIELDS, REQUIRED_PERFORMANCE_FIELDS
    
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
    Get asset categories for navigation
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary with asset categories
    """
    if language.lower() == "english":
        return {
            "📈 Equity Strategies": [
                "Global Equities (Market Cap)", "Momentum Equities", "Quality Equities", 
                "Value Equities", "Minimum Volatility Equities", "Small Cap Equities", 
                "Emerging Markets", "High Dividend Equities"
            ],
            "💰 Government & Corporate Bonds": [
                "Bonds 0-1 Years", "Bonds 1-3 Years", "Bonds 3-7 Years", 
                "Bonds 7-10 Years", "Bonds >10 Years"
            ],
            "🔸 Specialized Bonds": [
                "High Yield Bonds", "Inflation Linked Bonds", "Convertible Bonds", 
                "Subordinated Bonds"
            ],
            "🥇 Precious Metals": ["Gold", "Silver"],
            "🏢 Alternative Assets": ["Commodities", "REITs"]
        }
    else:  # Italian
        return {
            "📈 Strategie Azionarie": [
                "Azioni Globali (Market Cap)", "Azioni Momentum", "Azioni Quality", 
                "Azioni Value", "Azioni Minimum Volatility", "Azioni Small Cap", 
                "Mercati Emergenti", "Azionario High Dividend"
            ],
            "💰 Obbligazioni Gov. & Corporate": [
                "Obbligazioni 0-1 anni", "Obbligazioni 1-3 anni", "Obbligazioni 3-7 anni", 
                "Obbligazioni 7-10 anni", "Obbligazioni >10 anni"
            ],
            "🔸 Obbligazioni Specializzate": [
                "Bond High Yield", "Bond Inflation Linked", "Bond Convertibili", 
                "Obbligazioni Subordinate"
            ],
            "🥇 Metalli Preziosi": ["Oro", "Argento"],
            "🏢 Asset Alternativi": ["Materie Prime", "REIT"]
        }

# Cache for performance (optional)
_asset_cache = {}
_ui_cache = {}

def load_with_cache(language: str, force_reload: bool = False):
    """Load data with caching for better performance"""
    cache_key = language.lower()
    
    if force_reload or cache_key not in _asset_cache:
        _asset_cache[cache_key] = load_all_assets(language)
        _ui_cache[cache_key] = load_ui_text(language)
    
    return _asset_cache[cache_key], _ui_cache[cache_key]
