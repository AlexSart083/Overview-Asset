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

# Simple fallback functions that can be imported without circular dependencies
def get_fallback_assets(language="english"):
    """Simple fallback for assets"""
    return {}

def get_fallback_ui_text(language="english"):
    """Simple fallback for UI text"""
    return {
        "title": "Financial Asset Analyzer" if language == "english" else "Analizzatore Asset Finanziari",
        "subtitle": "Educational analysis of different financial assets" if language == "english" else "Analisi educativa di diversi asset finanziari",
        "sidebar_title": "Asset Selection" if language == "english" else "Selezione Asset",
        "language_label": "Language" if language == "english" else "Lingua",
        "asset_label": "Select Asset" if language == "english" else "Seleziona Asset",
        "analysis_title": "Asset Analysis: " if language == "english" else "Analisi Asset: ",
        "description_header": "📖 Description" if language == "english" else "📖 Descrizione",
        "performance_header": "📊 Historical Performance (Annualized)" if language == "english" else "📊 Performance Storica (Annualizzata)",
        "strengths_header": "✅ Strengths" if language == "english" else "✅ Punti di Forza",
        "weaknesses_header": "⚠️ Weaknesses" if language == "english" else "⚠️ Punti di Debolezza",
        "scenarios_header": "📊 Market Scenarios Performance" if language == "english" else "📊 Performance negli Scenari di Mercato",
        "allocation_header": "💼 Indicative Allocation Range" if language == "english" else "💼 Range di Allocazione Indicativo",
        "correlations_header": "🔗 Correlations with Other Assets" if language == "english" else "🔗 Correlazioni con Altri Asset",
        "summary_header": "📝 Educational Summary" if language == "english" else "📝 Riassunto Educativo",
        "warning": "⚠️ **Important Disclaimer**: This information is for educational purposes only and does not constitute personalized financial advice." if language == "english" else "⚠️ **Importante Disclaimer**: Queste informazioni sono a scopo puramente educativo e non costituiscono consigli finanziari personalizzati.",
        "performance_note": "📌 **Note**: Historical performance data is based on relevant market indices and is not a guarantee of future results." if language == "english" else "📌 **Nota**: I dati di performance storica sono basati su indici di mercato rilevanti e non garantiscono risultati futuri."
    }

# Export the constants and fallback functions
__all__ = [
    "SUPPORTED_LANGUAGES",
    "ASSET_CATEGORIES", 
    "REQUIRED_ASSET_FIELDS",
    "REQUIRED_PERFORMANCE_FIELDS",
    "get_fallback_assets",
    "get_fallback_ui_text"
]
