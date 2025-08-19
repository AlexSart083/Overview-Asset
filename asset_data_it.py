# Enhanced asset_data_it.py with historical performance data
ASSET_DATA_IT = {
    "Azioni Globali (Market Cap)": {
        "descrizione": "Investimenti azionari diversificati a livello mondiale ponderati per capitalizzazione di mercato, che rappresentano quote di proprietà nelle maggiori aziende quotate globalmente.",
        "performance_storica": {
            "20_anni": "7.0%",
            "10_anni": "10.6%",
            "5_anni": "14.4%",
            "1_anno": "14.9%",
            "indice_riferimento": "MSCI World Index"
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
            "indice_riferimento": "MSCI World Momentum Index"
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
            "indice_riferimento": "MSCI World Quality Index"
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
            "indice_riferimento": "MSCI World Value Index"
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
            "indice_riferimento": "MSCI World Minimum Volatility Index"
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
            "indice_riferimento": "MSCI World Small Cap Index"
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
            "indice_riferimento": "MSCI Emerging Markets Index"
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

    "Oro": {
        "descrizione": "Metallo prezioso considerato riserva di valore e copertura contro la svalutazione valutaria e l'instabilità geopolitica.",
        "performance_storica": {
            "20_anni": "8.4%",
            "10_anni": "4.2%",
            "5_anni": "7.8%",
            "1_anno": "27.0%",
            "indice_riferimento": "Prezzo Spot Oro (USD)"
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
            "indice_riferimento": "Prezzo Spot Argento (USD)"
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
            "indice_riferimento": "Bloomberg Commodity Index"
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
            "indice_riferimento": "FTSE Nareit All REITs Index"
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
    },

    "Obbligazioni 0-1 anni": {
        "descrizione": "Titoli di debito governativi e corporate a brevissimo termine con scadenza entro un anno, minimal duration risk.",
        "performance_storica": {
            "20_anni": "2.8%",
            "10_anni": "1.2%",
            "5_anni": "2.1%",
            "1_anno": "4.8%",
            "indice_riferimento": "Tasso BOT 3 mesi"
        },
        "punti_forza": [
            "Rischio di tasso di interesse minimo",
            "Alta liquidità",
            "Bassa volatilità",
            "Protezione del capitale",
            "Reinvestimento frequente ai tassi correnti"
        ],
        "punti_debolezza": [
            "Rendimenti molto bassi",
            "Nessuna protezione dall'inflazione se tassi reali negativi",
            "Rischio di reinvestimento",
            "Opportunità costo in ambienti di tassi crescenti"
        ],
        "scenari": {
            "Crescita economica": "Performance stabile ma rendimenti bassi",
            "Recessione": "Outperformance relativa per stabilità",
            "Inflazione elevata": "Performance negativa per tassi reali negativi",
            "Politiche restrittive": "Benefici graduali dal reinvestimento",
            "Politiche espansive": "Performance stabile ma rendimenti in calo"
        },
        "allocazione_range": "10-30% per liquidità e stabilità",
        "correlazioni": "Correlazione molto bassa con azioni, correlazione alta con tassi a breve"
    },

    "Obbligazioni 1-3 anni": {
        "descrizione": "Titoli di debito governativi e corporate a breve termine con duration limitata e buon compromesso rischio/rendimento.",
        "performance_storica": {
            "20_anni": "3.2%",
            "10_anni": "1.8%",
            "5_anni": "2.4%",
            "1_anno": "4.2%",
            "indice_riferimento": "BTP 2 anni"
        },
        "punti_forza": [
            "Rischio di tasso contenuto",
            "Rendimenti superiori al brevissimo termine",
            "Buona liquidità",
            "Volatilità moderata",
            "Diversificazione efficace"
        ],
        "punti_debolezza": [
            "Sensibilità ai tassi di interesse",
            "Rendimenti ancora limitati",
            "Rischio di credito per corporate",
            "Performance negativa con rialzi rapidi dei tassi"
        ],
        "scenari": {
            "Crescita economica": "Performance moderatamente negativa",
            "Recessione": "Performance positiva (flight to quality)",
            "Inflazione elevata": "Performance negativa ma limitata",
            "Politiche restrittive": "Pressione negativa contenuta",
            "Politiche espansive": "Performance moderatamente positiva"
        },
        "allocazione_range": "15-35% per bilanciamento rischio/rendimento",
        "correlazioni": "Correlazione negativa moderata con azioni"
    },

    "Obbligazioni 3-7 anni": {
        "descrizione": "Titoli di debito governativi e corporate a medio termine che offrono rendimenti più elevati ma con maggiore sensibilità ai tassi.",
        "performance_storica": {
            "20_anni": "4.1%",
            "10_anni": "2.8%",
            "5_anni": "1.2%",
            "1_anno": "2.8%",
            "indice_riferimento": "BTP 5 anni"
        },
        "punti_forza": [
            "Rendimenti più interessanti",
            "Sweet spot duration/rendimento",
            "Diversificazione del portafoglio",
            "Liquidità ancora buona",
            "Potenziali capital gain se tassi scendono"
        ],
        "punti_debolezza": [
            "Sensibilità significativa ai tassi di interesse",
            "Volatilità moderata-alta",
            "Rischio di duration",
            "Performance negativa con rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Performance negativa per aspettative rialzo tassi",
            "Recessione": "Performance fortemente positiva",
            "Inflazione elevata": "Performance significativamente negativa",
            "Politiche restrittive": "Pressione negativa significativa",
            "Politiche espansive": "Performance positiva"
        },
        "allocazione_range": "10-25% per rendimento con rischio controllato",
        "correlazioni": "Correlazione negativa con azioni, alta sensibilità ai tassi"
    },

    "Obbligazioni 7-10 anni": {
        "descrizione": "Titoli di debito governativi e corporate a medio-lungo termine con duration significativa e maggiore sensibilità alle aspettative di politica monetaria.",
        "performance_storica": {
            "20_anni": "4.8%",
            "10_anni": "3.2%",
            "5_anni": "0.8%",
            "1_anno": "1.4%",
            "indice_riferimento": "BTP 10 anni"
        },
        "punti_forza": [
            "Rendimenti potenzialmente attraenti",
            "Forti capital gain potenziali se tassi scendono",
            "Diversificazione significativa vs azioni",
            "Copertura deflazionistica",
            "Benchmark per molti fondi pensione"
        ],
        "punti_debolezza": [
            "Alta sensibilità ai tassi di interesse",
            "Volatilità significativa",
            "Rischio di duration elevato",
            "Performance molto negativa con inflazione/rialzo tassi"
        ],
        "scenari": {
            "Crescita economica": "Performance significativamente negativa",
            "Recessione": "Performance molto positiva (+10-20%)",
            "Inflazione elevata": "Performance molto negativa (-10-20%)",
            "Politiche restrittive": "Performance molto negativa",
            "Politiche espansive": "Performance fortemente positiva"
        },
        "allocazione_range": "5-20% per diversificazione duration",
        "correlazioni": "Correlazione negativa forte con azioni, correlazione negativa con tassi"
    },

    "Obbligazioni >10 anni": {
        "descrizione": "Titoli di debito governativi e corporate a lungo termine con duration massima e massima sensibilità alle variazioni dei tassi di interesse.",
        "performance_storica": {
            "20_anni": "5.2%",
            "10_anni": "4.1%",
            "5_anni": "-0.2%",
            "1_anno": "0.8%",
            "indice_riferimento": "BTP 30 anni"
        },
        "punti_forza": [
            "Rendimenti potenzialmente più alti",
            "Massimi capital gain potenziali",
            "Diversificazione massima vs azioni",
            "Copertura deflazione/recessione",
            "Matching long-term liabilities"
        ],
        "punti_debolezza": [
            "Volatilità molto elevata",
            "Rischio di duration massimo",
            "Sensibilità estrema ai tassi",
            "Rischio reinvestimento lontano",
            "Liquidità potenzialmente inferiore"
        ],
        "scenari": {
            "Crescita economica": "Performance molto negativa",
            "Recessione": "Performance eccezionale (+15-30%)",
            "Inflazione elevata": "Performance disastrosa (-15-30%)",
            "Politiche restrittive": "Performance molto negativa",
            "Politiche espansive": "Performance eccellente"
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
            "indice_riferimento": "Bloomberg High Yield Corporate Bond Index"
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
        "descrizione": "Obbligazioni il cui capitale e cedole sono indicizzati all'inflazione, progettate per proteggere il potere d'acquisto dell'investitore (TIPS, BTP€i).",
        "performance_storica": {
            "20_anni": "3.8%",
            "10_anni": "2.1%",
            "5_anni": "3.4%",
            "1_anno": "1.8%",
            "indice_riferimento": "BTP€i / TIPS Index"
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
            "indice_riferimento": "Refinitiv Global Convertible Bond Index"
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
        "descrizione": "Titoli di debito che in caso di liquidazione vengono rimborsati dopo i creditori senior, offrendo rendimenti più alti per il maggiore rischio (Tier 2, AT1).",
        "performance_storica": {
            "20_anni": "5.2%",
            "10_anni": "4.8%",
            "5_anni": "3.1%",
            "1_anno": "7.4%",
            "indice_riferimento": "Bank Subordinated Debt Index"
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
    },

    "Azionario High Dividend": {
        "descrizione": "Strategia che investe in azioni di società che distribuiscono dividendi elevati e sostenibili, spesso società mature con flussi di cassa stabili.",
        "performance_storica": {
            "20_anni": "6.8%",
            "10_anni": "9.2%",
            "5_anni": "10.4%",
            "1_anno": "11.8%",
            "indice_riferimento": "MSCI World High Dividend Yield Index"
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
}

# UI text in Italian
UI_TEXT_IT = {
    "title": "Analizzatore Asset Finanziari",
    "subtitle": "Analisi educativa di diversi asset finanziari",
    "sidebar_title": "Selezione Asset",
    "language_label": "Lingua",
    "asset_label": "Seleziona Asset",
    "analysis_title": "Analisi Asset: ",
    "description_header": "📖 Descrizione",
    "performance_header": "📊 Performance Storica (Annualizzata)",
    "strengths_header": "✅ Punti di Forza",
    "weaknesses_header": "⚠️ Punti di Debolezza",
    "scenarios_header": "📊 Performance negli Scenari di Mercato",
    "allocation_header": "💼 Range di Allocazione Indicativo",
    "correlations_header": "🔗 Correlazioni con Altri Asset",
    "summary_header": "📝 Riassunto Educativo",
    "warning": "⚠️ **Importante Disclaimer**: Queste informazioni sono a scopo puramente educativo e non costituiscono consigli finanziari personalizzati.",
    "visualization_title": "📈 Visualizzazione Performance",
    "heatmap_title": "Heatmap Performance Asset per Scenario di Mercato",
    "allocation_pie_title": "Allocazione Portfolio di Esempio",
    "performance_note": "📌 **Nota**: I dati di performance storica sono basati su indici di mercato rilevanti e non garantiscono risultati futuri. Le performance passate non predicono i rendimenti futuri."
}
