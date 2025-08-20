# data/italian/equity_assets_it.py
"""
Dati asset azionari e strategie azionarie in italiano
Include tutte le strategie di investimento azionario e mercati emergenti
"""

EQUITY_ASSETS_IT = {
    "Azioni Globali (Market Cap)": {
        "descrizione": "Investimenti azionari diversificati a livello mondiale ponderati per capitalizzazione di mercato, che rappresentano quote di proprietà nelle maggiori aziende quotate globalmente.",
        "performance_storica": {
            "20_anni": "7.0%",
            "10_anni": "10.6%",
            "5_anni": "14.4%",
            "1_anno": "14.9%",
            "indice_riferimento": "MSCI World Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
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

    "Azioni Momentum": {
        "descrizione": "Strategia che investe in azioni che hanno mostrato performance positive nel recente passato, sfruttando la tendenza dei titoli vincenti a continuare a sovraperformare nel breve-medio termine.",
        "performance_storica": {
            "20_anni": "8.5%",
            "10_anni": "12.8%",
            "5_anni": "16.2%",
            "1_anno": "18.5%",
            "indice_riferimento": "MSCI World Momentum Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Sfrutta trend di mercato consolidati",
            "Potenziale outperformance in mercati rialzisti",
            "Adattamento dinamico alle condizioni di mercato",
            "Disciplina sistematica nell'approccio"
        ],
        "punti_debolezza": [
            "Alta volatilità",
            "Rischio di inversioni improvvise di trend",
            "Maggiori costi di transazione per rotazione",
            "Performance negativa nei mercati laterali",
            "Rischio di acquistare sui massimi"
        ],
        "scenari": {
            "Crescita economica": "Performance molto positiva (+12-18% annuo)",
            "Recessione": "Performance molto negativa (-25-35%)",
            "Inflazione elevata": "Performance mista, dipende dai settori",
            "Politiche restrittive": "Pressione negativa significativa",
            "Politiche espansive": "Forte supporto positivo"
        },
        "allocazione_range": "10-25% come componente satellite tattica",
        "correlazioni": "Alta correlazione con azioni globali, amplifica i movimenti di mercato"
    },

    "Azioni Quality": {
        "descrizione": "Investimenti in aziende con fondamentali solidi: alta redditività, bassa leva finanziaria, crescita stabile degli utili e gestione efficiente.",
        "performance_storica": {
            "20_anni": "7.8%",
            "10_anni": "11.2%",
            "5_anni": "13.8%",
            "1_anno": "12.4%",
            "indice_riferimento": "MSCI World Quality Index",
            "data_
