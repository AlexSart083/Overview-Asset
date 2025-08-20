# data/italian/alternative_assets_it.py
"""
Dati asset alternativi in italiano
Include metalli preziosi, materie prime e fondi immobiliari
"""

ALTERNATIVE_ASSETS_IT = {
    "Oro": {
        "descrizione": "Metallo prezioso considerato riserva di valore e copertura contro la svalutazione valutaria e l'instabilità geopolitica.",
        "performance_storica": {
            "20_anni": "8.4%",
            "5_anni": "7.8%",
            "1_anno": "27.0%",
            "indice_riferimento": "Prezzo Spot Oro (USD)",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Copertura storica contro l'inflazione",
            "Riserva di valore durante le crisi",
            "Diversificazione del portafoglio",
            "Nessun rischio di controparte",
            "Riconoscimento e liquidità globali"
        ],
        "punti_debolezza": [
            "Nessuna generazione di reddito",
            "Alta volatilità nel breve termine",
            "Costi di stoccaggio e assicurazione",
            "Sensibile ai tassi di interesse reali",
            "Rischio valutario (denominato in USD)"
        ],
        "scenari": {
            "Crescita economica": "Performance moderatamente negativa",
            "Recessione": "Performance fortemente positiva (bene rifugio)",
            "Inflazione elevata": "Performance storicamente positiva",
            "Politiche restrittive": "Pressione negativa per tassi reali più alti",
            "Politiche espansive": "Positivo per timori di svalutazione valutaria"
        },
        "allocazione_range": "5-10% come copertura del portafoglio",
        "correlazioni": "Bassa correlazione con altri asset, inversa con USD"
    },

    "Argento": {
        "descrizione": "Metallo prezioso con doppia natura di bene rifugio e commodity industriale, più volatile dell'oro.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "2.1%",
            "5_anni": "9.2%",
            "1_anno": "32.5%",
            "indice_riferimento": "Prezzo Spot Argento (USD)",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Doppia domanda: investimento e industriale",
            "Maggiore volatilità può offrire opportunità",
            "Rapporto oro/argento storicamente ciclico",
            "Utilizzi tecnologici in crescita",
            "Prezzo relativamente più accessibile"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Più sensibile ai cicli industriali dell'oro",
            "Mercato più piccolo e meno liquido",
            "Maggiori costi di stoccaggio relativi",
            "Performance storicamente inferiore all'oro"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva per domanda industriale",
            "Recessione": "Performance mista (rifugio vs domanda industriale)",
            "Inflazione elevata": "Performance molto positiva",
            "Politiche restrittive": "Pressione da tassi reali alti",
            "Politiche espansive": "Forte supporto specialmente se supera l'oro"
        },
        "allocazione_range": "2-5% come satellite dell'oro",
        "correlazioni": "Alta correlazione con oro ma maggiore volatilità"
    },

    "Materie Prime": {
        "descrizione": "Materie prime e prodotti agricoli primari negoziati sui mercati globali, inclusi energia, metalli industriali e prodotti agricoli.",
        "performance_storica": {
            "20_anni": "4.8%",
            "10_anni": "3.2%",
            "5_anni": "8.1%",
            "1_anno": "12.4%",
            "indice_riferimento": "Bloomberg Commodity Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Protezione dall'inflazione",
            "Benefici di diversificazione",
            "Dinamiche domanda/offerta",
            "Esposizione all'economia globale",
            "Supporto di asset tangibili"
        ],
        "punti_debolezza": [
            "Volatilità elevata",
            "Nessuna generazione di reddito",
            "Costi di stoccaggio e trasporto",
            "Natura ciclica",
            "Rischi meteorologici e geopolitici"
        ],
        "scenari": {
            "Crescita economica": "Performance fortemente positiva",
            "Recessione": "Performance negativa per distruzione della domanda",
            "Inflazione elevata": "Performance fortemente positiva",
            "Politiche restrittive": "Impatto misto a seconda degli effetti economici",
            "Politiche espansive": "Positivo per aspettative di maggiore domanda"
        },
        "allocazione_range": "5-15% per protezione dall'inflazione",
        "correlazioni": "Correlazione positiva con inflazione, mista con azioni"
    },

    "REIT": {
        "descrizione": "Real Estate Investment Trust che forniscono esposizione ai mercati immobiliari attraverso titoli quotati in borsa.",
        "performance_storica": {
            "20_anni": "7.2%",
            "10_anni": "8.4%",
            "5_anni": "5.8%",
            "1_anno": "11.2%",
            "indice_riferimento": "FTSE Nareit All REITs Index",
            "data_calcolo": "Dati al 31 Dicembre 2024"
        },
        "punti_forza": [
            "Reddito regolare da dividendi",
            "Esposizione immobiliare senza proprietà diretta",
            "Gestione professionale",
            "Liquidità rispetto al mattone",
            "Potenziale copertura dall'inflazione"
        ],
        "punti_debolezza": [
            "Sensibilità ai tassi di interesse",
            "Dipendenza dai cicli immobiliari",
            "Diversificazione inferiore alle aspettative",
            "Commissioni di gestione",
            "Complessità fiscale"
        ],
        "scenari": {
            "Crescita economica": "Performance positiva per occupazione e crescita affitti",
            "Recessione": "Performance negativa per debolezza economica",
            "Inflazione elevata": "Performance mista (costi input vs aumenti affitti)",
            "Politiche restrittive": "Pressione negativa per tassi di sconto più alti",
            "Politiche espansive": "Supporto positivo per tassi più bassi"
        },
        "allocazione_range": "5-15% per esposizione immobiliare",
        "correlazioni": "Correlazione moderata con azioni, sensibili ai tassi di interesse"
    }
}
