# =============================================================================
# ALTERNATIVE ASSETS COMPLETI - ITALIANO E INGLESE CON RENDIMENTI ANNO PER ANNO
# =============================================================================

# 1. ALTERNATIVE ASSETS ITALIANO COMPLETO - data/italian/alternative_assets_it.py
ALTERNATIVE_ASSETS_IT = {
    "Oro": {
        "descrizione": "Metallo prezioso considerato riserva di valore e copertura contro la svalutazione valutaria e l'instabilità geopolitica.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "27.0%",   # 2024 - Anno eccezionale
                "anno_2": "13.1%",   # 2023 - Continua salita
                "anno_3": "0.4%",    # 2022 - Laterale con inflazione
                "anno_4": "-3.6%",   # 2021 - Pressione recovery
                "anno_5": "24.4%",   # 2020 - COVID flight to safety
                "anno_6": "18.3%",   # 2019 - Tensioni commerciali
                "anno_7": "-1.6%",   # 2018 - Dollaro forte
                "anno_8": "13.7%",   # 2017 - Incertezza geopolitica
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
            "indice_riferimento": "Prezzo Spot Oro (USD)",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Copertura storica contro l'inflazione",
            "Riserva di valore durante le crisi",
            "Diversificazione del portafoglio",
            "Nessun rischio di controparte",
            "Riconoscimento e liquidità globali"
        ],
        "punti_debolezza": [
            "Nessuna generazione di reddito",
            "Alta volatilità nel breve termine",
            "Costi di stoccaggio e assicurazione",
            "Sensibile ai tassi di interesse reali",
            "Rischio valutario (denominato in USD)"
        ],
        "scenari": {
            "Crescita economica": "Performance moderatamente negativa",
            "Recessione": "Performance fortemente positiva (bene rifugio)",
            "Inflazione elevata": "Performance storicamente positiva",
            "Politiche restrittive": "Pressione negativa per tassi reali più alti",
            "Politiche espansive": "Positivo per timori di svalutazione valutaria"
        },
        "allocazione_range": "5-10% come copertura del portafoglio",
        "correlazioni": "Bassa correlazione con altri asset, inversa con USD"
    },

    "Argento": {
        "descrizione": "Metallo prezioso con doppia natura di bene rifugio e commodity industriale, più volatile dell'oro.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "32.5%",   # 2024 - Outperformance vs oro
                "anno_2": "18.7%",   # 2023 - Rally industriale
                "anno_3": "-2.9%",   # 2022 - Domanda industriale debole
                "anno_4": "-11.8%",  # 2021 - Underperform oro
                "anno_5": "47.9%",   # 2020 - Stimulus + industrial
                "anno_6": "15.2%",   # 2019 - Segue oro ma meno
                "anno_7": "-8.4%",   # 2018 - Pressione industriale
                "anno_8": "6.3%",    # 2017 - Moderato rialzo
                "anno_9": "15.8%",   # 2016 - Recovery industriale
                "anno_10": "-11.3%", # 2015 - Crollano commodities
                "anno_11": "-19.5%", # 2014 - Forte pressure
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
            "indice_riferimento": "Prezzo Spot Argento (USD)",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Doppia domanda: investimento e industriale",
            "Maggiore volatilità può offrire opportunità",
            "Rapporto oro/argento storicamente ciclico",
            "Utilizzi tecnologici in crescita",
            "Prezzo relativamente più accessibile"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Più sensibile ai cicli industriali dell'oro",
            "Mercato più piccolo e meno liquido",
            "Maggiori costi di stoccaggio relativi",
            "Performance storicamente inferiore all'oro"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva per domanda industriale",
            "Recessione": "Performance mista (rifugio vs domanda industriale)",
            "Inflazione elevata": "Performance molto positiva",
            "Politiche restrittive": "Pressione da tassi reali alti",
            "Politiche espansive": "Forte supporto specialmente se supera l'oro"
        },
        "allocazione_range": "2-5% come satellite dell'oro",
        "correlazioni": "Alta correlazione con oro ma maggiore volatilità"
    },

    "Materie Prime": {
        "descrizione": "Materie prime e prodotti agricoli primari negoziati sui mercati globali, inclusi energia, metalli industriali e prodotti agricoli.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "12.4%",   # 2024 - Recovery post-inflazione
                "anno_2": "-16.9%",  # 2023 - Crollano dopo spike
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
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Protezione dall'inflazione",
            "Benefici di diversificazione",
            "Dinamiche domanda/offerta",
            "Esposizione all'economia globale",
            "Supporto di asset tangibili"
        ],
        "punti_debolezza": [
            "Volatilità elevata",
            "Nessuna generazione di reddito",
            "Costi di stoccaggio e trasporto",
            "Natura ciclica",
            "Rischi meteorologici e geopolitici"
        ],
        "scenari": {
            "Crescita economica": "Performance fortemente positiva",
            "Recessione": "Performance negativa per distruzione della domanda",
            "Inflazione elevata": "Performance fortemente positiva",
            "Politiche restrittive": "Impatto misto a seconda degli effetti economici",
            "Politiche espansive": "Positivo per aspettative di maggiore domanda"
        },
        "allocazione_range": "5-15% per protezione dall'inflazione",
        "correlazioni": "Correlazione positiva con inflazione, mista con azioni"
    },

    "REIT": {
        "descrizione": "Real Estate Investment Trust che forniscono esposizione ai mercati immobiliari attraverso titoli quotati in borsa.",
        "performance_storica": {
            "rendimenti_annuali": {
                "anno_1": "11.2%",   # 2024 - Tassi stabili
                "anno_2": "-2.5%",   # 2023 - Pressure da tassi
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
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Reddito regolare da dividendi",
            "Esposizione immobiliare senza proprietà diretta",
            "Gestione professionale",
            "Liquidità rispetto al mattone",
            "Potenziale copertura dall'inflazione"
        ],
        "punti_debolezza": [
            "Sensibilità ai tassi di interesse",
            "Dipendenza dai cicli immobiliari",
            "Diversificazione inferiore alle aspettative",
            "Commissioni di gestione",
            "Complessità fiscale"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva per occupazione e crescita affitti",
            "Recessione": "Performance negativa per debolezza economica",
            "Inflazione elevata": "Performance mista (costi input vs aumenti affitti)",
            "Politiche restrittive": "Pressione negativa per tassi di sconto più alti",
            "Politiche espansive": "Supporto positivo per tassi più bassi"
        },
        "allocazione_range": "5-15% per esposizione immobiliare",
        "correlazioni": "Correlazione moderata con azioni, sensibili ai tassi di interesse"
    }
}

