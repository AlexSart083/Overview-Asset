# data/english/equity_assets_en.py
"""
Equity and equity strategy assets data in English - COMPLETE WITH YEARLY RETURNS
Includes all equity-based investment strategies and emerging markets
"""

EQUITY_ASSETS_EN = {
    "Global Equities (Market Cap)": {
        "descrizione": "Globally diversified equity investments weighted by market capitalization, representing ownership stakes in the world's largest publicly traded companies.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "14.9%",   # 2024
                "anno_2": "16.8%",   # 2023
                "anno_3": "13.2%",   # 2022
                "anno_4": "21.8%",   # 2021
                "anno_5": "15.9%",   # 2020
                "anno_6": "27.7%",   # 2019
                "anno_7": "-8.7%",   # 2018
                "anno_8": "23.1%",   # 2017
                "anno_9": "7.5%",    # 2016
                "anno_10": "-0.9%",  # 2015
                "anno_11": "4.9%",   # 2014
                "anno_12": "22.8%",  # 2013
                "anno_13": "15.8%",  # 2012
                "anno_14": "-5.5%",  # 2011
                "anno_15": "11.8%",  # 2010
                "anno_16": "29.9%",  # 2009
                "anno_17": "-40.7%", # 2008
                "anno_18": "9.6%",   # 2007
                "anno_19": "20.1%",  # 2006
                "anno_20": "9.5%"    # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "18.5%",   # 2024
                "anno_2": "19.2%",   # 2023
                "anno_3": "15.8%",   # 2022
                "anno_4": "26.4%",   # 2021
                "anno_5": "18.7%",   # 2020
                "anno_6": "31.2%",   # 2019
                "anno_7": "-12.3%",  # 2018
                "anno_8": "28.9%",   # 2017
                "anno_9": "9.1%",    # 2016
                "anno_10": "-2.4%",  # 2015
                "anno_11": "6.8%",   # 2014
                "anno_12": "27.5%",  # 2013
                "anno_13": "18.9%",  # 2012
                "anno_14": "-8.2%",  # 2011
                "anno_15": "14.7%",  # 2010
                "anno_16": "35.1%",  # 2009
                "anno_17": "-48.5%", # 2008
                "anno_18": "11.8%",  # 2007
                "anno_19": "23.4%",  # 2006
                "anno_20": "12.1%"   # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "12.4%",   # 2024
                "anno_2": "14.5%",   # 2023
                "anno_3": "11.8%",   # 2022
                "anno_4": "18.9%",   # 2021
                "anno_5": "13.2%",   # 2020
                "anno_6": "25.1%",   # 2019
                "anno_7": "-6.8%",   # 2018
                "anno_8": "20.7%",   # 2017
                "anno_9": "6.3%",    # 2016
                "anno_10": "1.2%",   # 2015
                "anno_11": "7.5%",   # 2014
                "anno_12": "19.8%",  # 2013
                "anno_13": "13.4%",  # 2012
                "anno_14": "-3.1%",  # 2011
                "anno_15": "9.9%",   # 2010
                "anno_16": "26.8%",  # 2009
                "anno_17": "-35.2%", # 2008
                "anno_18": "7.9%",   # 2007
                "anno_19": "17.3%",  # 2006
                "anno_20": "8.1%"    # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "13.7%",   # 2024
                "anno_2": "12.9%",   # 2023
                "anno_3": "8.4%",    # 2022
                "anno_4": "16.2%",   # 2021
                "anno_5": "9.8%",    # 2020
                "anno_6": "21.3%",   # 2019
                "anno_7": "-4.1%",   # 2018
                "anno_8": "17.2%",   # 2017
                "anno_9": "15.6%",   # 2016
                "anno_10": "-3.8%",  # 2015
                "anno_11": "12.7%",  # 2014
                "anno_12": "31.1%",  # 2013
                "anno_13": "17.5%",  # 2012
                "anno_14": "-5.6%",  # 2011
                "anno_15": "15.1%",  # 2010
                "anno_16": "19.7%",  # 2009
                "anno_17": "-36.8%", # 2008
                "anno_18": "-0.2%",  # 2007
                "anno_19": "22.2%",  # 2006
                "anno_20": "7.1%"    # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "10.8%",   # 2024
                "anno_2": "11.9%",   # 2023
                "anno_3": "8.7%",    # 2022
                "anno_4": "14.2%",   # 2021
                "anno_5": "2.1%",    # 2020
                "anno_6": "20.5%",   # 2019
                "anno_7": "-1.8%",   # 2018
                "anno_8": "16.3%",   # 2017
                "anno_9": "11.4%",   # 2016
                "anno_10": "2.9%",   # 2015
                "anno_11": "8.7%",   # 2014
                "anno_12": "18.4%",  # 2013
                "anno_13": "14.9%",  # 2012
                "anno_14": "1.2%",   # 2011
                "anno_15": "12.8%",  # 2010
                "anno_16": "22.1%",  # 2009
                "anno_17": "-22.8%", # 2008
                "anno_18": "5.3%",   # 2007
                "anno_19": "15.7%",  # 2006
                "anno_20": "6.8%"    # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "15.2%",   # 2024
                "anno_2": "18.7%",   # 2023
                "anno_3": "9.3%",    # 2022
                "anno_4": "28.1%",   # 2021
                "anno_5": "-5.0%",   # 2020
                "anno_6": "25.5%",   # 2019
                "anno_7": "-11.0%",  # 2018
                "anno_8": "21.3%",   # 2017
                "anno_9": "21.3%",   # 2016
                "anno_10": "-4.4%",  # 2015
                "anno_11": "4.9%",   # 2014
                "anno_12": "38.8%",  # 2013
                "anno_13": "16.4%",  # 2012
                "anno_14": "-4.2%",  # 2011
                "anno_15": "26.9%",  # 2010
                "anno_16": "27.2%",  # 2009
                "anno_17": "-33.8%", # 2008
                "anno_18": "-1.6%",  # 2007
                "anno_19": "18.4%",  # 2006
                "anno_20": "4.6%"    # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "15.9%",   # 2024
                "anno_2": "-2.5%",   # 2023
                "anno_3": "-20.1%",  # 2022
                "anno_4": "-2.5%",   # 2021
                "anno_5": "18.3%",   # 2020
                "anno_6": "18.4%",   # 2019
                "anno_7": "-14.6%",  # 2018
                "anno_8": "37.3%",   # 2017
                "anno_9": "11.2%",   # 2016
                "anno_10": "-14.9%", # 2015
                "anno_11": "-2.2%",  # 2014
                "anno_12": "-2.6%",  # 2013
                "anno_13": "18.2%",  # 2012
                "anno_14": "-18.4%", # 2011
                "anno_15": "18.9%",  # 2010
                "anno_16": "78.5%",  # 2009
                "anno_17": "-53.3%", # 2008
                "anno_18": "39.4%",  # 2007
                "anno_19": "32.6%",  # 2006
                "anno_20": "34.5%"   # 2005
            },
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
            "rendimenti_annuali": {
                "anno_1": "11.8%",   # 2024
                "anno_2": "13.2%",   # 2023
                "anno_3": "5.1%",    # 2022
                "anno_4": "17.9%",   # 2021
                "anno_5": "-2.8%",   # 2020
                "anno_6": "21.7%",   # 2019
                "anno_7": "-4.3%",   # 2018
                "anno_8": "17.8%",   # 2017
                "anno_9": "17.8%",   # 2016
                "anno_10": "-3.4%",  # 2015
                "anno_11": "15.4%",  # 2014
                "anno_12": "26.1%",  # 2013
                "anno_13": "10.2%",  # 2012
                "anno_14": "5.9%",   # 2011
                "anno_15": "14.2%",  # 2010
                "anno_16": "10.1%",  # 2009
                "anno_17": "-18.9%", # 2008
                "anno_18": "-1.4%",  # 2007
                "anno_19": "20.8%",  # 2006
                "anno_20": "5.4%"    # 2005
            },
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
