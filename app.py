"""
Urdu Woodwork & Hardware Material Estimator Web Application
Bilingual Streamlit App for Pakistani Carpentry, PVC & Fastener Lists.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os
from market_database import DEFAULT_MARKET_RATES, get_categories, lookup_item_rate
from urdu_parser import parse_slip_text, CARPENTRY_DICTIONARY
from excel_exporter import generate_excel_bytes

# App Configuration
st.set_page_config(
    page_title="Pak Carpentry & Woodwork AI Estimator",
    page_icon="🪵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Urdu Font & Professional Blue Palette)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Inter:wght@400;500;600;700&display=swap');
    
    .urdu-font {
        font-family: 'Noto Nastaliq Urdu', 'Segoe UI', Tahoma, sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    .metric-box {
        background: #ffffff;
        padding: 16px 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Default Seed Data (All 41 items from the 2 slips)
SEED_ITEMS = [
    # Slip 1 - Bedroom
    {"urdu": "شیٹ شٹر الماری", "english": "Wardrobe Shutter Sheets (Laminated Board / Super Gloss)", "category": "Sheets & Boards", "area": "Bedroom", "qty": 8, "unit": "Sheets", "rate": 4800, "slip": "Slip 1"},
    {"urdu": "لامینیشن", "english": "Lamination / Formica Inner Sheets", "category": "Sheets & Boards", "area": "Bedroom", "qty": 6, "unit": "Sheets", "rate": 2600, "slip": "Slip 1"},
    {"urdu": "2 سوتر PVC", "english": "2 Suter (6mm) PVC Moisture Barrier Backing", "category": "Sheets & Boards", "area": "Bedroom", "qty": 8, "unit": "Sheets", "rate": 3200, "slip": "Slip 1"},
    {"urdu": "پریس ڈور", "english": "Pressed Door / Finished Wardrobe Shutter Panel", "category": "Sheets & Boards", "area": "Bedroom", "qty": 1, "unit": "Pcs", "rate": 2000, "slip": "Slip 1"},
    {"urdu": "لہر 30x60", "english": "PVC Edge Banding / Lipping Strips (30x60)", "category": "Trims & Lipping", "area": "Bedroom", "qty": 20, "unit": "Strips", "rate": 180, "slip": "Slip 1"},
    
    # Slip 1 - Washroom
    {"urdu": "واش روم 3/4 PVC کلو", "english": "3/4\" (18mm) Heavy Density Waterproof PVC Foam Board", "category": "Sheets & Boards", "area": "Washroom", "qty": 8, "unit": "Sheets", "rate": 7800, "slip": "Slip 1"},
    {"urdu": "الماری شٹر لامینیشن", "english": "Washroom Vanity Shutter Lamination Sheet", "category": "Sheets & Boards", "area": "Washroom", "qty": 4, "unit": "Sheets", "rate": 2800, "slip": "Slip 1"},
    {"urdu": "2 سوتر PVC", "english": "2 Suter (6mm) Waterproof PVC Backing Sheet", "category": "Sheets & Boards", "area": "Washroom", "qty": 5, "unit": "Sheets", "rate": 3200, "slip": "Slip 1"},
    {"urdu": "لہر 30x60", "english": "PVC Edge Banding / Lipping Strips (30x60)", "category": "Trims & Lipping", "area": "Washroom", "qty": 20, "unit": "Strips", "rate": 180, "slip": "Slip 1"},
    {"urdu": "قبضہ 7\"", "english": "Concealed Soft-Close Cabinet Hinges 7\"", "category": "Hardware & Hinges", "area": "Washroom", "qty": 40, "unit": "Pcs", "rate": 220, "slip": "Slip 1"},
    {"urdu": "پریس ڈور", "english": "Washroom Press Doors / Vanity Shutters", "category": "Sheets & Boards", "area": "Washroom", "qty": 2, "unit": "Pcs", "rate": 2000, "slip": "Slip 1"},
    {"urdu": "واش روم شیٹر / شٹر", "english": "Washroom Pre-cut Shutters / Board Panels", "category": "Sheets & Boards", "area": "Washroom", "qty": 27, "unit": "Pcs", "rate": 1500, "slip": "Slip 1"},
    
    # Slip 1 - Kitchen
    {"urdu": "کچن 3/4 PVC کلو (UV شیٹ 8 عدد)", "english": "Kitchen 3/4\" (18mm) PVC Board / UV High Gloss Sheet", "category": "Sheets & Boards", "area": "Kitchen", "qty": 8, "unit": "Sheets", "rate": 7500, "slip": "Slip 1"},
    {"urdu": "2 سوتر Back PVC", "english": "Kitchen Backing 2 Suter (6mm) PVC Sheets", "category": "Sheets & Boards", "area": "Kitchen", "qty": 4, "unit": "Sheets", "rate": 3200, "slip": "Slip 1"},
    {"urdu": "شٹر کچن الماری", "english": "Kitchen Cabinet Shutter Panels", "category": "Sheets & Boards", "area": "Kitchen", "qty": 9, "unit": "Sheets", "rate": 4800, "slip": "Slip 1"},
    {"urdu": "پریس ڈور", "english": "Kitchen Press Door Shutters", "category": "Sheets & Boards", "area": "Kitchen", "qty": 9, "unit": "Pcs", "rate": 2000, "slip": "Slip 1"},
    {"urdu": "کچن PVC گولا 16mm", "english": "Kitchen PVC Gola / Aluminum J-Profile Trim (16mm)", "category": "Trims & Lipping", "area": "Kitchen", "qty": 20, "unit": "Pcs", "rate": 320, "slip": "Slip 1"},
    
    # Slip 1 - Extra Finishing & Trims
    {"urdu": "سیٹ تالو / چینل 3", "english": "3-Lever Drawer Lock Set / Telescopic Channels", "category": "Hardware & Hinges", "area": "Hardware", "qty": 3, "unit": "Sets", "rate": 650, "slip": "Slip 1"},
    {"urdu": "لہر 27x60", "english": "PVC Edge Banding / Lipping Strips (27x60)", "category": "Trims & Lipping", "area": "Finishing", "qty": 102, "unit": "Strips", "rate": 160, "slip": "Slip 1"},
    {"urdu": "کاؤنٹر گولا / واش روم گولا", "english": "Countertop / Washroom PVC Edge Molding (Gola)", "category": "Trims & Lipping", "area": "Finishing", "qty": 20, "unit": "Meters", "rate": 250, "slip": "Slip 1"},
    {"urdu": "کیل پٹھے 8x11x1.5", "english": "Hardened Wood & Framing Nails (1.5\")", "category": "Nails & Pins", "area": "Hardware", "qty": 4, "unit": "Boxes", "rate": 450, "slip": "Slip 1"},
    {"urdu": "2 سوتر PVC 27", "english": "2 Suter (6mm) PVC Sheets (Size 27)", "category": "Sheets & Boards", "area": "Panels", "qty": 6, "unit": "Sheets", "rate": 3200, "slip": "Slip 1"},
    {"urdu": "کیل چھتری چپی 1.5x1/2", "english": "Umbrella Head Nails / Cap Screws (1.5\" x 1/2\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 70, "unit": "Pkt/Box", "rate": 180, "slip": "Slip 1"},
    
    # Slip 2 - Black Screws
    {"urdu": "کالے سکرو 3/4 x 6", "english": "Black Gypsum / Countersunk Wood Screws (6 x 3/4\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 6, "unit": "Packets", "rate": 250, "slip": "Slip 2"},
    {"urdu": "کالے سکرو 5/8 x 6", "english": "Black Countersunk Wood Screws (6 x 5/8\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 6, "unit": "Packets", "rate": 240, "slip": "Slip 2"},
    {"urdu": "کالے سکرو 1/2 x 6", "english": "Black Countersunk Wood Screws (6 x 1/2\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 6, "unit": "Packets", "rate": 220, "slip": "Slip 2"},
    {"urdu": "کالے سکرو 2\"", "english": "Heavy Duty Black Wood Screws (2\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 6, "unit": "Packets", "rate": 380, "slip": "Slip 2"},
    {"urdu": "کالے سکرو 6 x 1 1/2", "english": "Black Threaded Wood Screws (6 x 1-1/2\")", "category": "Screws & Fasteners", "area": "Hardware", "qty": 6, "unit": "Packets", "rate": 340, "slip": "Slip 2"},
    {"urdu": "سکرو 1 x 17", "english": "Countersunk Wood Screws / Pins (1\" x 17)", "category": "Screws & Fasteners", "area": "Hardware", "qty": 3, "unit": "Boxes", "rate": 280, "slip": "Slip 2"},
    
    # Slip 2 - Nails, Adhesives & Hinges
    {"urdu": "کیل 2 x 15 TP", "english": "TP Wire / Finishing Pins (2\" x 15 Gauge)", "category": "Nails & Pins", "area": "Hardware", "qty": 6, "unit": "Boxes", "rate": 320, "slip": "Slip 2"},
    {"urdu": "17 x 1 1/2 نمبر TP", "english": "TP Finish Nails / Panel Pins (1.5\" x 17 Gauge)", "category": "Nails & Pins", "area": "Hardware", "qty": 6, "unit": "Boxes", "rate": 300, "slip": "Slip 2"},
    {"urdu": "سٹیل کیل باریک 1\"", "english": "Fine Hardened Concrete / Steel Nails (1\")", "category": "Nails & Pins", "area": "Hardware", "qty": 3, "unit": "Boxes", "rate": 260, "slip": "Slip 2"},
    {"urdu": "سٹیل کیل 3/4\"", "english": "Hardened Steel Nails (3/4\")", "category": "Nails & Pins", "area": "Hardware", "qty": 3, "unit": "Boxes", "rate": 240, "slip": "Slip 2"},
    {"urdu": "سٹیل کیل 2\"", "english": "Heavy Hardened Steel Nails (2\")", "category": "Nails & Pins", "area": "Hardware", "qty": 6, "unit": "Boxes", "rate": 320, "slip": "Slip 2"},
    {"urdu": "سٹیل کیل 2 1/2\"", "english": "Concrete / Hardened Steel Nails (2.5\")", "category": "Nails & Pins", "area": "Hardware", "qty": 6, "unit": "Boxes", "rate": 360, "slip": "Slip 2"},
    {"urdu": "راد / راول کیل 2\"", "english": "Fluted Anchor / Rod Hardened Steel Nails (2\")", "category": "Nails & Pins", "area": "Hardware", "qty": 3, "unit": "Boxes", "rate": 350, "slip": "Slip 2"},
    {"urdu": "3/4 x 20 TP", "english": "TP Wire Panel Pins (3/4\" x 20 Gauge)", "category": "Nails & Pins", "area": "Hardware", "qty": 4, "unit": "Boxes", "rate": 250, "slip": "Slip 2"},
    {"urdu": "سمد بونڈ سلوشن 1 1/2 کلو", "english": "Samad Bond Synthetic Rubber Contact Adhesive (1.5 Kg Tin)", "category": "Adhesives & Tapes", "area": "Hardware", "qty": 3, "unit": "Tins", "rate": 1750, "slip": "Slip 2"},
    {"urdu": "فوم ٹیپ رول", "english": "Double-Sided High-Bond Acrylic Foam Tape Roll", "category": "Adhesives & Tapes", "area": "Hardware", "qty": 1, "unit": "Roll", "rate": 450, "slip": "Slip 2"},
    {"urdu": "گز 3 x 10", "english": "Aluminum / PVC Gaz Trim Profile (Size 3 x 10)", "category": "Trims & Lipping", "area": "Hardware", "qty": 1, "unit": "Box", "rate": 1100, "slip": "Slip 2"},
    {"urdu": "3D قبضہ فل راؤنڈ", "english": "3D Full Overlay Hydraulic Soft-Close Cabinet Hinges", "category": "Hardware & Hinges", "area": "Hardware", "qty": 30, "unit": "Pcs", "rate": 300, "slip": "Slip 2"},
]

# Initialize Session State
if "items" not in st.session_state:
    st.session_state.items = SEED_ITEMS.copy()

# Sidebar: Controls & Settings
with st.sidebar:
    st.title("⚙️ Project Controls")
    st.caption("Carpentry Material & Rate Management System")
    
    project_title = st.text_input("Project Name", "House Woodwork & PVC Cabinetry")
    client_name = st.text_input("Client / Location", "Islamabad / Rawalpindi")
    market_city = st.selectbox("Market Rate Profile", ["Islamabad / Rawalpindi (Golra / Raja Bazar)", "Lahore (Timber Market)", "Karachi (Old City)"])
    
    st.divider()
    
    # Global Rate Adjustment
    st.subheader("📈 Rate & Margin Adjuster")
    margin_pct = st.slider("Market Margin / Contractor Markup (%)", -20, 30, 0, step=5)
    
    st.divider()
    
    st.subheader("🔄 Quick Actions")
    if st.button("Reset to Default 41 Items"):
        st.session_state.items = SEED_ITEMS.copy()
        st.success("Reset successfully!")
        st.rerun()
        
    if st.button("Clear All Items"):
        st.session_state.items = []
        st.warning("All items cleared!")
        st.rerun()

# Main Header
st.title("🪵 Pakistani Woodwork, PVC & Hardware AI Estimator")
st.markdown("### لکڑی، پی وی سی، الماری اور ہارڈویئر کا مکمل تخمینہ لاگت")

# Calculate Totals & Stats
items_df = pd.DataFrame(st.session_state.items)

if not items_df.empty:
    # Apply margin if any
    items_df["adjusted_rate"] = items_df["rate"].apply(lambda r: int(r * (1 + margin_pct / 100)))
    items_df["total_amount"] = items_df["qty"] * items_df["adjusted_rate"]
    
    grand_total = items_df["total_amount"].sum()
    total_items = len(items_df)
    total_sheets = items_df[items_df["category"] == "Sheets & Boards"]["qty"].sum()
    hardware_cost = items_df[items_df["category"].isin(["Hardware & Hinges", "Screws & Fasteners", "Nails & Pins", "Adhesives & Tapes"])]["total_amount"].sum()
    sheets_cost = items_df[items_df["category"] == "Sheets & Boards"]["total_amount"].sum()
else:
    grand_total = 0
    total_items = 0
    total_sheets = 0
    hardware_cost = 0
    sheets_cost = 0

# Metric Cards Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("💰 Total Estimated Cost", f"₨ {grand_total:,.0f}", delta=f"{margin_pct}% Markup" if margin_pct != 0 else None)
c2.metric("📦 Total Line Items", f"{total_items} Items")
c3.metric("🪵 Sheets & Boards Cost", f"₨ {sheets_cost:,.0f}", f"{total_sheets} Sheets")
c4.metric("🔩 Hardware & Fasteners", f"₨ {hardware_cost:,.0f}")

st.divider()

# Tabs Interface
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Interactive Master Bill",
    "➕ Add & Parse Urdu Slips",
    "📊 Analytics & Cost Charts",
    "🔍 Market Rate Catalog",
    "📥 Export & Print Quotation"
])

# -------------------------------------------------------------
# TAB 1: Interactive Master Bill
# -------------------------------------------------------------
with tab1:
    st.subheader("Interactive Bill & Line Item Editor")
    st.caption("You can directly edit quantities, rates, and descriptions in the table below:")
    
    if not items_df.empty:
        # Filter options
        col_f1, col_f2 = st.columns([1, 1])
        with col_f1:
            area_filter = st.multiselect("Filter by Area / Room", options=list(items_df["area"].unique()), default=list(items_df["area"].unique()))
        with col_f2:
            cat_filter = st.multiselect("Filter by Category", options=list(items_df["category"].unique()), default=list(items_df["category"].unique()))
            
        filtered_df = items_df[items_df["area"].isin(area_filter) & items_df["category"].isin(cat_filter)].copy()
        
        # Display editable table
        display_cols = ["urdu", "english", "area", "category", "qty", "unit", "adjusted_rate", "total_amount"]
        rename_dict = {
            "urdu": "Urdu Text (اصل تحریر)",
            "english": "English Description",
            "area": "Area / Room",
            "category": "Category",
            "qty": "Quantity",
            "unit": "Unit",
            "adjusted_rate": "Rate (PKR)",
            "total_amount": "Total Amount (PKR)"
        }
        
        st.dataframe(
            filtered_df[display_cols].rename(columns=rename_dict),
            use_container_width=True,
            height=450
        )
        
        st.markdown(f"#### **Grand Total for Filtered Items: ₨ {filtered_df['total_amount'].sum():,.0f}**")
    else:
        st.info("No items in the list. Use the 'Add & Parse Urdu Slips' tab or click 'Reset to Default' in the sidebar.")

# -------------------------------------------------------------
# TAB 2: Add & Parse Urdu Slips
# -------------------------------------------------------------
with tab2:
    st.subheader("Urdu Slip Scanner & Manual Line Item Entry")
    
    t2_col1, t2_col2 = st.columns([1, 1])
    
    with t2_col1:
        st.markdown("#### 📝 Paste Handwritten Notes / Urdu Slip Text")
        urdu_sample = """بیڈروم الماری
