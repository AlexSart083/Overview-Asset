# Enhanced asset_data_en.py with historical performance data - CORRECTED VERSION
ASSET_DATA_EN = {
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
    },

    "Bonds 0-1 Years": {
        "descrizione": "Government and corporate debt securities with very short-term maturity within one year. European government bonds offer maximum credit safety while corporates provide additional spread but with higher credit risk.",
        "performance_storica": {
            "20_anni": "2.8%",
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

# UI text in English
UI_TEXT_EN = {
    "title": "Financial Asset Analyzer",
    "subtitle": "Educational analysis of different financial assets",
    "sidebar_title": "Asset Selection",
    "language_label": "Language",
    "asset_label": "Select Asset",
    "analysis_title": "Asset Analysis: ",
    "description_header": "📖 Description",
    "performance_header": "📊 Historical Performance (Annualized)",
    "strengths_header": "✅ Strengths",
    "weaknesses_header": "⚠️ Weaknesses", 
    "scenarios_header": "📊 Market Scenarios Performance",
    "allocation_header": "💼 Indicative Allocation Range",
    "correlations_header": "🔗 Correlations with Other Assets",
    "summary_header": "📝 Educational Summary",
    "warning": "⚠️ **Important Disclaimer**: This information is for educational purposes only and does not constitute personalized financial advice.",
    "visualization_title": "📈 Performance Visualization",
    "heatmap_title": "Asset Performance Heatmap by Market Scenario",
    "allocation_pie_title": "Sample Portfolio Allocation",
    "performance_note": "📌 **Note**: Historical performance data is based on relevant market indices and is not a guarantee of future results. Past performance does not predict future returns."
}
