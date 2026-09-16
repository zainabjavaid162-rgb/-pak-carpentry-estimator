"""
Excel Export Utility for Carpentry & Hardware Estimator
Generates multi-sheet formatted .xlsx files with live formulas and styled headers.
"""

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
import io

def generate_excel_bytes(items_list, project_name="Woodwork & Hardware Material Estimate", client_name="Standard Quotation"):
    wb = openpyxl.Workbook()
    
    # Palette
    HEADER_FILL = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    SUB_FILL = PatternFill(start_color="3B82F6", end_color="3B82F6", fill_type="solid")
    ZEBRA_FILL = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    TOTAL_FILL = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    SEC_FILL = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")

    FONT_TITLE = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
    FONT_SUB = Font(name="Segoe UI", size=10, italic=True, color="E2E8F0")
    FONT_TH = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    FONT_URDU = Font(name="Segoe UI", size=10, color="000000")
    FONT_ENG = Font(name="Segoe UI", size=10, color="1E293B")
    FONT_BOLD = Font(name="Segoe UI", size=10, bold=True, color="000000")
    FONT_TOTAL = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")

    THIN = Side(border_style="thin", color="CBD5E1")
    BORDER_DATA = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
    BORDER_TOTAL = Border(left=THIN, right=THIN, top=Side(border_style="medium", color="000000"), bottom=Side(border_style="double", color="000000"))

    # Active sheet
    ws = wb.active
    ws.title = "Detailed Estimate Bill"
    ws.views.sheetView[0].showGridLines = True

    # Title Block
    ws.merge_cells("A1:H1")
    ws["A1"] = f"{project_name.upper()} (تخمینہ لاگت بل)"
    ws["A1"].font = FONT_TITLE
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A2:H2")
    ws["A2"] = f"Client: {client_name} | Location: Islamabad / Rawalpindi Markets | Currency: PKR"
    ws["A2"].font = FONT_SUB
    ws["A2"].fill = HEADER_FILL
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    ws.row_dimensions[1].height = 26
    ws.row_dimensions[2].height = 18

    headers = [
        ("Sr #", 8, "center"),
        ("Original Urdu (اصل تحریر)", 28, "right"),
        ("English Description & Specification", 48, "left"),
        ("Category / Area", 18, "center"),
        ("Quantity", 12, "center"),
        ("Unit", 12, "center"),
        ("Rate (PKR)", 18, "right"),
        ("Total Amount (PKR)", 20, "right")
    ]

    for col_idx, (h_text, width, align) in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_idx, value=h_text)
        cell.font = FONT_TH
        cell.fill = SUB_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(col_idx)].width = width
    ws.row_dimensions[4].height = 26

    cur_row = 5
    for idx, item in enumerate(items_list, 1):
        ws.cell(row=cur_row, column=1, value=idx).alignment = Alignment(horizontal="center", vertical="center")
        
        u_cell = ws.cell(row=cur_row, column=2, value=item.get("urdu", ""))
        u_cell.font = FONT_URDU
        u_cell.alignment = Alignment(horizontal="right", vertical="center")
        
        e_cell = ws.cell(row=cur_row, column=3, value=item.get("english", ""))
        e_cell.font = FONT_ENG
        e_cell.alignment = Alignment(horizontal="left", vertical="center")
        
        ws.cell(row=cur_row, column=4, value=f"{item.get('area', '')} - {item.get('category', '')}").alignment = Alignment(horizontal="center", vertical="center")
        
        q_cell = ws.cell(row=cur_row, column=5, value=item.get("qty", 1))
        q_cell.alignment = Alignment(horizontal="center", vertical="center")
        q_cell.number_format = "#,##0"
        
        ws.cell(row=cur_row, column=6, value=item.get("unit", "Pcs")).alignment = Alignment(horizontal="center", vertical="center")
        
        r_cell = ws.cell(row=cur_row, column=7, value=item.get("rate", 0))
        r_cell.alignment = Alignment(horizontal="right", vertical="center")
        r_cell.number_format = "PKR #,##0"
        
        a_cell = ws.cell(row=cur_row, column=8, value=f"=E{cur_row}*G{cur_row}")
        a_cell.alignment = Alignment(horizontal="right", vertical="center")
        a_cell.font = FONT_BOLD
        a_cell.number_format = "PKR #,##0"
        
        fill = ZEBRA_FILL if idx % 2 == 0 else PatternFill(fill_type=None)
        for col in range(1, 9):
            cell = ws.cell(row=cur_row, column=col)
            cell.border = BORDER_DATA
            if fill.fill_type:
                cell.fill = fill
        
        ws.row_dimensions[cur_row].height = 20
        cur_row += 1

    # Grand Total Row
    ws.merge_cells(start_row=cur_row, start_column=1, end_row=cur_row, end_column=7)
    gt_label = ws.cell(row=cur_row, column=1, value="GRAND TOTAL ESTIMATED COST (PKR / کل رقم):")
    gt_label.font = FONT_TOTAL
    gt_label.alignment = Alignment(horizontal="right", vertical="center")

    gt_amt = ws.cell(row=cur_row, column=8, value=f"=SUM(H5:H{cur_row-1})")
    gt_amt.font = FONT_TOTAL
    gt_amt.alignment = Alignment(horizontal="right", vertical="center")
    gt_amt.number_format = "PKR #,##0"

    for col in range(1, 9):
        cell = ws.cell(row=cur_row, column=col)
        cell.fill = TOTAL_FILL
        cell.border = BORDER_TOTAL
    ws.row_dimensions[cur_row].height = 28

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return output.getvalue()
