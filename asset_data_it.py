# Asset data in Italian
ASSET_DATA_IT = {
    "Azioni Globali": {
        "descrizione": "Investimenti azionari diversificati a livello mondiale che rappresentano quote di proprietà in aziende quotate in borsa.",
        "punti_forza": [
            "Potenziale di crescita a lungo termine",
            "Protezione storica contro l'inflazione",
            "Liquidità elevata",
            "Diversificazione geografica e settoriale",
            "Potenziali dividendi"
        ],
        "punti_debolezza": [
            "Volatilità elevata nel breve periodo",
            "Rischio di perdite significative",
            "Dipendenza dai cicli economici",
            "Rischio valutario per investitori locali"
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
    
    "Mercati Emergenti": {
        "descrizione": "Azioni di aziende localizzate in paesi in via di sviluppo con economie in rapida crescita.",
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
    
    "Obbligazioni Governative": {
        "descrizione": "Titoli di debito emessi da governi nazionali, considerati investimenti a basso rischio.",
        "punti_forza": [
            "Basso rischio di credito (paesi sviluppati)",
            "Stabilità e prevedibilità dei flussi",
            "Correlazione negativa con azioni",
            "Liquidità elevata",
            "Diversificazione del portafoglio"
        ],
        "punti_debolezza": [
            "Rischio di tasso di interesse",
            "Rischio inflazione (erosione potere d'acquisto)",
            "Rendimenti bassi in ambienti di tassi bassi",
            "Rischio di duration per obbligazioni a lungo termine"
        ],
        "scenari": {
            "Crescita economica": "Performance moderatamente negativa per aspettative di rialzo tassi",
            "Recessione": "Performance fortemente positiva (flight to quality)",
            "Inflazione elevata": "Performance negativa per erosione rendimenti reali",
            "Politiche restrittive": "Performance negativa per rialzo tassi",
            "Politiche espansive": "Performance positiva per calo tassi"
        },
        "allocazione_range": "20-40% per stabilizzazione del portafoglio",
        "correlazioni": "Tipicamente correlazione negativa con azioni durante stress"
    },
    
    "Oro": {
        "descrizione": "Metallo prezioso considerato riserva di valore e copertura contro la svalutazione valutaria.",
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
    
    "Materie Prime": {
        "descrizione": "Materie prime e prodotti agricoli primari negoziati sui mercati globali.",
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
        "descrizione": "Real Estate Investment Trust che forniscono esposizione ai mercati immobiliari attraverso titoli quotati.",
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

# UI text in Italian
UI_TEXT_IT = {
    "title": "Analizzatore Asset Finanziari",
    "subtitle": "Analisi educativa di diversi asset finanziari",
    "sidebar_title": "Selezione Asset",
    "language_label": "Lingua",
    "asset_label": "Seleziona Asset",
    "analysis_title": "Analisi Asset: ",
    "description_header": "📖 Descrizione",
    "strengths_header": "✅ Punti di Forza",
    "weaknesses_header": "⚠️ Punti di Debolezza",
    "scenarios_header": "📊 Performance negli Scenari di Mercato",
    "allocation_header": "💼 Range di Allocazione Indicativo",
    "correlations_header": "🔗 Correlazioni con Altri Asset",
    "summary_header": "📝 Riassunto Educativo",
    "warning": "⚠️ **Importante Disclaimer**: Queste informazioni sono a scopo puramente educativo e non costituiscono consigli finanziari personalizzati.",
    "visualization_title": "📈 Visualizzazione Performance",
    "heatmap_title": "Heatmap Performance Asset per Scenario di Mercato",
    "allocation_pie_title": "Allocazione Portfolio di Esempio"
}
