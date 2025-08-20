# data/italian/bond_assets_it.py
"""
Dati obbligazioni e titoli a reddito fisso in italiano
Include obbligazioni governative, corporate e strategie obbligazionarie specializzate
"""

BOND_ASSETS_IT = {
    "Obbligazioni 0-1 anni": {
        "descrizione": "Titoli di debito governativi e corporate a brevissimo termine con scadenza entro un anno. I governativi europei offrono massima sicurezza creditizia mentre i corporate offrono spread aggiuntivi ma con rischio di credito superiore.",
        "performance_storica": {
            "20_anni": "2.8%",
            "10_anni": "1.2%",
            "5_anni": "2.1%",
            "1_anno": "4.8%",
            "indice_riferimento": "Euro Short-Term Rate (€STR) / Euro Corporate 0-1Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rischio di tasso di interesse minimo",
            "Alta liquidità (specialmente governativi)",
            "Bassa volatilità",
            "Protezione del capitale (governativi praticamente risk-free)",
            "Reinvestimento frequente ai tassi correnti",
            "Corporate: spread aggiuntivo per extra-rendimento"
        ],
        "punti_debolezza": [
            "Rendimenti molto bassi (specialmente governativi)",
            "Nessuna protezione dall'inflazione se tassi reali negativi",
            "Rischio di reinvestimento",
            "Corporate: rischio di credito e spread risk",
            "Opportunità costo in ambienti di tassi crescenti"
        ],
        "scenari": {
            "Crescita economica": "Governativi: performance stabile ma rendimenti bassi; Corporate: beneficiano da spread tightening",
            "Recessione": "Governativi: outperformance per flight-to-quality; Corporate: sotto pressione per rischio credito",
            "Inflazione elevata": "Performance negativa per tassi reali negativi",
            "Politiche restrittive": "Benefici graduali dal reinvestimento",
            "Politiche espansive": "Performance stabile ma rendimenti in calo"
        },
        "allocazione_range": "10-30% per liquidità e stabilità",
        "correlazioni": "Correlazione molto bassa con azioni, correlazione alta con tassi a breve"
    },

    "Obbligazioni 1-3 anni": {
        "descrizione": "Titoli di debito governativi e corporate a breve termine. I governativi europei offrono il benchmark risk-free, mentre i corporate aggiungono spread creditizio con duration limitata.",
        "performance_storica": {
            "20_anni": "3.2%",
            "10_anni": "1.8%",
            "5_anni": "2.4%",
            "1_anno": "4.2%",
            "indice_riferimento": "Euro Government 1-3Y Index / Euro Corporate 1-3Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rischio di tasso contenuto",
            "Rendimenti superiori al brevissimo termine",
            "Buona liquidità",
            "Volatilità moderata",
            "Diversificazione efficace",
            "Corporate: attractive spread pickup vs governativi"
        ],
        "punti_debolezza": [
            "Sensibilità ai tassi di interesse (limitata ma presente)",
            "Rendimenti ancora limitati per governativi",
            "Corporate: rischio di credito e spread widening risk",
            "Performance negativa con rialzi rapidi dei tassi"
        ],
        "scenari": {
            "Crescita economica": "Governativi: performance moderatamente negativa; Corporate: outperformance per miglioramento credito",
            "Recessione": "Governativi: performance positiva (flight to quality); Corporate: performance negativa per rischio credito",
            "Inflazione elevata": "Performance negativa ma limitata per entrambi",
            "Politiche restrittive": "Pressione negativa contenuta, corporate più vulnerabili",
            "Politiche espansive": "Performance moderatamente positiva"
        },
        "allocazione_range": "15-35% per bilanciamento rischio/rendimento",
        "correlazioni": "Correlazione negativa moderata con azioni"
    },

    "Obbligazioni 3-7 anni": {
        "descrizione": "Titoli di debito governativi e corporate a medio termine. Segmento dove la differenza tra governativi (risk-free rate) e corporate (credit spread) diventa più significativa con l'aumento della duration.",
        "performance_storica": {
            "20_anni": "4.1%",
            "10_anni": "2.8%",
            "5_anni": "1.2%",
            "1_anno": "2.8%",
            "indice_riferimento": "Euro Government 3-7Y Index / Euro Corporate 3-7Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti più interessanti",
            "Sweet spot duration/rendimento",
            "Diversificazione del portafoglio",
            "Liquidità ancora buona",
            "Corporate: spread significativi per extra-rendimento",
            "Potenziali capital gain se tassi scendono"
        ],
        "punti_debolezza": [
            "Sensibilità significativa ai tassi di interesse",
            "Volatilità moderata-alta",
            "Rischio di duration",
            "Corporate: sensibilità al credit cycle e spread volatility",
            "Performance negativa con rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Governativi: performance negativa per aspettative rialzo tassi; Corporate: performance mista (tassi negativi, credit positivo)",
            "Recessione": "Governativi: performance fortemente positiva; Corporate: performance negativa per deterioramento credito",
            "Inflazione elevata": "Performance significativamente negativa per entrambi",
            "Politiche restrittive": "Pressione negativa significativa, corporate doppiamente vulnerabili",
            "Politiche espansive": "Performance positiva, corporate outperformance"
        },
        "allocazione_range": "10-25% per rendimento con rischio controllato",
        "correlazioni": "Correlazione negativa con azioni, alta sensibilità ai tassi"
    },

    "Obbligazioni 7-10 anni": {
        "descrizione": "Titoli di debito governativi e corporate a medio-lungo termine. I governativi europei rappresentano il benchmark duration, mentre i corporate offrono spread sostanziali ma con significativo rischio di credito amplificato dalla duration.",
        "performance_storica": {
            "20_anni": "4.8%",
            "10_anni": "3.2%",
            "5_anni": "0.8%",
            "1_anno": "1.4%",
            "indice_riferimento": "Euro Government 7-10Y Index / Euro Corporate 7-10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti potenzialmente attraenti",
            "Forti capital gain potenziali se tassi scendono",
            "Diversificazione significativa vs azioni",
            "Governativi: copertura deflazionistica perfetta",
            "Corporate: spread interessanti per duration risk compensation",
            "Benchmark per molti fondi pensione"
        ],
        "punti_debolezza": [
            "Alta sensibilità ai tassi di interesse",
            "Volatilità significativa",
            "Rischio di duration elevato",
            "Corporate: amplificazione del rischio credito con la duration",
            "Performance molto negativa con inflazione/rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Governativi: performance significativamente negativa; Corporate: performance molto negativa (tassi + spread)",
            "Recessione": "Governativi: performance eccellente (+10-20%); Corporate: performance negativa per rischio default",
            "Inflazione elevata": "Performance molto negativa (-10-20%) per entrambi",
            "Politiche restrittive": "Performance molto negativa, corporate particolarmente vulnerabili",
            "Politiche espansive": "Performance fortemente positiva, corporate outperformance"
        },
        "allocazione_range": "5-20% per diversificazione duration",
        "correlazioni": "Correlazione negativa forte con azioni, correlazione negativa con tassi"
    },

    "Obbligazioni >10 anni": {
        "descrizione": "Titoli di debito governativi e corporate a lungo termine. I governativi offrono massima sensibilità duration per copertura deflazionistica, mentre i corporate concentrano rischio di credito e duration con spread molto elevati.",
        "performance_storica": {
            "20_anni": "5.2%",
            "10_anni": "4.1%",
            "5_anni": "-0.2%",
            "1_anno": "0.8%",
            "indice_riferimento": "Euro Government >10Y Index / Euro Corporate >10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti potenzialmente più alti",
            "Massimi capital gain potenziali",
            "Diversificazione massima vs azioni",
            "Governativi: copertura deflazione/recessione ottimale",
            "Corporate: spread massimi per compensare i rischi",
            "Matching long-term liabilities"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Rischio di duration massimo",
            "Sensibilità estrema ai tassi",
            "Corporate: concentrazione massima del rischio credito",
            "Liquidità potenzialmente inferiore",
            "Rischio reinvestimento lontano"
        ],
        "scenari": {
            "Crescita economica": "Governativi: performance molto negativa; Corporate: performance disastrosa",
            "Recessione": "Governativi: performance eccezionale (+15-30%); Corporate: performance molto negativa per rischio default",
            "Inflazione elevata": "Performance disastrosa (-15-30%) per entrambi",
            "Politiche restrittive": "Performance molto negativa, corporate estremamente vulnerabili",
            "Politiche espansive": "Performance eccellente, corporate outperformance se credit regge"
        },
        "allocazione_range": "0-15% solo per investitori con obiettivi specifici",
        "correlazioni": "Correlazione negativa massima con azioni, inversa perfetta con tassi"
    },

    "Bond High Yield": {
        "descrizione": "Obbligazioni societarie ad alto rendimento emesse da aziende con rating creditizio inferiore (junk bonds), che offrono rendimenti superiori per compensare il maggiore rischio di credito.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "5.4%",
            "5_anni": "4.2%",
            "1_anno": "8.9%",
            "indice_riferimento": "Bloomberg Pan-European High Yield Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti significativamente più alti",
            "Minore sensibilità ai tassi di interesse",
            "Comportamento simile agli asset rischiosi",
            "Diversificazione geografica e settoriale",
            "Potenziale di capital appreciation"
        ],
        "punti_debolezza": [
            "Rischio di credito elevato",
            "Alta correlazione con azioni nei momenti di stress",
            "Liquidità inferiore nei periodi di crisi",
            "Volatilità superiore alle obbligazioni investment grade",
            "Rischio di default significativo"
        ],
        "scenari": {
            "Crescita economica": "Performance molto positiva (+6-10% annuo)",
            "Recessione": "Performance molto negativa (-15-25%)",
            "Inflazione elevata": "Performance relativamente buona se economia tiene",
            "Politiche restrittive": "Pressione negativa ma limitata",
            "Politiche espansive": "Performance molto positiva"
        },
        "allocazione_range": "5-15% per incremento del rendimento con rischio controllato",
        "correlazioni": "Correlazione moderata-alta con azioni, bassa con tassi di interesse"
    },

    "Bond Inflation Linked": {
        "descrizione": "Obbligazioni il cui capitale e cedole sono indicizzati all'inflazione, progettate per proteggere il potere d'acquisto dell'investitore (BTP€i, OATi, Bund-i).",
        "performance_storica": {
            "20_anni": "3.8%",
            "10_anni": "2.1%",
            "5_anni": "3.4%",
            "1_anno": "1.8%",
            "indice_riferimento": "Euro Inflation-Linked Government Bond Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Protezione diretta dall'inflazione",
            "Rendimento reale garantito",
            "Diversificazione nei portafogli",
            "Basso rischio di credito (governative)",
            "Correlazione negativa con inflazione breakeven"
        ],
        "punti_debolezza": [
            "Performance negativa se inflazione scende",
            "Volatilità da variazioni aspettative inflazione",
            "Rendimenti reali spesso bassi",
            "Complessità di pricing",
            "Liquidità inferiore alle obbligazioni tradizionali"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva se accompagnata da inflazione",
            "Recessione": "Performance mista (deflazione negativa, flight to quality positivo)",
            "Inflazione elevata": "Performance eccellente (+5-15%)",
            "Politiche restrittive": "Performance negativa per aspettative disinflazione",
            "Politiche espansive": "Performance molto positiva per aspettative inflazione"
        },
        "allocazione_range": "5-20% per protezione specifica dall'inflazione",
        "correlazioni": "Correlazione positiva con aspettative di inflazione, negativa con bond nominali"
    },

    "Bond Convertibili": {
        "descrizione": "Obbligazioni che possono essere convertite in azioni della società emittente a condizioni predeterminate, offrendo caratteristiche ibride debt/equity.",
        "performance_storica": {
            "20_anni": "5.8%",
            "10_anni": "7.2%",
            "5_anni": "8.4%",
            "1_anno": "12.1%",
            "indice_riferimento": "Refinitiv Europe Convertible Bond Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Partecipazione all'upside azionario",
            "Protezione downside rispetto alle azioni",
            "Rendimento cedolare",
            "Potenziale di capital appreciation significativo",
            "Diversificazione ibrida"
        ],
        "punti_debolezza": [
            "Complessità di valutazione",
            "Sensibilità alla volatilità implicita",
            "Underperformance se azioni laterali",
            "Rischio di credito dell'emittente",
            "Liquidità spesso limitata"
        ],
        "scenari": {
            "Crescita economica": "Performance molto positiva (equity upside)",
            "Recessione": "Performance negativa ma migliore delle azioni (-8-18%)",
            "Inflazione elevata": "Performance mista dipende da settori sottostanti",
            "Politiche restrittive": "Pressione negativa per tassi e equity",
            "Politiche espansive": "Performance molto positiva (equity rally + tassi bassi)"
        },
        "allocazione_range": "3-10% per esposizione ibrida debt/equity",
        "correlazioni": "Correlazione moderata-alta con azioni, sensibile alla volatilità"
    },

    "Obbligazioni Subordinate": {
        "descrizione": "Titoli di debito che in caso di liquidazione vengono rimborsati dopo i creditori senior, offrendo rendimenti più alti per il maggiore rischio (Tier 2, AT1, subordinate bancarie europee).",
        "performance_storica": {
            "20_anni": "5.2%",
            "10_anni": "4.8%",
            "5_anni": "3.1%",
            "1_anno": "7.4%",
            "indice_riferimento": "European Bank Subordinated Debt Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti significativamente superiori",
            "Emittenti spesso di alta qualità (banche, utilities)",
            "Trattamento regolamentare favorevole per banche",
            "Diversificazione del rischio di credito",
            "Liquidità ragionevole nei mercati sviluppati"
        ],
        "punti_debolezza": [
            "Rischio di subordinazione",
            "Possibilità di cancellazione cedole o conversione",
            "Complessità strutturale",
            "Rischio regolamentare (Basel III)",
            "Correlazione con settore finanziario"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva (+4-8% annuo)",
            "Recessione": "Performance negativa significativa (-10-20%)",
            "Inflazione elevata": "Performance mista dipende dalla salute finanziaria emittenti",
            "Politiche restrittive": "Pressione negativa per stress settore bancario",
            "Politiche espansive": "Performance positiva per supporto al settore finanziario"
        },
        "allocazione_range": "2-8% per investitori sofisticati che comprendono i rischi",
        "correlazioni": "Alta correlazione con settore finanziario, moderata con azioni"
    }
}
