# bond_calculator.py
"""
Bond Duration and Convexity Calculator
Interactive tool for analyzing bond price sensitivity to interest rate changes
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Tabella di riferimento con duration e convessità predefinite
DURATION_TABLE_DATA = {
    'Variazione Tassi': ['+3.0%', '+2.5%', '+2.0%', '+1.5%', '+1.0%', '+0.5%', '0.0%', 
                         '-0.5%', '-1.0%', '-1.5%', '-2.0%', '-2.5%', '-3.0%'],
    'Duration 1 anno': ['-2.9%', '-2.4%', '-1.9%', '-1.5%', '-1.0%', '-0.5%', '0.0%', 
                        '+0.5%', '+1.0%', '+1.5%', '+2.0%', '+2.6%', '+3.1%'],
    'Duration 3 anni': ['-8.3%', '-7.0%', '-5.6%', '-4.3%', '-2.9%', '-1.5%', '0.0%', 
                        '+1.5%', '+3.1%', '+4.7%', '+6.4%', '+8.0%', '+9.7%'],
    'Duration 5 anni': ['-13.5%', '-11.4%', '-9.2%', '-7.0%', '-4.7%', '-2.4%', '0.0%', 
                        '+2.6%', '+5.3%', '+8.0%', '+10.8%', '+13.6%', '+16.5%'],
    'Duration 7 anni': ['-18.4%', '-15.5%', '-12.5%', '-9.4%', '-6.4%', '-3.3%', '0.0%', 
                        '+3.7%', '+7.6%', '+11.6%', '+15.5%', '+19.5%', '+23.6%'],
    'Duration 10 anni': ['-26.3%', '-22.2%', '-18.0%', '-13.6%', '-9.3%', '-4.8%', '0.0%', 
                         '+5.2%', '+10.7%', '+16.4%', '+22.0%', '+27.8%', '+33.8%']
}

# Parametri di convessità per ciascuna duration
CONVEXITY_PARAMS = {
    '1 anno': {'duration': 1.0, 'convexity': 1.5},
    '3 anni': {'duration': 3.0, 'convexity': 12.0},
    '5 anni': {'duration': 5.0, 'convexity': 35.0},
    '7 anni': {'duration': 7.0, 'convexity': 70.0},
    '10 anni': {'duration': 10.0, 'convexity': 130.0}
}

def calculate_bond_price_change(duration, convexity, rate_change):
    """
    Calcola la variazione percentuale del prezzo dell'obbligazione
    Formula: ΔP/P ≈ -Duration × ΔR + ½ × Convessità × (ΔR)²
    
    Args:
        duration: Duration modificata del bond
        convexity: Convessità del bond
        rate_change: Variazione dei tassi (in decimale, es. 0.01 per +1%)
    
    Returns:
        Variazione percentuale del prezzo
    """
    duration_effect = -duration * rate_change
    convexity_effect = 0.5 * convexity * (rate_change ** 2)
    total_change = duration_effect + convexity_effect
    return total_change * 100  # Converti in percentuale

def create_sensitivity_table(duration, convexity, language='italiano'):
    """Crea tabella di sensibilità per diversi scenari di tasso"""
    
    rate_changes = [3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0]
    
    results = []
    for rc in rate_changes:
        rate_change_decimal = rc / 100
        price_change = calculate_bond_price_change(duration, convexity, rate_change_decimal)
        
        # Determina il colore in base al risultato
        if price_change > 5:
            color = '🟢'
        elif price_change > 0:
            color = '🟡'
        elif price_change > -5:
            color = '🟠'
        else:
            color = '🔴'
        
        results.append({
            'Variazione Tassi': f"{rc:+.1f}%",
            'Impatto Duration': f"{-duration * rate_change_decimal * 100:.2f}%",
            'Effetto Convessità': f"{0.5 * convexity * (rate_change_decimal ** 2) * 100:.2f}%",
            'Variazione Prezzo': f"{price_change:.2f}%",
            'Trend': color
        })
    
    return pd.DataFrame(results)

def create_comparison_chart(duration, convexity):
    """Crea grafico che confronta effetto duration vs effetto completo (duration + convessità)"""
    
    rate_changes = np.linspace(-3, 3, 100)
    
    # Solo duration
    duration_only = [-duration * (rc/100) * 100 for rc in rate_changes]
    
    # Duration + Convessità
    duration_convexity = [calculate_bond_price_change(duration, convexity, rc/100) for rc in rate_changes]
    
    fig = go.Figure()
    
    # Linea duration pura
    fig.add_trace(go.Scatter(
        x=rate_changes,
        y=duration_only,
        mode='lines',
        name='Solo Duration (lineare)',
        line=dict(color='red', dash='dash', width=2),
        hovertemplate='Tasso: %{x:+.2f}%<br>Variazione: %{y:.2f}%<extra></extra>'
    ))
    
    # Linea duration + convessità
    fig.add_trace(go.Scatter(
        x=rate_changes,
        y=duration_convexity,
        mode='lines',
        name='Duration + Convessità',
        line=dict(color='green', width=3),
        hovertemplate='Tasso: %{x:+.2f}%<br>Variazione: %{y:.2f}%<extra></extra>'
    ))
    
    # Aggiungi area tra le curve per mostrare benefit della convessità
    fig.add_trace(go.Scatter(
        x=rate_changes.tolist() + rate_changes[::-1].tolist(),
        y=duration_convexity + duration_only[::-1],
        fill='toself',
        fillcolor='rgba(0,255,0,0.1)',
        line=dict(color='rgba(255,255,255,0)'),
        showlegend=False,
        name='Beneficio Convessità',
        hoverinfo='skip'
    ))
    
    fig.update_layout(
        title=f'📊 Impatto Variazione Tassi sul Prezzo del Bond<br><sub>Duration: {duration:.1f} anni | Convessità: {convexity:.0f}</sub>',
        xaxis_title='Variazione Tassi d\'Interesse (%)',
        yaxis_title='Variazione Prezzo Bond (%)',
        height=500,
        hovermode='x unified',
        plot_bgcolor='rgba(240,240,240,0.3)',
        xaxis=dict(
            showgrid=True, 
            gridcolor='lightgray',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black'
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='lightgray',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black'
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255,255,255,0.8)"
        )
    )
    
    # Aggiungi annotazioni
    fig.add_annotation(
        x=1.5, y=duration_convexity[int(len(rate_changes) * 0.75)],
        text="Beneficio della<br>Convessità ✓",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="green",
        font=dict(size=10, color="green"),
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="green",
        borderwidth=1
    )
    
    return fig

def create_3d_surface_chart():
    """Crea grafico 3D che mostra l'effetto combinato di duration e variazione tassi"""
    
    durations = np.linspace(1, 10, 30)
    rate_changes = np.linspace(-3, 3, 30)
    
    D, R = np.meshgrid(durations, rate_changes)
    
    # Calcola la variazione del prezzo per ogni combinazione
    # Usa convessità approssimativa: convessity ≈ duration²
    Z = -D * R + 0.5 * (D ** 2) * (R ** 2)
    
    fig = go.Figure(data=[go.Surface(
        x=D,
        y=R,
        z=Z,
        colorscale='RdYlGn',
        colorbar=dict(title='Variazione<br>Prezzo (%)')
    )])
    
    fig.update_layout(
        title='🎯 Superficie di Sensibilità: Duration vs Variazione Tassi',
        scene=dict(
            xaxis_title='Duration (anni)',
            yaxis_title='Variazione Tassi (%)',
            zaxis_title='Variazione Prezzo (%)',
            camera=dict(
                eye=dict(x=1.5, y=-1.5, z=1.2)
            )
        ),
        height=600
    )
    
    return fig

