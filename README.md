# 🪵 Pakistani Carpentry, Woodwork & Hardware AI Estimator
### لکڑی، پی وی سی، الماری اور ہارڈویئر کا مکمل تخمینہ لاگت بلڈر

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A modern, bilingual (**Urdu & English**) Web Application built for carpenters, contractors, interior designers, and homeowners in Pakistan. Quickly parse handwritten Urdu carpenter slips, look up wholesale timber and hardware market rates in **Islamabad & Rawalpindi**, calculate real-time totals, adjust margins, and export dynamic **Excel (`.xlsx`)** spreadsheets and printable bills.

---

## 🌟 Key Features

- 📝 **Urdu Slip Parser & Interpreter**: Paste raw Urdu handwritten notes (e.g. `شیٹ شٹر الماری 4+4`, `واش روم 3/4 PVC کلو 8 عدد`, `سمد بونڈ 1.5 کلو 3 ڈبے`) to auto-populate quantities, units, and rates.
- 💰 **Preloaded Islamabad & Rawalpindi Wholesale Rates**: Includes realistic rates for:
  - **Sheets & Boards**: PVC 3/4" (18mm), PVC 2 Suter (6mm), UV High Gloss, Lamination/Formica, Press Doors.
  - **Trims & Lipping**: PVC Lipping (30x60, 27x60), Kitchen PVC J-Gola (16mm), Countertop Molding.
  - **Fasteners & Screws**: Black Drywall Screws (3/4", 5/8", 1/2", 2", 1.5"), Umbrella Head Screws.
  - **Nails & Steel Pins**: TP Wire Pins, Hardened Steel Nails (1", 3/4", 2", 2.5"), Fluted Anchor Rods.
  - **Fittings & Adhesives**: 3D Soft-Close Hydraulic Hinges, 3-Lever Drawer Locks, Samad Bond 1.5kg, Foam Tape.
- 📊 **Interactive Analytics**: Real-time Plotly charts breaking down expenses by room (Bedroom, Washroom, Kitchen, Hardware) and material category.
- 📈 **Dynamic Margin Slider**: Adjust wholesale rates or apply contractor markups / discounts (-20% to +30%) globally with 1 click.
- 📥 **Export to Excel (`.xlsx`)**: Generates structured, styled multi-sheet workbooks with active mathematical formulas (`=Qty * Rate` and `=SUM(...)`).
- 🌐 **Zero-Setup Standalone HTML App**: Includes `standalone_app.html` for offline browser viewing without any installation.

---

## 🚀 How to Deploy on Streamlit Cloud (Free & 1-Click)

1. **Fork or Push this repository to your GitHub account**.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub.
3. Click **"New app"**.
4. Select this repository:
   - **Main file path**: `app.py`
   - **App URL**: Choose your desired URL name.
5. Click **"Deploy!"** 🎉

---

## 💻 Local Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/pak-carpentry-estimator.git
cd pak-carpentry-estimator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit App
streamlit run app.py
```

---

## 📂 Project Structure

```
├── app.py                  # Main Streamlit web application
├── market_database.py      # Wholesale market pricing database for Islamabad/Rawalpindi
├── urdu_parser.py          # Urdu carpenter terminology & quantity parsing engine
├── excel_exporter.py       # Styled OpenPyXL Excel spreadsheet exporter
├── standalone_app.html     # Portable single-page web app (Tailwind + JS)
├── run_app.bat             # 1-Click Windows shortcut launcher
├── requirements.txt        # Python package dependencies
├── .gitignore              # Git ignore rules
└── .streamlit/
    └── config.toml         # Custom Streamlit UI theme
```

---

## 📜 License

This project is licensed under the MIT License.
