# NVIDIA RTX Spark Competitive Intelligence Dashboard & Datasets

Intel x NVIDIA RTX Spark Competitive Intelligence POC (BridgeAI).

This repository contains the interactive intelligence dashboard, all 6 master competitive intelligence Excel workbooks (data period: 20 May – 20 Nov 2026), live retailer CSV exports and snapshots, price history infrastructure, and automated data normalization/verification tooling.

---

## Repository Structure

```
├── RTX_Spark_All_Data_v1.xlsx             # Master compiled workbook (78 sheets: CI, EX, SC, CO) [Untouched]
├── RTX_Spark_CI_Data_v1_latest.xlsx       # Latest CI data pull (includes 48 reviews & 217 Q&As) [Untouched]
├── RTX_Spark_CI_Data_v1.xlsx              # Baseline CI dataset [Untouched]
├── RTX_Spark_Company_Intel_v1.xlsx        # OEM partners, executive profiles, YouTube & transcripts [Untouched]
├── RTX_Spark_Scraper_Data_v1.xlsx         # Explorium firmographics, intent data, and technographics [Untouched]
├── RTX_Spark_Stock_Exchange_Data_v1.xlsx  # Stock quotes, SEC 10-K/10-Q filing hits, Taiwan revenue [Untouched]
├── data/                                  # Live retailer exports, snapshots, and verified data models
│   ├── snapshots/                         # Dated daily scraper snapshots
│   │   └── 2026-11-22/                    # Baseline snapshot dated 2026-11-22 (with captured_at)
│   │       ├── walmart.csv                # Walmart live search & product listings
│   │       ├── bestbuy.csv                # Best Buy live review and product feed
│   │       ├── google_shopping.csv        # Google Shopping competitor listings
│   │       ├── newegg.csv                 # Newegg marketplace pricing and stock
│   │       └── amazon.csv                 # Amazon search export
│   ├── price_history.csv                  # Normalized multi-date price history (seeded with 2026-11-22)
│   ├── excluded/                          # Audited excluded records with documented rationale
│   │   └── unrelated_amazon_reviews.csv   # 35 unrelated budget/student laptop reviews from broad search
│   ├── amazon_reviews_mapped.csv          # Verified RTX Spark Amazon reviews with asin and laptop columns
│   ├── TODO_AMAZON_ASINS.md               # Target ASIN list to re-run reviews scraper by exact ASIN
│   ├── bestbuy_reviews_surface_laptop_ultra.csv  # 8 verified Best Buy reviews (ratings: 4.38★ avg)
│   ├── google_shopping_intel_core_ultra.csv      # 60 live search listings for Intel Core Ultra competitors
│   ├── walmart_nvidia_rtx_spark_laptop.csv       # 10 live Walmart RTX Spark listings & Black Friday deals
│   └── dashboard_data.json                # Single source of truth compiled from clean_and_verify_data.py
├── scripts/                               # Data cleaning, snapshot ingestion, and verification scripts
│   ├── clean_and_verify_data.py           # Normalizes stock, merges GB/UK, verifies heatmap, Q&A, and pairs
│   └── ingest_snapshot.py                 # Normalizes snapshot folder and appends to price_history.csv
├── rtx-spark-intelligence/                # Production web application source
│   ├── index.html                         # Built single-page app (synchronized with root)
│   └── src/
│       ├── app.template.html              # Static single-page application template
│       ├── build.py                       # Injects dashboard_data.json and data.js with build assertions
│       └── data.js                        # Verified laptop configurations & source links
├── index.html                             # Root entrypoint for static deployment (Vercel)
└── vercel.json                            # Vercel deployment configuration
```

---

## Running the Dashboard

The dashboard is a static single-page web app with zero external runtime dependencies.

### Option 1: Direct File
Open `index.html` (or `rtx-spark-intelligence/index.html`) directly in any modern web browser.

### Option 2: Local HTTP Server
Run from the repository root:
```bash
python -m http.server 8080
```
Then navigate to `http://localhost:8080` in your browser.

