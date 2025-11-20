# bond_spread_table.py
"""
Bond Credit Spread Table by Maturity and Rating
Educational tool showing typical spread ranges for different bond categories
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Spread data in basis points (bps)
SPREAD_TABLE_DATA = {
    'Scadenza': ['1 Anno', '3 Anni', '5 Anni', '7 Anni', '10 Anni', '20 Anni'],
    'Governativo': ['0-10', '15-40', '25-55', '45-85', '50-100', '100-200'],
    'Corporate IG': ['10-20', '30-60', '50-90', '90-130', '100-160', '130-250'],
    'Corporate BBB': ['20-40', '50-100', '80-130', '120-180', '140-220', '200-300+'],
    'High Yield': ['50-100', '100-250', '150-350', '250-550', '300-650', '500-800+']
}

# Numeric midpoints for visualization
SPREAD_MIDPOINTS = {
    'Scadenza': [1, 3, 5, 7, 10, 20],
    'Governativo': [5, 27.5, 40, 65, 75, 150],
    'Corporate IG': [15, 45, 70, 110, 130, 190],
    'Corporate BBB': [30, 75, 105, 150, 180, 250],
    'High Yield': [75, 175, 250, 400, 475, 650]
}

def render_spread_table_tab(ui_text):
    """Render the bond spread table tab with educational content"""
    
    is_italian = "italian" in ui_text.get("language", "").lower() or ui_text.get("language", "") == "Italiano"
    
    if is_italian:
        st.markdown("## 📊 Spread Creditizi per Scadenza")
        st.markdown("*Range tipici degli spread obbligazionari in basis points (bps) rispetto ai tassi risk-free*")
    else:
        st.markdown("## 📊 Credit Spreads by Maturity")
        st.markdown("*Typical bond spread ranges in basis points (bps) over risk-free rates*")
    
    # Educational content
    display_spread_educational_content(is_italian)
    
    st.markdown("---")
    
    # Main table display
    display_spread_table(is_italian)
    
    st.markdown("---")
    
    # Visualization
    display_spread_visualization(is_italian)
    
    # Additional context
    display_spread_context(is_italian)


def display_spread_educational_content(is_italian):
    """Display educational content about credit spreads"""
    
    if is_italian:
        with st.expander("📚 Cosa sono gli Spread Creditizi?", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                #### 📏 Definizione di Spread
                
                Lo **spread creditizio** è il rendimento aggiuntivo che un'obbligazione offre rispetto a un titolo di stato privo di rischio con la stessa scadenza.
                
                **Espresso in:**
                - Basis points (bps)
                - 100 bps = 1%
                
                **Esempio pratico:**
                - BTP 10 anni: 3.5%
                - Corporate BBB 10 anni: 5.3%
                - Spread = 180 bps (1.8%)
                
                **Fattori che influenzano lo spread:**
                - Rating creditizio dell'emittente
                - Scadenza del bond
                - Liquidità del mercato
                - Condizioni economiche generali
                """)
            
            with col2:
                st.markdown("""
                #### 🏛️ Categorie di Rating
                
                **Governativo (AAA/AA):**
                - Titoli di stato di paesi con rating elevato
                - Spread minimo, massima sicurezza
                - Benchmark: Bund tedesco, Treasury USA
                
                **Corporate Investment Grade (IG):**
                - Rating da AAA a A-
                - Aziende solide con basso rischio default
                - Spread moderato
                
                **Corporate BBB:**
                - Ultimo gradino dell'Investment Grade
                - Rischio moderato ma ancora accettabile
                - Spread più elevato
                
                **High Yield (BB e inferiori):**
                - "Junk bonds" o obbligazioni speculative
                - Alto rischio di default
                - Spread elevati per compensare il rischio
                """)
    else:
        with st.expander("📚 What are Credit Spreads?", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                #### 📏 Spread Definition
                
                A **credit spread** is the additional yield a bond offers over a risk-free government security with the same maturity.
                
                **Expressed in:**
                - Basis points (bps)
                - 100 bps = 1%
                
                **Practical example:**
                - 10Y Treasury: 3.5%
                - 10Y Corporate BBB: 5.3%
                - Spread = 180 bps (1.8%)
                
                **Factors affecting spreads:**
                - Issuer's credit rating
                - Bond maturity
                - Market liquidity
                - General economic conditions
                """)
            
            with col2:
                st.markdown("""
                #### 🏛️ Rating Categories
                
                **Government (AAA/AA):**
                - Government bonds from highly-rated countries
                - Minimum spread, maximum safety
                - Benchmark: German Bunds, US Treasuries
                
                **Corporate Investment Grade (IG):**
                - Rating from AAA to A-
                - Solid companies with low default risk
                - Moderate spread
                
                **Corporate BBB:**
                - Lowest Investment Grade tier
                - Moderate but acceptable risk
                - Higher spread
                
                **High Yield (BB and below):**
                - "Junk bonds" or speculative bonds
                - High default risk
                - High spreads to compensate for risk
                """)


def display_spread_table(is_italian):
    """Display the main spread table with color coding"""
    
    if is_italian:
        st.markdown("### 📋 Tabella Spread per Scadenza e Rating")
        st.markdown("**Valori in basis points (bps) - Range tipici in condizioni di mercato normali**")
    else:
        st.markdown("### 📋 Spread Table by Maturity and Rating")
        st.markdown("**Values in basis points (bps) - Typical ranges under normal market conditions**")
    
    df = pd.DataFrame(SPREAD_TABLE_DATA)
    
    # Color coding function
    def color_spread_cells(val):
        if val in ['1 Anno', '3 Anni', '5 Anni', '7 Anni', '10 Anni', '20 Anni']:
            return 'background-color: #f0f0f0; font-weight: bold'
        
        # Extract numeric values for coloring
        try:
            # Get the first number from the range
            first_num = int(val.split('-')[0].replace('+', ''))
            
            if first_num <= 20:
                return 'background-color: #90EE90'  # Green - Low risk
            elif first_num <= 60:
                return 'background-color: #FFFFCC'  # Yellow - Moderate
            elif first_num <= 150:
                return 'background-color: #FFE4B5'  # Orange - Medium-high
            else:
                return 'background-color: #FFB6C1'  # Red - High risk
        except:
            return ''
    
    # Apply styling
    styled_df = df.style.applymap(color_spread_cells)
    
    # Display table
    st.dataframe(styled_df, use_container_width=True, height=280)
    
    # Legend
    if is_italian:
        st.markdown("**Legenda colori:**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("🟢 **0-20 bps**: Rischio minimo")
        with col2:
            st.markdown("🟡 **21-60 bps**: Rischio basso")
        with col3:
            st.markdown("🟠 **61-150 bps**: Rischio moderato")
        with col4:
            st.markdown("🔴 **>150 bps**: Rischio elevato")
    else:
        st.markdown("**Color legend:**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("🟢 **0-20 bps**: Minimal risk")
        with col2:
            st.markdown("🟡 **21-60 bps**: Low risk")
        with col3:
            st.markdown("🟠 **61-150 bps**: Moderate risk")
        with col4:
            st.markdown("🔴 **>150 bps**: High risk")


def display_spread_visualization(is_italian):
    """Display spread visualization chart"""
    
    if is_italian:
        st.markdown("### 📈 Visualizzazione Spread per Categoria")
    else:
        st.markdown("### 📈 Spread Visualization by Category")
    
    # Create line chart
    fig = go.Figure()
    
    categories = ['Governativo', 'Corporate IG', 'Corporate BBB', 'High Yield']
    colors = ['#2E7D32', '#1976D2', '#F57C00', '#C62828']
    
    for i, category in enumerate(categories):
        fig.add_trace(go.Scatter(
            x=SPREAD_MIDPOINTS['Scadenza'],
            y=SPREAD_MIDPOINTS[category],
            mode='lines+markers',
            name=category,
            line=dict(color=colors[i], width=3),
            marker=dict(size=10),
            hovertemplate=f"<b>{category}</b><br>" +
                         "Scadenza: %{x} anni<br>" +
                         "Spread: %{y} bps<extra></extra>"
        ))
    
    title = "Spread Creditizi per Scadenza (valori medi)" if is_italian else "Credit Spreads by Maturity (mid values)"
    xaxis_title = "Scadenza (anni)" if is_italian else "Maturity (years)"
    yaxis_title = "Spread (bps)" if is_italian else "Spread (bps)"
    
    fig.update_layout(
        title=dict(text=title, x=0.5),
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        height=450,
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(
            showgrid=True, 
            gridcolor='lightgray',
            tickvals=[1, 3, 5, 7, 10, 20]
        ),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)


def display_spread_context(is_italian):
    """Display additional context about spread interpretation"""
    
    if is_italian:
        st.info("""
        **📚 Come Interpretare la Tabella:**
        
        - **Scadenze più lunghe = Spread più alti**: Il rischio aumenta con il tempo
        - **Rating più basso = Spread più alto**: Compenso per il maggior rischio di default
        - **Condizioni di mercato**: In periodi di stress gli spread si allargano significativamente
        - **Ciclo economico**: Gli spread High Yield sono particolarmente sensibili alle recessioni
        
        ⚠️ **Nota**: I valori mostrati sono range tipici in condizioni normali. Durante crisi di mercato 
        (es. 2008, 2020) gli spread possono aumentare di 2-5 volte.
        """)
        
        with st.expander("💡 Applicazioni Pratiche", expanded=False):
            st.markdown("""
            #### Come usare questa tabella:
            
            **1. Valutazione del rendimento:**
            - Se un bond offre uno spread inferiore alla media → potrebbe essere sopravvalutato
            - Se offre uno spread superiore → verificare se c'è un rischio nascosto
            
            **2. Confronto tra emittenti:**
            - Confronta bond con stessa scadenza ma rating diverso
            - Valuta se lo spread aggiuntivo giustifica il rischio
            
            **3. Timing di mercato:**
            - Spread compressi = mercato ottimista (risk-on)
            - Spread ampliati = mercato pessimista (risk-off)
            
            **4. Costruzione portafoglio:**
            - Diversifica tra diverse categorie di rating
            - Considera il tuo orizzonte temporale e tolleranza al rischio
            """)
    else:
        st.info("""
        **📚 How to Interpret the Table:**
        
        - **Longer maturities = Higher spreads**: Risk increases over time
        - **Lower rating = Higher spread**: Compensation for higher default risk
        - **Market conditions**: During stress periods, spreads widen significantly
        - **Economic cycle**: High Yield spreads are particularly sensitive to recessions
        
        ⚠️ **Note**: Values shown are typical ranges under normal conditions. During market crises 
        (e.g., 2008, 2020) spreads can increase 2-5 times.
        """)
        
        with st.expander("💡 Practical Applications", expanded=False):
            st.markdown("""
            #### How to use this table:
            
            **1. Yield evaluation:**
            - If a bond offers a spread below average → might be overvalued
            - If it offers a higher spread → check for hidden risks
            
            **2. Issuer comparison:**
            - Compare bonds with same maturity but different ratings
            - Evaluate if the additional spread justifies the risk
            
            **3. Market timing:**
            - Compressed spreads = optimistic market (risk-on)
            - Wide spreads = pessimistic market (risk-off)
            
            **4. Portfolio construction:**
            - Diversify across different rating categories
            - Consider your time horizon and risk tolerance
            """)
