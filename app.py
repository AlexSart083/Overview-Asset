# ===== MAIN APPLICATION LOGIC =====

def main():
    # Store language in session state
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    
    # Display data source info
    if MODULAR_DATA_AVAILABLE:
        st.sidebar.success("✅ Using modular data structure")
    else:
        st.sidebar.warning("⚠️ Using legacy data structure")
    
    # Language selection in sidebar
    st.sidebar.title("🌍 Language | Lingua")
    language = st.sidebar.selectbox(
        "Select Language | Seleziona Lingua",
        ["English", "Italiano"],
        index=0 if st.session_state.language == "English" else 1
    )
    st.session_state.language = language
    
    # Get data based on language
    try:
        asset_data, ui_text = get_language_data(language)
        categories = categorize_assets(asset_data, language)
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        st.stop()
    
    # App title and description
    st.title(ui_text["title"])
    st.markdown(f"*{ui_text['subtitle']}*")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Assets", len(asset_data))
    with col2:
        equity_count = len([k for k in asset_data.keys() if any(word in k.lower() for word in ['equity', 'azioni', 'momentum', 'quality', 'value', 'small', 'emerging', 'dividend'])])
        st.metric("📈 Equity Strategies", equity_count)
    with col3:
        bond_count = len([k for k in asset_data.keys() if any(word in k.lower() for word in ['bond', 'obblig', 'yield', 'inflation', 'convert', 'subordin', 'government', 'corporate', 'governativ'])])
        st.metric("💰 Bond Types", bond_count)
    with col4:
        alt_count = len([k for k in asset_data.keys() if any(word in k.lower() for word in ['gold', 'oro', 'silver', 'argento', 'commodity', 'materie', 'reit'])])
        st.metric("🏢 Alternative Assets", alt_count)
    
    st.markdown("---")
    
    # Sidebar for asset selection
    st.sidebar.title(ui_text["sidebar_title"])
    selected_asset = create_asset_selector(asset_data, categories, ui_text)
    
    # Add comparison mode option
    st.sidebar.markdown("---")
    comparison_mode = st.sidebar.checkbox(
        "📊 " + ui_text.get("comparison_mode", "Comparison Mode"),
        help=ui_text.get("comparison_help", "Select multiple assets to compare")
    )
    
    if comparison_mode:
        st.sidebar.markdown("### " + ui_text.get("select_assets_compare", "Select Assets to Compare"))
        selected_assets = st.sidebar.multiselect(
            ui_text.get("choose_assets", "Choose assets:"),
            list(asset_data.keys()),
            default=[selected_asset] if selected_asset else [],
            max_selections=7
        )
    else:
        selected_assets = [selected_asset] if selected_asset else []
    
    # Main content
    if selected_asset and selected_asset in asset_data:
        asset_info = asset_data[selected_asset]
        
        # Title with emoji based on asset type
        asset_emoji = "📈" if any(word in selected_asset.lower() for word in ["equit", "azion", "mercati", "momentum", "quality", "value", "small", "dividend"]) else \
                     "💰" if any(word in selected_asset.lower() for word in ["bond", "obblig"]) else \
                     "🥇" if any(word in selected_asset.lower() for word in ["gold", "silver", "oro", "argento"]) else \
                     "🏢"
        
        st.header(f"{asset_emoji} {ui_text['analysis_title']}{selected_asset}")
        
        # Warning disclaimer
        st.warning(ui_text["warning"])
        
        # Description with improved formatting
        st.subheader(ui_text["description_header"])
        st.markdown(f"**{asset_info['descrizione']}**")
        
        # Historical Performance Section - UPDATED WITH NEW CHARTS
        if "performance_storica" in asset_info:
            st.subheader(ui_text["performance_header"])
            
            # NEW: Yearly performance chart with REAL YEARS
            yearly_chart = create_yearly_performance_chart(asset_info["performance_storica"], selected_asset, ui_text)
            if yearly_chart:
                st.plotly_chart(yearly_chart, use_container_width=True)
                
                # NEW: Yearly performance table with REAL YEARS
                display_yearly_performance_table(asset_info["performance_storica"], ui_text)
            else:
                # Fallback to legacy chart
                legacy_chart = create_performance_chart_legacy(asset_info["performance_storica"], selected_asset, ui_text)
                if legacy_chart:
                    st.plotly_chart(legacy_chart, use_container_width=True)
                
                # Legacy table
                display_performance_table_with_date(asset_info["performance_storica"], ui_text)
            
            # Performance note
            st.info(ui_text["performance_note"])
        
        # ENHANCED BOND ANALYSIS - NEW FEATURE
        if any(word in selected_asset.lower() for word in ["bond", "obblig"]):
            display_enhanced_bond_analysis(asset_data, selected_asset, selected_assets, ui_text)
        
        st.markdown("---")
        
        # Two column layout for strengths and weaknesses
        col1, col2 = st.columns(2)
        
        with col1:
            # Strengths
            st.subheader(ui_text["strengths_header"])
            for i, strength in enumerate(asset_info.get("punti_forza", []), 1):
                st.markdown(f"**{i}.** {strength}")
        
        with col2:
            # Weaknesses
            st.subheader(ui_text["weaknesses_header"])
            for i, weakness in enumerate(asset_info.get("punti_debolezza", []), 1):
                st.markdown(f"**{i}.** {weakness}")
        
        st.markdown("---")
        
        # Market scenarios with improved table
        st.subheader(ui_text["scenarios_header"])
        
        # Create enhanced dataframe for scenarios
        scenarios_data = []
        for scenario, performance in asset_info.get("scenari", {}).items():
            # Add simple color coding based on performance
            if any(word in performance.lower() for word in ["positive", "positiv", "outperform"]):
                trend = ui_text.get("trend_positive", "🟢 Positive")
            elif any(word in performance.lower() for word in ["negative", "negativ", "underperform"]):
                trend = ui_text.get("trend_negative", "🔴 Negative")
            else:
                trend = ui_text.get("trend_mixed", "🟡 Mixed")
            
            scenarios_data.append({
                ui_text.get("scenario_column", "🌍 Scenario"): scenario,
                ui_text.get("trend_column", "📊 Trend"): trend,
                ui_text.get("performance_column", "📝 Expected Performance"): performance
            })
        
        if scenarios_data:
            scenarios_df = pd.DataFrame(scenarios_data)
            st.dataframe(scenarios_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Allocation and correlations with better styling
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader(ui_text["allocation_header"])
            allocation_range = asset_info.get('allocazione_range', 'N/A')
            st.info(f"💼 **{allocation_range}**")
        
        with col4:
            st.subheader(ui_text["correlations_header"])
            correlations = asset_info.get('correlazioni', 'N/A')
            st.info(f"🔗 **{correlations}**")
        
        st.markdown("---")
        
        # Enhanced visualizations - UPDATED WITH NEW CHARTS
        st.subheader(ui_text["visualization_title"])
        
        # Create tabs for different visualizations
        if comparison_mode and len(selected_assets) > 1:
            tab1, tab2, tab3, tab4 = st.tabs([
                "📊 " + ui_text.get("performance_comparison", "Performance Comparison"),
                "🔥 Crisis Analysis",
                "⚖️ Risk-Return Profile", 
                "🥧 " + ui_text.get("sample_portfolio", "Sample Portfolio")
            ])
            
            with tab1:
                # NEW: Yearly comparison chart with REAL YEARS
                yearly_comparison = create_yearly_comparison_chart(asset_data, selected_assets, ui_text)
                if yearly_comparison:
                    st.plotly_chart(yearly_comparison, use_container_width=True)
                    st.caption("💡 Green markers = positive years, Red markers = negative years")
                else:
                    st.info("📊 Yearly comparison data not available for selected assets")
            
            with tab2:
                # NEW: Crisis performance analysis with REAL YEARS
                crisis_chart = create_crisis_performance_chart(asset_data, selected_assets, ui_text)
                if crisis_chart:
                    st.plotly_chart(crisis_chart, use_container_width=True)
                    st.caption("🔥 Performance during major market crises (2008 Financial Crisis, 2020 COVID, 2022 Rate Shock)")
                else:
                    st.info("📊 Crisis analysis data not available")
            
            with tab3:
                # NEW: Risk-return scatter plot
                risk_return_chart = create_volatility_comparison_chart(asset_data, selected_assets, ui_text)
                if risk_return_chart:
                    st.plotly_chart(risk_return_chart, use_container_width=True)
                    st.caption("⚖️ Higher up = better returns, Further right = higher risk")
                else:
                    st.info("📊 Risk-return analysis requires yearly data")
            
            with tab4:
                # Sample allocation
                try:
                    pie_fig = create_allocation_pie()
                    st.plotly_chart(pie_fig, use_container_width=True)
                    st.caption(ui_text.get("educational_example", "💡 This is just an educational example - not investment advice"))
                except Exception as e:
                    st.error(f"Error creating allocation chart: {e}")
                
        else:
            tab1, tab2 = st.tabs([
                "🥧 " + ui_text.get("sample_portfolio", "Sample Portfolio"),
                "📚 Educational Resources"
            ])
            
            with tab1:
                # Sample allocation
                try:
                    pie_fig = create_allocation_pie()
                    st.plotly_chart(pie_fig, use_container_width=True)
                    st.caption(ui_text.get("educational_example", "💡 This is just an educational example - not investment advice"))
                except Exception as e:
                    st.error(f"Error creating allocation chart: {e}")
            
            with tab2:
                # Educational content expanded
                st.markdown("### 📚 Understanding Investment Performance")
                st.markdown("""
                **Key Concepts:**
                - **Annualized Returns**: Average yearly performance over the time period
                - **Volatility**: How much returns vary from year to year (risk measure)
                - **Drawdown**: Maximum peak-to-trough decline during a period
                - **Correlation**: How assets move relative to each other
                
                **Reading the Charts:**
                - Green = Positive performance years
                - Red = Negative performance years
                - Moving averages smooth out short-term noise
                - Crisis years show how assets behave during stress
                """)
        
        st.markdown("---")
        
        # Educational summary with enhanced formatting
        st.subheader(ui_text["summary_header"])
        
        summary_text = f"""
        ### {ui_text.get('key_takeaways', '🎯 Key Takeaways for')} {selected_asset}
        
        **{selected_asset}** represents an asset with specific characteristics that make it suitable 
        for certain investment objectives. Its performance varies significantly based on macroeconomic 
        scenarios, making it important to understand its behavior in the context of a diversified portfolio.
        
        #### {ui_text.get('key_points', '📚 Key points to remember:')}
        - **{ui_text.get('diversification_key', '🎯 Diversification is fundamental')}**
        - **{ui_text.get('time_horizon', '⏰ Time horizon influences selection')}**
        - **{ui_text.get('correlations_change', '🔄 Correlations change during stress')}**
        - **{ui_text.get('risk_return', '⚖️ Risk and return must always be evaluated together')}**
        - **{ui_text.get('past_performance', '📊 Past performance doesn\'t guarantee future results')}**
        
        #### {ui_text.get('important_note', '🚨 Important:')}
        {ui_text.get('educational_purpose', 'This analysis is purely educational.')}
        """ if language == "English" else f"""
        ### {ui_text.get('key_takeaways', '🎯 Punti chiave per')} {selected_asset}
        
        **{selected_asset}** rappresenta un asset con caratteristiche specifiche che lo rendono adatto 
        a determinati obiettivi di investimento. La sua performance varia significativamente in base 
        agli scenari macroeconomici, rendendo importante comprenderne il comportamento nel contesto 
        di un portafoglio diversificato.
        
        #### {ui_text.get('key_points', '📚 Punti chiave da ricordare:')}
        - **{ui_text.get('diversification_key', '🎯 La diversificazione è fondamentale')}**
        - **{ui_text.get('time_horizon', '⏰ L\'orizzonte temporale influenza la scelta')}**
        - **{ui_text.get('correlations_change', '🔄 Le correlazioni cambiano nei momenti di stress')}**
        - **{ui_text.get('risk_return', '⚖️ Rischio e rendimento vanno sempre valutati insieme')}**
        - **{ui_text.get('past_performance', '📊 Le performance passate non garantiscono risultati futuri')}**
        
        #### {ui_text.get('important_note', '🚨 Importante:')}
        {ui_text.get('educational_purpose', 'Questa analisi è puramente educativa.')}
        """
        
        st.markdown(summary_text)
        
        # Additional resources section
        with st.expander("📖 " + ui_text.get("additional_resources", "Additional Resources")):
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
        with st.expander("🔬 " + ui_text.get("performance_methodology", "Performance Data Methodology")):
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
        
        # Special section for bonds with rate environment
        if any(word in selected_asset.lower() for word in ["bond", "obblig"]):
            with st.expander("🏛️ " + ("Bond Market Context" if language == "English" else "Contesto Mercato Obbligazionario")):
                if language == "Italiano":
                    st.markdown("""
                    **🎯 Contesto Attuale Mercato Obbligazionario:**
                    
                    - **Tassi BCE**: Ai massimi dal 2008 (4.5% nel 2024)
                    - **Inflazione**: In discesa dal picco 8.4% del 2022 a 2.4% nel 2024
                    - **Tassi Reali**: Positivi per la prima volta dal 2008
                    - **Duration Risk**: Elevato per le scadenze lunghe
                    
                    **💡 Implications per gli Investitori:**
                    - Bond a breve termine offrono rendimenti reali interessanti
                    - Bond a lungo termine sensibili a variazioni tassi
                    - Obbligazioni governative vs corporate: diversa sensibilità creditizia
                    - Monitoraggio politica BCE cruciale per timing
                    """)
                else:
                    st.markdown("""
                    **🎯 Current Bond Market Context:**
                    
                    - **ECB Rates**: At highest since 2008 (4.5% in 2024)
                    - **Inflation**: Down from 8.4% peak in 2022 to 2.4% in 2024
                    - **Real Rates**: Positive for first time since 2008
                    - **Duration Risk**: High for longer maturities
                    
                    **💡 Implications for Investors:**
                    - Short-term bonds offer attractive real returns
                    - Long-term bonds sensitive to rate changes
                    - Government vs corporate bonds: different credit sensitivity
                    - ECB policy monitoring crucial for timing
                    """)
    
    elif selected_asset:
        st.error(f"❌ Asset '{selected_asset}' not found in database.")
    else:
        # Welcome screen with enhanced information
        st.info("👈 Please select an asset from the sidebar to begin analysis.")
        
        # Display overview statistics
        st.markdown("## 🌟 Welcome to Financial Asset Analyzer")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📊 What you can analyze:
            - **Equity Strategies**: Global markets, momentum, quality, value
            - **Government Bonds**: All duration ranges (0-1Y to >10Y)
            - **Corporate Bonds**: Investment grade and high yield
            - **Alternative Assets**: Gold, commodities, REITs
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 Key Features:
            - **Historical Performance**: 20 years of data with real years (2024-2005)
            - **Market Scenarios**: How assets behave in different conditions
            - **Enhanced Bond Analysis**: Interest rates and inflation context
            - **Comparison Tools**: Multi-asset analysis
            """)
        
        # Sample chart to show capabilities
        if st.button("🎬 Show Demo: Bond vs Rates Analysis"):
            demo_asset = "Bond Governativi 3-7 anni" if language == "Italiano" else "Government Bonds 3-7 Years"
            if demo_asset in asset_data:
                demo_chart = create_enhanced_bond_chart(asset_data, demo_asset, ui_text)
                if demo_chart:
                    st.plotly_chart(demo_chart, use_container_width=True)
                    st.success("👆 This is an example of our enhanced bond analysis with ECB rates and inflation context!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
📈 Financial Asset Analyzer | Educational Tool for Investment Learning<br>
⚠️ This application is for educational purposes only - not financial advice<br>
🆕 Now with Real Year Labels (2024-2005) in all charts!
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import logging

# Configure page
st.set_page_config(
    page_title="Financial Asset Analyzer | Analizzatore Asset Finanziari",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import modular data
try:
    from data.loader import load_all_assets, load_ui_text, get_asset_categories, validate_asset_data
    MODULAR_DATA_AVAILABLE = True
    logger.info("Successfully loaded modular data structure")
except ImportError as e:
    logger.warning(f"Modular data not available: {e}")
    MODULAR_DATA_AVAILABLE = False
    
    # Fallback to legacy data structure
    try:
        from asset_data_en import ASSET_DATA_EN, UI_TEXT_EN
        from asset_data_it import ASSET_DATA_IT, UI_TEXT_IT
        logger.info("Using legacy data structure as fallback")
    except ImportError:
        logger.error("Neither modular nor legacy data available!")
        st.error("❌ Data files not found. Please ensure data files are available.")
        st.stop()

# European Interest Rates and Inflation Historical Data (2005-2024)
EUROPEAN_RATES_DATA = {
    "anni": [f"anno_{i}" for i in range(1, 21)],  # Y1 = 2024, Y20 = 2005
    "tassi_ecb": {
        "anno_1": "4.5%",    # 2024 - Tassi alti post-inflazione
        "anno_2": "4.0%",    # 2023 - Picco restrittivo
        "anno_3": "2.5%",    # 2022 - Inizio rialzi
        "anno_4": "0.0%",    # 2021 - Zero bound
        "anno_5": "0.0%",    # 2020 - COVID response
        "anno_6": "0.0%",    # 2019 - Dovish
        "anno_7": "0.0%",    # 2018 - Fine QE
        "anno_8": "0.0%",    # 2017 - QE in corso
        "anno_9": "0.0%",    # 2016 - Negative rates
        "anno_10": "0.0%",   # 2015 - QE start
        "anno_11": "0.1%",   # 2014 - Near zero
        "anno_12": "0.5%",   # 2013 - Crisi eurozona
        "anno_13": "1.0%",   # 2012 - Draghi "whatever it takes"
        "anno_14": "1.5%",   # 2011 - Eurocrisis peak
        "anno_15": "1.0%",   # 2010 - Crisi greca
        "anno_16": "1.0%",   # 2009 - Crisis response
        "anno_17": "2.5%",   # 2008 - Pre-crisis cuts
        "anno_18": "4.0%",   # 2007 - Pre-crisis high
        "anno_19": "3.5%",   # 2006 - Rising cycle
        "anno_20": "2.5%"    # 2005 - Moderate
    },
    "inflazione_hicp": {
        "anno_1": "2.4%",    # 2024 - Normalizzazione
        "anno_2": "5.4%",    # 2023 - Ancora elevata
        "anno_3": "8.4%",    # 2022 - Picco post-COVID
        "anno_4": "2.6%",    # 2021 - Recovery
        "anno_5": "0.3%",    # 2020 - COVID deflation
        "anno_6": "1.2%",    # 2019 - Target miss
        "anno_7": "1.8%",    # 2018 - Near target
        "anno_8": "1.5%",    # 2017 - Below target
        "anno_9": "0.2%",    # 2016 - Deflation fears
        "anno_10": "0.0%",   # 2015 - Deflation risk
        "anno_11": "0.4%",   # 2014 - Low inflation
        "anno_12": "1.4%",   # 2013 - Below target
        "anno_13": "2.5%",   # 2012 - Eurozone stress
        "anno_14": "3.1%",   # 2011 - Commodity spike
        "anno_15": "1.6%",   # 2010 - Recovery
        "anno_16": "-0.3%",  # 2009 - Deflation
        "anno_17": "3.3%",   # 2008 - Commodity boom
        "anno_18": "2.1%",   # 2007 - ECB target
        "anno_19": "2.2%",   # 2006 - Above target
        "anno_20": "2.2%"    # 2005 - Target level
    }
}

def get_language_data(language):
    """Get data and UI text based on selected language"""
    if MODULAR_DATA_AVAILABLE:
        try:
            # Normalize language input
            if language == "Italiano":
                normalized_lang = "italian"
            else:
                normalized_lang = "english"
            
            asset_data = load_all_assets(normalized_lang)
            ui_text = load_ui_text(normalized_lang)
            
            # Validate data integrity
            validate_asset_data(asset_data)
            
            return asset_data, ui_text
        except Exception as e:
            logger.error(f"Error loading modular data: {e}")
            st.error(f"❌ Error loading data: {e}")
            
            # Show debug information in sidebar for troubleshooting
            if st.sidebar.button("🔧 Debug Info"):
                from data.loader import debug_language_loading
                debug_info = debug_language_loading(language)
                st.sidebar.json(debug_info)
            
            st.stop()
    else:
        # Legacy fallback
        if language == "English":
            return ASSET_DATA_EN, UI_TEXT_EN
        else:
            return ASSET_DATA_IT, UI_TEXT_IT

def categorize_assets(asset_data, language):
    """Categorize assets by type for better organization"""
    if MODULAR_DATA_AVAILABLE:
        try:
            # Normalize language input for categories
            if language == "Italiano":
                normalized_lang = "italian"
            else:
                normalized_lang = "english"
            return get_asset_categories(normalized_lang)
        except Exception as e:
            logger.warning(f"Error getting categories from modular data: {e}")
    
    # Legacy fallback categories
    if language == "English":
        return {
            "📈 Equity Strategies": [
                "Global Equities (Market Cap)", "Momentum Equities", "Quality Equities", 
                "Value Equities", "Minimum Volatility Equities", "Small Cap Equities", 
                "Emerging Markets", "High Dividend Equities"
            ],
            "🏛️ Government Bonds": [
                "Government Bonds 0-1 Years", "Government Bonds 1-3 Years", "Government Bonds 3-7 Years", 
                "Government Bonds 7-10 Years", "Government Bonds >10 Years"
            ],
            "🏢 Corporate Bonds": [
                "Corporate Bonds 0-1 Years", "Corporate Bonds 1-3 Years", "Corporate Bonds 3-7 Years", 
                "Corporate Bonds 7-10 Years", "Corporate Bonds >10 Years"
            ],
            "🔸 Specialized Bonds": [
                "High Yield Bonds", "Inflation Linked Bonds", "Convertible Bonds", 
                "Subordinated Bonds"
            ],
            "🥇 Precious Metals": ["Gold", "Silver"],
            "🏗️ Alternative Assets": ["Commodities", "REITs"]
        }
    else:
        return {
            "📈 Strategie Azionarie": [
                "Azioni Globali (Market Cap)", "Azioni Momentum", "Azioni Quality", 
                "Azioni Value", "Azioni Minimum Volatility", "Azioni Small Cap", 
                "Mercati Emergenti", "Azionario High Dividend"
            ],
            "🏛️ Obbligazioni Governative": [
                "Bond Governativi 0-1 anni", "Bond Governativi 1-3 anni", "Bond Governativi 3-7 anni", 
                "Bond Governativi 7-10 anni", "Bond Governativi >10 anni"
            ],
            "🏢 Obbligazioni Corporate": [
                "Bond Corporate 0-1 anni", "Bond Corporate 1-3 anni", "Bond Corporate 3-7 anni", 
                "Bond Corporate 7-10 anni", "Bond Corporate >10 anni"
            ],
            "🔸 Obbligazioni Specializzate": [
                "Bond High Yield", "Bond Inflation Linked", "Bond Convertibili", 
                "Obbligazioni Subordinate"
            ],
            "🥇 Metalli Preziosi": ["Oro", "Argento"],
            "🏗️ Asset Alternativi": ["Materie Prime", "REIT"]
        }

def create_asset_selector(asset_data, categories, ui_text):
    """Create an improved asset selector with multiple options"""
    
    # Selection method choice
    selection_method = st.sidebar.radio(
        "🔧 " + ui_text.get("selection_method", "Selection Method"),
        [ui_text.get("by_category", "📂 By Category"), 
         ui_text.get("search", "🔍 Search"), 
         ui_text.get("full_list", "📋 Full List")],
        index=0
    )
    
    selected_asset = None
    
    if selection_method == ui_text.get("by_category", "📂 By Category"):
        # Category-based selection
        st.sidebar.markdown("### " + ui_text.get("select_category", "Select Category"))
        
        selected_category = st.sidebar.selectbox(
            ui_text.get("choose_category", "Choose asset category:"),
            list(categories.keys()),
            index=0
        )
        
        if selected_category:
            st.sidebar.markdown("### " + ui_text.get("select_asset", "Select Asset"))
            assets_in_category = categories[selected_category]
            # Filter assets that actually exist in the data
            available_assets = [asset for asset in assets_in_category if asset in asset_data]
            if available_assets:
                selected_asset = st.sidebar.radio(
                    f"{ui_text.get('assets', 'Assets')} in {selected_category}:",
                    available_assets,
                    index=0
                )
    
    elif selection_method == ui_text.get("search", "🔍 Search"):
        # Search-based selection
        st.sidebar.markdown("### " + ui_text.get("search_assets", "Search Assets"))
        
        search_term = st.sidebar.text_input(
            ui_text.get("type_to_search", "Type to search assets:"),
            placeholder=ui_text.get("search_placeholder", "e.g., Gold, Bond, Equity...")
        )
        
        if search_term:
            # Filter assets based on search term
            matching_assets = [asset for asset in asset_data.keys() 
                             if search_term.lower() in asset.lower()]
            
            if matching_assets:
                selected_asset = st.sidebar.selectbox(
                    f"📍 {ui_text.get('found_assets', 'Found')} {len(matching_assets)} {ui_text.get('assets_found', 'assets:')}",
                    matching_assets,
                    index=0
                )
            else:
                st.sidebar.warning(ui_text.get("no_assets_found", "❌ No assets found. Try different keywords."))
        else:
            st.sidebar.info(ui_text.get("start_typing", "💡 Start typing to search..."))
    
    else:  # Full List
        # Traditional dropdown for those who prefer it
        st.sidebar.markdown("### " + ui_text.get("full_asset_list", "Full Asset List"))
        selected_asset = st.sidebar.selectbox(
            ui_text.get("all_assets", "All assets (A-Z):"),
            sorted(list(asset_data.keys())),
            index=0
        )
    
    return selected_asset

# ===== ENHANCED BOND CHART FUNCTIONS =====

def create_enhanced_bond_chart(asset_data, asset_name, ui_text):
    """Create enhanced bond chart with interest rates and inflation overlay"""
    
    if asset_name not in asset_data or "performance_storica" not in asset_data[asset_name]:
        return None
    
    performance_data = asset_data[asset_name]["performance_storica"]
    
    # Skip if not bond asset
    is_bond = any(word in asset_name.lower() for word in 
                 ["bond", "obblig", "yield", "inflation", "convert", "subordin"])
    
    if not is_bond or "rendimenti_annuali" not in performance_data:
        return None
    
    # Extract bond performance data
    yearly_data = performance_data["rendimenti_annuali"]
    current_year = 2024
    
    years = []
    bond_returns = []
    ecb_rates = []
    inflation_rates = []
    
    for i in range(1, 21):
        year_key = f"anno_{i}"
        
        if year_key in yearly_data:
            try:
                # Bond performance
                bond_perf = float(yearly_data[year_key].replace('%', ''))
                bond_returns.append(bond_perf)
                
                # ECB rates
                ecb_rate = float(EUROPEAN_RATES_DATA["tassi_ecb"][year_key].replace('%', ''))
                ecb_rates.append(ecb_rate)
                
                # Inflation
                inflation = float(EUROPEAN_RATES_DATA["inflazione_hicp"][year_key].replace('%', ''))
                inflation_rates.append(inflation)
                
                # Real years
                actual_year = current_year - (i - 1)
                years.append(str(actual_year))
                
            except (ValueError, KeyError):
                continue
    
    if not bond_returns:
        return None
    
    # Create subplot with secondary y-axis
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=[
            f"📊 {asset_name} Performance vs Market Environment",
            "🎯 ECB Policy Rates vs Eurozone Inflation (HICP)"
        ],
        vertical_spacing=0.15,
        specs=[[{"secondary_y": True}],
               [{"secondary_y": False}]]
    )
    
    # === TOP CHART: Bond Performance vs ECB Rates ===
    
    # Bond performance (bars)
    colors = ['green' if x >= 0 else 'red' for x in bond_returns]
    fig.add_trace(
        go.Bar(
            x=years,
            y=bond_returns,
            name=f"{asset_name} Return",
            marker_color=colors,
            opacity=0.7,
            text=[f"{r:.1f}%" for r in bond_returns],
            textposition='auto',
            hovertemplate="<b>%{x}</b><br>Bond Return: %{y}%<extra></extra>"
        ),
        row=1, col=1
    )
    
    # ECB rates (line on secondary y-axis)
    fig.add_trace(
        go.Scatter(
            x=years,
            y=ecb_rates,
            mode='lines+markers',
            name='ECB Main Rate',
            line=dict(color='blue', width=3),
            marker=dict(size=6, color='blue'),
            yaxis='y2',
            hovertemplate="<b>%{x}</b><br>ECB Rate: %{y}%<extra></extra>"
        ),
        row=1, col=1, secondary_y=True
    )
    
    # === BOTTOM CHART: ECB Rates vs Inflation ===
    
    # ECB rates
    fig.add_trace(
        go.Scatter(
            x=years,
            y=ecb_rates,
            mode='lines+markers',
            name='ECB Main Rate',
            line=dict(color='blue', width=3),
            marker=dict(size=6, color='blue'),
            showlegend=False,
            hovertemplate="<b>%{x}</b><br>ECB Rate: %{y}%<extra></extra>"
        ),
        row=2, col=1
    )
    
    # Inflation
    fig.add_trace(
        go.Scatter(
            x=years,
            y=inflation_rates,
            mode='lines+markers',
            name='Eurozone Inflation (HICP)',
            line=dict(color='orange', width=3),
            marker=dict(size=6, color='orange'),
            fill='tonexty',
            fillcolor='rgba(255,165,0,0.1)',
            hovertemplate="<b>%{x}</b><br>Inflation: %{y}%<extra></extra>"
        ),
        row=2, col=1
    )
    
    # Calculate real rates (ECB rate - inflation) and add as shaded area
    real_rates = [ecb - inf for ecb, inf in zip(ecb_rates, inflation_rates)]
    
    fig.add_trace(
        go.Scatter(
            x=years,
            y=real_rates,
            mode='lines',
            name='Real Rate (ECB - Inflation)',
            line=dict(color='purple', width=2, dash='dash'),
            hovertemplate="<b>%{x}</b><br>Real Rate: %{y:.1f}%<extra></extra>"
        ),
        row=2, col=1
    )
    
    # === ANNOTATIONS AND REFERENCE LINES ===
    
    # Add ECB 2% inflation target line
    fig.add_hline(y=2.0, line_dash="dot", line_color="red", opacity=0.5, 
                  annotation_text="ECB Target: 2%", row=2, col=1)
    
    # Add zero line for real rates
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, row=2, col=1)
    
    # Zero line for bond performance
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.3, row=1, col=1)
    
    # === LAYOUT AND STYLING ===
    
    fig.update_layout(
        title_text=f"📈 {asset_name} - Market Environment Analysis (2005-2024)",
        title_x=0.5,
        height=800,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(240,240,240,0.1)',
        paper_bgcolor='white'
    )
    
    # Update x-axes - REVERSE ORDER so 2024 is on left
    fig.update_xaxes(
        title_text="Anno", 
        showgrid=True, 
        gridcolor='lightgray',
        autorange='reversed'  # 2024 a sinistra, 2005 a destra
    )
    
    # Update y-axes for top chart
    fig.update_yaxes(title_text="Bond Return (%)", showgrid=True, gridcolor='lightgray', row=1, col=1)
    fig.update_yaxes(title_text="ECB Rate (%)", showgrid=False, row=1, col=1, secondary_y=True)
    
    # Update y-axes for bottom chart  
    fig.update_yaxes(title_text="Rate/Inflation (%)", showgrid=True, gridcolor='lightgray', row=2, col=1)
    
    return fig

def create_bond_correlation_analysis(asset_data, selected_bond_assets, ui_text):
    """Create correlation analysis between different bond types and rates/inflation"""
    
    if len(selected_bond_assets) < 2:
        return None
    
    # Filter only bond assets
    bond_assets = [asset for asset in selected_bond_assets 
                  if any(word in asset.lower() for word in 
                        ["bond", "obblig", "yield", "inflation", "convert", "subordin"])]
    
    if len(bond_assets) < 2:
        return None
    
    # Create correlation matrix
    correlation_data = []
    
    # Add ECB rates and inflation as reference
    ecb_rates_series = []
    inflation_series = []
    
    for i in range(1, 21):
        year_key = f"anno_{i}"
        try:
            ecb_rate = float(EUROPEAN_RATES_DATA["tassi_ecb"][year_key].replace('%', ''))
            inflation = float(EUROPEAN_RATES_DATA["inflazione_hicp"][year_key].replace('%', ''))
            ecb_rates_series.append(ecb_rate)
            inflation_series.append(inflation)
        except (KeyError, ValueError):
            continue
    
    # Calculate correlations
    all_series = {
        "ECB Rates": ecb_rates_series,
        "Inflation": inflation_series
    }
    
    # Add bond series
    for asset_name in bond_assets:
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            if "rendimenti_annuali" in performance_data:
                yearly_data = performance_data["rendimenti_annuali"]
                returns = []
                
                for i in range(1, 21):
                    year_key = f"anno_{i}"
                    if year_key in yearly_data:
                        try:
                            ret = float(yearly_data[year_key].replace('%', ''))
                            returns.append(ret)
                        except (ValueError, AttributeError):
                            continue
                
                if len(returns) == len(ecb_rates_series):
                    all_series[asset_name] = returns
    
    # Calculate correlation matrix
    asset_names = list(all_series.keys())
    correlation_matrix = []
    
    for i, asset1 in enumerate(asset_names):
        row = []
        for j, asset2 in enumerate(asset_names):
            if i == j:
                correlation = 1.0
            else:
                series1 = all_series[asset1]
                series2 = all_series[asset2]
                correlation = np.corrcoef(series1, series2)[0, 1]
            row.append(correlation)
        correlation_matrix.append(row)
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix,
        x=asset_names,
        y=asset_names,
        colorscale='RdBu',
        zmid=0,
        text=[[f"{val:.2f}" for val in row] for row in correlation_matrix],
        texttemplate="%{text}",
        textfont={"size": 10},
        hovertemplate="<b>%{y} vs %{x}</b><br>Correlation: %{z:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title="🔗 Bond Correlations with Rates & Inflation",
        title_x=0.5,
        height=500,
        width=600
    )
    
    return fig

def create_duration_sensitivity_chart(asset_data, selected_bond_assets, ui_text):
    """Create chart showing duration sensitivity to rate changes"""
    
    # Duration estimates by bond type (approximate)
    DURATION_ESTIMATES = {
        # Government bonds
        "Government Bonds 0-1 Years": 0.5,
        "Bond Governativi 0-1 anni": 0.5,
        "Government Bonds 1-3 Years": 2.0,
        "Bond Governativi 1-3 anni": 2.0,
        "Government Bonds 3-7 Years": 5.0,
        "Bond Governativi 3-7 anni": 5.0,
        "Government Bonds 7-10 Years": 8.5,
        "Bond Governativi 7-10 anni": 8.5,
        "Government Bonds >10 Years": 15.0,
        "Bond Governativi >10 anni": 15.0,
        
        # Corporate bonds
        "Corporate Bonds 0-1 Years": 0.5,
        "Bond Corporate 0-1 anni": 0.5,
        "Corporate Bonds 1-3 Years": 2.0,
        "Bond Corporate 1-3 anni": 2.0,
        "Corporate Bonds 3-7 Years": 5.0,
        "Bond Corporate 3-7 anni": 5.0,
        "Corporate Bonds 7-10 Years": 8.5,
        "Bond Corporate 7-10 anni": 8.5,
        "Corporate Bonds >10 Years": 15.0,
        "Bond Corporate >10 anni": 15.0,
        
        # Specialized bonds
        "High Yield Bonds": 4.0,
        "Bond High Yield": 4.0,
        "Inflation Linked Bonds": 8.0,
        "Bond Inflation Linked": 8.0,
        "Convertible Bonds": 3.0,
        "Bond Convertibili": 3.0,
        "Subordinated Bonds": 6.0,
        "Obbligazioni Subordinate": 6.0
    }
    
    bond_assets = [asset for asset in selected_bond_assets 
                  if any(word in asset.lower() for word in 
                        ["bond", "obblig", "yield", "inflation", "convert", "subordin"])]
    
    if not bond_assets:
        return None
    
    # Calculate average returns and durations
    duration_data = []
    
    for asset_name in bond_assets:
        if asset_name in asset_data and asset_name in DURATION_ESTIMATES:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            if "rendimenti_annuali" in performance_data:
                yearly_data = performance_data["rendimenti_annuali"]
                returns = []
                
                for year_key in yearly_data.keys():
                    try:
                        ret = float(yearly_data[year_key].replace('%', ''))
                        returns.append(ret)
                    except (ValueError, AttributeError):
                        continue
                
                if returns:
                    avg_return = np.mean(returns)
                    volatility = np.std(returns)
                    duration = DURATION_ESTIMATES[asset_name]
                    
                    duration_data.append({
                        "Asset": asset_name,
                        "Duration": duration,
                        "Avg Return": avg_return,
                        "Volatility": volatility
                    })
    
    if not duration_data:
        return None
    
    # Create scatter plot
    fig = go.Figure()
    
    for data_point in duration_data:
        # Color based on government vs corporate
        if "Government" in data_point["Asset"] or "Governativ" in data_point["Asset"]:
            color = 'blue'
            symbol = 'circle'
        elif "Corporate" in data_point["Asset"]:
            color = 'red'
            symbol = 'square'
        else:
            color = 'green'
            symbol = 'diamond'
        
        fig.add_trace(go.Scatter(
            x=[data_point["Duration"]],
            y=[data_point["Avg Return"]],
            mode='markers+text',
            text=[data_point["Asset"].replace(" ", "<br>")],
            textposition="top center",
            marker=dict(
                size=data_point["Volatility"] * 2,  # Size based on volatility
                color=color,
                symbol=symbol,
                opacity=0.7,
                line=dict(width=2, color='darkblue')
            ),
            name=data_point["Asset"],
            hovertemplate=f"<b>{data_point['Asset']}</b><br>" +
                         f"Duration: {data_point['Duration']:.1f} years<br>" +
                         f"Avg Return: {data_point['Avg Return']:.1f}%<br>" +
                         f"Volatility: {data_point['Volatility']:.1f}%<extra></extra>",
            showlegend=False
        ))
    
    fig.update_layout(
        title="⏱️ Bond Duration vs Return Profile",
        xaxis_title="Duration (Years) - Interest Rate Sensitivity",
        yaxis_title="Average Annual Return (%)",
        height=500,
        title_x=0.5,
        plot_bgcolor='rgba(240,240,240,0.1)',
        annotations=[
            dict(
                x=0.02,
                y=0.98,
                xref="paper",
                yref="paper",
                text="💡 Bubble size = Volatility<br>" +
                     "🔵 Government  🔴 Corporate  🟢 Specialized",
                showarrow=False,
                font=dict(size=10),
                bgcolor="rgba(255,255,255,0.8)",
                bordercolor="gray",
                borderwidth=1
            )
        ]
    )
    
    # Add reference lines
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    return fig

def display_enhanced_bond_analysis(asset_data, selected_asset, selected_assets, ui_text):
    """Display enhanced bond analysis with rates and inflation context"""
    
    # Check if we're dealing with bonds
    is_bond_analysis = any(word in selected_asset.lower() for word in 
                          ["bond", "obblig", "yield", "inflation", "convert", "subordin"])
    
    if not is_bond_analysis:
        return
    
    st.markdown("---")
    st.subheader("🏛️ Bond Market Environment Analysis")
    
    # Enhanced bond chart
    enhanced_chart = create_enhanced_bond_chart(asset_data, selected_asset, ui_text)
    if enhanced_chart:
        st.plotly_chart(enhanced_chart, use_container_width=True)
        
        # Educational explanation
        st.info("""
        **📚 Understanding Bond-Rate Relationships:**
        
        - **Inverse Relationship**: Bond prices typically move opposite to interest rates
        - **Duration Risk**: Longer-term bonds are more sensitive to rate changes  
        - **Real Returns**: Bond performance relative to inflation determines real purchasing power
        - **Policy Impact**: ECB rate decisions directly affect bond market dynamics
        """)
    
    # If multiple bonds selected, show correlation analysis
    if len(selected_assets) > 1:
        st.markdown("### 🔗 Bond Correlation Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            corr_chart = create_bond_correlation_analysis(asset_data, selected_assets, ui_text)
            if corr_chart:
                st.plotly_chart(corr_chart, use_container_width=True)
        
        with col2:
            duration_chart = create_duration_sensitivity_chart(asset_data, selected_assets, ui_text)
            if duration_chart:
                st.plotly_chart(duration_chart, use_container_width=True)
    
    # Market environment summary
    st.markdown("### 📊 Current Market Environment Impact")
    
    # Calculate recent trends
    current_ecb = 4.5  # 2024 level
    current_inflation = 2.4  # 2024 level
    real_rate = current_ecb - current_inflation
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("ECB Main Rate", f"{current_ecb}%", 
                 delta="↑ From 0% (2019-2022)")
    
    with col2:
        st.metric("Eurozone Inflation", f"{current_inflation}%", 
                 delta="↓ From 8.4% peak (2022)")
    
    with col3:
        st.metric("Real Interest Rate", f"{real_rate:.1f}%", 
                 delta="Positive (first time since 2008)")
    
    # Key insights based on current environment
    if real_rate > 0:
        st.success("""
        **🎯 Current Environment Insights:**
        - Real rates are positive for the first time in over a decade
        - Government bonds offer attractive real returns
        - Duration risk remains significant with rates at cycle highs
        - Inflation normalization supports bond fundamentals
        """)
    else:
        st.warning("""
        **⚠️ Current Environment Insights:**
        - Real rates remain negative, eroding purchasing power
        - Bonds may struggle to provide inflation protection
        - Consider inflation-linked alternatives
        - Monitor ECB policy for directional changes
        """)

# ===== YEARLY PERFORMANCE CHART FUNCTIONS - UPDATED WITH REAL YEARS =====

def create_yearly_performance_chart(performance_data, asset_name, ui_text):
    """Create yearly performance visualization chart with real years (2024, 2023, etc.)"""
    
    if "rendimenti_annuali" not in performance_data:
        # Fallback to old chart if yearly data not available
        return create_performance_chart_legacy(performance_data, asset_name, ui_text)
    
    yearly_data = performance_data["rendimenti_annuali"]
    current_year = 2024
    
    years = []
    returns = []
    
    # Debug: Print what we're getting
    st.sidebar.write("🔍 Debug - Raw Data Keys:", list(yearly_data.keys())[:5])
    
    # Get data in chronological order (most recent first)
    for i in range(1, 21):
        year_key = f"anno_{i}"
        if year_key in yearly_data:
            try:
                value = float(yearly_data[year_key].replace('%', ''))
                actual_year = current_year - (i - 1)  # 2024, 2023, 2022, etc.
                years.append(str(actual_year))
                returns.append(value)
            except (ValueError, AttributeError):
                continue
    
    # Debug: Print what we're plotting
    st.sidebar.write("🔍 Debug - Years to plot:", years[:5])
    
    if not returns:
        return None
    
    fig = go.Figure()
    
    # Main line with colored markers based on performance
    colors = ['green' if x >= 0 else 'red' for x in returns]
    
    fig.add_trace(go.Scatter(
        x=years,
        y=returns,
        mode='lines+markers',
        name=asset_name,
        line=dict(width=3, color='steelblue'),
        marker=dict(size=8, color=colors, line=dict(width=1, color='darkblue')),
        hovertemplate="<b>Anno %{x}</b><br>Rendimento: %{y}%<extra></extra>"
    ))
    
    # 5-year moving average
    if len(returns) >= 5:
        moving_avg_5 = []
        for i in range(len(returns)):
            if i >= 4:
                avg = sum(returns[i-4:i+1]) / 5
                moving_avg_5.append(avg)
            else:
                moving_avg_5.append(None)
        
        fig.add_trace(go.Scatter(
            x=years,
            y=moving_avg_5,
            mode='lines',
            name='Media Mobile 5 Anni',
            line=dict(width=2, color='orange', dash='dash'),
            hovertemplate="<b>Media 5Y - Anno %{x}</b><br>%{y:.1f}%<extra></extra>"
        ))
    
    # Enhanced layout
    fig.update_layout(
        title=f"📈 Rendimenti Annuali Storici - {asset_name}",
        xaxis_title="Anno",
        yaxis_title="Rendimento Annualizzato (%)",
        height=500,
        title_x=0.5,
        hovermode='x unified',
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(
            showgrid=True, 
            gridcolor='lightgray',
            # Reverse the x-axis so most recent year (2024) is on the left
            autorange='reversed',
            type='category'  # Ensure years are treated as categories
        ),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    
    # Reference lines
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 0, 0, 0.5)")
    
    overall_avg = sum(returns) / len(returns)
    fig.add_hline(
        y=overall_avg, 
        line_dash="dot", 
        line_color="green",
        annotation_text=f"Media 20Y: {overall_avg:.1f}%",
        annotation_position="top right"
    )
    
    # Add data date annotation
    data_date = performance_data.get('data_calcolo', 'Data non specificata')
    fig.add_annotation(
        x=0.99,
        y=0.01,
        xref="paper",
        yref="paper",
        text=f"📅 {data_date}",
        showarrow=False,
        font=dict(size=10, color="gray"),
        xanchor="right",
        yanchor="bottom"
    )
    
    return fig

def create_yearly_comparison_chart(asset_data, selected_assets, ui_text):
    """Create yearly comparison chart for multiple assets with real years"""
    
    if len(selected_assets) <= 1:
        return None
    
    fig = go.Figure()
    
    colors = ['steelblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']
    current_year = 2024
    
    for idx, asset_name in enumerate(selected_assets[:7]):  # Limit to 7 assets for readability
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            if "rendimenti_annuali" not in performance_data:
                continue
                
            yearly_data = performance_data["rendimenti_annuali"]
            
            years = []
            returns = []
            
            for i in range(1, 21):
                year_key = f"anno_{i}"
                if year_key in yearly_data:
                    try:
                        value = float(yearly_data[year_key].replace('%', ''))
                        actual_year = current_year - (i - 1)  # 2024, 2023, 2022, etc.
                        years.append(str(actual_year))
                        returns.append(value)
                    except (ValueError, AttributeError):
                        continue
            
            if returns:
                fig.add_trace(go.Scatter(
                    x=years,
                    y=returns,
                    mode='lines+markers',
                    name=asset_name,
                    line=dict(width=3, color=colors[idx % len(colors)]),
                    marker=dict(size=6),
                    hovertemplate=f"<b>{asset_name}</b><br>Anno %{{x}}: %{{y}}%<extra></extra>"
                ))
    
    fig.update_layout(
        title="📊 Confronto Rendimenti Annuali - Asset Selezionati",
        xaxis_title="Anno",
        yaxis_title="Rendimento Annualizzato (%)",
        height=600,
        title_x=0.5,
        hovermode='x unified',
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(
            showgrid=True, 
            gridcolor='lightgray',
            # Reverse the x-axis so most recent year (2024) is on the left
            autorange='reversed',
            type='category'  # Ensure years are treated as categories
        ),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 0, 0, 0.5)")
    
    return fig

def display_yearly_performance_table(performance_data, ui_text):
    """Display yearly performance table with real years"""
    
    if "rendimenti_annuali" not in performance_data:
        # Fallback to old table
        return display_performance_table_with_date(performance_data, ui_text)
    
    yearly_data = performance_data["rendimenti_annuali"]
    current_year = 2024
    
    # Recent 10 years with real years
    recent_data = []
    for i in range(1, 11):
        year_key = f"anno_{i}"
        if year_key in yearly_data:
            actual_year = current_year - (i - 1)
            recent_data.append({
                "Anno": str(actual_year),
                "Rendimento": yearly_data[year_key]
            })
    
    if recent_data:
        st.subheader("📊 Performance Ultimi 10 Anni")
        df_yearly = pd.DataFrame(recent_data)
        st.dataframe(df_yearly, hide_index=True, use_container_width=True)
        
        # Statistics
        numeric_returns = []
        for item in recent_data:
            try:
                numeric_returns.append(float(item["Rendimento"].replace('%', '')))
            except:
                continue
        
        if numeric_returns:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Media 10Y", f"{sum(numeric_returns)/len(numeric_returns):.1f}%")
            with col2:
                st.metric("Anno Migliore", f"{max(numeric_returns):.1f}%")
            with col3:
                st.metric("Anno Peggiore", f"{min(numeric_returns):.1f}%")
            with col4:
                volatility = np.std(numeric_returns)
                st.metric("Volatilità", f"{volatility:.1f}%")

# ===== LEGACY FUNCTIONS FOR BACKWARD COMPATIBILITY =====

def create_performance_chart_legacy(performance_data, asset_name, ui_text):
    """Legacy performance chart for backward compatibility"""
    
    periods = ["20_anni", "10_anni", "5_anni", "1_anno"]
    period_labels = {
        "20_anni": ui_text.get("years_20", "20Y"),
        "10_anni": ui_text.get("years_10", "10Y"), 
        "5_anni": ui_text.get("years_5", "5Y"),
        "1_anno": ui_text.get("years_1", "1Y")
    }
    
    # Extract performance values and convert to float
    performance_values = []
    labels = []
    
    for period in periods:
        if period in performance_data:
            try:
                # Remove % sign and convert to float
                value = float(performance_data[period].replace('%', ''))
                performance_values.append(value)
                labels.append(period_labels[period])
            except (ValueError, AttributeError) as e:
                logger.warning(f"Error parsing performance data for {period}: {e}")
                continue
    
    if not performance_values:
        return None
    
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
    
    # Get data calculation date
    data_date = performance_data.get('data_calcolo', 'Date not specified')
    
    fig.update_layout(
        title=f"{ui_text.get('historical_returns', 'Historical Annualized Returns')} - {asset_name}",
        xaxis_title=ui_text.get("time_period", "Time Period"),
        yaxis_title=ui_text.get("annualized_return", "Annualized Return (%)"),
        height=400,
        title_x=0.5,
        showlegend=False,
        # Add data date annotation
        annotations=[
            dict(
                x=0.99,
                y=0.01,
                xref="paper",
                yref="paper",
                text=f"📅 {data_date}",
                showarrow=False,
                font=dict(size=10, color="gray"),
                xanchor="right",
                yanchor="bottom"
            )
        ]
    )
    
    # Add reference line at 0%
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255, 0, 0, 0.5)")
    
    return fig

def display_performance_table_with_date(performance_data, ui_text):
    """Display performance table with prominent data date"""
    
    # Create nice display table
    perf_display = {
        ui_text.get("period", "Period"): [
            f"20 {ui_text.get('years', 'Years') if 'English' in st.session_state.get('language', 'English') else 'Anni'}",
            f"10 {ui_text.get('years', 'Years') if 'English' in st.session_state.get('language', 'English') else 'Anni'}",
            f"5 {ui_text.get('years', 'Years') if 'English' in st.session_state.get('language', 'English') else 'Anni'}",
            f"1 {ui_text.get('year', 'Year') if 'English' in st.session_state.get('language', 'English') else 'Anno'}"
        ],
        ui_text.get("return", "Return"): [
            performance_data.get("20_anni", "N/A"),
            performance_data.get("10_anni", "N/A"),
            performance_data.get("5_anni", "N/A"),
            performance_data.get("1_anno", "N/A")
        ]
    }
    
    df_perf = pd.DataFrame(perf_display)
    st.dataframe(df_perf, hide_index=True, use_container_width=True)
    
    # Reference index and data date
    ref_index = performance_data.get('indice_riferimento', 'N/A')
    data_date = performance_data.get('data_calcolo', 'Date not specified')
    
    st.caption(f"📚 **{ui_text.get('reference_index', 'Reference Index')}:** {ref_index}")
    st.caption(f"📅 **{ui_text.get('calculation_date', 'Calculation Date')}:** {data_date}")

# ===== SPECIALIZED CHART FUNCTIONS - UPDATED WITH REAL YEARS =====

def create_crisis_performance_chart(asset_data, selected_assets, ui_text):
    """Create chart showing performance during major crisis years with real years"""
    
    # Crisis years mapping with real years
    crisis_years = {
        "2008 Financial Crisis": ("anno_17", "2008"),
        "2020 COVID": ("anno_5", "2020"), 
        "2022 Rate Shock": ("anno_3", "2022")
    }
    
    fig = go.Figure()
    
    colors = ['steelblue', 'orange', 'green', 'red', 'purple']
    
    for idx, asset_name in enumerate(selected_assets[:5]):
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            if "rendimenti_annuali" not in performance_data:
                continue
                
            yearly_data = performance_data["rendimenti_annuali"]
            
            crisis_performance = []
            crisis_labels = []
            
            for crisis_name, (year_key, real_year) in crisis_years.items():
                if year_key in yearly_data:
                    try:
                        perf = float(yearly_data[year_key].replace('%', ''))
                        crisis_performance.append(perf)
                        crisis_labels.append(f"{crisis_name}\n({real_year})")
                    except (ValueError, AttributeError):
                        continue
            
            if crisis_performance:
                fig.add_trace(go.Bar(
                    x=crisis_labels,
                    y=crisis_performance,
                    name=asset_name,
                    text=[f"{p:.1f}%" for p in crisis_performance],
                    textposition='auto',
                    marker_color=colors[idx % len(colors)]
                ))
    
    fig.update_layout(
        title="🔥 Performance Durante le Principali Crisi",
        yaxis_title="Performance (%)",
        height=500,
        title_x=0.5,
        barmode='group',
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(showgrid=True, gridcolor='lightgray'),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    
    return fig

def create_volatility_comparison_chart(asset_data, selected_assets, ui_text):
    """Create chart comparing volatility across assets"""
    
    volatility_data = []
    
    for asset_name in selected_assets:
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            if "rendimenti_annuali" in performance_data:
                yearly_data = performance_data["rendimenti_annuali"]
                returns = []
                
                for year_key in yearly_data.keys():
                    try:
                        ret = float(yearly_data[year_key].replace('%', ''))
                        returns.append(ret)
                    except (ValueError, AttributeError):
                        continue
                
                if returns:
                    volatility = np.std(returns)
                    avg_return = np.mean(returns)
                    volatility_data.append({
                        "Asset": asset_name,
                        "Volatility": volatility,
                        "Average Return": avg_return
                    })
    
    if not volatility_data:
        return None
    
    df_vol = pd.DataFrame(volatility_data)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_vol["Volatility"],
        y=df_vol["Average Return"],
        mode='markers+text',
        text=df_vol["Asset"],
        textposition="top center",
        marker=dict(
            size=12,
            color=df_vol["Average Return"],
            colorscale='RdYlGn',
            showscale=True,
            colorbar=dict(title="Avg Return (%)")
        ),
        hovertemplate="<b>%{text}</b><br>Volatility: %{x:.1f}%<br>Avg Return: %{y:.1f}%<extra></extra>"
    ))
    
    fig.update_layout(
        title="⚖️ Risk-Return Profile (20Y Historical Data)",
        xaxis_title="Volatility (%)",
        yaxis_title="Average Annual Return (%)",
        height=500,
        title_x=0.5,
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(showgrid=True, gridcolor='lightgray'),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    
    # Add quadrant lines
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=df_vol["Volatility"].median(), line_dash="dash", line_color="gray", opacity=0.5)
    
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
