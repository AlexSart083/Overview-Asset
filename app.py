import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Import data files
try:
    from asset_data_en import ASSET_DATA_EN, UI_TEXT_EN
    from asset_data_it import ASSET_DATA_IT, UI_TEXT_IT
except ImportError:
    # Fallback - include basic data directly in app
    ASSET_DATA_EN = {
        "Global Equities (Market Cap)": {
            "descrizione": "Globally diversified equity investments weighted by market capitalization, representing ownership stakes in the world's largest publicly traded companies.",
            "performance_storica": {
                "20_anni": "7.0%",
                "10_anni": "10.6%",
                "5_anni": "14.4%",
                "1_anno": "14.9%",
                "indice_riferimento": "MSCI World Index"
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
        
        "Emerging Markets": {
            "descrizione": "Equities from companies located in developing countries with rapidly growing economies.",
            "performance_storica": {
                "20_anni": "4.3%",
                "10_anni": "6.1%",
                "5_anni": "5.6%",
                "1_anno": "15.9%",
                "indice_riferimento": "MSCI Emerging Markets Index"
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
                "indice_riferimento": "Gold Spot Price (USD)"
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

        "Bonds 7-10 Years": {
            "descrizione": "Government and corporate debt securities with medium-long term maturity with significant duration and greater sensitivity to monetary policy expectations.",
            "performance_storica": {
                "20_anni": "4.8%",
                "10_anni": "3.2%",
                "5_anni": "0.8%",
                "1_anno": "1.4%",
                "indice_riferimento": "10-Year Treasury Note"
            },
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

        "REITs": {
            "descrizione": "Real Estate Investment Trusts providing exposure to real estate markets through publicly traded securities.",
            "performance_storica": {
                "20_anni": "7.2%",
                "10_anni": "8.4%",
                "5_anni": "5.8%",
                "1_anno": "11.2%",
                "indice_riferimento": "FTSE Nareit All REITs Index"
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

    ASSET_DATA_IT = {
        "Azioni Globali (Market Cap)": {
            "descrizione": "Investimenti azionari diversificati a livello mondiale ponderati per capitalizzazione di mercato, che rappresentano quote di proprietà nelle maggiori aziende quotate globalmente.",
            "performance_storica": {
                "20_anni": "7.0%",
                "10_anni": "10.6%",
                "5_anni": "14.4%",
                "1_anno": "14.9%",
                "indice_riferimento": "MSCI World Index"
            },
            "punti_forza": [
                "Potenziale di crescita a lungo termine",
                "Protezione storica contro l'inflazione",
                "Liquidità elevata",
                "Diversificazione geografica e settoriale automatica",
                "Potenziali dividendi",
                "Esposizione alle aziende più grandi e stabili"
            ],
            "punti_debolezza": [
                "Volatilità elevata nel breve periodo",
                "Rischio di perdite significative",
                "Dipendenza dai cicli economici",
                "Rischio valutario per investitori locali",
                "Concentrazione verso mega-cap"
            ],
            "scenari": {
                "Crescita economica": "Performance positiva (+8-12% annuo)",
                "Recessione": "Performance negativa (-15-30%)",
                "Inflazione elevata": "Performance mista (dipende dalla capacità di pricing power)",
                "Politiche restrittive": "Pressione negativa per tassi più alti",
                "Politiche espansive": "Supporto positivo per liquidità abbondante"
            },
            "allocazione_range": "40-70% per investitori con orizzonte lungo termine",
            "correlazioni": "Correlazione negativa con obbligazioni lunghe, positiva con materie prime"
        },
        
        "Mercati Emergenti": {
            "descrizione": "Azioni di aziende localizzate in paesi in via di sviluppo con economie in rapida crescita.",
            "performance_storica": {
                "20_anni": "4.3%",
                "10_anni": "6.1%",
                "5_anni": "5.6%",
                "1_anno": "15.9%",
                "indice_riferimento": "MSCI Emerging Markets Index"
            },
            "punti_forza": [
                "Potenziale di crescita superiore ai mercati sviluppati",
                "Valutazioni spesso più attraenti",
                "Benefici demografici (popolazione giovane)",
                "Diversificazione geografica",
                "Esposizione a trend di crescita globali"
            ],
            "punti_debolezza": [
                "Volatilità molto elevata",
                "Rischi politici e regolamentari",
                "Liquidità inferiore",
                "Rischio valutario significativo",
                "Correlazione elevata nei momenti di stress"
            ],
            "scenari": {
                "Crescita economica": "Outperformance vs mercati sviluppati (+10-15%)",
                "Recessione": "Underperformance significativa (-25-40%)",
                "Inflazione elevata": "Performance mista, alcuni paesi beneficiano",
                "Politiche restrittive": "Pressione per deflussi di capitali",
                "Politiche espansive": "Forte attrattiva per yield hunting"
            },
            "allocazione_range": "5-15% come componente satellite del portafoglio",
            "correlazioni": "Alta correlazione con azioni globali, sensibili al dollaro USA"
        },

        "Oro": {
            "descrizione": "Metallo prezioso considerato riserva di valore e copertura contro la svalutazione valutaria e l'instabilità geopolitica.",
            "performance_storica": {
                "20_anni": "8.4%",
                "10_anni": "4.2%",
                "5_anni": "7.8%",
                "1_anno": "27.0%",
                "indice_riferimento": "Prezzo Spot Oro (USD)"
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

        "Obbligazioni 7-10 anni": {
            "descrizione": "Titoli di debito governativi e corporate a medio-lungo termine con duration significativa e maggiore sensibilità alle aspettative di politica monetaria.",
            "performance_storica": {
                "20_anni": "4.8%",
                "10_anni": "3.2%",
                "5_anni": "0.8%",
                "1_anno": "1.4%",
                "indice_riferimento": "BTP 10 anni"
            },
            "punti_forza": [
                "Rendimenti potenzialmente attraenti",
                "Forti capital gain potenziali se tassi scendono",
                "Diversificazione significativa vs azioni",
                "Copertura deflazionistica",
                "Benchmark per molti fondi pensione"
            ],
            "punti_debolezza": [
                "Alta sensibilità ai tassi di interesse",
                "Volatilità significativa",
                "Rischio di duration elevato",
                "Performance molto negativa con inflazione/rialzo tassi"
            ],
            "scenari": {
                "Crescita economica": "Performance significativamente negativa",
                "Recessione": "Performance molto positiva (+10-20%)",
                "Inflazione elevata": "Performance molto negativa (-10-20%)",
                "Politiche restrittive": "Performance molto negativa",
                "Politiche espansive": "Performance fortemente positiva"
            },
            "allocazione_range": "5-20% per diversificazione duration",
            "correlazioni": "Correlazione negativa forte con azioni, correlazione negativa con tassi"
        },

        "REIT": {
            "descrizione": "Real Estate Investment Trust che forniscono esposizione ai mercati immobiliari attraverso titoli quotati in borsa.",
            "performance_storica": {
                "20_anni": "7.2%",
                "10_anni": "8.4%",
                "5_anni": "5.8%",
                "1_anno": "11.2%",
                "indice_riferimento": "FTSE Nareit All REITs Index"
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

    # UI text
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

    UI_TEXT_IT = {
        "title": "Analizzatore Asset Finanziari",
        "subtitle": "Analisi educativa di diversi asset finanziari",
        "sidebar_title": "Selezione Asset",
        "language_label": "Lingua",
        "asset_label": "Seleziona Asset",
        "analysis_title": "Analisi Asset: ",
        "description_header": "📖 Descrizione",
        "performance_header": "📊 Performance Storica (Annualizzata)",
        "strengths_header": "✅ Punti di Forza",
        "weaknesses_header": "⚠️ Punti di Debolezza",
        "scenarios_header": "📊 Performance negli Scenari di Mercato",
        "allocation_header": "💼 Range di Allocazione Indicativo",
        "correlations_header": "🔗 Correlazioni con Altri Asset",
        "summary_header": "📝 Riassunto Educativo",
        "warning": "⚠️ **Importante Disclaimer**: Queste informazioni sono a scopo puramente educativo e non costituiscono consigli finanziari personalizzati.",
        "visualization_title": "📈 Visualizzazione Performance",
        "heatmap_title": "Heatmap Performance Asset per Scenario di Mercato",
        "allocation_pie_title": "Allocazione Portfolio di Esempio",
        "performance_note": "📌 **Nota**: I dati di performance storica sono basati su indici di mercato rilevanti e non garantiscono risultati futuri. Le performance passate non predicono i rendimenti futuri."
    }

# Configure page
st.set_page_config(
    page_title="Financial Asset Analyzer | Analizzatore Asset Finanziari",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_language_data(language):
    """Get data and UI text based on selected language"""
    if language == "English":
        return ASSET_DATA_EN, UI_TEXT_EN
    else:
        return ASSET_DATA_IT, UI_TEXT_IT

def categorize_assets(asset_data, language):
    """Categorize assets by type for better organization"""
    if language == "English":
        categories = {
            "📈 Equity Strategies": [
                "Global Equities (Market Cap)", "Momentum Equities", "Quality Equities", 
                "Value Equities", "Minimum Volatility Equities", "Small Cap Equities", 
                "Emerging Markets", "High Dividend Equities"
            ],
            "💰 Government & Corporate Bonds": [
                "Bonds 0-1 Years", "Bonds 1-3 Years", "Bonds 3-7 Years", 
                "Bonds 7-10 Years", "Bonds >10 Years"
            ],
            "🔸 Specialized Bonds": [
                "High Yield Bonds", "Inflation Linked Bonds", "Convertible Bonds", 
                "Subordinated Bonds"
            ],
            "🥇 Precious Metals": ["Gold", "Silver"],
            "🏢 Alternative Assets": ["Commodities", "REITs"]
        }
    else:
        categories = {
            "📈 Strategie Azionarie": [
                "Azioni Globali (Market Cap)", "Azioni Momentum", "Azioni Quality", 
                "Azioni Value", "Azioni Minimum Volatility", "Azioni Small Cap", 
                "Mercati Emergenti", "Azionario High Dividend"
            ],
            "💰 Obbligazioni Gov. & Corporate": [
                "Obbligazioni 0-1 anni", "Obbligazioni 1-3 anni", "Obbligazioni 3-7 anni", 
                "Obbligazioni 7-10 anni", "Obbligazioni >10 anni"
            ],
            "🔸 Obbligazioni Specializzate": [
                "Bond High Yield", "Bond Inflation Linked", "Bond Convertibili", 
                "Obbligazioni Subordinate"
            ],
            "🥇 Metalli Preziosi": ["Oro", "Argento"],
            "🏢 Asset Alternativi": ["Materie Prime", "REIT"]
        }
    
    return categories

def create_asset_selector(asset_data, categories, ui_text):
    """Create an improved asset selector with multiple options"""
    
    # Selection method choice
    selection_method = st.sidebar.radio(
        "🔧 " + ("Selection Method" if "English" in str(ui_text) else "Metodo di Selezione"),
        ["📂 By Category", "🔍 Search", "📋 Full List"],
        index=0
    )
    
    selected_asset = None
    
    if selection_method == "📂 By Category":
        # Category-based selection
        st.sidebar.markdown("### " + ("Select Category" if "English" in str(ui_text) else "Seleziona Categoria"))
        
        selected_category = st.sidebar.selectbox(
            ("Choose asset category:" if "English" in str(ui_text) else "Scegli categoria di asset:"),
            list(categories.keys()),
            index=0
        )
        
        if selected_category:
            st.sidebar.markdown("### " + ("Select Asset" if "English" in str(ui_text) else "Seleziona Asset"))
            assets_in_category = categories[selected_category]
            selected_asset = st.sidebar.radio(
                ("Asset in " if "English" in str(ui_text) else "Asset in ") + selected_category + ":",
                assets_in_category,
                index=0
            )
    
    elif selection_method == "🔍 Search":
        # Search-based selection
        st.sidebar.markdown("### " + ("Search Assets" if "English" in str(ui_text) else "Cerca Asset"))
        
        search_term = st.sidebar.text_input(
            ("Type to search assets:" if "English" in str(ui_text) else "Digita per cercare asset:"),
            placeholder=("e.g., Gold, Bond, Equity..." if "English" in str(ui_text) else "es., Oro, Bond, Azioni...")
        )
        
        if search_term:
            # Filter assets based on search term
            matching_assets = [asset for asset in asset_data.keys() 
                             if search_term.lower() in asset.lower()]
            
            if matching_assets:
                selected_asset = st.sidebar.selectbox(
                    f"📍 " + ("Found" if "English" in str(ui_text) else "Trovati") + f" {len(matching_assets)} " + ("assets:" if "English" in str(ui_text) else "asset:"),
                    matching_assets,
                    index=0
                )
            else:
                st.sidebar.warning("❌ " + ("No assets found. Try different keywords." if "English" in str(ui_text) else "Nessun asset trovato. Prova parole chiave diverse."))
        else:
            st.sidebar.info("💡 " + ("Start typing to search..." if "English" in str(ui_text) else "Inizia a digitare per cercare..."))
    
    else:  # Full List
        # Traditional dropdown for those who prefer it
        st.sidebar.markdown("### " + ("Full Asset List" if "English" in str(ui_text) else "Lista Completa Asset"))
        selected_asset = st.sidebar.selectbox(
            ("All assets (A-Z):" if "English" in str(ui_text) else "Tutti gli asset (A-Z):"),
            sorted(list(asset_data.keys())),
            index=0
        )
    
    return selected_asset

def create_performance_chart(performance_data, asset_name, ui_text):
    """Create performance visualization chart"""
    
    periods = ["20_anni", "10_anni", "5_anni", "1_anno"]
    period_labels = {
        "20_anni": "20Y" if "English" in str(ui_text) else "20A",
        "10_anni": "10Y" if "English" in str(ui_text) else "10A", 
        "5_anni": "5Y" if "English" in str(ui_text) else "5A",
        "1_anno": "1Y" if "English" in str(ui_text) else "1A"
    }
    
    # Extract performance values and convert to float
    performance_values = []
    labels = []
    
    for period in periods:
        if period in performance_data:
            # Remove % sign and convert to float
            value = float(performance_data[period].replace('%', ''))
            performance_values.append(value)
            labels.append(period_labels[period])
    
    # Create bar chart
    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=performance_values,
            text=[f"{val}%" for val in performance_values],
            textposition='auto',
            marker_color=['lightcoral' if val < 0 else 'lightgreen' for val in performance_values],
            hovertemplate="<b>%{x}</b><br>Return: %{y}%<extra></extra>"
        )
    ])
    
    fig.update_layout(
        title=f"Historical Annualized Returns - {asset_name}" if "English" in str(ui_text) else f"Rendimenti Annualizzati Storici - {asset_name}",
        xaxis_title="Time Period" if "English" in str(ui_text) else "Periodo Temporale",
        yaxis_title="Annualized Return (%)" if "English" in str(ui_text) else "Rendimento Annualizzato (%)",
        height=400,
        title_x=0.5,
        showlegend=False
    )
    
    # Add reference line at 0%
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 0, 0, 0.5)")
    
    return fig

def create_scenario_heatmap(asset_data, ui_text):
    """Create heatmap showing asset performance across different scenarios"""
    
    # Performance mapping (simplified for visualization)
    performance_mapping = {
        "Strong positive": 3, "Positive": 2, "Mixed": 1, 
        "Moderate negative": -1, "Negative": -2, "Significant negative": -3,
        "Fortemente positiva": 3, "Positiva": 2, "Mista": 1,
        "Moderatamente negativa": -1, "Negativa": -2, "Significativamente negativa": -3,
        "Performance positiva": 2, "Performance negativa": -2, "Performance mista": 1,
        "Performance fortemente positiva": 3, "Performance moderatamente negativa": -1,
        "Outperformance": 2, "Underperformance": -2, "Strong": 3
    }
    
    assets = list(asset_data.keys())
    scenarios = list(list(asset_data.values())[0]["scenari"].keys())
    
    # Create performance matrix
    performance_matrix = []
    for asset in assets:
        row = []
        for scenario in scenarios:
            scenario_text = asset_data[asset]["scenari"][scenario]
            # Simple mapping based on key words
            score = 0
            for key, value in performance_mapping.items():
                if key.lower() in scenario_text.lower():
                    score = value
                    break
            # Fallback mapping based on +/- signs
            if score == 0:
                if "+" in scenario_text:
                    score = 2
                elif "-" in scenario_text:
                    score = -2
                else:
                    score = 1
            row.append(score)
        performance_matrix.append(row)
    
    # Create heatmap
    fig = px.imshow(
        performance_matrix,
        x=scenarios,
        y=assets,
        color_continuous_scale="RdYlGn",
        aspect="auto",
        title=ui_text["heatmap_title"]
    )
    
    fig.update_layout(
        title_x=0.5,
        height=600,
        xaxis_title="Market Scenarios" if "English" in str(ui_text) else "Scenari di Mercato",
        yaxis_title="Assets",
        font=dict(size=10)
    )
    
    return fig

def create_allocation_pie():
    """Create sample portfolio allocation pie chart"""
    
    # Sample allocation data
    allocation_data = {
        'Asset': ['Global Equities', 'Government Bonds', 'High Yield Bonds', 'REITs', 'Gold', 'Commodities'],
        'Allocation': [45, 30, 10, 8, 4, 3]
    }
    
    df = pd.DataFrame(allocation_data)
    
    fig = px.pie(
        df, 
        values='Allocation', 
        names='Asset',
        title="Sample Conservative Portfolio Allocation (%)"
    )
    
    fig.update_layout(title_x=0.5, height=400)
    
    return fig

def create_performance_comparison_chart(asset_data, selected_assets, ui_text):
    """Create comparison chart for multiple assets"""
    
    if len(selected_assets) <= 1:
        return None
    
    periods = ["1_anno", "5_anni", "10_anni", "20_anni"]
    period_labels = {
        "1_anno": "1Y" if "English" in str(ui_text) else "1A",
        "5_anni": "5Y" if "English" in str(ui_text) else "5A", 
        "10_anni": "10Y" if "English" in str(ui_text) else "10A",
        "20_anni": "20Y" if "English" in str(ui_text) else "20A"
    }
    
    fig = go.Figure()
    
    for asset_name in selected_assets:
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            performance_values = []
            labels = []
            
            for period in periods:
                if period in performance_data:
                    # Remove % sign and convert to float
                    value = float(performance_data[period].replace('%', ''))
                    performance_values.append(value)
                    labels.append(period_labels[period])
            
            fig.add_trace(go.Scatter(
                x=labels,
                y=performance_values,
                mode='lines+markers',
                name=asset_name,
                line=dict(width=3),
                marker=dict(size=8)
            ))
    
    fig.update_layout(
        title="Performance Comparison" if "English" in str(ui_text) else "Confronto Performance",
        xaxis_title="Time Period" if "English" in str(ui_text) else "Periodo Temporale",
        yaxis_title="Annualized Return (%)" if "English" in str(ui_text) else "Rendimento Annualizzato (%)",
        height=500,
        title_x=0.5,
        hovermode='x unified'
    )
    
    # Add reference line at 0%
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 0, 0, 0.5)")
    
    return fig

def main():
    # Language selection in sidebar
    st.sidebar.title("🌍 Language | Lingua")
    language = st.sidebar.selectbox(
        "Select Language | Seleziona Lingua",
        ["English", "Italiano"],
        index=0
    )
    
    # Get data based on language
    asset_data, ui_text = get_language_data(language)
    categories = categorize_assets(asset_data, language)
    
    # App title and description
    st.title(ui_text["title"])
    st.markdown(f"*{ui_text['subtitle']}*")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Assets", len(asset_data))
    with col2:
        st.metric("📈 Equity Strategies", len(categories[list(categories.keys())[0]]))
    with col3:
        st.metric("💰 Bond Types", len(categories[list(categories.keys())[1]]) + len(categories[list(categories.keys())[2]]))
    with col4:
        st.metric("🏢 Alternative Assets", len(categories[list(categories.keys())[3]]) + len(categories[list(categories.keys())[4]]))
    
    st.markdown("---")
    
    # Sidebar for asset selection
    st.sidebar.title(ui_text["sidebar_title"])
    selected_asset = create_asset_selector(asset_data, categories, ui_text)
    
    # Add comparison mode option
    st.sidebar.markdown("---")
    comparison_mode = st.sidebar.checkbox(
        "📊 " + ("Comparison Mode" if "English" in str(ui_text) else "Modalità Confronto"),
        help=("Select multiple assets to compare" if "English" in str(ui_text) else "Seleziona più asset da confrontare")
    )
    
    if comparison_mode:
        st.sidebar.markdown("### " + ("Select Assets to Compare" if "English" in str(ui_text) else "Seleziona Asset da Confrontare"))
        selected_assets = st.sidebar.multiselect(
            ("Choose assets:" if "English" in str(ui_text) else "Scegli asset:"),
            list(asset_data.keys()),
            default=[selected_asset] if selected_asset else [],
            max_selections=5
        )
    else:
        selected_assets = [selected_asset] if selected_asset else []
    
    # Main content
    if selected_asset:
        asset_info = asset_data[selected_asset]
        
        # Title with emoji based on asset type
        asset_emoji = "📈" if any("Equit" in selected_asset or "Azion" in selected_asset or "Mercati" in selected_asset for _ in [None]) else \
                     "💰" if any(word in selected_asset for word in ["Bond", "Obblig"]) else \
                     "🥇" if selected_asset in ["Gold", "Silver", "Oro", "Argento"] else \
                     "🏢"
        
        st.header(f"{asset_emoji} {ui_text['analysis_title']}{selected_asset}")
        
        # Warning disclaimer
        st.warning(ui_text["warning"])
        
        # Description with improved formatting
        st.subheader(ui_text["description_header"])
        st.markdown(f"**{asset_info['descrizione']}**")
        
        # Historical Performance Section (NEW!)
        if "performance_storica" in asset_info:
            st.subheader(ui_text["performance_header"])
            
            # Display performance table and chart side by side
            col_perf1, col_perf2 = st.columns([1, 2])
            
            with col_perf1:
                # Performance table
                perf_data = asset_info["performance_storica"]
                
                # Create nice display table
                perf_display = {
                    ("Period" if "English" in str(ui_text) else "Periodo"): [
                        "20 " + ("Years" if "English" in str(ui_text) else "Anni"),
                        "10 " + ("Years" if "English" in str(ui_text) else "Anni"),
                        "5 " + ("Years" if "English" in str(ui_text) else "Anni"),
                        "1 " + ("Year" if "English" in str(ui_text) else "Anno")
                    ],
                    ("Return" if "English" in str(ui_text) else "Rendimento"): [
                        perf_data.get("20_anni", "N/A"),
                        perf_data.get("10_anni", "N/A"),
                        perf_data.get("5_anni", "N/A"),
                        perf_data.get("1_anno", "N/A")
                    ]
                }
                
                df_perf = pd.DataFrame(perf_display)
                st.dataframe(df_perf, hide_index=True, use_container_width=True)
                
                # Reference index
                st.caption(f"📚 **{('Reference Index' if 'English' in str(ui_text) else 'Indice di Riferimento')}:** {perf_data.get('indice_riferimento', 'N/A')}")
            
            with col_perf2:
                # Performance chart
                if "performance_storica" in asset_info:
                    perf_chart = create_performance_chart(asset_info["performance_storica"], selected_asset, ui_text)
                    st.plotly_chart(perf_chart, use_container_width=True)
            
            # Performance note
            st.info(ui_text["performance_note"])
        
        st.markdown("---")
        
        # Two column layout for strengths and weaknesses
        col1, col2 = st.columns(2)
        
        with col1:
            # Strengths
            st.subheader(ui_text["strengths_header"])
            for i, strength in enumerate(asset_info["punti_forza"], 1):
                st.markdown(f"**{i}.** {strength}")
        
        with col2:
            # Weaknesses
            st.subheader(ui_text["weaknesses_header"])
            for i, weakness in enumerate(asset_info["punti_debolezza"], 1):
                st.markdown(f"**{i}.** {weakness}")
        
        st.markdown("---")
        
        # Market scenarios with improved table
        st.subheader(ui_text["scenarios_header"])
        
        # Create enhanced dataframe for scenarios
        scenarios_data = []
        for scenario, performance in asset_info["scenari"].items():
            # Add simple color coding based on performance
            if any(word in performance.lower() for word in ["positive", "positiv", "outperform"]):
                trend = "🟢 Positive"
            elif any(word in performance.lower() for word in ["negative", "negativ", "underperform"]):
                trend = "🔴 Negative"
            else:
                trend = "🟡 Mixed"
            
            scenarios_data.append({
                "🌍 Scenario": scenario,
                "📊 Trend": trend,
                "📝 Expected Performance": performance
            })
        
        scenarios_df = pd.DataFrame(scenarios_data)
        st.dataframe(scenarios_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Allocation and correlations with better styling
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader(ui_text["allocation_header"])
            st.info(f"💼 **{asset_info['allocazione_range']}**")
        
        with col4:
            st.subheader(ui_text["correlations_header"])
            st.info(f"🔗 **{asset_info['correlazioni']}**")
        
        st.markdown("---")
        
        # Enhanced visualizations
        st.subheader(ui_text["visualization_title"])
        
        # Create tabs for different visualizations
        if comparison_mode and len(selected_assets) > 1:
            tab1, tab2, tab3 = st.tabs([
                "📊 " + ("Performance Comparison" if "English" in str(ui_text) else "Confronto Performance"),
                "🗺️ " + ("All Assets Heatmap" if "English" in str(ui_text) else "Heatmap Tutti gli Asset"),
                "🥧 " + ("Sample Portfolio" if "English" in str(ui_text) else "Portfolio di Esempio")
            ])
            
            with tab1:
                # Performance comparison
                comparison_chart = create_performance_comparison_chart(asset_data, selected_assets, ui_text)
                if comparison_chart:
                    st.plotly_chart(comparison_chart, use_container_width=True)
                    
                    # Comparison table
                    st.markdown("#### " + ("Performance Comparison Table" if "English" in str(ui_text) else "Tabella Confronto Performance"))
                    
                    comparison_data = []
                    for asset_name in selected_assets:
                        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
                            perf_data = asset_data[asset_name]["performance_storica"]
                            comparison_data.append({
                                "Asset": asset_name,
                                "1Y": perf_data.get("1_anno", "N/A"),
                                "5Y": perf_data.get("5_anni", "N/A"),
                                "10Y": perf_data.get("10_anni", "N/A"),
                                "20Y": perf_data.get("20_anni", "N/A"),
                                ("Reference" if "English" in str(ui_text) else "Riferimento"): perf_data.get("indice_riferimento", "N/A")
                            })
                    
                    if comparison_data:
                        comparison_df = pd.DataFrame(comparison_data)
                        st.dataframe(comparison_df, hide_index=True, use_container_width=True)
                else:
                    st.info("📊 " + ("Select at least 2 assets to compare" if "English" in str(ui_text) else "Seleziona almeno 2 asset per confrontare"))
            
            with tab2:
                # Heatmap
                heatmap_fig = create_scenario_heatmap(asset_data, ui_text)
                st.plotly_chart(heatmap_fig, use_container_width=True)
                st.caption("💡 " + ("Green = Positive performance, Red = Negative performance" if "English" in str(ui_text) else "Verde = Performance positiva, Rosso = Performance negativa"))
            
            with tab3:
                # Sample allocation
                pie_fig = create_allocation_pie()
                st.plotly_chart(pie_fig, use_container_width=True)
                st.caption("💡 " + ("This is just an educational example - not investment advice" if "English" in str(ui_text) else "Questo è solo un esempio educativo - non un consiglio di investimento"))
                
        else:
            tab1, tab2 = st.tabs([
                "🗺️ " + ("All Assets Heatmap" if "English" in str(ui_text) else "Heatmap Tutti gli Asset"),
                "🥧 " + ("Sample Portfolio" if "English" in str(ui_text) else "Portfolio di Esempio")
            ])
            
            with tab1:
                # Heatmap
                heatmap_fig = create_scenario_heatmap(asset_data, ui_text)
                st.plotly_chart(heatmap_fig, use_container_width=True)
                st.caption("💡 " + ("Green = Positive performance, Red = Negative performance" if "English" in str(ui_text) else "Verde = Performance positiva, Rosso = Performance negativa"))
            
            with tab2:
                # Sample allocation
                pie_fig = create_allocation_pie()
                st.plotly_chart(pie_fig, use_container_width=True)
                st.caption("💡 " + ("This is just an educational example - not investment advice" if "English" in str(ui_text) else "Questo è solo un esempio educativo - non un consiglio di investimento"))
        
        st.markdown("---")
        
        # Educational summary with enhanced formatting
        st.subheader(ui_text["summary_header"])
        
        summary_text = f"""
        ### 🎯 Key Takeaways for {selected_asset}
        
        **{selected_asset}** rappresenta un asset con caratteristiche specifiche che lo rendono adatto 
        a determinati obiettivi di investimento. La sua performance varia significativamente in base 
        agli scenari macroeconomici, rendendo importante comprenderne il comportamento nel contesto 
        di un portafoglio diversificato.
        
        #### 📚 Punti chiave da ricordare:
        - **🎯 Diversificazione è fondamentale** - Mai concentrare tutto su un singolo asset
        - **⏰ L'orizzonte temporale influenza la scelta** - Asset diversi per obiettivi diversi  
        - **🔄 Le correlazioni cambiano nei momenti di stress** - I rapporti storici possono variare
        - **⚖️ Rischio e rendimento vanno sempre valutati insieme** - Non esistere rendimenti senza rischi
        - **📊 Le performance passate non garantiscono risultati futuri** - Usa i dati storici come guida, non come certezza
        
        #### 🚨 Importante:
        Questa analisi è puramente educativa. Per decisioni di investimento personalizzate, consulta sempre 
        un consulente finanziario qualificato che possa valutare la tua situazione specifica.
        """ if language == "Italiano" else f"""
        ### 🎯 Key Takeaways for {selected_asset}
        
        **{selected_asset}** represents an asset with specific characteristics that make it suitable 
        for certain investment objectives. Its performance varies significantly based on macroeconomic 
        scenarios, making it important to understand its behavior in the context of a diversified portfolio.
        
        #### 📚 Key points to remember:
        - **🎯 Diversification is fundamental** - Never concentrate everything in a single asset
        - **⏰ Time horizon influences selection** - Different assets for different objectives
        - **🔄 Correlations change during stress** - Historical relationships can vary
        - **⚖️ Risk and return must always be evaluated together** - No returns without risks
        - **📊 Past performance doesn't guarantee future results** - Use historical data as guidance, not certainty
        
        #### 🚨 Important:
        This analysis is purely educational. For personalized investment decisions, always consult 
        a qualified financial advisor who can assess your specific situation.
        """
        
        st.markdown(summary_text)
        
        # Additional resources section
        with st.expander("📖 " + ("Additional Resources" if "English" in str(ui_text) else "Risorse Aggiuntive")):
            if language == "Italiano":
                st.markdown("""
                **📚 Per approfondire:**
                - Studia i fondamentali della finanza personale
                - Comprendi il tuo profilo di rischio
                - Impara sui costi degli investimenti
                - Considera l'orizzonte temporale dei tuoi obiettivi
                - Analizza le performance storiche nel contesto
                
                **🔍 Domande da porsi:**
                - Qual è il mio orizzonte temporale?
                - Quanto rischio posso tollerare?
                - Quali sono i miei obiettivi finanziari?
                - Ho un fondo di emergenza?
                - Come si è comportato questo asset in passato?
                
                **📊 Interpretazione delle performance:**
                - I rendimenti annualizzati mostrano la media nel tempo
                - Performance recenti possono essere influenzate da eventi specifici
                - Considera sempre la volatilità insieme ai rendimenti
                - Diversi periodi possono mostrare risultati molto diversi
                """)
            else:
                st.markdown("""
                **📚 To learn more:**
                - Study personal finance fundamentals
                - Understand your risk profile
                - Learn about investment costs
                - Consider your goals' time horizon
                - Analyze historical performance in context
                
                **🔍 Questions to ask yourself:**
                - What is my time horizon?
                - How much risk can I tolerate?
                - What are my financial goals?
                - Do I have an emergency fund?
                - How has this asset performed historically?
                
                **📊 Performance interpretation:**
                - Annualized returns show average over time
                - Recent performance may be influenced by specific events
                - Always consider volatility alongside returns
                - Different time periods may show very different results
                """)
        
        # Performance methodology note
        with st.expander("🔬 " + ("Performance Data Methodology" if "English" in str(ui_text) else "Metodologia Dati Performance")):
            if language == "Italiano":
                st.markdown("""
                **📋 Come interpretiamo i dati:**
                
                - **Rendimenti Annualizzati**: Calcolati come media geometrica per il periodo
                - **Indici di Riferimento**: Utilizzati indici di mercato riconosciuti (MSCI, Bloomberg, etc.)
                - **Valuta**: Performance generalmente in USD, convertite quando appropriato
                - **Commissioni**: Dati al lordo di commissioni di gestione per semplicità educativa
                - **Reinvestimento**: Assumiamo il reinvestimento di dividendi/cedole
                
                **⚠️ Limitazioni:**
                - Dati storici basati su indici, non su investimenti diretti
                - Performance passate non predicono risultati futuri
                - Non considerano tasse individuali o commissioni specifiche
                - Alcuni dati possono essere stimati per periodi più lunghi
                """)
            else:
                st.markdown("""
                **📋 How we interpret the data:**
                
                - **Annualized Returns**: Calculated as geometric average for the period
                - **Reference Indices**: Used recognized market indices (MSCI, Bloomberg, etc.)
                - **Currency**: Performance generally in USD, converted when appropriate
                - **Fees**: Data gross of management fees for educational simplicity
                - **Reinvestment**: We assume reinvestment of dividends/coupons
                
                **⚠️ Limitations:**
                - Historical data based on indices, not direct investments
                - Past performance doesn't predict future results
                - Doesn't consider individual taxes or specific fees
                - Some data may be estimated for longer periods
                """)

if __name__ == "__main__":
    main()
