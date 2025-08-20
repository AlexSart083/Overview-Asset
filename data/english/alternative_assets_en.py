# data/english/alternative_assets_en.py
"""
Alternative assets data in English
Includes precious metals, commodities, and real estate investment trusts
"""

ALTERNATIVE_ASSETS_EN = {
    "Gold": {
        "descrizione": "Precious metal considered a store of value and hedge against currency debasement and geopolitical instability.",
        "performance_storica": {
            "20_anni": "8.4%",
            "10_anni": "4.2%",
            "5_anni": "7.8%",
            "1_anno": "27.0%",
            "indice_riferimento": "Gold Spot Price (USD)",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Historical inflation hedge",
            "Store of value during crises",
            "Portfolio diversification",
            "No counterparty risk",
            "Global recognition and liquidity"
        ],
        "punti_debolezza": [
            "No income generation",
            "High short-term volatility",
            "Storage and insurance costs",
            "Sensitive to real interest rates",
            "Currency risk (USD-denominated)"
        ],
        "scenari": {
            "Economic growth": "Moderate negative performance",
            "Recession": "Strong positive performance (safe haven)",
            "High inflation": "Historically positive performance",
            "Restrictive policies": "Negative pressure from higher real rates",
            "Expansive policies": "Positive from currency debasement fears"
        },
        "allocazione_range": "5-10% as portfolio hedge",
        "correlazioni": "Low correlation with other assets, inverse with USD"
    },

    "Silver": {
        "descrizione": "Precious metal with dual nature as safe haven and industrial commodity, more volatile than gold.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "2.1%",
            "5_anni": "9.2%",
            "1_anno": "32.5%",
            "indice_riferimento": "Silver Spot Price (USD)",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Dual demand: investment and industrial",
            "Higher volatility can offer opportunities",
            "Gold/silver ratio historically cyclical",
            "Growing technological uses",
            "Relatively more accessible price"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "More sensitive to industrial cycles than gold",
            "Smaller and less liquid market",
            "Higher relative storage costs",
            "Historically inferior performance to gold"
        ],
        "scenari": {
            "Economic growth": "Positive performance from industrial demand",
            "Recession": "Mixed performance (safe haven vs industrial demand)",
            "High inflation": "Very positive performance",
            "Restrictive policies": "Pressure from high real rates",
            "Expansive policies": "Strong support especially if outperforming gold"
        },
        "allocazione_range": "2-5% as gold satellite",
        "correlazioni": "High correlation with gold but higher volatility"
    },

    "Commodities": {
        "descrizione": "Raw materials and primary agricultural products traded on global exchanges, including energy, industrial metals, and agricultural products.",
        "performance_storica": {
            "20_anni": "4.8%",
            "10_anni": "3.2%",
            "5_anni": "8.1%",
            "1_anno": "12.4%",
            "indice_riferimento": "Bloomberg Commodity Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Inflation protection",
            "Diversification benefits",
            "Supply/demand dynamics",
            "Global economic exposure",
            "Tangible asset backing"
        ],
        "punti_debolezza": [
            "High volatility",
            "No income generation",
            "Storage and transportation costs",
            "Cyclical nature",
            "Weather and geopolitical risks"
        ],
        "scenari": {
            "Economic growth": "Strong positive performance",
            "Recession": "Negative performance from demand destruction",
            "High inflation": "Strong positive performance",
            "Restrictive policies": "Mixed impact depending on economic effects",
            "Expansive policies": "Positive from increased demand expectations"
        },
        "allocazione_range": "5-15% for inflation protection",
        "correlazioni": "Positive correlation with inflation, mixed with equities"
    },

    "REITs": {
        "descrizione": "Real Estate Investment Trusts providing exposure to real estate markets through publicly traded securities.",
        "performance_storica": {
            "20_anni": "7.2%",
            "10_anni": "8.4%",
            "5_anni": "5.8%",
            "1_anno": "11.2%",
            "indice_riferimento": "FTSE Nareit All REITs Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Regular dividend income",
            "Real estate exposure without direct ownership",
            "Professional management",
            "Liquidity compared to direct real estate",
            "Inflation hedge potential"
        ],
        "punti_debolezza": [
            "Interest rate sensitivity",
            "Real estate cycle dependency",
            "Lower diversification than expected",
            "Management fees",
            "Tax complexity"
        ],
        "scenari": {
            "Economic growth": "Positive performance from occupancy and rent growth",
            "Recession": "Negative performance from economic weakness",
            "High inflation": "Mixed performance (input costs vs rent increases)",
            "Restrictive policies": "Negative pressure from higher discount rates",
            "Expansive policies": "Positive support from lower rates"
        },
        "allocazione_range": "5-15% for real estate exposure",
        "correlazioni": "Moderate correlation with equities, sensitive to interest rates"
    }
}
