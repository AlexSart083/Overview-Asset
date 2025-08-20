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
            "Minore volatilità rispetto al mercato generale",
            "Migliore resistenza nelle recessioni",
            "Qualità gestionale superiore",
            "Crescita sostenibile degli utili",
            "Bilanci solidi"
        ],
        "punti_debolezza": [
            "Valutazioni spesso elevate",
            "Possibile underperformance in mercati speculativi",
            "Crescita potenzialmente più lenta",
            "Concentrazione settoriale (tech, healthcare)",
            "Sensibilità ai tassi di interesse"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva ma moderata (+6-10% annuo)",
            "Recessione": "Outperformance relativa (-5-15%)",
            "Inflazione elevata": "Performance relativamente buona",
            "Politiche restrittive": "Pressione moderata",
            "Politiche espansive": "Benefici modesti"
        },
        "allocazione_range": "15-30% come componente core difensiva",
        "correlazioni": "Correlazione moderata con azioni globali, correlazione negativa con volatilità"
    },

    "Azioni Value": {
        "descrizione": "Strategia che investe in azioni considerate sottovalutate dal mercato rispetto ai loro fondamentali, spesso con P/E bassi e rendimenti da dividendi elevati.",
        "performance_storica": {
            "20_anni": "6.2%",
            "10_anni": "8.9%",
            "5_anni": "11.5%",
            "1_anno": "13.7%",
            "indice_riferimento": "MSCI World Value Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Potenziale di recupero di valore",
            "Valutazioni attraenti",
            "Rendimenti da dividendi spesso elevati",
            "Performance storicamente solida nel lungo periodo",
            "Protezione contro bolle speculative"
        ],
        "punti_debolezza": [
            "Possibili 'value traps'",
            "Underperformance prolungata possibile",
            "Esposizione a settori in declino",
            "Sensibilità ai cicli economici",
            "Crescita limitata"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva (+8-14% annuo)",
            "Recessione": "Performance negativa ma migliore del growth (-10-20%)",
            "Inflazione elevata": "Performance generalmente positiva",
            "Politiche restrittive": "Benefici relativi",
            "Politiche espansive": "Underperformance vs growth"
        },
        "allocazione_range": "15-35% come componente core contrarian",
        "correlazioni": "Correlazione moderata con azioni globali, inversa con growth"
    },

    "Azioni Minimum Volatility": {
        "descrizione": "Strategia che seleziona azioni con la minore volatilità storica, mirando a ridurre il rischio complessivo del portafoglio azionario.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "9.4%",
            "5_anni": "11.2%",
            "1_anno": "10.8%",
            "indice_riferimento": "MSCI World Minimum Volatility Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Volatilità significativamente ridotta",
            "Migliore risk-adjusted return",
            "Outperformance in mercati ribassisti",
            "Approccio sistematico alla riduzione del rischio",
            "Drawdown contenuti"
        ],
        "punti_debolezza": [
            "Underperformance in mercati fortemente rialzisti",
            "Possibile concentrazione settoriale (utilities, staples)",
            "Costi di gestione più elevati",
            "Rendimenti potenzialmente più bassi nel lungo termine"
        ],
        "scenari": {
            "Crescita economica": "Performance moderata (+4-8% annuo)",
            "Recessione": "Outperformance significativa (-5-12%)",
            "Inflazione elevata": "Performance difensiva moderata",
            "Politiche restrittive": "Resilienza superiore",
            "Politiche espansive": "Underperformance relativa"
        },
        "allocazione_range": "10-25% per riduzione del rischio azionario",
        "correlazioni": "Correlazione positiva ma ridotta con azioni globali"
    },

    "Azioni Small Cap": {
        "descrizione": "Investimenti in aziende a piccola capitalizzazione con maggiore potenziale di crescita ma anche maggiore rischio e volatilità.",
        "performance_storica": {
            "20_anni": "8.2%",
            "10_anni": "11.8%",
            "5_anni": "13.4%",
            "1_anno": "15.2%",
            "indice_riferimento": "MSCI World Small Cap Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Maggiore potenziale di crescita",
            "Possibilità di scoprire aziende prima del mercato",
            "Minore copertura analisti (inefficienze)",
            "Maggiore agilità gestionale",
            "Diversificazione rispetto alle large cap"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Liquidità inferiore",
            "Maggiore rischio di fallimento",
            "Sensibilità ai cicli economici",
            "Costi di transazione più elevati"
        ],
        "scenari": {
            "Crescita economica": "Outperformance significativa (+12-20% annuo)",
            "Recessione": "Underperformance marcata (-30-45%)",
            "Inflazione elevata": "Performance molto variabile",
            "Politiche restrittive": "Pressione significativa",
            "Politiche espansive": "Forte supporto"
        },
        "allocazione_range": "5-15% come componente satellite ad alto rischio/rendimento",
        "correlazioni": "Alta correlazione con azioni globali ma amplificata"
    },

    "Mercati Emergenti": {
        "descrizione": "Azioni di aziende localizzate in paesi in via di sviluppo con economie in rapida crescita.",
        "performance_storica": {
            "20_anni": "4.3%",
            "10_anni": "6.1%",
            "5_anni": "5.6%",
            "1_anno": "15.9%",
            "indice_riferimento": "MSCI Emerging Markets Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
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

    "Azionario High Dividend": {
        "descrizione": "Strategia che investe in azioni di società che distribuiscono dividendi elevati e sostenibili, spesso società mature con flussi di cassa stabili.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "9.2%",
            "5_anni": "10.4%",
            "1_anno": "11.8%",
            "indice_riferimento": "MSCI World High Dividend Yield Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Reddito corrente elevato e regolare",
            "Minore volatilità rispetto al mercato generale",
            "Protezione parziale nei mercati ribassisti",
            "Potenziale crescita dei dividendi nel tempo",
            "Disciplina gestionale delle aziende"
        ],
        "punti_debolezza": [
            "Crescita del capitale limitata",
            "Concentrazione settoriale (utilities, REIT, energia)",
            "Sensibilità ai tassi di interesse",
            "Rischio di taglio dividendi in crisi",
            "Possibile value trap"
        ],
        "scenari": {
            "Crescita economica": "Performance moderatamente positiva (+5-9% annuo)",
            "Recessione": "Performance negativa ma limitata (-8-15%)",
            "Inflazione elevata": "Performance mista (utilities positive, altri settori pressione)",
            "Politiche restrittive": "Pressione negativa per competizione con bond",
            "Politiche espansive": "Performance positiva per search for yield"
        },
        "allocazione_range": "15-30% per investitori orientati al reddito",
        "correlazioni": "Correlazione moderata con azioni, correlazione negativa con tassi di interesse"
    }
}calcolo": "Dati al 31 Dicembre 2024"
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
