# Asset data in English - Expanded Version
ASSET_DATA_EN = {
    "Global Equities (Market Cap)": {
        "descrizione": "Globally diversified equity investments weighted by market capitalization, representing ownership stakes in the world's largest publicly traded companies.",
        "punti_forza": [
            "Long-term growth potential",
            "Historical inflation protection",
            "High liquidity",
            "Automatic geographic and sectoral diversification",
            "Dividend potential",
            "Exposure to largest and most stable companies"
        ],
        "punti_debolezza": [
            "High short-term volatility",
            "Risk of significant losses",
            "Economic cycle dependency",
            "Currency risk for local investors",
            "Concentration towards mega-cap stocks"
        ],
        "scenari": {
            "Economic growth": "Significant outperformance (+12-20% annually)",
            "Recession": "Marked underperformance (-30-45%)",
            "High inflation": "Very variable performance",
            "Restrictive policies": "Significant pressure",
            "Expansive policies": "Strong support"
        },
        "allocazione_range": "5-15% as high risk/return satellite component",
        "correlazioni": "High correlation with global equities but amplified"
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

    "Gold": {
        "descrizione": "Precious metal considered a store of value and hedge against currency debasement and geopolitical instability.",
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
    },

    "Bonds 0-1 Years": {
        "descrizione": "Government and corporate debt securities with very short-term maturity within one year, minimal duration risk.",
        "punti_forza": [
            "Minimal interest rate risk",
            "High liquidity",
            "Low volatility",
            "Capital protection",
            "Frequent reinvestment at current rates"
        ],
        "punti_debolezza": [
            "Very low yields",
            "No inflation protection if real rates negative",
            "Reinvestment risk",
            "Opportunity cost in rising rate environments"
        ],
        "scenari": {
            "Economic growth": "Stable performance but low yields",
            "Recession": "Relative outperformance for stability",
            "High inflation": "Negative performance from negative real rates",
            "Restrictive policies": "Gradual benefits from reinvestment",
            "Expansive policies": "Stable performance but declining yields"
        },
        "allocazione_range": "10-30% for liquidity and stability",
        "correlazioni": "Very low correlation with equities, high correlation with short-term rates"
    },

    "Bonds 1-3 Years": {
        "descrizione": "Government and corporate debt securities with short-term maturity offering limited duration and good risk/return compromise.",
        "punti_forza": [
            "Contained interest rate risk",
            "Higher yields than very short-term",
            "Good liquidity",
            "Moderate volatility",
            "Effective diversification"
        ],
        "punti_debolezza": [
            "Interest rate sensitivity",
            "Still limited yields",
            "Credit risk for corporates",
            "Negative performance with rapid rate rises"
        ],
        "scenari": {
            "Economic growth": "Moderately negative performance",
            "Recession": "Positive performance (flight to quality)",
            "High inflation": "Negative but limited performance",
            "Restrictive policies": "Contained negative pressure",
            "Expansive policies": "Moderately positive performance"
        },
        "allocazione_range": "15-35% for risk/return balance",
        "correlazioni": "Moderate negative correlation with equities"
    },

    "Bonds 3-7 Years": {
        "descrizione": "Government and corporate debt securities with medium-term maturity offering higher yields but with greater rate sensitivity.",
        "punti_forza": [
            "More interesting yields",
            "Duration/yield sweet spot",
            "Portfolio diversification",
            "Still good liquidity",
            "Potential capital gains if rates fall"
        ],
        "punti_debolezza": [
            "Significant interest rate sensitivity",
            "Moderate-high volatility",
            "Duration risk",
            "Negative performance with rising rates"
        ],
        "scenari": {
            "Economic growth": "Negative performance from rate rise expectations",
            "Recession": "Strong positive performance",
            "High inflation": "Significantly negative performance",
            "Restrictive policies": "Significant negative pressure",
            "Expansive policies": "Positive performance"
        },
        "allocazione_range": "10-25% for yield with controlled risk",
        "correlazioni": "Negative correlation with equities, high rate sensitivity"
    },

    "Bonds 7-10 Years": {
        "descrizione": "Government and corporate debt securities with medium-long term maturity with significant duration and greater sensitivity to monetary policy expectations.",
        "punti_forza": [
            "Potentially attractive yields",
            "Strong potential capital gains if rates fall",
            "Significant diversification vs equities",
            "Deflationary hedge",
            "Benchmark for many pension funds"
        ],
        "punti_debolezza": [
            "High interest rate sensitivity",
            "Significant volatility",
            "High duration risk",
            "Very negative performance with inflation/rising rates"
        ],
        "scenari": {
            "Economic growth": "Significantly negative performance",
            "Recession": "Very positive performance (+10-20%)",
            "High inflation": "Very negative performance (-10-20%)",
            "Restrictive policies": "Very negative performance",
            "Expansive policies": "Strong positive performance"
        },
        "allocazione_range": "5-20% for duration diversification",
        "correlazioni": "Strong negative correlation with equities, negative correlation with rates"
    },

    "Bonds >10 Years": {
        "descrizione": "Government and corporate debt securities with long-term maturity with maximum duration and maximum sensitivity to interest rate changes.",
        "punti_forza": [
            "Potentially highest yields",
            "Maximum potential capital gains",
            "Maximum diversification vs equities",
            "Deflation/recession hedge",
            "Matching long-term liabilities"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "Maximum duration risk",
            "Extreme rate sensitivity",
            "Distant reinvestment risk",
            "Potentially lower liquidity"
        ],
        "scenari": {
            "Economic growth": "Very negative performance",
            "Recession": "Exceptional performance (+15-30%)",
            "High inflation": "Disastrous performance (-15-30%)",
            "Restrictive policies": "Very negative performance",
            "Expansive policies": "Excellent performance"
        },
        "allocazione_range": "0-15% only for investors with specific objectives",
        "correlazioni": "Maximum negative correlation with equities, perfect inverse with rates"
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
            "Economic growth": "Positive performance (+8-12% annually)",
            "Recession": "Negative performance (-15-30%)",
            "High inflation": "Mixed performance (depends on pricing power capability)",
            "Restrictive policies": "Negative pressure from higher rates",
            "Expansive policies": "Positive support from abundant liquidity"
        },
        "allocazione_range": "40-70% for long-term horizon investors",
        "correlazioni": "Negative correlation with long bonds, positive with commodities"
    },

    "Momentum Equities": {
        "descrizione": "Strategy that invests in stocks that have shown positive performance in the recent past, exploiting the tendency of winning stocks to continue outperforming in the short-medium term.",
        "punti_forza": [
            "Exploits established market trends",
            "Potential outperformance in bull markets",
            "Dynamic adaptation to market conditions",
            "Systematic approach discipline"
        ],
        "punti_debolezza": [
            "High volatility",
            "Risk of sudden trend reversals",
            "Higher transaction costs due to turnover",
            "Poor performance in sideways markets",
            "Risk of buying at peaks"
        ],
        "scenari": {
            "Economic growth": "Very positive performance (+12-18% annually)",
            "Recession": "Very negative performance (-25-35%)",
            "High inflation": "Mixed performance, depends on sectors",
            "Restrictive policies": "Significant negative pressure",
            "Expansive policies": "Strong positive support"
        },
        "allocazione_range": "10-25% as tactical satellite component",
        "correlazioni": "High correlation with global equities, amplifies market movements"
    },

    "Quality Equities": {
        "descrizione": "Investments in companies with strong fundamentals: high profitability, low financial leverage, stable earnings growth, and efficient management.",
        "punti_forza": [
            "Lower volatility than general market",
            "Better recession resistance",
            "Superior management quality",
            "Sustainable earnings growth",
            "Strong balance sheets"
        ],
        "punti_debolezza": [
            "Often high valuations",
            "Possible underperformance in speculative markets",
            "Potentially slower growth",
            "Sector concentration (tech, healthcare)",
            "Interest rate sensitivity"
        ],
        "scenari": {
            "Economic growth": "Positive but moderate performance (+6-10% annually)",
            "Recession": "Relative outperformance (-5-15%)",
            "High inflation": "Relatively good performance",
            "Restrictive policies": "Moderate pressure",
            "Expansive policies": "Modest benefits"
        },
        "allocazione_range": "15-30% as defensive core component",
        "correlazioni": "Moderate correlation with global equities, negative correlation with volatility"
    },

    "Value Equities": {
        "descrizione": "Strategy that invests in stocks considered undervalued by the market relative to their fundamentals, often with low P/E ratios and high dividend yields.",
        "punti_forza": [
            "Value recovery potential",
            "Attractive valuations",
            "Often high dividend yields",
            "Historically solid long-term performance",
            "Protection against speculative bubbles"
        ],
        "punti_debolezza": [
            "Possible value traps",
            "Possible prolonged underperformance",
            "Exposure to declining sectors",
            "Economic cycle sensitivity",
            "Limited growth"
        ],
        "scenari": {
            "Economic growth": "Positive performance (+8-14% annually)",
            "Recession": "Negative but better than growth (-10-20%)",
            "High inflation": "Generally positive performance",
            "Restrictive policies": "Relative benefits",
            "Expansive policies": "Underperformance vs growth"
        },
        "allocazione_range": "15-35% as contrarian core component",
        "correlazioni": "Moderate correlation with global equities, inverse with growth"
    },

    "Minimum Volatility Equities": {
        "descrizione": "Strategy that selects stocks with the lowest historical volatility, aiming to reduce the overall risk of the equity portfolio.",
        "punti_forza": [
            "Significantly reduced volatility",
            "Better risk-adjusted returns",
            "Outperformance in bear markets",
            "Systematic approach to risk reduction",
            "Contained drawdowns"
        ],
        "punti_debolezza": [
            "Underperformance in strong bull markets",
            "Possible sector concentration (utilities, staples)",
            "Higher management costs",
            "Potentially lower long-term returns"
        ],
        "scenari": {
            "Economic growth": "Moderate performance (+4-8% annually)",
            "Recession": "Significant outperformance (-5-12%)",
            "High inflation": "Moderate defensive performance",
            "Restrictive policies": "Superior resilience",
            "Expansive policies": "Relative underperformance"
        },
        "allocazione_range": "10-25% for equity risk reduction",
        "correlazioni": "Positive but reduced correlation with global equities"
    },

    "Small Cap Equities": {
        "descrizione": "Investments in small capitalization companies with greater growth potential but also higher risk and volatility.",
        "punti_forza": [
            "Higher growth potential",
            "Possibility to discover companies before the market",
            "Lower analyst coverage (inefficiencies)",
            "Greater management agility",
            "Diversification vs large caps"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "Lower liquidity",
            "Higher bankruptcy risk",
            "Economic cycle sensitivity",
            "Higher transaction costs"
        ],
        "scenari": {
