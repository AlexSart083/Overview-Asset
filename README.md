# Financial Asset Analyzer - Streamlit App

An educational web application for analyzing different financial assets, available in both English and Italian.

## 📁 File Structure

```
your-app-folder/
│
├── app.py                 # Main Streamlit application
├── asset_data_en.py       # Asset data and UI text in English  
├── asset_data_it.py       # Asset data and UI text in Italian
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Local Development

1. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app locally:**
```bash
streamlit run app.py
```

## 🌐 Streamlit Cloud Deployment

### Step 1: Prepare your GitHub Repository

1. Create a new GitHub repository
2. Upload all the files:
   - `app.py`
   - `asset_data_en.py`
   - `asset_data_it.py` 
   - `requirements.txt`
   - `README.md`

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `app.py`
6. Click "Deploy!"

### Step 3: Configuration (Optional)

Create a `config.toml` file in `.streamlit/` folder for custom configuration:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[server]
headless = true
port = 8501
```

## ✨ Features

- **Bilingual Support**: Complete English and Italian translation
- **Interactive Analysis**: Detailed breakdown of 6 major asset classes
- **Visual Analytics**: Heatmaps and charts for better understanding
- **Educational Focus**: Clear disclaimers and educational content
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Analyzed Assets

### English Version:
- Global Equities
- Emerging Markets  
- Government Bonds
- Gold
- Commodities
- REITs

### Italian Version:
- Azioni Globali
- Mercati Emergenti
- Obbligazioni Governative
- Oro
- Materie Prime
- REIT

## 🔧 Customization

### Adding New Assets

1. **Update `asset_data_en.py`** - Add new asset with English data
2. **Update `asset_data_it.py`** - Add corresponding Italian translation
3. **Maintain structure**: Follow the existing data structure

### Modifying UI Text

- Edit `UI_TEXT_EN` in `asset_data_en.py` for English interface
- Edit `UI_TEXT_IT` in `asset_data_it.py` for Italian interface

### Adding New Market Scenarios

To add new market scenarios (e.g., "Stagflation", "Currency Crisis"):

1. Update the `scenari` dictionary in both language files
2. Add corresponding performance descriptions
3. Update the `performance_mapping` in `app.py` if needed

## 📈 Data Structure Example

```python
"Asset Name": {
    "descrizione": "Asset description...",
    "punti_forza": ["Strength 1", "Strength 2", ...],
    "punti_debolezza": ["Weakness 1", "Weakness 2", ...],
    "scenari": {
        "Scenario 1": "Performance description",
        "Scenario 2": "Performance description",
        ...
    },
    "allocazione_range": "X-Y% allocation guidance",
    "correlazioni": "Correlation information"
}
```

## 🛠️ Troubleshooting

### Common Issues:

1. **Import Error**: Make sure all files are in the same directory
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Streamlit Cloud Build Fails**: Check that all imports are correct and files are uploaded

### Performance Optimization:

- Data is loaded once and cached
- Plotly charts are optimized for web display
- Minimal external dependencies

## 🔒 Security & Disclaimers

- **Educational Purpose Only**: App includes prominent disclaimers
- **No Financial Advice**: Clear warnings about not providing personalized advice
- **Data Sources**: All data is for educational demonstration only

## 📝 License

This application is for educational purposes. Make sure to:
- Add appropriate disclaimers for your jurisdiction
- Verify all financial information before publication
- Consider consulting with financial professionals for accuracy

## 🤝 Contributing

To contribute or suggest improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues with:
- **Streamlit deployment**: Check [Streamlit documentation](https://docs.streamlit.io/)
- **Code issues**: Review the error logs in Streamlit Cloud
- **Data accuracy**: This is educational data only - verify with official sources

## 🔄 Updates and Maintenance

### Regular Updates Needed:
- Market scenario descriptions
- Asset allocation ranges  
- Correlation information
- UI improvements

### Version History:
- v1.0: Initial release with 6 asset classes
- v1.1: Added bilingual support
- v1.2: Enhanced visualizations

---

**Happy Analyzing! 📊✨**
