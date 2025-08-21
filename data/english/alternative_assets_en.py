# data/english/alternative_assets_en.py
"""
Alternative assets data in English - COMPLETE WITH YEARLY RETURNS
Includes precious metals, commodities, and real estate investment trusts
"""

ALTERNATIVE_ASSETS_EN = {
    "Gold": {
        "descrizione": "Precious metal considered a store of value and hedge against currency debasement and geopolitical instability.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "27.0%",   # 2024 - Exceptional year
                "anno_2": "13.1%",   # 2023 - Continued rise
                "anno_3": "0.4%",    # 2022 - Sideways with inflation
                "anno_4": "-3.6%",   # 2021 - Recovery pressure
                "anno_5": "24.4%",   # 2020 - COVID flight to safety
                "anno_6": "18.3%",   # 2019 - Trade tensions
                "anno_7": "-1.6%",   # 2018 - Strong dollar
                "anno_8": "13.7%",   # 2017 - Geopolitical uncertainty
                "anno_9": "8.1%",    # 2016 - Brexit, Trump
                "anno_10": "-10.4%", # 2015 - Fed hawkish
                "anno_11": "-1.5%",  # 2014 - Tapering fears
                "anno_12": "-28.3%", # 2013 - Taper tantrum
                "anno_13": "7.0%",   # 2012 - QE3 launch
                "anno_14": "10.2%",  # 2011 - Eurocrisis, QE2
                "anno_15": "29.8%",  # 2010 - QE1 effects
                "anno_16": "23.9%",  # 2009 - Crisis response
                "anno_17": "5.8%",   # 2008 - Crisis begin
                "anno_18": "31.4%",  # 2007 - Subprime fears
                "anno_19": "22.8%",  # 2006 - Housing bubble fears
                "anno_20": "18.2%"   # 2005 - Fed tightening cycle
            },
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
            "rendimenti_annuali": {
                "anno_1": "32.5%",   # 2024 - Outperformance vs gold
                "anno_2": "18.7%",   # 2023 - Industrial rally
                "anno_3": "-2.9%",   # 2022 - Weak industrial demand
                "anno_4": "-11.8%",  # 2021 - Underperform gold
                "anno_5": "47.9%",   # 2020 - Stimulus + industrial
                "anno_6": "15.2%",   # 2019 - Follows gold but less
                "anno_7": "-8.4%",   # 2018 - Industrial pressure
                "anno_8": "6.3%",    # 2017 - Moderate rise
                "anno_9": "15.8%",   # 2016 - Industrial recovery
                "anno_10": "-11.3%", # 2015 - Commodities collapse
                "anno_11": "-19.5%", # 2014 - Strong pressure
                "anno_12": "-35.9%", # 2013 - Disaster year
                "anno_13": "8.3%",   # 2012 - QE effects
                "anno_14": "83.7%",  # 2011 - Supercycle peak
                "anno_15": "69.2%",  # 2010 - QE1 + industrial
                "anno_16": "49.3%",  # 2009 - Crisis + stimulus
                "anno_17": "-26.9%", # 2008 - Industrial collapse
                "anno_18": "15.4%",  # 2007 - Commodity boom
                "anno_19": "46.1%",  # 2006 - China supercycle
                "anno_20": "29.8%"   # 2005 - Industrial demand
            },
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
            "Expansive policies": "Strong support especially if outperforming gold"
        },
        "allocazione_range": "2-5% as gold satellite",
        "correlazioni": "High correlation with gold but higher volatility"
    },

    "Commodities": {
        "descrizione": "Raw materials and primary agricultural products traded on global exchanges, including energy, industrial metals, and agricultural products.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "12.4%",   # 2024 - Recovery post-inflation
                "anno_2": "-16.9%",  # 2023 - Collapse after spike
                "anno_3": "16.1%",   # 2022 - Ukraine war spike
                "anno_4": "27.1%",   # 2021 - Reflation trade
                "anno_5": "-3.1%",   # 2020 - COVID demand shock
                "anno_6": "7.7%",    # 2019 - Trade war effects
                "anno_7": "-11.2%",  # 2018 - Strong dollar
                "anno_8": "1.7%",    # 2017 - Modest growth
                "anno_9": "11.8%",   # 2016 - Recovery begin
                "anno_10": "-24.7%", # 2015 - Commodity crash
                "anno_11": "-17.0%", # 2014 - End of supercycle
                "anno_12": "-1.1%",  # 2013 - China slowdown
                "anno_13": "-1.1%",  # 2012 - Modest recovery
                "anno_14": "1.9%",   # 2011 - Peak supercycle
                "anno_15": "16.8%",  # 2010 - Recovery + China
                "anno_16": "18.9%",  # 2009 - Stimulus effects
                "anno_17": "-35.7%", # 2008 - Financial crisis
                "anno_18": "9.5%",   # 2007 - China boom
                "anno_19": "6.5%",   # 2006 - Supercycle
                "anno_20": "21.0%"   # 2005 - China acceleration
            },
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
            "rendimenti_annuali": {
                "anno_1": "11.2%",   # 2024 - Stable rates
                "anno_2": "-2.5%",   # 2023 - Rate pressure
                "anno_3": "-25.1%",  # 2022 - Rate shock disaster
                "anno_4": "43.2%",   # 2021 - Recovery + low rates
                "anno_5": "-5.1%",   # 2020 - COVID lockdowns
                "anno_6": "22.8%",   # 2019 - Rate cuts
                "anno_7": "-4.6%",   # 2018 - Rising rates
                "anno_8": "9.3%",    # 2017 - Moderate growth
                "anno_9": "8.6%",    # 2016 - Rate stability
                "anno_10": "2.5%",   # 2015 - Rate uncertainty
                "anno_11": "28.0%",  # 2014 - QE3 effects
                "anno_12": "2.9%",   # 2013 - Taper tantrum
                "anno_13": "19.7%",  # 2012 - QE boost
                "anno_14": "8.3%",   # 2011 - Crisis recovery
                "anno_15": "27.9%",  # 2010 - QE1 + recovery
                "anno_16": "28.0%",  # 2009 - Recovery from lows
                "anno_17": "-37.7%", # 2008 - Real estate crisis
                "anno_18": "-15.7%", # 2007 - Housing peak
                "anno_19": "35.1%",  # 2006 - Bubble peak
                "anno_20": "12.2%"   # 2005 - Pre-bubble
            },
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