شیٹ شٹر الماری 4+4
لامینیشن 3+3
2 سوتر PVC 4+4
واش روم 3/4 PVC کلو 8 عدد
قبضہ 7 انچ 40 عدد
کالے سکرو 3/4 x 6 پیکٹ 6
سمد بونڈ 1.5 کلو 3 ڈبے"""
        
        pasted_text = st.text_area("Paste carpenter Urdu text here:", value="", height=200, placeholder=urdu_sample)
        
        if st.button("🚀 Parse & Append to Master List"):
            if pasted_text.strip():
                new_items = parse_slip_text(pasted_text)
                for item in new_items:
                    st.session_state.items.append(item)
                st.success(f"Successfully added {len(new_items)} items from Urdu text!")
                st.rerun()
            else:
                st.warning("Please paste some text first!")
                
    with t2_col2:
        st.markdown("#### ➕ Add Single Custom Material")
        with st.form("add_custom_item"):
            c_urdu = st.text_input("Urdu Item Name (e.g. ہائی گلوس شیٹ)", "")
            c_eng = st.text_input("English Name / Spec", "")
            c_area = st.selectbox("Area / Room", ["Bedroom", "Washroom", "Kitchen", "Hardware", "Finishing", "General"])
            c_cat = st.selectbox("Category", get_categories() + ["Other"])
            c_qty = st.number_input("Quantity", min_value=1, value=1)
            c_unit = st.selectbox("Unit", ["Sheets", "Pcs", "Strips", "Meters", "Boxes", "Packets", "Tins", "Roll", "Kg"])
            c_rate = st.number_input("Unit Rate (PKR)", min_value=0, value=1000, step=50)
            
            submitted = st.form_submit_button("Add Item to Bill")
            if submitted:
                st.session_state.items.append({
                    "urdu": c_urdu if c_urdu else c_eng,
                    "english": c_eng if c_eng else c_urdu,
                    "area": c_area,
                    "category": c_cat,
                    "qty": c_qty,
                    "unit": c_unit,
                    "rate": c_rate,
                    "slip": "Custom Entry"
                })
                st.success("Item added successfully!")
                st.rerun()

# -------------------------------------------------------------
# TAB 3: Analytics & Cost Charts
# -------------------------------------------------------------
with tab3:
    st.subheader("Cost Distribution & Visual Analytics")
    
    if not items_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            # Area-wise Breakdown
            area_summary = items_df.groupby("area")["total_amount"].sum().reset_index()
            fig_area = px.pie(
                area_summary,
                values="total_amount",
                names="area",
                title="Cost Breakdown by Area / Room",
                color_discrete_sequence=px.colors.qualitative.Prism,
                hole=0.4
            )
            st.plotly_chart(fig_area, use_container_width=True)
            
        with chart_col2:
            # Category-wise Breakdown
            cat_summary = items_df.groupby("category")["total_amount"].sum().reset_index().sort_values("total_amount", ascending=False)
            fig_cat = px.bar(
                cat_summary,
                x="category",
                y="total_amount",
                title="Expense by Material Category (PKR)",
                text="total_amount",
                color="category"
            )
            fig_cat.update_traces(texttemplate='₨ %{text:,.0f}', textposition='outside')
            st.plotly_chart(fig_cat, use_container_width=True)
            
        st.markdown("#### 🏆 Top 5 Highest Cost Line Items")
        top5 = items_df.sort_values("total_amount", ascending=False).head(5)[["english", "urdu", "qty", "unit", "adjusted_rate", "total_amount"]]
        st.table(top5.rename(columns={
            "english": "Item Name",
            "urdu": "Urdu",
            "qty": "Qty",
            "unit": "Unit",
            "adjusted_rate": "Rate (PKR)",
            "total_amount": "Total (PKR)"
        }))

# -------------------------------------------------------------
# TAB 4: Market Rate Catalog
# -------------------------------------------------------------
with tab4:
    st.subheader("Islamabad & Rawalpindi Market Rate Catalog (Wholesale)")
    st.caption("Prevailing rates from Golra Road, Raja Bazar, and I-9 Timber/PVC Markets")
    
    catalog_list = []
    for k, v in DEFAULT_MARKET_RATES.items():
        catalog_list.append({
            "Item Name": k,
            "Urdu Name (اصل تحریر)": v["urdu"],
            "Category": v["category"],
            "Unit": v["unit"],
            "Min Rate (PKR)": v["min_rate"],
            "Average Rate (PKR)": v["avg_rate"],
            "Max Rate (PKR)": v["max_rate"],
            "Description": v["desc"]
        })
    cat_df = pd.DataFrame(catalog_list)
    st.dataframe(cat_df, use_container_width=True, height=450)

# -------------------------------------------------------------
# TAB 5: Export & Print Quotation
# -------------------------------------------------------------
with tab5:
    st.subheader("Export Formatted Estimate & Quotations")
    
    exp_col1, exp_col2 = st.columns(2)
    
    with exp_col1:
        st.markdown("#### 📗 Excel Spreadsheet Export (`.xlsx`)")
        st.caption("Generates dynamic Excel workbook with formulas, styled borders, and bilingual columns.")
        
        excel_data = generate_excel_bytes(st.session_state.items, project_name=project_title, client_name=client_name)
        
        st.download_button(
            label="📥 Download Excel Estimate (.xlsx)",
            data=excel_data,
            file_name=f"{project_title.replace(' ', '_')}_Estimate.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
    with exp_col2:
        st.markdown("#### 📄 CSV / JSON Raw Data")
        st.caption("Export raw dataset for mobile apps or accounting software.")
        
        csv_data = items_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV Dataset",
            data=csv_data,
            file_name=f"{project_title.replace(' ', '_')}_Data.csv",
            mime="text/csv"
        )
        
    st.divider()
    st.markdown("#### 🖨️ Printable Quotation Preview")
    
    # HTML Invoice Card
    preview_html = f"""
    <div style="background: #ffffff; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px; font-family: sans-serif;">
        <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #1e3a8a; padding-bottom: 12px;">
            <div>
                <h2 style="margin: 0; color: #1e3a8a;">{project_title}</h2>
                <p style="margin: 4px 0 0 0; color: #64748b;">Client: {client_name} | Location: Islamabad / Rawalpindi</p>
            </div>
            <div style="text-align: right;">
                <h3 style="margin: 0; color: #15803d;">Total: ₨ {grand_total:,.0f}</h3>
                <span style="font-size: 12px; color: #64748b;">{len(st.session_state.items)} Items</span>
            </div>
        </div>
    </div>
    """
    st.components.v1.html(preview_html, height=120)