# 2. ALTERNATIVE ASSETS INGLESE COMPLETO - data/english/alternative_assets_en.py
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
            "Restrictive policies": "Pressure from high real rates",
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

# 3. FUNZIONI SPECIALIZZATE PER ALTERNATIVE ASSETS

def create_alternative_assets_correlation_matrix(asset_data, ui_text):
    """Crea matrice di correlazione specifica per alternative assets"""
    
    alternative_assets = ["Oro", "Argento", "Materie Prime", "REIT"]
    
    # Calcola correlazioni basate sui rendimenti storici
    correlation_data = []
    
    for asset1 in alternative_assets:
        if asset1 in asset_data:
            yearly_data1 = asset_data[asset1]["performance_storica"]["rendimenti_annuali"]
            returns1 = [float(v.replace('%','')) for v in yearly_data1.values()]
            
            row = []
            for asset2 in alternative_assets:
                if asset2 in asset_data:
                    yearly_data2 = asset_data[asset2]["performance_storica"]["rendimenti_annuali"]
                    returns2 = [float(v.replace('%','')) for v in yearly_data2.values()]
                    
                    # Calcola correlazione
                    correlation = np.corrcoef(returns1, returns2)[0,1]
                    row.append(correlation)
                else:
                    row.append(0)
            
            correlation_data.append(row)
    
    # Crea heatmap
    fig = px.imshow(
        correlation_data,
        x=alternative_assets,
        y=alternative_assets,
        color_continuous_scale="RdBu",
        aspect="auto",
        title="🔗 Matrice di Correlazione - Alternative Assets",
        color_continuous_midpoint=0
    )
    
    # Aggiungi valori nella matrice
    for i, row in enumerate(correlation_data):
        for j, val in enumerate(row):
            fig.add_annotation(
                x=j, y=i,
                text=f"{val:.2f}",
                showarrow=False,
                font=dict(color="white" if abs(val) > 0.5 else "black")
            )
    
    fig.update_layout(height=500, title_x=0.5)
    
    return fig

