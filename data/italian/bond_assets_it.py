# data/italian/bond_assets_it.py
"""
Dati obbligazioni e titoli a reddito fisso in italiano
Separazione chiara tra obbligazioni governative e corporate
"""

BOND_ASSETS_IT = {
    # ===== OBBLIGAZIONI GOVERNATIVE =====
    "Bond Governativi 0-1 anni": {
        "descrizione": "Titoli di Stato europei a brevissimo termine con scadenza entro un anno. Rappresentano il benchmark risk-free per eccellenza, con rischio di credito praticamente nullo ma rendimenti molto contenuti.",
        "performance_storica": {
            "20_anni": "2.5%",
            "10_anni": "0.8%",
            "5_anni": "1.8%",
            "1_anno": "4.2%",
            "indice_riferimento": "Euro Short-Term Rate (€STR) / Euro Government 0-1Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rischio di credito nullo (backing governativo)",
            "Liquidità massima sui mercati",
            "Volatilità minima",
            "Protezione assoluta del capitale",
            "Reinvestimento frequente ai tassi correnti",
            "Benchmark risk-free per tutti gli altri asset"
        ],
        "punti_debolezza": [
            "Rendimenti molto bassi o negativi",
            "Nessuna protezione dall'inflazione se tassi reali negativi",
            "Rischio di reinvestimento",
            "Opportunità costo elevato in mercati rialzisti",
            "Performance reale negativa in periodi inflattivi"
        ],
        "scenari": {
            "Crescita economica": "Performance stabile ma rendimenti molto bassi",
            "Recessione": "Massima outperformance per flight-to-quality",
            "Inflazione elevata": "Performance reale negativa per tassi reali negativi",
            "Politiche restrittive": "Benefici graduali dal reinvestimento a tassi più alti",
            "Politiche espansive": "Performance stabile ma rendimenti in ulteriore calo"
        },
        "allocazione_range": "15-40% per liquidità assoluta e stabilità",
        "correlazioni": "Correlazione nulla con azioni, perfetta con tassi a breve termine"
    },

    "Bond Governativi 1-3 anni": {
        "descrizione": "Titoli di Stato europei a breve termine che offrono il punto di equilibrio ottimale tra sicurezza e rendimento nel segmento governativo, mantenendo il rischio di credito nullo.",
        "performance_storica": {
            "20_anni": "3.0%",
            "10_anni": "1.5%",
            "5_anni": "2.2%",
            "1_anno": "3.8%",
            "indice_riferimento": "Euro Government 1-3Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Combinazione ottimale sicurezza/rendimento nel gov",
            "Rischio di tasso contenuto",
            "Liquidità eccellente",
            "Volatilità bassa",
            "Diversificazione efficace vs equity",
            "Nessun rischio di credito"
        ],
        "punti_debolezza": [
            "Rendimenti ancora limitati",
            "Sensibilità ai tassi presente anche se contenuta",
            "Performance negativa con rialzi rapidi dei tassi",
            "Protezione inflazione limitata"
        ],
        "scenari": {
            "Crescita economica": "Performance leggermente negativa per aspettative rialzo tassi",
            "Recessione": "Performance fortemente positiva (flight to quality)",
            "Inflazione elevata": "Performance negativa ma molto contenuta",
            "Politiche restrittive": "Pressione negativa limitata",
            "Politiche espansive": "Performance moderatamente positiva"
        },
        "allocazione_range": "20-45% come core difensivo del portafoglio",
        "correlazioni": "Correlazione negativa moderata con azioni"
    },

    "Bond Governativi 3-7 anni": {
        "descrizione": "Titoli di Stato europei a medio termine che rappresentano il sweet spot della curva governativa, offrendo rendimenti più interessanti mantenendo la sicurezza creditizia assoluta.",
        "performance_storica": {
            "20_anni": "3.8%",
            "10_anni": "2.5%",
            "5_anni": "0.9%",
            "1_anno": "2.2%",
            "indice_riferimento": "Euro Government 3-7Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti governativi più interessanti",
            "Sweet spot della curva dei tassi",
            "Rischio di credito nullo",
            "Liquidità ancora molto buona",
            "Potenziali capital gain significativi se tassi scendono",
            "Diversificazione ottimale vs azioni"
        ],
        "punti_debolezza": [
            "Sensibilità significativa ai tassi di interesse",
            "Volatilità moderata-alta",
            "Rischio di duration",
            "Performance negativa con rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Performance negativa per aspettative rialzo tassi",
            "Recessione": "Performance fortemente positiva (+8-15%)",
            "Inflazione elevata": "Performance significativamente negativa",
            "Politiche restrittive": "Pressione negativa significativa",
            "Politiche espansive": "Performance positiva con capital gain"
        },
        "allocazione_range": "15-30% per rendimento governativo con rischio controllato",
        "correlazioni": "Correlazione negativa con azioni, alta sensibilità ai tassi"
    },

    "Bond Governativi 7-10 anni": {
        "descrizione": "Titoli di Stato europei a medio-lungo termine che rappresentano il benchmark duration per eccellenza, offrendo la massima copertura deflazionistica nel segmento governativo.",
        "performance_storica": {
            "20_anni": "4.5%",
            "10_anni": "3.0%",
            "5_anni": "0.5%",
            "1_anno": "1.0%",
            "indice_riferimento": "Euro Government 7-10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti governativi potenzialmente attraenti",
            "Forti capital gain potenziali se tassi scendono",
            "Diversificazione massima vs azioni",
            "Copertura deflazionistica perfetta",
            "Benchmark per fondi pensione",
            "Nessun rischio di credito"
        ],
        "punti_debolezza": [
            "Alta sensibilità ai tassi di interesse",
            "Volatilità significativa",
            "Rischio di duration elevato",
            "Performance molto negativa con inflazione/rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Performance significativamente negativa",
            "Recessione": "Performance eccellente (+12-25%)",
            "Inflazione elevata": "Performance molto negativa (-10-20%)",
            "Politiche restrittive": "Performance molto negativa",
            "Politiche espansive": "Performance fortemente positiva"
        },
        "allocazione_range": "10-25% per copertura deflazionistica",
        "correlazioni": "Correlazione negativa forte con azioni, inversa con tassi"
    },

    "Bond Governativi >10 anni": {
        "descrizione": "Titoli di Stato europei a lungo termine che offrono la massima sensibilità duration e rappresentano la copertura definitiva contro scenari deflazionistici estremi.",
        "performance_storica": {
            "20_anni": "4.9%",
            "10_anni": "3.8%",
            "5_anni": "-0.5%",
            "1_anno": "0.5%",
            "indice_riferimento": "Euro Government >10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Rendimenti governativi potenzialmente più alti",
            "Massimi capital gain potenziali",
            "Diversificazione massima vs azioni",
            "Copertura deflazione/recessione ottimale",
            "Matching perfetto per passività a lungo termine",
            "Sicurezza creditizia assoluta"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Rischio di duration massimo",
            "Sensibilità estrema ai tassi",
            "Liquidità potenzialmente inferiore",
            "Performance disastrosa con inflazione",
            "Rischio reinvestimento molto lontano"
        ],
        "scenari": {
            "Crescita economica": "Performance molto negativa",
            "Recessione": "Performance eccezionale (+15-35%)",
            "Inflazione elevata": "Performance disastrosa (-15-30%)",
            "Politiche restrittive": "Performance molto negativa",
            "Politiche espansive": "Performance eccellente"
        },
        "allocazione_range": "0-15% solo per copertura specifica deflazione",
        "correlazioni": "Correlazione negativa massima con azioni, inversa perfetta con tassi"
    },

    # ===== OBBLIGAZIONI CORPORATE =====
    "Bond Corporate 0-1 anni": {
        "descrizione": "Obbligazioni societarie europee a brevissimo termine che offrono spread creditizi interessanti con duration minima, ideali per incrementare il rendimento mantenendo bassa la volatilità.",
        "performance_storica": {
            "20_anni": "3.2%",
            "10_anni": "1.6%",
            "5_anni": "2.5%",
            "1_anno": "5.4%",
            "indice_riferimento": "Euro Corporate 0-1Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Spread creditizio attraente vs governativi",
            "Duration minima limita il rischio tasso",
            "Buona liquidità su emittenti primari",
            "Diversificazione settoriale",
            "Reinvestimento frequente con spread pickup",
            "Volatilità contenuta"
        ],
        "punti_debolezza": [
            "Rischio di credito presente",
            "Spread risk durante stress di mercato",
            "Correlazione con ciclo economico",
            "Possibile deterioramento rating",
            "Liquidità inferiore vs governativi"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva per miglioramento fondamentali",
            "Recessione": "Pressione negativa per rischio credito e spread widening",
            "Inflazione elevata": "Performance mista, dipende dalla capacità di pricing power",
            "Politiche restrittive": "Pressione per rischio recessione",
            "Politiche espansive": "Performance positiva per supporto all'economia"
        },
        "allocazione_range": "10-25% per extra-rendimento a basso rischio",
        "correlazioni": "Bassa correlazione con azioni, moderata con spread creditizi"
    },

    "Bond Corporate 1-3 anni": {
        "descrizione": "Obbligazioni societarie europee a breve termine che combinano spread creditizi interessanti con duration limitata, offrendo il miglior rapporto rischio/rendimento nel segmento corporate.",
        "performance_storica": {
            "20_anni": "3.8%",
            "10_anni": "2.4%",
            "5_anni": "2.8%",
            "1_anno": "4.8%",
            "indice_riferimento": "Euro Corporate 1-3Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Ottimo trade-off spread/duration",
            "Spread significativi vs governativi equivalenti",
            "Diversificazione settoriale ampia",
            "Buona liquidità su emittenti investment grade",
            "Potenziale di outperformance in crescita economica",
            "Duration controllata"
        ],
        "punti_debolezza": [
            "Rischio di credito e spread",
            "Sensibilità al ciclo economico",
            "Correlazione con azioni in stress periods",
            "Possibili downgrade di rating",
            "Complessità di analisi creditizia"
        ],
        "scenari": {
            "Crescita economica": "Outperformance significativa per spread tightening",
            "Recessione": "Performance negativa per deterioramento credito",
            "Inflazione elevata": "Performance variabile per settore",
            "Politiche restrittive": "Pressione per possibile stress creditizio",
            "Politiche espansive": "Performance positiva per miglioramento fondamentali"
        },
        "allocazione_range": "15-30% come core del segmento corporate",
        "correlazioni": "Correlazione moderata con azioni, alta con spread creditizi"
    },

    "Bond Corporate 3-7 anni": {
        "descrizione": "Obbligazioni societarie europee a medio termine dove gli spread creditizi diventano più significativi, offrendo rendimenti superiori ma con maggiore esposizione al rischio di credito amplificato dalla duration.",
        "performance_storica": {
            "20_anni": "4.5%",
            "10_anni": "3.2%",
            "5_anni": "1.6%",
            "1_anno": "3.2%",
            "indice_riferimento": "Euro Corporate 3-7Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Spread creditizi molto interessanti",
            "Rendimenti superiori al segmento governativo",
            "Diversificazione settoriale significativa",
            "Potenziali capital gain da spread tightening",
            "Buona liquidità su emittenti primari",
            "Esposizione a crescita economica"
        ],
        "punti_debolezza": [
            "Doppia esposizione: duration + credit risk",
            "Volatilità elevata in periodi di stress",
            "Sensibilità amplificata ai cicli creditizi",
            "Correlazione crescente con azioni in crisi",
            "Rischio di significativo spread widening"
        ],
        "scenari": {
            "Crescita economica": "Performance molto positiva per double alpha (tassi + spread)",
            "Recessione": "Performance molto negativa per deterioramento credito",
            "Inflazione elevata": "Performance mista, settori diversamente impattati",
            "Politiche restrittive": "Doppia pressione negativa (tassi + credito)",
            "Politiche espansive": "Performance eccellente se fondamentali reggono"
        },
        "allocazione_range": "10-20% per rendimento superiore con rischi controllati",
        "correlazioni": "Correlazione moderata-alta con azioni, molto alta con spread"
    },

    "Bond Corporate 7-10 anni": {
        "descrizione": "Obbligazioni societarie europee a medio-lungo termine che concentrano il massimo rischio di credito con duration elevata, adatte solo a investitori che comprendono la complessità rischio/rendimento.",
        "performance_storica": {
            "20_anni": "5.1%",
            "10_anni": "3.8%",
            "5_anni": "1.2%",
            "1_anno": "1.8%",
            "indice_riferimento": "Euro Corporate 7-10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Spread massimi per compensare i rischi",
            "Potenziali capital gain molto elevati",
            "Rendimenti potenzialmente attraenti",
            "Diversificazione settoriale",
            "Benefici massimi in scenari di recovery",
            "Esposizione amplificata alla crescita"
        ],
        "punti_debolezza": [
            "Concentrazione massima del rischio",
            "Volatilità molto elevata",
            "Amplificazione di duration + credit risk",
            "Correlazione alta con azioni in stress",
            "Possibili perdite severe in recessioni",
            "Complessità gestionale elevata"
        ],
        "scenari": {
            "Crescita economica": "Performance eccellente ma con alta volatilità",
            "Recessione": "Performance disastrosa per combinazione duration + credit",
            "Inflazione elevata": "Performance molto negativa",
            "Politiche restrittive": "Estremamente vulnerabili",
            "Politiche espansive": "Outperformance significativa se credit regge"
        },
        "allocazione_range": "5-15% solo per investitori sofisticati",
        "correlazioni": "Alta correlazione con azioni, massima con spread creditizi"
    },

    "Bond Corporate >10 anni": {
        "descrizione": "Obbligazioni societarie europee a lungo termine che rappresentano l'asset più complesso e rischioso del segmento fixed income, combinando duration estrema con rischio di credito massimo.",
        "performance_storica": {
            "20_anni": "5.5%",
            "10_anni": "4.5%",
            "5_anni": "0.2%",
            "1_anno": "1.2%",
            "indice_riferimento": "Euro Corporate >10Y Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Spread massimi assoluti",
            "Potenziali capital gain estremi",
            "Rendimenti potenzialmente molto elevati",
            "Matching per passività corporate a lungo termine",
            "Massima esposizione ai cicli creditizi",
            "Diversificazione settoriale"
        ],
        "punti_debolezza": [
            "Rischio massimo assoluto nel fixed income",
            "Volatilità estrema",
            "Liquidità potenzialmente problematica",
            "Correlazione massima con azioni in crisi",
            "Rischio di perdite devastanti",
            "Complessità analitica estrema"
        ],
        "scenari": {
            "Crescita economica": "Performance potenzialmente eccellente ma volatilissima",
            "Recessione": "Performance catastrofica",
            "Inflazione elevata": "Performance disastrosa",
            "Politiche restrittive": "Estremamente vulnerabili",
            "Politiche espansive": "Massima outperformance possibile se tutto va bene"
        },
        "allocazione_range": "0-10% solo per investitori altamente sofisticati",
        "correlazioni": "Correlazione massima con azioni e spread, duration estrema"
    },

    # ===== OBBLIGAZIONI SPECIALIZZATE =====
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
