# data/italian/__init__.py
"""
Italian language data package
Contiene tutti i dati degli asset e testi UI in italiano
"""

from .equity_assets_it import EQUITY_ASSETS_IT
from .bond_assets_it import BOND_ASSETS_IT
from .alternative_assets_it import ALTERNATIVE_ASSETS_IT
from .ui_text_it import UI_TEXT_IT

# Combina tutti i dati degli asset
ALL_ASSETS_IT = {}
ALL_ASSETS_IT.update(EQUITY_ASSETS_IT)
ALL_ASSETS_IT.update(BOND_ASSETS_IT)
ALL_ASSETS_IT.update(ALTERNATIVE_ASSETS_IT)

__all__ = [
    "EQUITY_ASSETS_IT",
    "BOND_ASSETS_IT",
    "ALTERNATIVE_ASSETS_IT", 
    "UI_TEXT_IT",
    "ALL_ASSETS_IT"
]