def create_crisis_performance_chart(asset_data, ui_text):
    """Analizza performance durante crisi storiche"""
    
    # Anni di crisi identificati
    crisis_years = {
        "2008 Financial Crisis": "anno_17",
        "2020 COVID": "anno_5", 
        "2022 Rate Shock": "anno_3"
    }
    
    alternative_assets = ["Oro", "Argento", "Materie Prime", "REIT"]
    
    fig = go.Figure()
    
    for asset in alternative_assets:
        if asset in asset_data:
            yearly_data = asset_data[asset]["performance_storica"]["rendimenti_annuali"]
            
            crisis_performance = []
            crisis_labels = []
            
            for crisis_name, year_key in crisis_years.items():
                if year_key in yearly_data:
                    perf = float(yearly_data[year_key].replace('%', ''))
                    crisis_performance.append(perf)
                    crisis_labels.append(crisis_name)
            
            fig.add_trace(go.Bar(
                x=crisis_labels,
                y=crisis_performance,
                name=asset,
                text=[f"{p:.1f}%" for p in crisis_performance],
                textposition='auto'
            ))
    
    fig.update_layout(
        title="🔥 Performance Alternative Assets Durante le Crisi",
        yaxis_title="Performance (%)",
        height=500,
        title_x=0.5,
        barmode='group'
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    
    return fig

def analyze_gold_silver_ratio(asset_data, ui_text):
    """Analizza il rapporto oro/argento storico"""
    
    if "Oro" not in asset_data or "Argento" not in asset_data:
        return None
    
    gold_data = asset_data["Oro"]["performance_storica"]["rendimenti_annuali"]
    silver_data = asset_data["Argento"]["performance_storica"]["rendimenti_annuali"]
    
    years = []
    ratios = []
    
    # Simula prezzi cumulativi per calcolare ratio
    gold_price = 1000  # Base price
    silver_price = 20   # Base price
    
    for i in range(20, 0, -1):  # Dal più vecchio al più recente
        year_key = f"anno_{i}"
        
        if year_key in gold_data and year_key in silver_data:
            gold_return = float(gold_data[year_key].replace('%', '')) / 100
            silver_return = float(silver_data[year_key].replace('%', '')) / 100
            
            gold_price *= (1 + gold_return)
            silver_price *= (1 + silver_return)
            
            ratio = gold_price / silver_price
            ratios.append(ratio)
            years.append(f"Y{21-i}")  # Anno dal più recente
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=ratios,
        mode='lines+markers',
        name='Gold/Silver Ratio',
        line=dict(width=3, color='gold'),
        marker=dict(size=6),
        hovertemplate="<b>%{x}</b><br>Ratio: %{y:.1f}<extra></extra>"
    ))
    
    # Aggiungi linee di riferimento storiche
    avg_ratio = sum(ratios) / len(ratios)
    fig.add_hline(y=avg_ratio, line_dash="dash", line_color="orange", 
                  annotation_text=f"Media: {avg_ratio:.1f}")
    
    fig.update_layout(
        title="📊 Rapporto Oro/Argento Storico",
        xaxis_title="Anno",
        yaxis_title="Ratio Oro/Argento",
        height=400,
        title_x=0.5
    )
    
    return fig

def create_inflation_hedge_analysis(asset_data, ui_text):
    """Analizza efficacia come hedge inflazione"""
    
    # Anni ad alta inflazione identificati (approssimazione)
    high_inflation_years = {
        "anno_18": "2007",  # Pre-crisis
        "anno_17": "2008",  # Crisis year
        "anno_15": "2010",  # QE1 effects
        "anno_14": "2011",  # QE2 + Eurocrisis
        "anno_3": "2022",   # Post-COVID inflation
        "anno_1": "2024"    # Recent inflation
    }
    
    alternative_assets = ["Oro", "Argento", "Materie Prime", "REIT"]
    
    inflation_performance = {}
    
    for asset in alternative_assets:
        if asset in asset_data:
            yearly_data = asset_data[asset]["performance_storica"]["rendimenti_annuali"]
            
            performances = []
            for year_key in high_inflation_years.keys():
                if year_key in yearly_data:
                    perf = float(yearly_data[year_key].replace('%', ''))
                    performances.append(perf)
            
            if performances:
                avg_performance = sum(performances) / len(performances)
                inflation_performance[asset] = avg_performance
    
    # Crea grafico a barre
    assets = list(inflation_performance.keys())
    performances = list(inflation_performance.values())
    
    colors = ['gold' if p > 0 else 'red' for p in performances]
    
    fig = go.Figure(data=[
        go.Bar(
            x=assets,
            y=performances,
            text=[f"{p:.1f}%" for p in performances],
            textposition='auto',
            marker_color=colors
        )
    ])
    
    fig.update_layout(
        title="🔥 Efficacia come Hedge Inflazione (Media Anni Inflattivi)",
        yaxis_title="Performance Media (%)",
        height=400,
        title_x=0.5
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="black")
    
    return fig

