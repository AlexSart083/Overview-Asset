# Asset data in English
ASSET_DATA_EN = {
    "Global Equities": {
        "descrizione": "Globally diversified equity investments representing ownership stakes in publicly traded companies worldwide.",
        "punti_forza": [
            "Long-term growth potential",
            "Historical inflation protection",
            "High liquidity",
            "Geographic and sectoral diversification",
            "Dividend potential"
        ],
        "punti_debolezza": [
            "High short-term volatility",
            "Risk of significant losses",
            "Economic cycle dependency",
            "Currency risk for local investors"
        ],
        "scenari": {
            "Economic growth": "Positive performance (+8-12% annually)",
            "Recession": "Negative performance (-15-30%)",
            "High inflation": "Mixed performance (depends on pricing power capability)",
            "Restrictive policies": "Negative pressure from higher rates",
            "Expansive policies": "Positive support from abundant liquidity"
        },
        "allocazione_range": "40-70% for long-term horizon investors",
        "correlazioni": "Negative correlation with long bonds, positive with commodities"
    },
    
    "Emerging Markets": {
        "descrizione": "Equities from companies located in developing countries with rapidly growing economies.",
        "punti_forza": [
            "Higher growth potential than developed markets",
            "Often more attractive valuations",
            "Demographic benefits (young population)",
            "Geographic diversification",
            "Exposure to global growth trends"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "Political and regulatory risks",
            "Lower liquidity",
            "Significant currency risk",
            "High correlation during stress periods"
        ],
        "scenari": {
            "Economic growth": "Outperformance vs developed markets (+10-15%)",
            "Recession": "Significant underperformance (-25-40%)",
            "High inflation": "Mixed performance, some countries benefit",
            "Restrictive policies": "Pressure from capital outflows",
            "Expansive policies": "Strong appeal for yield hunting"
        },
        "allocazione_range": "5-15% as satellite portfolio component",
        "correlazioni": "High correlation with global equities, sensitive to USD"
    },
    
    "Government Bonds": {
        "descrizione": "Debt securities issued by national governments, considered low-risk investments.",
        "punti_forza": [
            "Low credit risk (developed countries)",
            "Stability and predictability of cash flows",
            "Negative correlation with equities",
            "High liquidity",
            "Portfolio diversification"
        ],
        "punti_debolezza": [
            "Interest rate risk",
            "Inflation risk (purchasing power erosion)",
            "Low yields in low rate environments",
            "Duration risk for long-term bonds"
        ],
        "scenari": {
            "Economic growth": "Moderate negative performance due to rate expectations",
            "Recession": "Strong positive performance (flight to quality)",
            "High inflation": "Negative performance due to real yield erosion",
            "Restrictive policies": "Negative performance from rising rates",
            "Expansive policies": "Positive performance from falling rates"
        },
        "allocazione_range": "20-40% for portfolio stabilization",
        "correlazioni": "Typically negative correlation with equities during stress"
    },
    
    "Gold": {
        "descrizione": "Precious metal considered a store of value and hedge against currency debasement.",
        "punti_forza": [
            "Inflation hedge historically",
            "Store of value during crises",
            "Portfolio diversification",
            "No counterparty risk",
            "Global recognition and liquidity"
        ],
        "punti_debolezza": [
            "No income generation",
            "High volatility in short term",
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
    
    "Commodities": {
        "descrizione": "Raw materials and primary agricultural products traded on global exchanges.",
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

# UI text in English
UI_TEXT_EN = {
    "title": "Financial Asset Analyzer",
    "subtitle": "Educational analysis of different financial assets",
    "sidebar_title": "Asset Selection",
    "language_label": "Language",
    "asset_label": "Select Asset",
    "analysis_title": "Asset Analysis: ",
    "description_header": "📖 Description",
    "strengths_header": "✅ Strengths",
    "weaknesses_header": "⚠️ Weaknesses", 
    "scenarios_header": "📊 Market Scenarios Performance",
    "allocation_header": "💼 Indicative Allocation Range",
    "correlations_header": "🔗 Correlations with Other Assets",
    "summary_header": "📝 Educational Summary",
    "warning": "⚠️ **Important Disclaimer**: This information is for educational purposes only and does not constitute personalized financial advice.",
    "visualization_title": "📈 Performance Visualization",
    "heatmap_title": "Asset Performance Heatmap by Market Scenario",
    "allocation_pie_title": "Sample Portfolio Allocation"
}
