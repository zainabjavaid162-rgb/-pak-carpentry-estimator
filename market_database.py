"""
Market Rate Database for Carpentry, PVC, and Hardware Materials
Focus Area: Islamabad & Rawalpindi Wholesale Markets (Golra Road, I-9, Raja Bazar, Peshawar Road)
"""

DEFAULT_MARKET_RATES = {
    # 1. Sheets & Boards
    "PVC 3/4 (18mm) Heavy Density": {
        "urdu": "3/4 PVC کلو",
        "category": "Sheets & Boards",
        "unit": "Sheets",
        "avg_rate": 7800,
        "min_rate": 7200,
        "max_rate": 8500,
        "desc": "18mm Waterproof PVC Foam Board (Heavy Density)"
    },
    "PVC 2 Suter (6mm) Backing Sheet": {
        "urdu": "2 سوتر PVC",
        "category": "Sheets & Boards",
        "unit": "Sheets",
        "avg_rate": 3200,
        "min_rate": 2800,
        "max_rate": 3600,
        "desc": "6mm Moisture-Proof PVC Backing Sheet"
    },
    "UV High Gloss / Acrylic Sheet": {
        "urdu": "UV شیٹ / شٹر",
        "category": "Sheets & Boards",
        "unit": "Sheets",
        "avg_rate": 7500,
        "min_rate": 6500,
        "max_rate": 8800,
        "desc": "UV Ultra High Gloss MDF Shutter Sheet"
    },
    "Laminated Shutter Sheet / Super Gloss": {
        "urdu": "شیٹ شٹر الماری",
        "category": "Sheets & Boards",
        "unit": "Sheets",
        "avg_rate": 4800,
        "min_rate": 4200,
        "max_rate": 5600,
        "desc": "Laminated MDF / Chipboard Wardrobe Shutter Sheet"
    },
    "Inner Lamination / Formica Sheet": {
        "urdu": "لامینیشن شیٹ",
        "category": "Sheets & Boards",
        "unit": "Sheets",
        "avg_rate": 2600,
        "min_rate": 2200,
        "max_rate": 3200,
        "desc": "Formica / Melamine Interior Lamination Sheet"
    },
    "Press Door / Shutter Panel": {
        "urdu": "پریس ڈور",
        "category": "Sheets & Boards",
        "unit": "Pcs",
        "avg_rate": 2000,
        "min_rate": 1600,
        "max_rate": 2500,
        "desc": "Pressed and Edged Door / Vanity Shutter Panel"
    },
    "Pre-cut Washroom Shutter": {
        "urdu": "واش روم شٹر",
        "category": "Sheets & Boards",
        "unit": "Pcs",
        "avg_rate": 1500,
        "min_rate": 1200,
        "max_rate": 1800,
        "desc": "Cut-to-size Waterproof Washroom Shutter"
    },

    # 2. Edge Banding & Trims (لہر اور گولا)
    "PVC Edge Banding (Lipping 30x60)": {
        "urdu": "لہر 30x60",
        "category": "Trims & Lipping",
        "unit": "Strips",
        "avg_rate": 180,
        "min_rate": 150,
        "max_rate": 220,
        "desc": "PVC Lipping Strip Size 30x60"
    },
    "PVC Edge Banding (Lipping 27x60)": {
        "urdu": "لہر 27x60",
        "category": "Trims & Lipping",
        "unit": "Strips",
        "avg_rate": 160,
        "min_rate": 130,
        "max_rate": 200,
        "desc": "PVC Lipping Strip Size 27x60"
    },
    "Kitchen PVC Gola 16mm (J-Profile)": {
        "urdu": "کچن PVC گولا 16mm",
        "category": "Trims & Lipping",
        "unit": "Pcs",
        "avg_rate": 320,
        "min_rate": 260,
        "max_rate": 400,
        "desc": "16mm J-Profile Aluminum / PVC Handleless Gola"
    },
    "Countertop / Washroom Molding Gola": {
        "urdu": "کاؤنٹر گولا / واش روم گولا",
        "category": "Trims & Lipping",
        "unit": "Meters",
        "avg_rate": 250,
        "min_rate": 200,
        "max_rate": 320,
        "desc": "Molding Trim Gola for Vanity & Countertops"
    },
    "Gaz Profile Strip 3x10": {
        "urdu": "گز 3 x 10",
        "category": "Trims & Lipping",
        "unit": "Box",
        "avg_rate": 1100,
        "min_rate": 900,
        "max_rate": 1350,
        "desc": "Gaz Threaded / Trim Strip Profile 3x10"
    },

    # 3. Fasteners & Screws (سکرو)
    "Black Wood Screws 6 x 3/4\"": {
        "urdu": "کالے سکرو 3/4 x 6",
        "category": "Screws & Fasteners",
        "unit": "Packets",
        "avg_rate": 250,
        "min_rate": 200,
        "max_rate": 300,
        "desc": "Gypsum / Drywall Black Screws 6 x 3/4\""
    },
    "Black Wood Screws 6 x 5/8\"": {
        "urdu": "کالے سکرو 5/8 x 6",
        "category": "Screws & Fasteners",
        "unit": "Packets",
        "avg_rate": 240,
        "min_rate": 190,
        "max_rate": 280,
        "desc": "Countersunk Black Screws 6 x 5/8\""
    },
    "Black Wood Screws 6 x 1/2\"": {
        "urdu": "کالے سکرو 1/2 x 6",
        "category": "Screws & Fasteners",
        "unit": "Packets",
        "avg_rate": 220,
        "min_rate": 180,
        "max_rate": 260,
        "desc": "Short Black Wood Screws 6 x 1/2\""
    },
    "Black Wood Screws 2\"": {
        "urdu": "کالے سکرو 2\"",
        "category": "Screws & Fasteners",
        "unit": "Packets",
        "avg_rate": 380,
        "min_rate": 320,
        "max_rate": 450,
        "desc": "Heavy Drywall / Wood Screws 2\""
    },
    "Black Wood Screws 6 x 1-1/2\"": {
        "urdu": "کالے سکرو 6 x 1 1/2",
        "category": "Screws & Fasteners",
        "unit": "Packets",
        "avg_rate": 340,
        "min_rate": 280,
        "max_rate": 400,
        "desc": "Countersunk Black Screws 6 x 1.5\""
    },
    "Countersunk Screws 1\" x 17": {
        "urdu": "سکرو 1 x 17",
        "category": "Screws & Fasteners",
        "unit": "Boxes",
        "avg_rate": 280,
        "min_rate": 220,
        "max_rate": 340,
        "desc": "Panel Screws / Pins 1\" x 17"
    },
    "Umbrella Head Screws / Nails (1.5x1/2)": {
        "urdu": "کیل چھتری چپی 1.5x1/2",
        "category": "Screws & Fasteners",
        "unit": "Pkt/Box",
        "avg_rate": 180,
        "min_rate": 140,
        "max_rate": 240,
        "desc": "Cap Screws / Umbrella Head Nails for PVC"
    },

    # 4. Nails & Steel Pins (کیل اور ٹی پی)
    "TP Wire Nails 2\" x 15 Gauge": {
        "urdu": "کیل 2 x 15 TP",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 320,
        "min_rate": 260,
        "max_rate": 380,
        "desc": "TP Finishing Wire Nails 2\" x 15"
    },
    "TP Panel Pins 1.5\" x 17 Gauge": {
        "urdu": "17 x 1 1/2 نمبر TP",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 300,
        "min_rate": 240,
        "max_rate": 360,
        "desc": "TP Fine Finishing Pins 1.5\" x 17"
    },
    "TP Wire Nails 3/4\" x 20 Gauge": {
        "urdu": "3/4 x 20 TP",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 250,
        "min_rate": 200,
        "max_rate": 300,
        "desc": "Fine TP Wire Pins 3/4\" x 20"
    },
    "Hardened Steel Nails Fine 1\"": {
        "urdu": "سٹیل کیل باریک 1\"",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 260,
        "min_rate": 210,
        "max_rate": 320,
        "desc": "Hardened Concrete / Steel Nails 1\""
    },
    "Hardened Steel Nails 3/4\"": {
        "urdu": "سٹیل کیل 3/4\"",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 240,
        "min_rate": 190,
        "max_rate": 290,
        "desc": "Hardened Steel Nails 3/4\""
    },
    "Hardened Steel Nails 2\"": {
        "urdu": "سٹیل کیل 2\"",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 320,
        "min_rate": 260,
        "max_rate": 380,
        "desc": "Heavy Hardened Steel Nails 2\""
    },
    "Hardened Steel Nails 2-1/2\"": {
        "urdu": "سٹیل کیل 2 1/2\"",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 360,
        "min_rate": 300,
        "max_rate": 430,
        "desc": "Heavy Concrete Steel Nails 2.5\""
    },
    "Fluted Anchor Rod Steel Nails 2\"": {
        "urdu": "راد / راول کیل 2\"",
        "category": "Nails & Pins",
        "unit": "Boxes",
        "avg_rate": 350,
        "min_rate": 280,
        "max_rate": 420,
        "desc": "Fluted Rod Anchor Nails 2\""
    },
    "Carpentry Wood & Framing Nails (1.5\")": {
        "urdu": "کیل پٹھے 8x11x1.5",
        "category": "Nails & Pins",
        "unit": "Boxes/Kg",
        "avg_rate": 450,
        "min_rate": 380,
        "max_rate": 530,
        "desc": "Pathe Keel for Carpentry Framing"
    },

    # 5. Hardware, Hinges & Adhesives (قبضہ، سمد بونڈ، تالے)
    "3D Full Overlay Soft-Close Hinges": {
        "urdu": "3D قبضہ فل راؤنڈ",
        "category": "Hardware & Hinges",
        "unit": "Pcs",
        "avg_rate": 300,
        "min_rate": 250,
        "max_rate": 420,
        "desc": "3D Adjustable Hydraulic Soft-Close Hinges"
    },
    "Standard Concealed Soft-Close Hinges 7\"": {
        "urdu": "قبضہ 7\"",
        "category": "Hardware & Hinges",
        "unit": "Pcs",
        "avg_rate": 220,
        "min_rate": 180,
        "max_rate": 280,
        "desc": "Concealed Auto Hinges 7\""
    },
    "3-Lever Drawer Lock Set / Channels": {
        "urdu": "سیٹ تالو / چینل 3",
        "category": "Hardware & Hinges",
        "unit": "Sets",
        "avg_rate": 650,
        "min_rate": 500,
        "max_rate": 850,
        "desc": "3-Lever Lock Set / Telescopic Drawer Slides"
    },
    "Samad Bond Adhesive (1.5 Kg Can)": {
        "urdu": "سمد بونڈ سلوشن 1 1/2 کلو",
        "category": "Adhesives & Tapes",
        "unit": "Tins/Cans",
        "avg_rate": 1750,
        "min_rate": 1550,
        "max_rate": 2000,
        "desc": "Samad Bond Contact Adhesive 1.5 Kg Tin"
    },
    "High-Bond Acrylic Foam Tape Roll": {
        "urdu": "فوم ٹیپ رول",
        "category": "Adhesives & Tapes",
        "unit": "Roll",
        "avg_rate": 450,
        "min_rate": 350,
        "max_rate": 600,
        "desc": "Double Sided High-Strength Foam Tape"
    },
}

def get_categories():
    return sorted(list({item["category"] for item in DEFAULT_MARKET_RATES.values()}))

def lookup_item_rate(query_str):
    q = query_str.lower().strip()
    for name, data in DEFAULT_MARKET_RATES.items():
        if q in name.lower() or q in data["urdu"].lower() or any(w in data["urdu"].lower() for w in q.split()):
            return name, data
    return None, None
