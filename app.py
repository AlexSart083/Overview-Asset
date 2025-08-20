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

def create_performance_chart(performance_data, asset_name, ui_text):
    """Create performance visualization chart with data date"""
    
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

def create_performance_comparison_chart(asset_data, selected_assets, ui_text):
    """Create comparison chart for multiple assets without data dates"""
    
    if len(selected_assets) <= 1:
        return None
    
    periods = ["1_anno", "5_anni", "10_anni", "20_anni"]
    period_labels = {
        "1_anno": ui_text.get("years_1", "1Y"),
        "5_anni": ui_text.get("years_5", "5Y"), 
        "10_anni": ui_text.get("years_10", "10Y"),
        "20_anni": ui_text.get("years_20", "20Y")
    }
    
    fig = go.Figure()
    
    for asset_name in selected_assets:
        if asset_name in asset_data and "performance_storica" in asset_data[asset_name]:
            performance_data = asset_data[asset_name]["performance_storica"]
            
            performance_values = []
            labels = []
            
            for period in periods:
                if period in performance_data:
                    try:
                        # Remove % sign and convert to float
                        value = float(performance_data[period].replace('%', ''))
                        performance_values.append(value)
                        labels.append(period_labels[period])
                    except (ValueError, AttributeError):
                        continue
            
            if performance_values:
                fig.add_trace(go.Scatter(
                    x=labels,
                    y=performance_values,
                    mode='lines+markers',
                    name=asset_name,
                    line=dict(width=3),
                    marker=dict(size=8),
                    hovertemplate=f"<b>{asset_name}</b><br>%{{x}}: %{{y}}%<extra></extra>"
                ))
    
    fig.update_layout(
        title=ui_text.get("performance_comparison", "Performance Comparison"),
        xaxis_title=ui_text.get("time_period", "Time Period"),
        yaxis_title=ui_text.get("annualized_return", "Annualized Return (%)"),
        height=500,
        title_x=0.5,
        hovermode='x unified'
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
    if not assets:
        return None
        
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
        title=ui_text.get("heatmap_title", "Asset Performance Heatmap by Market Scenario")
    )
    
    fig.update_layout(
        title_x=0.5,
        height=600,
        xaxis_title=ui_text.get("market_scenarios", "Market Scenarios"),
        yaxis_title=ui_text.get("assets", "Assets"),
        font=dict(size=10)
    )
    
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

