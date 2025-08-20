# data/english/equity_assets_en.py
"""
Equity and equity strategy assets data in English
Includes all equity-based investment strategies and emerging markets
"""

EQUITY_ASSETS_EN = {
    "Global Equities (Market Cap)": {
        "descrizione": "Globally diversified equity investments weighted by market capitalization, representing ownership stakes in the world's largest publicly traded companies.",
        "performance_storica": {
            "20_anni": "7.0%",
            "10_anni": "10.6%",
            "5_anni": "14.4%",
            "1_anno": "14.9%",
            "indice_riferimento": "MSCI World Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "8.5%",
            "10_anni": "12.8%",
            "5_anni": "16.2%",
            "1_anno": "18.5%",
            "indice_riferimento": "MSCI World Momentum Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "7.8%",
            "10_anni": "11.2%",
            "5_anni": "13.8%",
            "1_anno": "12.4%",
            "indice_riferimento": "MSCI World Quality Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "6.2%",
            "10_anni": "8.9%",
            "5_anni": "11.5%",
            "1_anno": "13.7%",
            "indice_riferimento": "MSCI World Value Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "9.4%",
            "5_anni": "11.2%",
            "1_anno": "10.8%",
            "indice_riferimento": "MSCI World Minimum Volatility Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "8.2%",
            "10_anni": "11.8%",
            "5_anni": "13.4%",
            "1_anno": "15.2%",
            "indice_riferimento": "MSCI World Small Cap Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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
        "performance_storica": {
            "20_anni": "4.3%",
            "10_anni": "6.1%",
            "5_anni": "5.6%",
            "1_anno": "15.9%",
            "indice_riferimento": "MSCI Emerging Markets Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
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

    "High Dividend Equities": {
        "descrizione": "Strategy that invests in stocks of companies that distribute high and sustainable dividends, often mature companies with stable cash flows.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "9.2%",
            "5_anni": "10.4%",
            "1_anno": "11.8%",
            "indice_riferimento": "MSCI World High Dividend Yield Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "High and regular current income",
            "Lower volatility than general market",
            "Partial protection in bear markets",
            "Potential dividend growth over time",
            "Management discipline of companies"
        ],
        "punti_debolezza": [
            "Limited capital growth",
            "Sector concentration (utilities, REITs, energy)",
            "Interest rate sensitivity",
            "Risk of dividend cuts in crisis",
            "Possible value trap"
        ],
        "scenari": {
            "Economic growth": "Moderately positive performance (+5-9% annually)",
            "Recession": "Negative but limited performance (-8-15%)",
            "High inflation": "Mixed performance (utilities positive, other sectors pressure)",
            "Restrictive policies": "Negative pressure from bond competition",
            "Expansive policies": "Positive performance from search for yield"
        },
        "allocazione_range": "15-30% for income-oriented investors",
        "correlazioni": "Moderate correlation with equities, negative correlation with interest rates"
    }
}