*Note on Sign-in:* Any email and password can be entered on the initial demo gate.

---

## Rebuilding the Application

The build flow is fully automated. Running the cleaning script followed by the build script updates the dashboard with no manual edits:

```bash
# 1. Clean, normalize, and verify all datasets -> updates data/dashboard_data.json
python scripts/clean_and_verify_data.py

# 2. Ingest dated snapshots into price history (optional if adding new snapshots)
python scripts/ingest_snapshot.py

# 3. Inject data and rebuild both index.html and rtx-spark-intelligence/index.html
python rtx-spark-intelligence/src/build.py
```

`build.py` automatically executes validation assertions:
- Confirms zero occurrences of forbidden/unverified claims (`285H`, `-$3,109`, `100% of sub`).
- Asserts that every headline metric, mention count, shopper concern count, and review score matches `data/dashboard_data.json` exactly.
- Fails the build with exit code 1 if any discrepancy is found.

---

## Data Cleaning & Verification Audit

All figures shown in the dashboard trace directly to repository files:

1. **Stock Normalization & Geographic Standardization**:
   - Stock labels normalized from localized strings into standard categories: `In Stock`, `Pre-Order`, `Limited`, `Out of Stock`, and `No Data`.
   - Merged `UK` and `GB` country codes into `GB` (120 listings total; was 95 GB + 25 UK).
   - Separated 897 retailer category/search page rows (`page_type == 'retailer category/search page'`) from 1,194 specific product listings and price views.

2. **Availability Heatmap Verification (45 Cells)**:
   - 26 of 45 cells verified from `CI_5_Ecommerce`.
   - 19 unsupported regional cells (e.g., China search pages where stock status was unrecorded) are transparently marked as `No Data`.

3. **Competitor Mentions Audit**:
   - 775 verified rival mentions across 2,091 listings:
     - **Intel Core Ultra**: 325 mentions (41.9%)
     - **AMD Ryzen AI**: 304 mentions (39.2%)
     - **Apple MacBook Pro**: 146 mentions (18.8%)

4. **Shopper Q&A Themes Alignment**:
   - Aligned 217 questions from `CI_5b` with raw verified tags:
     - Technical Specifications (RAM/Specs): 116 (`specs`)
     - General Inquiries & Portability: 44 (`other` + `portability`)
     - OS & Software Compatibility: 23 (`compatibility`)
     - Gaming & Graphics: 14 (`gaming`)
     - Pricing & Discounts: 9 (`price`)
     - Battery Life: 7 (`battery`)
     - Display Quality: 4 (`display`)

