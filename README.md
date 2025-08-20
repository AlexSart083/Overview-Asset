# Financial Asset Analyzer - Streamlit App (Modular Version)

Un'applicazione web educativa per analizzare diversi asset finanziari, ora con **struttura modulare migliorata** per una gestione più semplice e scalabile.

## 🚀 **Nuova Struttura Modulare**

### 📁 Struttura File

```
financial-asset-analyzer/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                      # Questa documentazione
│
├── data/                          # 📂 Cartella dati modulare
│   ├── __init__.py               # Package init
│   ├── loader.py                 # 🔧 Funzioni caricamento dati
│   │
│   ├── english/                  # 🇺🇸 Dati in inglese
│   │   ├── __init__.py
│   │   ├── equity_assets_en.py   # Azioni e strategie azionarie
│   │   ├── bond_assets_en.py     # Obbligazioni
│   │   ├── alternative_assets_en.py # Asset alternativi
│   │   └── ui_text_en.py         # Testi interfaccia
│   │
│   └── italian/                  # 🇮🇹 Dati in italiano
│       ├── __init__.py
│       ├── equity_assets_it.py   # Azioni e strategie azionarie
│       ├── bond_assets_it.py     # Obbligazioni
│       ├── alternative_assets_it.py # Asset alternativi
│       └── ui_text_it.py         # Testi interfaccia
│
└── legacy/                       # 📜 File legacy (opzionale)
    ├── asset_data_en.py         # Dati originali inglese
    └── asset_data_it.py         # Dati originali italiano
```

## 🎯 **Vantaggi della Nuova Struttura**

### ✅ **Modularità**
- **File più piccoli e gestibili**: Ogni categoria di asset in file separati
- **Manutenzione semplificata**: Facile trovare e modificare dati specifici
- **Scalabilità**: Aggiungere nuovi asset o categorie è più semplice

### ✅ **Organizzazione Linguistica**
- **Separazione netta**: Inglese e italiano in cartelle separate
- **Facile traduzione**: Aggiungere nuove lingue è immediato
- **Meno errori**: Ridotto rischio di mescolare traduzioni

### ✅ **Compatibilità**
- **Fallback automatico**: Se i file modulari non sono disponibili, usa quelli legacy
- **Migrazione graduale**: Puoi passare alla nuova struttura quando vuoi
- **Zero downtime**: L'app continua a funzionare durante la transizione

## 📊 **Divisione Asset per Categoria**

### 🔢 **Equity Assets** (`equity_assets_xx.py`)
- Global Equities (Market Cap)
- Momentum Equities
- Quality Equities
- Value Equities
- Minimum Volatility Equities
- Small Cap Equities
- Emerging Markets
- High Dividend Equities

### 💰 **Bond Assets** (`bond_assets_xx.py`)
- Bonds 0-1 Years
- Bonds 1-3 Years
- Bonds 3-7 Years
- Bonds 7-10 Years
- Bonds >10 Years
- High Yield Bonds
- Inflation Linked Bonds
- Convertible Bonds
- Subordinated Bonds

### 🏢 **Alternative Assets** (`alternative_assets_xx.py`)
- Gold
- Silver
- Commodities
- REITs

## 🚀 **Installazione e Avvio**

### 1. **Setup Ambiente**
```bash
# Clona/scarica i file del progetto
git clone <your-repo> financial-asset-analyzer
cd financial-asset-analyzer

# Crea ambiente virtuale
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installa dipendenze
pip install -r requirements.txt
```

### 2. **Avvio Applicazione**
```bash
streamlit run app.py
```

### 3. **Verifica Struttura**
- ✅ **Modular**: Se vedi "✅ Using modular data structure" nella sidebar
- ⚠️ **Legacy**: Se vedi "⚠️ Using legacy data structure"

## 🔧 **Come Aggiungere Nuovi Asset**

### Per la Struttura Modulare:

1. **Identifica la categoria** (equity, bond, alternative)
2. **Apri il file appropriato** (es. `data/english/equity_assets_en.py`)
3. **Aggiungi il nuovo asset** seguendo la struttura esistente:

```python
"Nuovo
