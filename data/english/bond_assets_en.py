# data/english/bond_assets_en.py
"""
Bond and fixed income assets data in English
Includes government bonds, corporate bonds, and specialized bond strategies
"""

BOND_ASSETS_EN = {
    "Bonds 0-1 Years": {
        "descrizione": "Government and corporate debt securities with very short-term maturity within one year. European government bonds offer maximum credit safety while corporates provide additional spread but with higher credit risk.",
        "performance_storica": {
            "20_anni": "4.1%",
            "10_anni": "2.8%",
            "5_anni": "1.2%",
            "1_anno": "2.8%",
            "indice_riferimento": "Euro Government 3-7Y Index / Euro Corporate 3-7Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "More interesting yields",
            "Duration/yield sweet spot",
            "Portfolio diversification",
            "Still good liquidity",
            "Corporate: significant spreads for extra yield",
            "Potential capital gains if rates fall"
        ],
        "punti_debolezza": [
            "Significant interest rate sensitivity",
            "Moderate-high volatility",
            "Duration risk",
            "Corporate: sensitivity to credit cycle and spread volatility",
            "Negative performance with rising rates"
        ],
        "scenari": {
            "Economic growth": "Government: negative performance from rate rise expectations; Corporate: mixed performance (rates negative, credit positive)",
            "Recession": "Government: strongly positive performance; Corporate: negative performance from credit deterioration",
            "High inflation": "Significantly negative performance for both",
            "Restrictive policies": "Significant negative pressure, corporates doubly vulnerable",
            "Expansive policies": "Positive performance, corporate outperformance"
        },
        "allocazione_range": "10-25% for yield with controlled risk",
        "correlazioni": "Negative correlation with equities, high rate sensitivity"
    },

    "Bonds 7-10 Years": {
        "descrizione": "Government and corporate debt securities with medium-long term maturity. European government bonds represent the duration benchmark, while corporates offer substantial spreads but with significant credit risk amplified by duration.",
        "performance_storica": {
            "20_anni": "4.8%",
            "10_anni": "3.2%",
            "5_anni": "0.8%",
            "1_anno": "1.4%",
            "indice_riferimento": "Euro Government 7-10Y Index / Euro Corporate 7-10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Potentially attractive yields",
            "Strong potential capital gains if rates fall",
            "Significant diversification vs equities",
            "Government: perfect deflationary hedge",
            "Corporate: attractive spreads for duration risk compensation",
            "Benchmark for many pension funds"
        ],
        "punti_debolezza": [
            "High interest rate sensitivity",
            "Significant volatility",
            "High duration risk",
            "Corporate: amplification of credit risk with duration",
            "Very negative performance with inflation/rising rates"
        ],
        "scenari": {
            "Economic growth": "Government: significantly negative performance; Corporate: very negative performance (rates + spreads)",
            "Recession": "Government: excellent performance (+10-20%); Corporate: negative performance from default risk",
            "High inflation": "Very negative performance (-10-20%) for both",
            "Restrictive policies": "Very negative performance, corporates particularly vulnerable",
            "Expansive policies": "Strongly positive performance, corporate outperformance"
        },
        "allocazione_range": "5-20% for duration diversification",
        "correlazioni": "Strong negative correlation with equities, negative correlation with rates"
    },

    "Bonds >10 Years": {
        "descrizione": "Government and corporate debt securities with long-term maturity. Government bonds offer maximum duration sensitivity for deflationary hedging, while corporates concentrate credit and duration risk with very high spreads.",
        "performance_storica": {
            "20_anni": "5.2%",
            "10_anni": "4.1%",
            "5_anni": "-0.2%",
            "1_anno": "0.8%",
            "indice_riferimento": "Euro Government >10Y Index / Euro Corporate >10Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Potentially highest yields",
            "Maximum potential capital gains",
            "Maximum diversification vs equities",
            "Government: optimal deflation/recession hedge",
            "Corporate: maximum spreads to compensate risks",
            "Matching long-term liabilities"
        ],
        "punti_debolezza": [
            "Very high volatility",
            "Maximum duration risk",
            "Extreme rate sensitivity",
            "Corporate: maximum concentration of credit risk",
            "Potentially lower liquidity",
            "Distant reinvestment risk"
        ],
        "scenari": {
            "Economic growth": "Government: very negative performance; Corporate: disastrous performance",
            "Recession": "Government: exceptional performance (+15-30%); Corporate: very negative performance from default risk",
            "High inflation": "Disastrous performance (-15-30%) for both",
            "Restrictive policies": "Very negative performance, corporates extremely vulnerable",
            "Expansive policies": "Excellent performance, corporate outperformance if credit holds"
        },
        "allocazione_range": "0-15% only for investors with specific objectives",
        "correlazioni": "Maximum negative correlation with equities, perfect inverse with rates"
    },

    "High Yield Bonds": {
        "descrizione": "High-yield corporate bonds issued by companies with lower credit ratings (junk bonds), offering higher yields to compensate for greater credit risk.",
        "performance_storica": {
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
}": "2.8%",
            "10_anni": "1.2%",
            "5_anni": "2.1%",
            "1_anno": "4.8%",
            "indice_riferimento": "Euro Short-Term Rate (€STR) / Euro Corporate 0-1Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Minimal interest rate risk",
            "High liquidity (especially government bonds)",
            "Low volatility",
            "Capital protection (government bonds virtually risk-free)",
            "Frequent reinvestment at current rates",
            "Corporate: additional spread for extra yield"
        ],
        "punti_debolezza": [
            "Very low yields (especially government bonds)",
            "No inflation protection if real rates negative",
            "Reinvestment risk",
            "Corporate: credit risk and spread risk",
            "Opportunity cost in rising rate environments"
        ],
        "scenari": {
            "Economic growth": "Government: stable performance but low yields; Corporate: benefit from spread tightening",
            "Recession": "Government: outperformance from flight-to-quality; Corporate: under pressure from credit risk",
            "High inflation": "Negative performance from negative real rates",
            "Restrictive policies": "Gradual benefits from reinvestment",
            "Expansive policies": "Stable performance but declining yields"
        },
        "allocazione_range": "10-30% for liquidity and stability",
        "correlazioni": "Very low correlation with equities, high correlation with short-term rates"
    },

    "Bonds 1-3 Years": {
        "descrizione": "Government and corporate debt securities with short-term maturity. European government bonds offer the risk-free benchmark, while corporates add credit spread with limited duration.",
        "performance_storica": {
            "20_anni": "3.2%",
            "10_anni": "1.8%",
            "5_anni": "2.4%",
            "1_anno": "4.2%",
            "indice_riferimento": "Euro Government 1-3Y Index / Euro Corporate 1-3Y Index",
            "data_calcolo": "Data as of December 31, 2024"
        },
        "punti_forza": [
            "Contained interest rate risk",
            "Higher yields than very short-term",
            "Good liquidity",
            "Moderate volatility",
            "Effective diversification",
            "Corporate: attractive spread pickup vs government"
        ],
        "punti_debolezza": [
            "Interest rate sensitivity (limited but present)",
            "Still limited yields for government bonds",
            "Corporate: credit risk and spread widening risk",
            "Negative performance with rapid rate rises"
        ],
        "scenari": {
            "Economic growth": "Government: moderately negative performance; Corporate: outperformance from credit improvement",
            "Recession": "Government: positive performance (flight to quality); Corporate: negative performance from credit risk",
            "High inflation": "Negative but limited performance for both",
            "Restrictive policies": "Contained negative pressure, corporates more vulnerable",
            "Expansive policies": "Moderately positive performance"
        },
        "allocazione_range": "15-35% for risk/return balance",
        "correlazioni": "Moderate negative correlation with equities"
    },

    "Bonds 3-7 Years": {
        "descrizione": "Government and corporate debt securities with medium-term maturity. Segment where the difference between government (risk-free rate) and corporate (credit spread) becomes more significant with increased duration.",
        "performance_storica": {
            "20_anni
