import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Import data files
from asset_data_en import ASSET_DATA_EN, UI_TEXT_EN
from asset_data_it import ASSET_DATA_IT, UI_TEXT_IT

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
                
                **🔍 Domande da porsi:**
                - Qual è il mio orizzonte temporale?
                - Quanto rischio posso tollerare?
                - Quali sono i miei obiettivi finanziari?
                - Ho un fondo di emergenza?
                """)
            else:
                st.markdown("""
                **📚 To learn more:**
                - Study personal finance fundamentals
                - Understand your risk profile
                - Learn about investment costs
                - Consider your goals' time horizon
                
                **🔍 Questions to ask yourself:**
                - What is my time horizon?
                - How much risk can I tolerate?
                - What are my financial goals?
                - Do I have an emergency fund?
                """)

if __name__ == "__main__":
    main()
