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
        height=400,
        xaxis_title="Market Scenarios" if "English" in str(ui_text) else "Scenari di Mercato",
        yaxis_title="Assets"
    )
    
    return fig

def create_allocation_pie():
    """Create sample portfolio allocation pie chart"""
    
    # Sample allocation data
    allocation_data = {
        'Asset': ['Global Equities', 'Government Bonds', 'Emerging Markets', 'REITs', 'Gold', 'Commodities'],
        'Allocation': [50, 25, 10, 8, 4, 3]
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
    
    # App title and description
    st.title(ui_text["title"])
    st.markdown(f"*{ui_text['subtitle']}*")
    st.markdown("---")
    
    # Sidebar for asset selection
    st.sidebar.title(ui_text["sidebar_title"])
    selected_asset = st.sidebar.selectbox(
        ui_text["asset_label"],
        list(asset_data.keys())
    )
    
    # Main content
    if selected_asset:
        asset_info = asset_data[selected_asset]
        
        # Title
        st.header(f"{ui_text['analysis_title']}{selected_asset}")
        
        # Warning disclaimer
        st.warning(ui_text["warning"])
        
        # Description
        st.subheader(ui_text["description_header"])
        st.write(asset_info["descrizione"])
        
        # Two column layout
        col1, col2 = st.columns(2)
        
        with col1:
            # Strengths
            st.subheader(ui_text["strengths_header"])
            for strength in asset_info["punti_forza"]:
                st.write(f"• {strength}")
        
        with col2:
            # Weaknesses
            st.subheader(ui_text["weaknesses_header"])
            for weakness in asset_info["punti_debolezza"]:
                st.write(f"• {weakness}")
        
        st.markdown("---")
        
        # Market scenarios
        st.subheader(ui_text["scenarios_header"])
        
        # Create dataframe for scenarios
        scenarios_df = pd.DataFrame([
            {"Scenario": scenario, "Expected Performance": performance}
            for scenario, performance in asset_info["scenari"].items()
        ])
        
        st.dataframe(scenarios_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Allocation and correlations
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader(ui_text["allocation_header"])
            st.info(asset_info["allocazione_range"])
        
        with col4:
            st.subheader(ui_text["correlations_header"])
            st.info(asset_info["correlazioni"])
        
        st.markdown("---")
        
        # Visualizations
        st.subheader(ui_text["visualization_title"])
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Heatmap
            heatmap_fig = create_scenario_heatmap(asset_data, ui_text)
            st.plotly_chart(heatmap_fig, use_container_width=True)
        
        with viz_col2:
            # Sample allocation
            pie_fig = create_allocation_pie()
            st.plotly_chart(pie_fig, use_container_width=True)
        
        st.markdown("---")
        
        # Educational summary
        st.subheader(ui_text["summary_header"])
        
        summary_text = f"""
        **{selected_asset}** rappresenta un asset con caratteristiche specifiche che lo rendono adatto 
        a determinati obiettivi di investimento. La sua performance varia significativamente in base 
        agli scenari macroeconomici, rendendo importante comprenderne il comportamento nel contesto 
        di un portafoglio diversificato.
        
        **Punti chiave da ricordare:**
        - Diversificazione è fondamentale
        - L'orizzonte temporale influenza la scelta degli asset
        - Le correlazioni cambiano nei momenti di stress
        - Mai investire tutto in un singolo asset
        """ if language == "Italiano" else f"""
        **{selected_asset}** represents an asset with specific characteristics that make it suitable 
        for certain investment objectives. Its performance varies significantly based on macroeconomic 
        scenarios, making it important to understand its behavior in the context of a diversified portfolio.
        
        **Key points to remember:**
        - Diversification is fundamental
        - Time horizon influences asset selection
        - Correlations change during stress periods
        - Never invest everything in a single asset
        """
        
        st.write(summary_text)

if __name__ == "__main__":
    main()