def create_comparison_table_with_dates(asset_data, selected_assets, ui_text):
    """Create comparison table without showing individual data dates"""
    
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
                ui_text.get("reference", "Reference"): perf_data.get("indice_riferimento", "N/A")
            })
    
    if comparison_data:
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, hide_index=True, use_container_width=True)
    
    return comparison_data

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
            max_selections=5
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
        
        # Historical Performance Section
        if "performance_storica" in asset_info:
            st.subheader(ui_text["performance_header"])
            
            # Display performance table and chart side by side
            col_perf1, col_perf2 = st.columns([1, 2])
            
            with col_perf1:
                # Performance table with date
                display_performance_table_with_date(asset_info["performance_storica"], ui_text)
            
            with col_perf2:
                # Performance chart with date
                perf_chart = create_performance_chart(asset_info["performance_storica"], selected_asset, ui_text)
                if perf_chart:
                    st.plotly_chart(perf_chart, use_container_width=True)
                else:
                    st.info("📊 Performance chart data not available")
            
            # Performance note
            st.info(ui_text["performance_note"])
        
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
        
        # Enhanced visualizations
        st.subheader(ui_text["visualization_title"])
        
        # Create tabs for different visualizations
        if comparison_mode and len(selected_assets) > 1:
            tab1, tab2, tab3 = st.tabs([
                "📊 " + ui_text.get("performance_comparison", "Performance Comparison"),
                "🗺️ " + ui_text.get("all_assets_heatmap", "All Assets Heatmap"),
                "🥧 " + ui_text.get("sample_portfolio", "Sample Portfolio")
            ])
            
            with tab1:
                # Performance comparison
                comparison_chart = create_performance_comparison_chart(asset_data, selected_assets, ui_text)
                if comparison_chart:
                    st.plotly_chart(comparison_chart, use_container_width=True)
                    
                    # Comparison table
                    st.markdown("#### " + ui_text.get("performance_comparison_table", "Performance Comparison Table"))
                    create_comparison_table_with_dates(asset_data, selected_assets, ui_text)
                else:
                    st.info(ui_text.get("select_two_assets", "📊 Select at least 2 assets to compare"))
            
            with tab2:
                # Heatmap
                try:
                    heatmap_fig = create_scenario_heatmap(asset_data, ui_text)
                    if heatmap_fig:
                        st.plotly_chart(heatmap_fig, use_container_width=True)
                        st.caption(ui_text.get("green_positive", "💡 Green = Positive performance, Red = Negative performance"))
                    else:
                        st.info("📊 Heatmap data not available")
                except Exception as e:
                    st.error(f"Error creating heatmap: {e}")
            
            with tab3:
                # Sample allocation
                try:
                    pie_fig = create_allocation_pie()
                    st.plotly_chart(pie_fig, use_container_width=True)
                    st.caption(ui_text.get("educational_example", "💡 This is just an educational example - not investment advice"))
                except Exception as e:
                    st.error(f"Error creating allocation chart: {e}")
                
        else:
            tab1, tab2 = st.tabs([
                "🗺️ " + ui_text.get("all_assets_heatmap", "All Assets Heatmap"),
                "🥧 " + ui_text.get("sample_portfolio", "Sample Portfolio")
            ])
            
            with tab1:
                # Heatmap
                try:
                    heatmap_fig = create_scenario_heatmap(asset_data, ui_text)
                    if heatmap_fig:
                        st.plotly_chart(heatmap_fig, use_container_width=True)
                        st.caption(ui_text.get("green_positive", "💡 Green = Positive performance, Red = Negative performance"))
                    else:
                        st.info("📊 Heatmap data not available")
                except Exception as e:
                    st.error(f"Error creating heatmap: {e}")
            
            with tab2:
                # Sample allocation
                try:
                    pie_fig = create_allocation_pie()
                    st.plotly_chart(pie_fig, use_container_width=True)
                    st.caption(ui_text.get("educational_example", "💡 This is just an educational example - not investment advice"))
                except Exception as e:
                    st.error(f"Error creating allocation chart: {e}")
        
        st.markdown("---")
        
        # Educational summary with enhanced formatting
        st.subheader(ui_text["summary_header"])
        
        summary_text = f"""
        ### {ui_text.get('key_takeaways', '🎯 Key Takeaways for')} {selected_asset}
        
        **{selected_asset}** rappresenta un asset con caratteristiche specifiche che lo rendono adatto 
        a determinati obiettivi di investimento. La sua performance varia significativamente in base 
        agli scenari macroeconomici, rendendo importante comprenderne il comportamento nel contesto 
        di un portafoglio diversificato.
        
        #### {ui_text.get('key_points', '📚 Punti chiave da ricordare:')}
        - **{ui_text.get('diversification_key', '🎯 Diversificazione è fondamentale')}**
        - **{ui_text.get('time_horizon', '⏰ L\'orizzonte temporale influenza la scelta')}**
        - **{ui_text.get('correlations_change', '🔄 Le correlazioni cambiano nei momenti di stress')}**
        - **{ui_text.get('risk_return', '⚖️ Rischio e rendimento vanno sempre valutati insieme')}**
        - **{ui_text.get('past_performance', '📊 Le performance passate non garantiscono risultati futuri')}**
        
        #### {ui_text.get('important_note', '🚨 Importante:')}
        {ui_text.get('educational_purpose', 'Questa analisi è puramente educativa.')}
        """ if language == "Italiano" else f"""
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
    
    elif selected_asset:
        st.error(f"❌ Asset '{selected_asset}' not found in database.")
    else:
        st.info("👈 Please select an asset from the sidebar to begin analysis.")

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

if __name__ == "__main__":
    main()
