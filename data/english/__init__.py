# data/english/__init__.py
"""
English language data package
Contains all asset data and UI text in English
"""

from .equity_assets_en import EQUITY_ASSETS_EN
from .bond_assets_en import BOND_ASSETS_EN
from .alternative_assets_en import ALTERNATIVE_ASSETS_EN
from .ui_text_en import UI_TEXT_EN

# Combine all asset data
ALL_ASSETS_EN = {}
ALL_ASSETS_EN.update(EQUITY_ASSETS_EN)
ALL_ASSETS_EN.update(BOND_ASSETS_EN)
ALL_ASSETS_EN.update(ALTERNATIVE_ASSETS_EN)

__all__ = [
    "EQUITY_ASSETS_EN",
    "BOND_ASSETS_EN", 
    "ALTERNATIVE_ASSETS_EN",
    "UI_TEXT_EN",
    "ALL_ASSETS_EN"
]