def display_reference_table():
    """Mostra la tabella di riferimento completa"""
    
    st.markdown("### 📋 Tabella di Riferimento Completa")
    st.markdown("**Variazione del prezzo delle obbligazioni in base a duration e variazione dei tassi**")
    
    df = pd.DataFrame(DURATION_TABLE_DATA)
    
    # Funzione per colorare le celle
    def color_values(val):
        if val == '0.0%':
            return 'background-color: #f0f0f0'
        try:
            num_val = float(val.replace('%', '').replace('+', ''))
            if num_val > 10:
                return 'background-color: #90EE90'  # Verde chiaro
            elif num_val > 0:
                return 'background-color: #FFFFCC'  # Giallo chiaro
            elif num_val > -10:
                return 'background-color: #FFE4B5'  # Arancio chiaro
            else:
                return 'background-color: #FFB6C1'  # Rosso chiaro
        except:
            return ''
    
    styled_df = df.style.applymap(color_values, subset=df.columns[1:])
    
    st.dataframe(styled_df, use_container_width=True, height=500)
    
    # Legenda
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("🟢 **> +10%**: Forte guadagno")
    with col2:
        st.markdown("🟡 **0% a +10%**: Guadagno moderato")
    with col3:
        st.markdown("🟠 **-10% a 0%**: Perdita moderata")
    with col4:
        st.markdown("🔴 **< -10%**: Forte perdita")

