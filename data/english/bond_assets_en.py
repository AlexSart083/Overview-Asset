# data/english/bond_assets_en.py
"""
Bond and fixed income assets data in English - COMPLETE WITH YEARLY RETURNS
Clear separation between government and corporate bonds
"""

BOND_ASSETS_EN = {
    # ===== GOVERNMENT BONDS =====
    "Government Bonds 0-1 Years": {
        "descrizione": "European government debt securities with very short-term maturity within one year. They represent the ultimate risk-free benchmark with virtually zero credit risk but very contained yields.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "4.2%",    # 2024
                "anno_2": "3.8%",    # 2023
                "anno_3": "1.9%",    # 2022
                "anno_4": "-0.1%",   # 2021
                "anno_5": "-0.3%",   # 2020
                "anno_6": "-0.2%",   # 2019
                "anno_7": "-0.1%",   # 2018
                "anno_8": "-0.4%",   # 2017
                "anno_9": "-0.3%",   # 2016
                "anno_10": "0.1%",   # 2015
                "anno_11": "0.2%",   # 2014
                "anno_12": "0.3%",   # 2013
                "anno_13": "0.8%",   # 2012
                "anno_14": "1.4%",   # 2011
                "anno_15": "0.8%",   # 2010
                "anno_16": "1.2%",   # 2009
                "anno_17": "4.2%",   # 2008
                "anno_18": "4.1%",   # 2007
                "anno_19": "3.6%",   # 2006
                "anno_20": "2.8%"    # 2005
            },
            "20_anni": "2.5%",
            "10_anni": "0.8%",
            "5_anni": "1.8%",
            "1_anno": "4.2%",
            "indice_riferimento": "Euro Short-Term Rate (€STR) / Euro Government 0-1Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Zero credit risk (government backing)",
            "Maximum liquidity in markets",
            "Minimum volatility",
            "Absolute capital protection",
            "Frequent reinvestment at current rates",
            "Risk-free benchmark for all other assets"
        ],
        "punti_debolezza": [
            "Very low or negative yields",
            "No inflation protection if real rates negative",
            "Reinvestment risk",
            "High opportunity cost in rising markets",
            "Negative real performance in inflationary periods"
        ],
        "scenari": {
            "Economic growth": "Stable performance but very low yields",
            "Recession": "Maximum outperformance from flight-to-quality",
            "High inflation": "Negative real performance from negative real rates",
            "Restrictive policies": "Gradual benefits from reinvestment at higher rates",
            "Expansive policies": "Stable performance but yields decline further"
        },
        "allocazione_range": "15-40% for absolute liquidity and stability",
        "correlazioni": "Zero correlation with equities, perfect with short-term rates"
    },

    "Government Bonds 1-3 Years": {
        "descrizione": "European government bonds with short-term maturity offering the optimal balance between safety and yield in the government segment, maintaining zero credit risk.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "3.8%",    # 2024
                "anno_2": "2.9%",    # 2023
                "anno_3": "-1.2%",   # 2022
                "anno_4": "-0.5%",   # 2021
                "anno_5": "0.8%",    # 2020
                "anno_6": "0.9%",    # 2019
                "anno_7": "0.6%",    # 2018
                "anno_8": "-0.2%",   # 2017
                "anno_9": "-0.1%",   # 2016
                "anno_10": "0.4%",   # 2015
                "anno_11": "1.2%",   # 2014
                "anno_12": "1.8%",   # 2013
                "anno_13": "2.9%",   # 2012
                "anno_14": "3.8%",   # 2011
                "anno_15": "3.1%",   # 2010
                "anno_16": "4.2%",   # 2009
                "anno_17": "5.8%",   # 2008
                "anno_18": "4.9%",   # 2007
                "anno_19": "3.7%",   # 2006
                "anno_20": "3.2%"    # 2005
            },
            "20_anni": "3.0%",
            "10_anni": "1.5%",
            "5_anni": "2.2%",
            "1_anno": "3.8%",
            "indice_riferimento": "Euro Government 1-3Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Optimal safety/yield combination in government segment",
            "Contained interest rate risk",
            "Excellent liquidity",
            "Low volatility",
            "Effective diversification vs equity",
            "No credit risk"
        ],
        "punti_debolezza": [
            "Still limited yields",
            "Interest rate sensitivity present though contained",
            "Negative performance with rapid rate rises",
            "Limited inflation protection"
        ],
        "scenari": {
            "Economic growth": "Slightly negative performance from rate rise expectations",
            "Recession": "Strongly positive performance (flight to quality)",
            "High inflation": "Negative but very contained performance",
            "Restrictive policies": "Limited negative pressure",
            "Expansive policies": "Moderately positive performance"
        },
        "allocazione_range": "20-45% as defensive portfolio core",
        "correlazioni": "Moderate negative correlation with equities"
    },

    "Government Bonds 3-7 Years": {
        "descrizione": "European government bonds with medium-term maturity representing the sweet spot of the government curve, offering more interesting yields while maintaining absolute credit safety.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "2.2%",    # 2024
                "anno_2": "-3.1%",   # 2023
                "anno_3": "-8.4%",   # 2022
                "anno_4": "-2.8%",   # 2021
                "anno_5": "4.1%",    # 2020
                "anno_6": "6.8%",    # 2019
                "anno_7": "1.2%",    # 2018
                "anno_8": "1.8%",    # 2017
                "anno_9": "3.4%",    # 2016
                "anno_10": "1.9%",   # 2015
                "anno_11": "8.1%",   # 2014
                "anno_12": "2.4%",   # 2013
                "anno_13": "7.8%",   # 2012
                "anno_14": "9.7%",   # 2011
                "anno_15": "4.1%",   # 2010
                "anno_16": "8.9%",   # 2009
                "anno_17": "7.2%",   # 2008
                "anno_18": "1.8%",   # 2007
                "anno_19": "2.1%",   # 2006
                "anno_20": "4.7%"    # 2005
            },
            "20_anni": "3.8%",
            "10_anni": "2.5%",
            "5_anni": "0.9%",
            "1_anno": "2.2%",
            "indice_riferimento": "Euro Government 3-7Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "More interesting government yields",
            "Sweet spot of the yield curve",
            "Zero credit risk",
            "Still very good liquidity",
            "Significant potential capital gains if rates fall",
            "Optimal diversification vs equities"
        ],
        "punti_debolezza": [
            "Significant interest rate sensitivity",
            "Moderate-high volatility",
            "Duration risk",
            "Negative performance with rising rates"
        ],
        "scenari": {
            "Economic growth": "Negative performance from rate rise expectations",
            "Recession": "Strongly positive performance (+8-15%)",
            "High inflation": "Significantly negative performance",
            "Restrictive policies": "Significant negative pressure",
            "Expansive policies": "Positive performance with capital gains"
        },
        "allocazione_range": "15-30% for government yield with controlled risk",
        "correlazioni": "Negative correlation with equities, high rate sensitivity"
    },

    "Government Bonds 7-10 Years": {
        "descrizione": "European government bonds with medium-long term maturity representing the ultimate duration benchmark, offering maximum deflationary hedge in the government segment.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "1.0%",    # 2024
                "anno_2": "-5.8%",   # 2023
                "anno_3": "-14.2%",  # 2022
                "anno_4": "-4.1%",   # 2021
                "anno_5": "8.9%",    # 2020
                "anno_6": "9.7%",    # 2019
                "anno_7": "2.1%",    # 2018
                "anno_8": "2.8%",    # 2017
                "anno_9": "4.8%",    # 2016
                "anno_10": "1.2%",   # 2015
                "anno_11": "12.9%",  # 2014
                "anno_12": "1.8%",   # 2013
                "anno_13": "11.4%",  # 2012
                "anno_14": "14.2%",  # 2011
                "anno_15": "6.8%",   # 2010
                "anno_16": "12.1%",  # 2009
                "anno_17": "8.9%",   # 2008
                "anno_18": "1.2%",   # 2007
                "anno_19": "1.8%",   # 2006
                "anno_20": "6.2%"    # 2005
            },
            "20_anni": "4.5%",
            "10_anni": "3.0%",
            "5_anni": "0.5%",
            "1_anno": "1.0%",
            "indice_riferimento": "Euro Government 7-10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Potentially attractive government yields",
            "Strong potential capital gains if rates fall",
            "Maximum diversification vs equities",
            "Perfect deflationary hedge",
            "Pension fund benchmark",
            "No credit risk"
        ],
        "punti_debolezza": [
            "High interest rate sensitivity",
            "Significant volatility",
            "High duration risk",
            "Very negative performance with inflation/rising rates"
        ],
        "scenari": {
            "Economic growth": "Significantly negative performance",
            "Recession": "Excellent performance (+12-25%)",
            "High inflation": "Very negative performance (-10-20%)",
            "Restrictive policies": "Very negative performance",
            "Expansive policies": "Strongly positive performance"
        },
        "allocazione_range": "10-25% for deflationary hedge",
        "correlazioni": "Strong negative correlation with equities, inverse with rates"
    },

    "Government Bonds >10 Years": {
        "descrizione": "European government bonds with long-term maturity offering maximum duration sensitivity and representing the ultimate hedge against extreme deflationary scenarios.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "0.5%",    # 2024
                "anno_2": "-7.9%",   # 2023
                "anno_3": "-18.1%",  # 2022
                "anno_4": "-5.2%",   # 2021
                "anno_5": "12.1%",   # 2020
                "anno_6": "11.8%",   # 2019
                "anno_7": "2.8%",    # 2018
                "anno_8": "3.2%",    # 2017
                "anno_9": "6.1%",    # 2016
                "anno_10": "0.8%",   # 2015
                "anno_11": "15.8%",  # 2014
                "anno_12": "1.2%",   # 2013
                "anno_13": "14.9%",  # 2012
                "anno_14": "17.8%",  # 2011
                "anno_15": "8.2%",   # 2010
                "anno_16": "14.8%",  # 2009
                "anno_17": "10.1%",  # 2008
                "anno_18": "0.8%",   # 2007
                "anno_19": "1.4%",   # 2006
                "anno_20": "7.8%"    # 2005
            },
            "20_anni": "4.9%",
            "10_anni": "3.8%",
            "5_anni": "-0.5%",
            "1_anno": "0.5%",
            "indice_riferimento": "Euro Government >10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Potentially highest government yields",
            "Maximum potential capital gains",
            "Maximum diversification vs equities",
            "Optimal deflation/recession hedge",
            "Perfect matching for long-term liabilities",
            "Absolute credit safety"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "Maximum duration risk",
            "Extreme rate sensitivity",
            "Potentially lower liquidity",
            "Disastrous performance with inflation",
            "Very distant reinvestment risk"
        ],
        "scenari": {
            "Economic growth": "Very negative performance",
            "Recession": "Exceptional performance (+15-35%)",
            "High inflation": "Disastrous performance (-15-30%)",
            "Restrictive policies": "Very negative performance",
            "Expansive policies": "Excellent performance"
        },
        "allocazione_range": "0-15% only for specific deflation hedge",
        "correlazioni": "Maximum negative correlation with equities, perfect inverse with rates"
    },

    # ===== CORPORATE BONDS =====
    "Corporate Bonds 0-1 Years": {
        "descrizione": "European corporate bonds with very short-term maturity offering attractive credit spreads with minimal duration, ideal for enhancing yield while maintaining low volatility.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "5.4%",    # 2024
                "anno_2": "4.8%",    # 2023
                "anno_3": "2.1%",    # 2022
                "anno_4": "0.2%",    # 2021
                "anno_5": "0.8%",    # 2020
                "anno_6": "1.2%",    # 2019
                "anno_7": "0.8%",    # 2018
                "anno_8": "0.3%",    # 2017
                "anno_9": "0.6%",    # 2016
                "anno_10": "0.9%",   # 2015
                "anno_11": "1.4%",   # 2014
                "anno_12": "1.8%",   # 2013
                "anno_13": "2.9%",   # 2012
                "anno_14": "3.2%",   # 2011
                "anno_15": "2.1%",   # 2010
                "anno_16": "4.8%",   # 2009
                "anno_17": "6.9%",   # 2008
                "anno_18": "4.2%",   # 2007
                "anno_19": "3.8%",   # 2006
                "anno_20": "3.1%"    # 2005
            },
            "20_anni": "3.2%",
            "10_anni": "1.6%",
            "5_anni": "2.5%",
            "1_anno": "5.4%",
            "indice_riferimento": "Euro Corporate 0-1Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Attractive credit spread vs government",
            "Minimal duration limits rate risk",
            "Good liquidity on primary issuers",
            "Sector diversification",
            "Frequent reinvestment with spread pickup",
            "Contained volatility"
        ],
        "punti_debolezza": [
            "Credit risk present",
            "Spread risk during market stress",
            "Economic cycle correlation",
            "Possible rating deterioration",
            "Lower liquidity vs government"
        ],
        "scenari": {
            "Economic growth": "Positive performance from improving fundamentals",
            "Recession": "Negative pressure from credit risk and spread widening",
            "High inflation": "Mixed performance, depends on pricing power",
            "Restrictive policies": "Pressure from recession risk",
            "Expansive policies": "Positive performance from economic support"
        },
        "allocazione_range": "10-25% for extra yield at low risk",
        "correlazioni": "Low correlation with equities, moderate with credit spreads"
    },

    "Corporate Bonds 1-3 Years": {
        "descrizione": "European corporate bonds with short-term maturity combining attractive credit spreads with limited duration, offering the best risk/return ratio in the corporate segment.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "4.8%",    # 2024
                "anno_2": "3.9%",    # 2023
                "anno_3": "-0.4%",   # 2022
                "anno_4": "-0.2%",   # 2021
                "anno_5": "2.8%",    # 2020
                "anno_6": "2.4%",    # 2019
                "anno_7": "1.2%",    # 2018
                "anno_8": "1.8%",    # 2017
                "anno_9": "2.1%",    # 2016
                "anno_10": "1.8%",   # 2015
                "anno_11": "3.9%",   # 2014
                "anno_12": "3.2%",   # 2013
                "anno_13": "6.8%",   # 2012
                "anno_14": "4.1%",   # 2011
                "anno_15": "6.2%",   # 2010
                "anno_16": "9.1%",   # 2009
                "anno_17": "-2.8%",  # 2008
                "anno_18": "3.1%",   # 2007
                "anno_19": "2.8%",   # 2006
                "anno_20": "3.9%"    # 2005
            },
            "20_anni": "3.8%",
            "10_anni": "2.4%",
            "5_anni": "2.8%",
            "1_anno": "4.8%",
            "indice_riferimento": "Euro Corporate 1-3Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Optimal spread/duration trade-off",
            "Significant spreads vs equivalent government",
            "Broad sector diversification",
            "Good liquidity on investment grade issuers",
            "Outperformance potential in economic growth",
            "Controlled duration"
        ],
        "punti_debolezza": [
            "Credit and spread risk",
            "Economic cycle sensitivity",
            "Equity correlation in stress periods",
            "Possible rating downgrades",
            "Credit analysis complexity"
        ],
        "scenari": {
            "Economic growth": "Significant outperformance from spread tightening",
            "Recession": "Negative performance from credit deterioration",
            "High inflation": "Variable performance by sector",
            "Restrictive policies": "Pressure from possible credit stress",
            "Expansive policies": "Positive performance from improving fundamentals"
        },
        "allocazione_range": "15-30% as corporate segment core",
        "correlazioni": "Moderate correlation with equities, high with credit spreads"
    },

    "Corporate Bonds 3-7 Years": {
        "descrizione": "European corporate bonds with medium-term maturity where credit spreads become more significant, offering superior yields but with greater credit risk exposure amplified by duration.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "3.2%",    # 2024
                "anno_2": "-1.8%",   # 2023
                "anno_3": "-7.2%",   # 2022
                "anno_4": "-1.4%",   # 2021
                "anno_5": "6.8%",    # 2020
                "anno_6": "7.9%",    # 2019
                "anno_7": "-0.9%",   # 2018
                "anno_8": "3.1%",    # 2017
                "anno_9": "4.8%",    # 2016
                "anno_10": "0.8%",   # 2015
                "anno_11": "9.4%",   # 2014
                "anno_12": "4.1%",   # 2013
                "anno_13": "12.8%",  # 2012
                "anno_14": "7.9%",   # 2011
                "anno_15": "8.1%",   # 2010
                "anno_16": "18.2%",  # 2009
                "anno_17": "-8.4%",  # 2008
                "anno_18": "1.9%",   # 2007
                "anno_19": "2.4%",   # 2006
                "anno_20": "5.1%"    # 2005
            },
            "20_anni": "4.5%",
            "10_anni": "3.2%",
            "5_anni": "1.6%",
            "1_anno": "3.2%",
            "indice_riferimento": "Euro Corporate 3-7Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Very attractive credit spreads",
            "Superior yields to government segment",
            "Significant sector diversification",
            "Potential capital gains from spread tightening",
            "Good liquidity on primary issuers",
            "Economic growth exposure"
        ],
        "punti_debolezza": [
            "Double exposure: duration + credit risk",
            "High volatility in stress periods",
            "Amplified sensitivity to credit cycles",
            "Increasing equity correlation in crisis",
            "Risk of significant spread widening"
        ],
        "scenari": {
            "Economic growth": "Very positive performance from double alpha (rates + spreads)",
            "Recession": "Very negative performance from credit deterioration",
            "High inflation": "Mixed performance, sectors differently impacted",
            "Restrictive policies": "Double negative pressure (rates + credit)",
            "Expansive policies": "Excellent performance if fundamentals hold"
        },
        "allocazione_range": "10-20% for superior yield with controlled risks",
        "correlazioni": "Moderate-high correlation with equities, very high with spreads"
    },

    "Corporate Bonds 7-10 Years": {
        "descrizione": "European corporate bonds with medium-long term maturity concentrating maximum credit risk with high duration, suitable only for investors who understand the risk/return complexity.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "1.8%",    # 2024
                "anno_2": "-4.2%",   # 2023
                "anno_3": "-12.1%",  # 2022
                "anno_4": "-2.8%",   # 2021
                "anno_5": "9.4%",    # 2020
                "anno_6": "10.8%",   # 2019
                "anno_7": "-1.9%",   # 2018
                "anno_8": "4.1%",    # 2017
                "anno_9": "6.8%",    # 2016
                "anno_10": "-0.2%",  # 2015
                "anno_11": "12.4%",  # 2014
                "anno_12": "5.9%",   # 2013
                "anno_13": "18.1%",  # 2012
                "anno_14": "8.4%",   # 2011
                "anno_15": "11.2%",  # 2010
                "anno_16": "24.8%",  # 2009
                "anno_17": "-14.2%", # 2008
                "anno_18": "0.8%",   # 2007
                "anno_19": "2.1%",   # 2006
                "anno_20": "6.8%"    # 2005
            },
            "20_anni": "5.1%",
            "10_anni": "3.8%",
            "5_anni": "1.2%",
            "1_anno": "1.8%",
            "indice_riferimento": "Euro Corporate 7-10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Maximum spreads to compensate risks",
            "Very high potential capital gains",
            "Potentially attractive yields",
            "Sector diversification",
            "Maximum benefits in recovery scenarios",
            "Amplified growth exposure"
        ],
        "punti_debolezza": [
            "Maximum risk concentration",
            "Very high volatility",
            "Duration + credit risk amplification",
            "High equity correlation in stress",
            "Possible severe losses in recessions",
            "High management complexity"
        ],
        "scenari": {
            "Economic growth": "Excellent but highly volatile performance",
            "Recession": "Disastrous performance from duration + credit combination",
            "High inflation": "Very negative performance",
            "Restrictive policies": "Extremely vulnerable",
            "Expansive policies": "Significant outperformance if credit holds"
        },
        "allocazione_range": "5-15% only for sophisticated investors",
        "correlazioni": "High correlation with equities, maximum with credit spreads"
    },

    "Corporate Bonds >10 Years": {
        "descrizione": "European corporate bonds with long-term maturity representing the most complex and risky asset in the fixed income segment, combining extreme duration with maximum credit risk.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "1.2%",    # 2024
                "anno_2": "-6.8%",   # 2023
                "anno_3": "-16.4%",  # 2022
                "anno_4": "-4.1%",   # 2021
                "anno_5": "12.8%",   # 2020
                "anno_6": "13.9%",   # 2019
                "anno_7": "-2.1%",   # 2018
                "anno_8": "5.2%",    # 2017
                "anno_9": "8.4%",    # 2016
                "anno_10": "-1.8%",  # 2015
                "anno_11": "16.2%",  # 2014
                "anno_12": "7.1%",   # 2013
                "anno_13": "22.4%",  # 2012
                "anno_14": "9.8%",   # 2011
                "anno_15": "14.1%",  # 2010
                "anno_16": "31.2%",  # 2009
                "anno_17": "-21.8%", # 2008
                "anno_18": "-0.4%",  # 2007
                "anno_19": "1.8%",   # 2006
                "anno_20": "8.9%"    # 2005
            },
            "20_anni": "5.5%",
            "10_anni": "4.5%",
            "5_anni": "0.2%",
            "1_anno": "1.2%",
            "indice_riferimento": "Euro Corporate >10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Absolute maximum spreads",
            "Extreme potential capital gains",
            "Potentially very high yields",
            "Matching for long-term corporate liabilities",
            "Maximum exposure to credit cycles",
            "Sector diversification"
        ],
        "punti_debolezza": [
            "Absolute maximum risk in fixed income",
            "Extreme volatility",
            "Potentially problematic liquidity",
            "Maximum equity correlation in crisis",
            "Risk of devastating losses",
            "Extreme analytical complexity"
        ],
        "scenari": {
            "Economic growth": "Potentially excellent but extremely volatile performance",
            "Recession": "Catastrophic performance",
            "High inflation": "Disastrous performance",
            "Restrictive policies": "Extremely vulnerable",
            "Expansive policies": "Maximum possible outperformance if everything goes well"
        },
        "allocazione_range": "0-10% only for highly sophisticated investors",
        "correlazioni": "Maximum correlation with equities and spreads, extreme duration"
    },

    # ===== SPECIALIZED BONDS =====
    "High Yield Bonds": {
        "descrizione": "High-yield corporate bonds issued by companies with lower credit ratings (junk bonds), offering higher yields to compensate for greater credit risk.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "8.9%",    # 2024
                "anno_2": "5.8%",    # 2023
                "anno_3": "-11.2%",  # 2022
                "anno_4": "5.3%",    # 2021
                "anno_5": "7.1%",    # 2020
                "anno_6": "14.4%",   # 2019
                "anno_7": "-2.1%",   # 2018
                "anno_8": "7.5%",    # 2017
                "anno_9": "17.5%",   # 2016
                "anno_10": "-4.5%",  # 2015
                "anno_11": "2.5%",   # 2014
                "anno_12": "7.4%",   # 2013
                "anno_13": "15.8%",  # 2012
                "anno_14": "4.4%",   # 2011
                "anno_15": "15.1%",  # 2010
                "anno_16": "57.5%",  # 2009
                "anno_17": "-26.2%", # 2008
                "anno_18": "-1.6%",  # 2007
                "anno_19": "11.9%",  # 2006
                "anno_20": "2.7%"    # 2005
            },
            "20_anni": "6.8%",
            "10_anni": "5.4%",
            "5_anni": "4.2%",
            "1_anno": "8.9%",
            "indice_riferimento": "Bloomberg Pan-European High Yield Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Significantly higher yields",
            "Lower interest rate sensitivity",
            "Behavior similar to risky assets",
            "Geographic and sector diversification",
            "Capital appreciation potential"
        ],
        "punti_debolezza": [
            "High credit risk",
            "High correlation with equities during stress",
            "Lower liquidity during crisis periods",
            "Higher volatility than investment grade bonds",
            "Significant default risk"
        ],
        "scenari": {
            "Economic growth": "Very positive performance (+6-10% annually)",
            "Recession": "Very negative performance (-15-25%)",
            "High inflation": "Relatively good performance if economy holds",
            "Restrictive policies": "Negative but limited pressure",
            "Expansive policies": "Very positive performance"
        },
        "allocazione_range": "5-15% for yield enhancement with controlled risk",
        "correlazioni": "Moderate-high correlation with equities, low with interest rates"
    },

    "Inflation Linked Bonds": {
        "descrizione": "Bonds whose principal and coupons are indexed to inflation, designed to protect the investor's purchasing power (Euro inflation-linked bonds, TIPS equivalent).",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "1.8%",    # 2024
                "anno_2": "5.4%",    # 2023
                "anno_3": "1.2%",    # 2022
                "anno_4": "3.8%",    # 2021
                "anno_5": "7.9%",    # 2020
                "anno_6": "4.1%",    # 2019
                "anno_7": "0.8%",    # 2018
                "anno_8": "2.1%",    # 2017
                "anno_9": "0.4%",    # 2016
                "anno_10": "-0.7%",  # 2015
                "anno_11": "6.8%",   # 2014
                "anno_12": "-1.2%",  # 2013
                "anno_13": "1.8%",   # 2012
                "anno_14": "13.5%",  # 2011
                "anno_15": "2.3%",   # 2010
                "anno_16": "11.4%",  # 2009
                "anno_17": "2.1%",   # 2008
                "anno_18": "1.2%",   # 2007
                "anno_19": "0.9%",   # 2006
                "anno_20": "1.6%"    # 2005
            },
            "20_anni": "3.8%",
            "10_anni": "2.1%",
            "5_anni": "3.4%",
            "1_anno": "1.8%",
            "indice_riferimento": "Euro Inflation-Linked Government Bond Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Direct inflation protection",
            "Guaranteed real return",
            "Portfolio diversification",
            "Low credit risk (government)",
            "Negative correlation with inflation breakeven"
        ],
        "punti_debolezza": [
            "Negative performance if inflation falls",
            "Volatility from inflation expectation changes",
            "Often low real yields",
            "Pricing complexity",
            "Lower liquidity than conventional bonds"
        ],
        "scenari": {
            "Economic growth": "Positive performance if accompanied by inflation",
            "Recession": "Mixed performance (deflation negative, flight to quality positive)",
            "High inflation": "Excellent performance (+5-15%)",
            "Restrictive policies": "Negative performance from disinflation expectations",
            "Expansive policies": "Very positive performance from inflation expectations"
        },
        "allocazione_range": "5-20% for specific inflation protection",
        "correlazioni": "Positive correlation with inflation expectations, negative with nominal bonds"
    },

    "Convertible Bonds": {
        "descrizione": "Bonds that can be converted into shares of the issuing company under predetermined conditions, offering hybrid debt/equity characteristics.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "12.1%",   # 2024
                "anno_2": "1.8%",    # 2023
                "anno_3": "-15.4%",  # 2022
                "anno_4": "7.9%",    # 2021
                "anno_5": "32.0%",   # 2020
                "anno_6": "15.8%",   # 2019
                "anno_7": "-8.9%",   # 2018
                "anno_8": "14.5%",   # 2017
                "anno_9": "4.2%",    # 2016
                "anno_10": "-3.1%",  # 2015
                "anno_11": "9.5%",   # 2014
                "anno_12": "21.6%",  # 2013
                "anno_13": "17.8%",  # 2012
                "anno_14": "-9.4%",  # 2011
                "anno_15": "15.2%",  # 2010
                "anno_16": "38.9%",  # 2009
                "anno_17": "-35.7%", # 2008
                "anno_18": "-3.1%",  # 2007
                "anno_19": "4.8%",   # 2006
                "anno_20": "3.2%"    # 2005
            },
            "20_anni": "5.8%",
            "10_anni": "7.2%",
            "5_anni": "8.4%",
            "1_anno": "12.1%",
            "indice_riferimento": "Refinitiv Europe Convertible Bond Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Participation in equity upside",
            "Downside protection vs equities",
            "Coupon income",
            "Significant capital appreciation potential",
            "Hybrid diversification"
        ],
        "punti_debolezza": [
            "Valuation complexity",
            "Sensitivity to implied volatility",
            "Underperformance if stocks sideways",
            "Issuer credit risk",
            "Often limited liquidity"
        ],
        "scenari": {
            "Economic growth": "Very positive performance (equity upside)",
            "Recession": "Negative but better than equities (-8-18%)",
            "High inflation": "Mixed performance depends on underlying sectors",
            "Restrictive policies": "Negative pressure from rates and equity",
            "Expansive policies": "Very positive performance (equity rally + low rates)"
        },
        "allocazione_range": "3-10% for hybrid debt/equity exposure",
        "correlazioni": "Moderate-high correlation with equities, sensitive to volatility"
    },

    "Subordinated Bonds": {
        "descrizione": "Debt securities that in case of liquidation are repaid after senior creditors, offering higher yields for greater risk (European Tier 2, AT1, subordinated bank bonds).",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "7.4%",    # 2024
                "anno_2": "8.2%",    # 2023
                "anno_3": "-9.1%",   # 2022
                "anno_4": "3.8%",    # 2021
                "anno_5": "-2.4%",   # 2020
                "anno_6": "9.7%",    # 2019
                "anno_7": "-5.2%",   # 2018
                "anno_8": "6.1%",    # 2017
                "anno_9": "8.9%",    # 2016
                "anno_10": "2.1%",   # 2015
                "anno_11": "11.4%",  # 2014
                "anno_12": "12.8%",  # 2013
                "anno_13": "19.4%",  # 2012
                "anno_14": "-8.7%",  # 2011
                "anno_15": "13.5%",  # 2010
                "anno_16": "45.2%",  # 2009
                "anno_17": "-18.9%", # 2008
                "anno_18": "-0.8%",  # 2007
                "anno_19": "1.4%",   # 2006
                "anno_20": "2.9%"    # 2005
            },
            "20_anni": "5.2%",
            "10_anni": "4.8%",
            "5_anni": "3.1%",
            "1_anno": "7.4%",
            "indice_riferimento": "European Bank Subordinated Debt Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Significantly higher yields",
            "Often high-quality issuers (banks, utilities)",
            "Favorable regulatory treatment for banks",
            "Credit risk diversification",
            "Reasonable liquidity in developed markets"
        ],
        "punti_debolezza": [
            "Subordination risk",
            "Possibility of coupon cancellation or conversion",
            "Structural complexity",
            "Regulatory risk (Basel III)",
            "Correlation with financial sector"
        ],
        "scenari": {
            "Economic growth": "Positive performance (+4-8% annually)",
            "Recession": "Significant negative performance (-10-20%)",
            "High inflation": "Mixed performance depends on issuer financial health",
            "Restrictive policies": "Negative pressure from banking sector stress",
            "Expansive policies": "Positive performance from financial sector support"
        },
        "allocazione_range": "2-8% for sophisticated investors who understand risks",
        "correlazioni": "High correlation with financial sector, moderate with equities"
    }
}
