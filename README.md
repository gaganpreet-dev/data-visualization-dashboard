# Data Visualization Dashboard

A simple interactive data visualization dashboard built with Dash and Plotly that allows users to upload a CSV or use a sample dataset to explore charts and tables.

## Features
- Upload CSV or use provided sample data (`sample_sales.csv`)
- Interactive filters (date range, category)
- Line chart, bar chart, and pie chart
- Responsive layout suitable for demo and portfolio

## Tech Stack
- Python 3.8+
- Dash
- Plotly
- Pandas

## Quick Start (Local)
1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows PowerShell
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

Open http://127.0.0.1:8050 in your browser.

## Files
- `app.py` - Main Dash application
- `data/sample_sales.csv` - Sample dataset
- `requirements.txt` - Python dependencies
- `README.md` - This file
- `.gitignore` - standard Python ignores

## How to upload to GitHub (commands)
```bash
git init
git add .
git commit -m "Initial commit: Data Visualization Dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/data-visualization-dashboard.git
git push -u origin main
```
After pushing, your repository link will be:
`https://github.com/<your-username>/data-visualization-dashboard`

Replace `<your-username>` with your GitHub username.

## Notes
- This repo is ready to be uploaded to GitHub.
- If you want, I can also generate a polished GitHub README with badges, or create a Streamlit version.