def display_alternative_assets_summary_stats(asset_data, ui_text):
    """Mostra statistiche riassuntive per alternative assets"""
    
    alternative_assets = ["Oro", "Argento", "Materie Prime", "REIT"]
    
    summary_data = []
    
    for asset in alternative_assets:
        if asset in asset_data:
            yearly_data = asset_data[asset]["performance_storica"]["rendimenti_annuali"]
            returns = [float(v.replace('%','')) for v in yearly_data.values()]
            
            stats = {
                "Asset": asset,
                "Media 20Y": f"{sum(returns)/len(returns):.1f}%",
                "Volatilità": f"{np.std(returns):.1f}%",
                "Max Anno": f"{max(returns):.1f}%",
                "Min Anno": f"{min(returns):.1f}%",
                "Sharpe*": f"{(sum(returns)/len(returns)) / np.std(returns):.2f}"
            }
            summary_data.append(stats)
    
    if summary_data:
        df_summary = pd.DataFrame(summary_data)
        st.dataframe(df_summary, hide_index=True, use_container_width=True)
        
        st.caption("* Sharpe semplificato (rendimento/volatilità, senza risk-free rate)")

# 4. APPROFONDIMENTI STORICI E PATTERN

def get_alternative_assets_insights():
    """Fornisce insights storici sui pattern degli alternative assets"""
    
    insights = {
        "oro": {
            "supercicli": [
                "2001-2012: Bull market decennale (+650%)",
                "2013-2015: Bear market (-45%)", 
                "2016-2024: Nuovo bull market (+180%)"
            ],
            "drivers": [
                "Politiche monetarie espansive",
                "Crisi geopolitiche e finanziarie",
                "Inflazione e svalutazione valutaria",
                "Incertezza macroeconomica"
            ],
            "correlazioni_negative": [
                "Dollaro USA forte",
                "Tassi reali elevati",
                "Risk-on sentiment",
                "Crescita economica robusta"
            ]
        },
        "argento": {
            "caratteristiche": [
                "Volatilità 2-3x superiore all'oro",
                "Rapporto oro/argento: 15-80 (media ~65)",
                "Domanda industriale ~60%, investimento ~40%",
                "Outperform oro in bull market, underperform in bear"
            ],
            "anni_chiave": [
                "2011: +83.7% (picco superciclo commodities)",
                "2013: -35.9% (fine QE, dollaro forte)",
                "2020: +47.9% (stimulus + ripresa industriale)"
            ]
        },
        "commodities": {
            "supercicli": [
                "2002-2008: China supercycle (+140%)",
                "2009-2011: Recovery + stimulus (+45%)",
                "2012-2020: Bear market (-50%)",
                "2021-2024: Nuovo ciclo inflattivo"
            ],
            "settori": [
                "Energia: 35-40% dell'indice",
                "Metalli industriali: 20-25%",
                "Agricoltura: 15-20%",
                "Metalli preziosi: 10-15%"
            ]
        },
        "reit": {
            "sensibilita_tassi": [
                "Duration media: 5-7 anni",
                "Beta vs tassi 10Y: -4 to -6",
                "Correlazione con bond: +0.30-0.50"
            ],
            "cicli_storici": [
                "2000-2007: Bubble immobiliare (+180%)",
                "2008-2009: Crash (-70%)",
                "2010-2021: Recovery + QE (+350%)",
                "2022: Rate shock (-25%)"
            ]
        }
    }
    
    return insights

# 5. MESSAGGI EDUCATIVI SPECIFICI

