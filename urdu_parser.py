"""
Urdu Carpentry Slip Parser & Interpreter
Translates Pakistani carpenter jargon, dimensions, fractions, and sum notations into structured items.
"""

import re
from market_database import DEFAULT_MARKET_RATES, lookup_item_rate

CARPENTRY_DICTIONARY = {
    "شیٹ": "Sheet / Board",
    "شٹر": "Shutter / Cabinet Door",
    "الماری": "Wardrobe / Cupboard / Cabinet",
    "لامینیشن": "Lamination / Formica",
    "سوتر": "Suter (1/8th inch thickness unit, 2 سوتر = 6mm)",
    "کلو": "Heavy / High Density / Kilo grade",
    "واش روم": "Washroom / Bathroom Vanity",
    "کچن": "Kitchen Cabinets",
    "بیڈروم": "Bedroom",
    "لہر": "PVC Edge Banding / Lipping Tape",
    "گولا": "Molding / Trim Profile",
    "قبضہ": "Hinges",
    "پریس ڈور": "Pressed Shutter Door",
    "تالو": "Lock / Drawer Locks",
    "چینل": "Drawer Slide Channels",
    "کیل": "Nails / Wire Pins",
    "سکرو": "Screws",
    "سمد بونڈ": "Samad Bond Adhesive",
    "فوم ٹیپ": "Foam Tape",
    "گز": "Gaz / Profile Strip",
    "پٹھے": "Carpentry Nails / Strips",
    "چھتری": "Umbrella Head",
    "چپی": "Cap / Washers",
    "راول": "Rawl / Anchor Plug / Hardened Rod",
}

def parse_urdu_quantity(qty_str):
    """
    Parses complex quantities like '4+4', '3+3', '2+2', '8 عدد', '20 میٹر'
    """
    qty_str = str(qty_str).strip()
    
    # Check if sum notation like '4+4' or '4 + 4'
    if '+' in qty_str:
        parts = re.findall(r'\d+', qty_str)
        if parts:
            return sum(int(p) for p in parts)
            
    # Extract first integer or float
    digits = re.findall(r'\d+(?:\.\d+)?', qty_str)
    if digits:
        return float(digits[0]) if '.' in digits[0] else int(digits[0])
        
    return 1

def parse_slip_text(raw_text):
    """
    Parses multi-line text pasted from carpenter slip into structured line items.
    """
    lines = raw_text.strip().split('\n')
    parsed_items = []
    current_area = "General / Miscellaneous"
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Detect header lines
        if "بیڈروم" in line:
            current_area = "Bedroom"
            continue
        elif "واش روم" in line:
            current_area = "Washroom"
            continue
        elif "کچن" in line:
            current_area = "Kitchen"
            continue
        elif "ہارڈویئر" in line or "سکرو" in line or "کیل" in line:
            current_area = "Hardware & Fasteners"
            
        # Try finding quantity
        qty_matches = re.findall(r'(\d+(?:\s*\+\s*\d+)?)\s*(?:عدد|میٹر|پیکٹ|ڈبے|کلو|sheets|pcs|boxes)?', line)
        qty = 1
        if qty_matches:
            qty = parse_urdu_quantity(qty_matches[-1])
            
        # Match against market database
        matched_name, matched_data = lookup_item_rate(line)
        
        if matched_data:
            parsed_items.append({
                "urdu": line,
                "english": matched_name,
                "category": matched_data["category"],
                "area": current_area,
                "qty": qty,
                "unit": matched_data["unit"],
                "rate": matched_data["avg_rate"],
                "total": qty * matched_data["avg_rate"]
            })
        else:
            # Fallback entry
            parsed_items.append({
                "urdu": line,
                "english": f"Custom Item ({line})",
                "category": "Other",
                "area": current_area,
                "qty": qty,
                "unit": "Pcs",
                "rate": 500,
                "total": qty * 500
            })
            
    return parsed_items