5. **Amazon Reviews Audit & ASIN Mapping**:
   - 35 Amazon review rows in the raw export captured unrelated budget laptops (e.g. NIMO 15.6", generic student Celeron/Ryzen laptops) from an unconstrained keyword search.
   - These 35 rows were moved to `data/excluded/unrelated_amazon_reviews.csv` with documented exclusion reasons.
   - The 2 verified RTX Spark reviews are preserved in `data/amazon_reviews_mapped.csv` with `asin` and `laptop` columns (Surface Laptop Ultra: `B0HFQVF89X`, 3★; RTX Spark 128GB: `B0DFRTXSPK`, 3★).
   - Added `data/TODO_AMAZON_ASINS.md` with target ASINs for all 9 RTX Spark models to re-run the scraper by ASIN.

6. **Verified Price-Pair Comparisons & Headline Advantage**:
   - Verified like-for-like OEM chassis configurations with matching memory tiers:
     - **HP OmniBook X 14**: OmniBook X 14 RTX Spark 32GB/1TB ($2,499.00 Walmart Black Friday sale) vs HP.com OmniBook X 14 Intel Core Ultra 3K touch 32GB ($2,199.99) → **-$299.01 lower (-12%)**. Abt ($1,899.99, 24GB) and Target ($1,499.99, memory unstated) are shown as labeled secondary reference points.
     - **Lenovo Pro 9n / Yoga Pro 9i**: Pro 9n 32GB/1TB ($2,999.99 Walmart) vs Yoga Pro 9i Aura Edition 32GB ($2,634.99 at Lenovo.com, chip unverified) → **-$365.00 lower (-12%)**.
     - **MSI Prestige 16 Flip**: Prestige N16 Flip AI+ 32GB ($3,299.00 Walmart) vs Prestige 16 Flip Intel Core Ultra 7 32GB ($1,999.99 at Best Buy) → **-$1,299.01 lower (-39%)**.
     - **ASUS ProArt P16**: The $1,390.30 Best Buy listing in `data/google_shopping_intel_core_ultra.csv` is titled "ASUS 16\" OLED Touchscreen Laptop - Intel Core Ultra 7 258V". It is a consumer OLED laptop, not a ProArt workstation chassis. Relabeled `ASUS 16" OLED (Intel Core Ultra 7 258V)`, removed from the ProArt P16 pair, and the previous `-$3,109 / -69%` claim removed. The comparison transparently states: *"No like-for-like Intel ProArt sibling found; the closest ProArt P16 sibling listed is AMD-based ($2,399.00)"*.
   - **Verified Headline Advantage**: **-$300 to -$1,300 lower** acquisition cost for Intel Core Ultra across matching OEM chassis tiers. Both `README.md` and the app display the exact same verified range.

7. **Price History Support**:
   - Seeded snapshot folder `data/snapshots/2026-11-22/` containing individual CSV exports (`walmart.csv`, `bestbuy.csv`, `google_shopping.csv`, `newegg.csv`, `amazon.csv`) with `captured_at`.
   - `scripts/ingest_snapshot.py` compiles snapshots into `data/price_history.csv`.
   - Price trend view displays **"Collecting: needs 2+ snapshots"** until two or more dated snapshots exist, avoiding misleading single-day trend lines.

8. **Missing Views Added**:
   - **Share of Shelf**: Table of 897 retailer search-page rows detailing search query, platform, brand share (Asus 39.5%, Microsoft 36.5%, MSI 13.6%, Lenovo 3.9%, Dell 3.6%, HP 3.0%), chip tier, organic rank position (`Collecting`), and listed price (`No Data` where not priced).
   - **Listing Claims**: Side-by-side comparison of RTX Spark product claims vs. Intel Core Ultra claims extracted strictly from Google Shopping titles and details (`No Data` for unrecorded dimensions).
   - **Seller Mix**: Breakdown of official 1st-party store vs. 3rd-party marketplace fulfillment per laptop across Walmart, Newegg, Best Buy, and eBay.
   - **Reviews Coverage Table**: Per-laptop review counts across Best Buy and Amazon, highlighting that Surface Laptop Ultra is the only model with live review volume (8 Best Buy, 1 Amazon), while 8 of 9 laptops currently have zero buyer reviews in live feeds.

---

## Retail Data Ingestion & Monitoring Pipeline

### Current State
As of **22 November 2026**, one dated baseline snapshot has been ingested into the repository:
- `data/snapshots/2026-11-22/` contains raw exports from Walmart, Best Buy, Google Shopping, Newegg, and Amazon with `captured_at` timestamps.
- Normalized records are stored in `data/price_history.csv` (423 records, 1 snapshot date).
- The repository does not run background scheduled scrapers internally; exports are ingested on demand via `scripts/ingest_snapshot.py`.

### Planned Monitoring Workflow
- Daily snapshots are planned through the end of the Black Friday campaign window (28 November 2026).
- When a new snapshot is exported from Apify or retailer scrapers, place the CSV files in `data/snapshots/YYYY-MM-DD/` and run:
  ```bash
  python scripts/ingest_snapshot.py
  python scripts/clean_and_verify_data.py
  python rtx-spark-intelligence/src/build.py
  ```
- Once 2 or more snapshot dates exist in `data/price_history.csv`, multi-day price trajectory trend lines activate automatically.