ALTERNATIVE_ASSETS_EDUCATION = {
    "oro_education": """
    🥇 **Oro - Il Re dei Metalli Preziosi**
    
    **📊 Pattern Storici:**
    - Bull market: 2001-2012 (+650% in 11 anni)
    - Bear market: 2013-2015 (-45% in 3 anni)  
    - Nuovo bull: 2016-2024 (+180% in 8 anni)
    
    **🎯 Quando Performa Meglio:**
    - Crisi finanziarie (2008: +5.8%, 2020: +24.4%)
    - Politiche monetarie espansive (QE periods)
    - Alta incertezza geopolitica
    - Inflazione elevata (ma non sempre!)
    
    **⚠️ Quando Soffre:**
    - Dollaro USA molto forte (2015: -10.4%)
    - Tassi reali elevati (Fed hawkish)
    - Risk-on sentiment estremo
    - Aspettative deflazionistiche
    """,
    
    "argento_education": """
    🥈 **Argento - Il Metallo della Volatilità**
    
    **📊 Caratteristica Chiave:**
    Volatilità 2-3x superiore all'oro = Opportunità e Rischi amplificati
    
    **🔄 Rapporto Oro/Argento:**
    - Range storico: 15-80
    - Media long-term: ~65
    - Sotto 50: Argento costoso vs oro
    - Sopra 80: Argento a sconto vs oro
    
    **⚡ Anni Estremi:**
    - 2011: +83.7% (picco commodities supercycle)
    - 2013: -35.9% (taper tantrum disaster)
    - 2020: +47.9% (perfect storm: stimulus + industrial)
    
    **🏭 Doppia Natura:**
    - 60% domanda industriale (tech, automotive, solar)
    - 40% domanda investimento (segue oro)
    """,
    
    "commodities_education": """
    🌾 **Materie Prime - Il Barometro dell'Economia Globale**
    
    **📊 Supercicli Storici:**
    - 2002-2008: China supercycle (+140%)
    - 2009-2011: Stimulus recovery (+45%)
    - 2012-2020: Bear market secolare (-50%)
    - 2021-2024: Inflazione + reshoring
    
    **🔥 Eventi Estremi:**
    - 2008: -35.7% (demand destruction)
    - 2009: +18.9% (stimulus effects)
    - 2021: +27.1% (reflation trade)
    - 2022: +16.1% (Ukraine war)
    
    **🏭 Composizione Bloomberg Index:**
    - Energia: 35-40% (petrolio, gas)
    - Metalli industriali: 20-25% (rame, alluminio)
    - Agricoltura: 15-20% (grano, soia)
    - Livestock: 5-10% (bovini, suini)
    """,
    
    "reit_education": """
    🏢 **REIT - Real Estate Senza Mattone**
    
    **📊 Sensibilità ai Tassi:**
    Duration media: 5-7 anni (come bond medio-lunghi)
    
    **⚡ Rate Sensitivity Events:**
    - 2013: Taper tantrum (+2.9% solo)
    - 2018: Fed aggressive (-4.6%)
    - 2022: Shock tassi (-25.1% disaster!)
    - 2021: Tassi zero (+43.2% boom)
    
    **🏠 Cicli Immobiliari:**
    - 2000-2007: Bubble (+180% in 7 anni)
    - 2008-2009: Crash (-70% devastante)
    - 2010-2021: QE recovery (+350%)
    - 2022-2024: Rate normalization volatility
    
    **💰 Caratteristiche Uniche:**
    - Dividend yield: 3-6% tipico
    - Correlazione con bond: +0.30-0.50
    - Correlazione con azioni: +0.60-0.70
    - Asset class ibrida per natura
    """
}

print("✅ ALTERNATIVE ASSETS COMPLETI - Implementazione Finale!")
print("\n🎯 Assets Implementati:")
print("- 🥇 Oro: Store of value, hedge inflation")
print("- 🥈 Argento: Industrial + precious, alta volatilità")  
print("- 🌾 Materie Prime: Economic barometer, supercicli")
print("- 🏢 REIT: Real estate exposure, rate sensitive")

print("\n📊 Funzionalità Specializzate:")
print("- ✅ Matrice correlazioni alternative assets")
print("- ✅ Performance durante crisi storiche")
print("- ✅ Analisi rapporto oro/argento")
print("- ✅ Efficacia hedge inflazione")
print("- ✅ Statistiche riassuntive avanzate")

print("\n🔍 Insights Chiave dai Dati:")
print("- 💥 Oro: Bull 2001-2012 (+650%), Bear 2013-2015 (-45%)")
print("- ⚡ Argento: Volatilità 2-3x oro, ratio 15-80 range")
print("- 🌊 Commodities: Supercicli decennali, China-driven")
print("- 🏠 REIT: Rate sensitivity estrema, cicli immobiliari")

print("\n🎓 Valore Educativo:")
print("- 📚 Pattern storici chiari e documentati")
print("- 📈 Correlazioni e diversificazione benefits")
print("- ⚠️ Risk management attraverso volatilità")
print("- 🎯 Timing e asset allocation insights")