def display_educational_content():
    """Mostra contenuti educativi su duration e convessità"""
    
    with st.expander("📚 Cosa sono Duration e Convessità?", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 📏 Duration (Durata)
            
            La **duration** misura la sensibilità del prezzo di un'obbligazione alle variazioni dei tassi d'interesse.
            
            **Caratteristiche:**
            - Misurata in anni
            - Approssimazione lineare della sensibilità
            - Relazione inversa: ↑ tassi = ↓ prezzi
            - Duration più alta = maggiore sensibilità
            
            **Formula base:**
            ```
            ΔPrezzo ≈ -Duration × ΔTassi
            ```
            
            **Esempio pratico:**
            - Bond con duration 5 anni
            - Tassi aumentano del +1%
            - Prezzo diminuisce circa -5%
            """)
        
        with col2:
            st.markdown("""
            #### 🔄 Convessità
            
            La **convessità** misura la curvatura della relazione prezzo-tassi, correggendo l'approssimazione lineare della duration.
            
            **Caratteristiche:**
            - Sempre positiva per bond standard
            - Beneficio per l'investitore
            - Più importante per grandi variazioni tassi
            - Maggiore per duration elevate
            
            **Formula completa:**
            ```
            ΔPrezzo ≈ -Duration × ΔTassi + 
                       ½ × Convessità × (ΔTassi)²
            ```
            
            **Vantaggi:**
            - Riduce le perdite quando i tassi salgono
            - Aumenta i guadagni quando i tassi scendono
            - Effetto "ammortizzatore" in alta volatilità
            """)
    
    with st.expander("💡 Scenari Pratici ed Esempi", expanded=False):
        st.markdown("""
        ### 📊 Scenari di Mercato
        
        #### Scenario 1: Rialzo dei Tassi (+2%)
        
        | Duration | Solo Duration | Duration + Convessità | Beneficio Convessità |
        |----------|---------------|----------------------|---------------------|
        | 3 anni   | -6.0%        | -5.6%                | +0.4%              |
        | 7 anni   | -14.0%       | -12.5%               | +1.5%              |
        | 10 anni  | -20.0%       | -18.0%               | +2.0%              |
        
        ⚠️ **Perdite minori grazie alla convessità**
        
        #### Scenario 2: Ribasso dei Tassi (-2%)
        
        | Duration | Solo Duration | Duration + Convessità | Beneficio Convessità |
        |----------|---------------|----------------------|---------------------|
        | 3 anni   | +6.0%        | +6.4%                | +0.4%              |
        | 7 anni   | +14.0%       | +15.5%               | +1.5%              |
        | 10 anni  | +20.0%       | +22.0%               | +2.0%              |
        
        ✅ **Guadagni maggiori grazie alla convessità**
        
        ---
        
        ### 🎯 Quando la Convessità è Cruciale:
        
        1. **Alta volatilità dei tassi**: L'effetto è proporzionale al quadrato della variazione
        2. **Bond a lunga duration**: L'effetto cresce con la duration
        3. **Grandi movimenti di mercato**: Divergenze significative vs solo duration
        4. **Gestione del rischio**: Protezione automatica in scenari estremi
        
        ---
        
        ### 📈 Implicazioni per il Portfolio:
        
        - **Bond lunghi (>7 anni)**: Massimo beneficio convessità ma alta volatilità
        - **Bond medi (3-7 anni)**: Bilanciamento ottimale rischio/rendimento
        - **Bond corti (<3 anni)**: Stabilità ma minor upside
        - **Mix strategico**: Diversifica per duration per gestire diversi scenari
        """)

def render_bond_calculator_tab(ui_text):
    """Funzione principale per renderizzare il tab del calcolatore"""
    
    st.markdown("## 📐 Calcolatrice Duration e Convessità")
    st.markdown("*Strumento interattivo per analizzare la sensibilità delle obbligazioni alle variazioni dei tassi d'interesse*")
    
    # Mostra contenuto educativo
    display_educational_content()
    
    st.markdown("---")
    
    # Sezione calcolatrice interattiva
    st.markdown("### 🧮 Calcolatrice Interattiva")
    
    calc_col1, calc_col2 = st.columns([2, 3])
    
    with calc_col1:
        st.markdown("#### ⚙️ Parametri del Bond")
        
        # Scelta rapida o personalizzata
        calc_mode = st.radio(
            "Modalità di calcolo:",
            ["📋 Usa Profilo Predefinito", "✏️ Personalizza Parametri"],
            help="Scegli un profilo standard o inserisci parametri personalizzati"
        )
        
        if calc_mode == "📋 Usa Profilo Predefinito":
            preset = st.selectbox(
                "Seleziona Duration:",
                list(CONVEXITY_PARAMS.keys()),
                index=2
            )
            duration = CONVEXITY_PARAMS[preset]['duration']
            convexity = CONVEXITY_PARAMS[preset]['convexity']
            
            st.info(f"**Duration:** {duration:.1f} anni  \n**Convessità:** {convexity:.0f}")
        
        else:
            duration = st.slider(
                "Duration (anni)",
                min_value=0.5,
                max_value=15.0,
                value=5.0,
                step=0.5,
                help="Sensibilità del bond alle variazioni dei tassi"
            )
            
            # Convessità suggerita in base alla duration
            suggested_convexity = duration ** 2 * 1.5
            
            convexity = st.slider(
                "Convessità",
                min_value=1.0,
                max_value=300.0,
                value=min(suggested_convexity, 300.0),
                step=1.0,
                help="Curvatura della relazione prezzo-tassi"
            )
            
            st.info(f"💡 Convessità tipica per duration {duration:.1f} anni: ~{suggested_convexity:.0f}")
        
        # Variazione dei tassi
        st.markdown("#### 📊 Scenario dei Tassi")
        rate_change = st.slider(
            "Variazione tassi d'interesse (%)",
            min_value=-3.0,
            max_value=3.0,
            value=1.0,
            step=0.1,
            help="Variazione attesa dei tassi di mercato"
        )
        
        # Calcola risultati
        price_change = calculate_bond_price_change(duration, convexity, rate_change/100)
        duration_only = -duration * rate_change
        convexity_benefit = price_change - duration_only
        
        # Mostra risultati
        st.markdown("#### 📈 Risultati")
        
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.metric(
                "Effetto Duration",
                f"{duration_only:.2f}%",
                delta=None
            )
        
        with result_col2:
            st.metric(
                "Beneficio Convessità",
                f"{convexity_benefit:.2f}%",
                delta=None,
                delta_color="normal"
            )
        
        with result_col3:
            color = "normal" if price_change >= 0 else "inverse"
            st.metric(
                "Variazione Totale",
                f"{price_change:.2f}%",
                delta=f"{abs(price_change):.2f}%",
                delta_color=color
            )
        
        # Interpretazione
        if price_change > 0:
            st.success(f"✅ **Guadagno:** Il valore del bond aumenta del {price_change:.2f}%")
        else:
            st.error(f"⚠️ **Perdita:** Il valore del bond diminuisce del {abs(price_change):.2f}%")
        
        if abs(convexity_benefit) > 0.1:
            st.info(f"💡 La convessità {'riduce la perdita' if rate_change > 0 else 'aumenta il guadagno'} di {abs(convexity_benefit):.2f}%")
    
    with calc_col2:
        # Grafico di confronto
        comparison_fig = create_comparison_chart(duration, convexity)
        st.plotly_chart(comparison_fig, use_container_width=True)
        
        # Tabella di sensibilità
        st.markdown("#### 📋 Tabella di Sensibilità")
        sensitivity_df = create_sensitivity_table(duration, convexity)
        st.dataframe(sensitivity_df, use_container_width=True, height=400)
    
    st.markdown("---")
    
    # Grafici avanzati
    st.markdown("### 📊 Analisi Avanzata")
    
    tab1, tab2, tab3 = st.tabs([
        "🌐 Superficie 3D",
        "📋 Tabella Completa di Riferimento",
        "📖 Metodologia"
    ])
    
    with tab1:
        st.markdown("**Visualizzazione tridimensionale dell'impatto combinato di duration e variazione tassi**")
        surface_fig = create_3d_surface_chart()
        st.plotly_chart(surface_fig, use_container_width=True)
        
        st.info("""
        💡 **Come leggere il grafico:**
        - **Asse X:** Duration del bond (da 1 a 10 anni)
        - **Asse Y:** Variazione dei tassi (da -3% a +3%)
        - **Asse Z (colore):** Variazione del prezzo del bond
        - **Verde:** Guadagni (tassi in calo)
        - **Rosso:** Perdite (tassi in rialzo)
        """)
    
    with tab2:
        display_reference_table()
        
        st.markdown("""
        ---
        **💾 Parametri utilizzati:**
        
        | Duration | Convessità |
        |----------|-----------|
        | 1 anno   | 1.5       |
        | 3 anni   | 12        |
        | 5 anni   | 35        |
        | 7 anni   | 70        |
        | 10 anni  | 130       |
        
        *Formula applicata: Variazione % ≈ -Duration × ΔTassi + ½ × Convessità × (ΔTassi)²*
        """)
    
    with tab3:
        st.markdown("""
        ### 🔬 Metodologia di Calcolo
        
        #### Formula Completa
        
        La variazione percentuale del prezzo di un'obbligazione è approssimata da:
        
        ```
        ΔP/P ≈ -Duration × ΔR + ½ × Convexity × (ΔR)²
        ```
        
        Dove:
        - **ΔP/P** = Variazione percentuale del prezzo
        - **Duration** = Duration modificata (in anni)
        - **ΔR** = Variazione dei tassi d'interesse (in decimale)
        - **Convexity** = Convessità del bond
        
        ---
        
        #### Componenti
        
        **1. Effetto Duration (Primo Ordine - Lineare)**
        ```
        Effetto Duration = -Duration × ΔR
        ```
        - Approssimazione lineare
        - Valida per piccole variazioni di tassi
        - Relazione inversa (tassi ↑ = prezzo ↓)
        
        **2. Effetto Convessità (Secondo Ordine - Quadratico)**
        ```
        Effetto Convessità = ½ × Convexity × (ΔR)²
        ```
        - Correzione non lineare
        - Sempre positivo (beneficio per l'investitore)
        - Aumenta con il quadrato della variazione
        
        ---
        
        #### Esempi Numerici
        
        **Esempio 1: Bond a 5 anni, tassi +2%**
        ```
        Duration = 5 anni
        Convexity = 35
        ΔR = +0.02 (2%)
        
        Effetto Duration = -5 × 0.02 = -0.10 = -10.0%
        Effetto Convessità = 0.5 × 35 × (0.02)² = 0.007 = +0.7%
        
        Variazione Totale = -10.0% + 0.7% = -9.3%
        ```
        
        **Esempio 2: Bond a 7 anni, tassi -1.5%**
        ```
        Duration = 7 anni
        Convexity = 70
        ΔR = -0.015 (-1.5%)
        
        Effetto Duration = -7 × (-0.015) = +0.105 = +10.5%
        Effetto Convessità = 0.5 × 70 × (0.015)² = 0.008 = +0.8%
        
        Variazione Totale = +10.5% + 0.8% = +11.3%
        ```
        
        ---
        
        #### Assunzioni e Limiti
        
        **Assunzioni:**
        - Movimenti paralleli della curva dei tassi
        - Assenza di opzioni embedded
        - Rendimenti reinvestiti al nuovo tasso
        - Mercato liquido ed efficiente
        
        **Limiti:**
        - Approssimazione valida per variazioni moderate (<3%)
        - Non considera lo spread creditizio
        - Non include effetti fiscali
        - Non tiene conto della liquidità di mercato
        
        **Quando è più accurata:**
        - Bond governativi senza opzioni
        - Variazioni di tassi entro ±2-3%
        - Mercati normali (non stress)
        - Time horizon breve-medio
        
        ---
        
        #### Bibliografia e Approfondimenti
        
        - Fabozzi, F.J. (2021). *Bond Markets, Analysis, and Strategies*
        - Tuckman, B. & Serrat, A. (2011). *Fixed Income Securities*
        - BIS Papers on Duration and Convexity Management
        """)
