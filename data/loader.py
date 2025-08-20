# data/loader.py
"""
Data loader functions for the Financial Asset Analyzer
Updated to handle Government/Corporate bond separation
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
    Get asset categories for navigation with Government/Corporate separation
    
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

def get_bond_risk_explanation(language: str = "english") -> Dict[str, str]:
    """
    Provide educational explanation of Government vs Corporate bond differences
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary with explanatory text
    """
    if language.lower() == "english":
        return {
            "government_explanation": """
            **🏛️ Government Bonds** represent debt issued by European governments (Germany, France, Italy, etc.). 
            They are considered the **risk-free benchmark** because:
            - **Zero credit risk**: Governments can print money to repay debt
            - **Maximum liquidity**: Highly traded in global markets  
            - **Flight-to-quality asset**: Investors buy them during crises
            - **Lower yields**: Safety comes at the cost of lower returns
            """,
            "corporate_explanation": """
            **🏢 Corporate Bonds** are issued by companies and offer higher yields but with additional risks:
            - **Credit risk**: Companies can default on their debt
            - **Spread risk**: The extra yield vs government bonds can fluctuate
            - **Economic sensitivity**: Performance tied to business cycles
            - **Higher yields**: Extra compensation for taking additional risk
            """,
            "duration_explanation": """
            **Duration matters for both**: Longer-term bonds (7-10+ years) are much more sensitive to interest rate changes 
            than short-term bonds (0-3 years), regardless of whether they're government or corporate.
            """
        }
    else:  # Italian
        return {
            "government_explanation": """
            **🏛️ Obbligazioni Governative** rappresentano debito emesso dai governi europei (Germania, Francia, Italia, ecc.). 
            Sono considerate il **benchmark risk-free** perché:
            - **Rischio credito nullo**: I governi possono stampare moneta per ripagare il debito
            - **Liquidità massima**: Altamente scambiate sui mercati globali
            - **Asset flight-to-quality**: Gli investitori le comprano durante le crisi  
            - **Rendimenti più bassi**: La sicurezza costa in termini di rendimenti inferiori
            """,
            "corporate_explanation": """
            **🏢 Obbligazioni Corporate** sono emesse dalle aziende e offrono rendimenti superiori ma con rischi aggiuntivi:
            - **Rischio di credito**: Le aziende possono andare in default
            - **Rischio spread**: Il rendimento extra vs governativi può fluttuare
            - **Sensibilità economica**: Performance legata ai cicli economici
            - **Rendimenti superiori**: Compenso extra per il rischio aggiuntivo
            """,
            "duration_explanation": """
            **La duration conta per entrambi**: Le obbligazioni a lungo termine (7-10+ anni) sono molto più sensibili 
            ai cambiamenti dei tassi di interesse rispetto a quelle a breve termine (0-3 anni), 
            indipendentemente dal fatto che siano governative o corporate.
            """
        }

def get_bond_allocation_guidance(language: str = "english") -> Dict[str, str]:
    """
    Provide allocation guidance for Government vs Corporate bonds
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary with allocation guidance
    """
    if language.lower() == "english":
        return {
            "conservative_portfolio": """
            **Conservative Portfolio (Low Risk Tolerance)**:
            - Government Bonds 1-3Y: 40-50%
            - Government Bonds 3-7Y: 15-25%
            - Corporate Bonds 1-3Y: 10-15%
            - Corporate Bonds 3-7Y: 5-10%
            """,
            "balanced_portfolio": """
            **Balanced Portfolio (Moderate Risk Tolerance)**:
            - Government Bonds 1-3Y: 25-35%
            - Government Bonds 3-7Y: 10-20%
            - Corporate Bonds 1-3Y: 15-25%
            - Corporate Bonds 3-7Y: 10-20%
            - High Yield Bonds: 5-10%
            """,
            "aggressive_portfolio": """
            **Growth-Oriented Portfolio (Higher Risk Tolerance)**:
            - Government Bonds 1-3Y: 15-25%
            - Corporate Bonds 3-7Y: 15-25%
            - Corporate Bonds 7-10Y: 5-15%
            - High Yield Bonds: 10-20%
            """,
            "risk_ladder": """
            **Risk Ladder (from safest to riskiest)**:
            1. 🟢 Government Bonds 0-3Y (Safest)
            2. 🟡 Corporate Bonds 0-3Y 
            3. 🟡 Government Bonds 3-10Y
            4. 🟠 Corporate Bonds 3-10Y
            5. 🔴 High Yield Bonds
            6. 🔴 Subordinated Bonds (Riskiest)
            """
        }
    else:  # Italian
        return {
            "conservative_portfolio": """
            **Portfolio Conservativo (Bassa Tolleranza al Rischio)**:
            - Bond Governativi 1-3 anni: 40-50%
            - Bond Governativi 3-7 anni: 15-25%
            - Bond Corporate 1-3 anni: 10-15%
            - Bond Corporate 3-7 anni: 5-10%
            """,
            "balanced_portfolio": """
            **Portfolio Bilanciato (Media Tolleranza al Rischio)**:
            - Bond Governativi 1-3 anni: 25-35%
            - Bond Governativi 3-7 anni: 10-20%
            - Bond Corporate 1-3 anni: 15-25%
            - Bond Corporate 3-7 anni: 10-20%
            - Bond High Yield: 5-10%
            """,
            "aggressive_portfolio": """
            **Portfolio Orientato alla Crescita (Alta Tolleranza al Rischio)**:
            - Bond Governativi 1-3 anni: 15-25%
            - Bond Corporate 3-7 anni: 15-25%
            - Bond Corporate 7-10 anni: 5-15%
            - Bond High Yield: 10-20%
            """,
            "risk_ladder": """
            **Scala del Rischio (dal più sicuro al più rischioso)**:
            1. 🟢 Bond Governativi 0-3 anni (Più Sicuri)
            2. 🟡 Bond Corporate 0-3 anni
            3. 🟡 Bond Governativi 3-10 anni
            4. 🟠 Bond Corporate 3-10 anni
            5. 🔴 Bond High Yield
            6. 🔴 Obbligazioni Subordinate (Più Rischiose)
            """
        }

def get_educational_content(language: str = "english") -> Dict[str, str]:
    """
    Provide educational content about bond investing
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary with educational content
    """
    if language.lower() == "english":
        return {
            "duration_risk": """
            **Understanding Duration Risk**:
            Duration measures how much a bond's price will change when interest rates move. 
            - **Short Duration (0-3 years)**: Small price changes, lower risk
            - **Medium Duration (3-7 years)**: Moderate price changes, balanced risk/return
            - **Long Duration (7+ years)**: Large price changes, higher risk but potential for bigger gains
            """,
            "credit_risk": """
            **Understanding Credit Risk**:
            Credit risk is the chance that the bond issuer won't be able to make payments.
            - **Government bonds**: Virtually no credit risk (governments can print money)
            - **Investment Grade Corporate**: Low credit risk (strong companies)
            - **High Yield**: Higher credit risk but higher yields to compensate
            """,
            "interest_rate_environment": """
            **Interest Rate Scenarios**:
            - **Rising Rates**: Bond prices fall (longer duration bonds fall more)
            - **Falling Rates**: Bond prices rise (longer duration bonds rise more)
            - **Stable Rates**: Bonds earn their coupon/yield to maturity
            """,
            "diversification_strategy": """
            **Diversification Strategy**:
            - Mix government and corporate bonds for balance of safety and yield
            - Spread across different durations to manage interest rate risk
            - Consider adding specialized bonds (inflation-linked, convertible) for specific risks
            """
        }
    else:  # Italian
        return {
            "duration_risk": """
            **Comprendere il Rischio Duration**:
            La duration misura quanto cambia il prezzo di un'obbligazione al variare dei tassi di interesse.
            - **Duration Breve (0-3 anni)**: Piccole variazioni di prezzo, rischio basso
            - **Duration Media (3-7 anni)**: Variazioni moderate, rischio/rendimento bilanciato
            - **Duration Lunga (7+ anni)**: Grandi variazioni di prezzo, rischio alto ma potenziali guadagni maggiori
            """,
            "credit_risk": """
            **Comprendere il Rischio di Credito**:
            Il rischio di credito è la probabilità che l'emittente non riesca a effettuare i pagamenti.
            - **Obbligazioni governative**: Rischio di credito praticamente nullo (i governi possono stampare moneta)
            - **Corporate Investment Grade**: Basso rischio di credito (aziende solide)
            - **High Yield**: Rischio di credito più alto ma rendimenti superiori come compenso
            """,
            "interest_rate_environment": """
            **Scenari dei Tassi di Interesse**:
            - **Tassi in Rialzo**: I prezzi delle obbligazioni scendono (duration lunghe scendono di più)
            - **Tassi in Ribasso**: I prezzi delle obbligazioni salgono (duration lunghe salgono di più)
            - **Tassi Stabili**: Le obbligazioni rendono la loro cedola/rendimento a scadenza
            """,
            "diversification_strategy": """
            **Strategia di Diversificazione**:
            - Mescola obbligazioni governative e corporate per bilanciare sicurezza e rendimento
            - Distribuisci su diverse duration per gestire il rischio tassi di interesse
            - Considera l'aggiunta di obbligazioni specializzate (inflation-linked, convertibili) per rischi specifici
            """
        }

# Cache for performance (optional)
_asset_cache = {}
_ui_cache = {}
_education_cache = {}

def load_with_cache(language: str, force_reload: bool = False):
    """Load data with caching for better performance"""
    cache_key = language.lower()
    
    if force_reload or cache_key not in _asset_cache:
        _asset_cache[cache_key] = load_all_assets(language)
        _ui_cache[cache_key] = load_ui_text(language)
        _education_cache[cache_key] = {
            'risk_explanation': get_bond_risk_explanation(language),
            'allocation_guidance': get_bond_allocation_guidance(language),
            'educational_content': get_educational_content(language)
        }
    
    return _asset_cache[cache_key], _ui_cache[cache_key], _education_cache[cache_key]

def get_bond_comparison_matrix(language: str = "english") -> Dict[str, Any]:
    """
    Create a comparison matrix for different bond types
    
    Args:
        language: "english" or "italian"
        
    Returns:
        Dictionary with comparison matrix data
    """
    if language.lower() == "english":
        bond_types = [
            "Government Bonds 0-1 Years", "Government Bonds 1-3 Years", "Government Bonds 3-7 Years",
            "Corporate Bonds 0-1 Years", "Corporate Bonds 1-3 Years", "Corporate Bonds 3-7 Years",
            "High Yield Bonds", "Inflation Linked Bonds"
        ]
        
        comparison_matrix = {
            "Bond Type": bond_types,
            "Credit Risk": ["None", "None", "None", "Low", "Low", "Medium", "High", "None"],
            "Duration Risk": ["Very Low", "Low", "Medium", "Very Low", "Low", "Medium", "Low", "Medium"],
            "Liquidity": ["Very High", "Very High", "High", "High", "High", "Medium", "Medium", "Medium"],
            "Yield Level": ["Very Low", "Low", "Medium", "Low", "Medium", "Medium-High", "High", "Low-Medium"],
            "Complexity": ["Very Low", "Very Low", "Low", "Low", "Low", "Medium", "Medium", "High"]
        }
    else:  # Italian
        bond_types = [
            "Bond Governativi 0-1 anni", "Bond Governativi 1-3 anni", "Bond Governativi 3-7 anni",
            "Bond Corporate 0-1 anni", "Bond Corporate 1-3 anni", "Bond Corporate 3-7 anni", 
            "Bond High Yield", "Bond Inflation Linked"
        ]
        
        comparison_matrix = {
            "Tipo Obbligazione": bond_types,
            "Rischio Credito": ["Nullo", "Nullo", "Nullo", "Basso", "Basso", "Medio", "Alto", "Nullo"],
            "Rischio Duration": ["Molto Basso", "Basso", "Medio", "Molto Basso", "Basso", "Medio", "Basso", "Medio"],
            "Liquidità": ["Altissima", "Altissima", "Alta", "Alta", "Alta", "Media", "Media", "Media"],
            "Livello Rendimento": ["Molto Basso", "Basso", "Medio", "Basso", "Medio", "Medio-Alto", "Alto", "Basso-Medio"],
            "Complessità": ["Molto Bassa", "Molto Bassa", "Bassa", "Bassa", "Bassa", "Media", "Media", "Alta"]
        }
    
    return comparison_matrix
