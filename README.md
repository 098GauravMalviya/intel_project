# NVIDIA RTX Spark Competitive Intelligence Dashboard & Datasets

Intel x NVIDIA RTX Spark Competitive Intelligence POC (BridgeAI).

This repository contains the interactive intelligence dashboard, all 6 master competitive intelligence Excel workbooks (data period: 20 May – 20 Nov 2026), live retailer CSV exports, and data normalization/verification tooling.

---

## Repository Structure

```
├── RTX_Spark_All_Data_v1.xlsx             # Master compiled workbook (78 sheets: CI, EX, SC, CO)
├── RTX_Spark_CI_Data_v1_latest.xlsx       # Latest CI data pull (includes 48 reviews & 217 Q&As)
├── RTX_Spark_CI_Data_v1.xlsx              # Baseline CI dataset
├── RTX_Spark_Company_Intel_v1.xlsx        # OEM partners, executive profiles, YouTube & transcripts
├── RTX_Spark_Scraper_Data_v1.xlsx         # Explorium firmographics, intent data, and technographics
├── RTX_Spark_Stock_Exchange_Data_v1.xlsx  # Stock quotes, SEC 10-K/10-Q filing hits, Taiwan revenue
├── data/                                  # Live retailer scraper exports & clean data models
│   ├── bestbuy_reviews_surface_laptop_ultra.csv  # 8 verified Best Buy reviews (ratings: 4.38★ avg)
│   ├── google_shopping_intel_core_ultra.csv      # 60 live search listings for Intel Core Ultra competitors
│   ├── walmart_nvidia_rtx_spark_laptop.csv       # 10 live Walmart RTX Spark listings & Black Friday deals
│   └── dashboard_data.json                       # Clean compiled JSON data models
├── scripts/                               # Data cleaning and pipeline verification scripts
│   └── clean_and_verify_data.py                  # Normalizes stock, merges GB/UK, audits heatmap & mentions
├── rtx-spark-intelligence/                # Production web application source
│   ├── index.html                         # Built single-page app (synchronized with root)
│   ├── README.md                          # Front-end documentation
│   └── src/
│       ├── app.template.html              # Application source template
│       ├── build.py                       # Rebuilds index.html from template and data.js
│       └── data.js                        # Verified laptop configurations & source links
├── index.html                             # Root entrypoint for static deployment (Vercel)
└── vercel.json                            # Vercel deployment configuration
```

---

## Running the Dashboard

The dashboard is a static single-page web app with zero dependencies.

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

To clean the raw datasets and rebuild the static dashboard:
```bash
# 1. Clean, normalize, and verify all datasets
python scripts/clean_and_verify_data.py

# 2. Rebuild index.html (both root and rtx-spark-intelligence/index.html)
python rtx-spark-intelligence/src/build.py
```

---

## Data Cleaning & Verification Audit

All datasets have been audited and verified against the raw intelligence workbooks:
1. **Stock Normalization & Geographic Standardization**:
   - Stock labels normalized from localized strings into standard categories: `In Stock`, `Pre-Order`, `Limited`, `Out of Stock`, and `No Data`.
   - Merged `UK` and `GB` country codes into `GB` (120 listings total; was 95 GB + 25 UK).
   - Separated 897 category and search page views (`page_type == 'retailer category/search page'`) from 1,194 specific product listings and price views.
2. **Regional Availability Heatmap**:
   - 26 of 45 cells verified from `CI_5_Ecommerce`.
   - 19 unsupported regional cells (e.g., China search pages where stock status was unrecorded) are transparently marked as `No Data`.
3. **Competitor Mentions**:
   - Verified 775 rival mentions across 2,091 listings:
     - **Intel Core Ultra**: 325 mentions (41.9%)
     - **AMD Ryzen AI**: 304 mentions (39.2%)
     - **Apple MacBook Pro**: 146 mentions (18.8%)
4. **Shopper Q&A Themes**:
   - Aligned 217 questions from `CI_5b` with verified tags:
     - Technical Specifications (RAM/Specs): 116 (`specs`)
     - General Inquiries & Portability: 44 (`other` + `portability`)
     - OS & Software Compatibility: 23 (`compatibility`)
     - Gaming & Graphics: 14 (`gaming`)
     - Pricing & Discounts: 9 (`price`)
     - Battery Life: 7 (`battery`)
     - Display Quality: 4 (`display`)
5. **Surface Laptop Ultra Reviews**:
   - Best Buy verified rating: **4.38★** (4.4★) from 8 reviews (`[5, 4, 5, 1, 5, 5, 5, 5]`).
   - Mapped Amazon review `R1JO7MK3OG1W05` (3★) directly to Surface Laptop Ultra.
   - Documented 35 unmapped Amazon rows as generic third-party budget laptop scrapes.
6. **Price Ladder & Verified Chassis Differences**:
   - Intel Core Ultra configurations span $829 to $2,635 across 6 major OEM models.
   - Intel delivers **$300 to $1,550 lower acquisition cost** across matching OEM chassis tiers:
     - Lenovo: Pro 9n ($2,999.99) vs Yoga Pro 9i Core Ultra 9 ($2,634.99 at Lenovo.com) → -$365 lower (-12%)
     - MSI: Prestige N16 Flip ($3,299.00) vs Prestige 16 Flip Core Ultra 7 ($1,999.99 at Best Buy) → -$1,300 lower (-39%)
     - HP: OmniBook X 14 N1X ($2,499 sale / $2,899 MSRP) vs OmniBook X Core Ultra 7 24GB ($1,899.99 at Abt / $1,499.99 at Target) → -$600 to -$1,000 lower (-24% to -40%)
     - ASUS: ProArt P16 N1X ($4,499.99) vs ProArt P16 Core Ultra 7 258V ($1,390.30 at Best Buy) → -$3,109 lower (-69%)
   - Dell XPS 16 updated to current Intel Core Ultra model ($2,249.99 at Best Buy).
   - Apple MacBook Pro 16" updated to **M5** ($2,499.00 list price).

---

## Apify Monitoring & Black Friday Tracking Pipeline

Automated daily price, stock, and promo monitoring is scheduled daily through **28 November 2026**:
* **Walmart** (`walmart-scraper`): Tracks HP OmniBook X 14" ($400 discount ending 28 Nov) and Surface Laptop Ultra ($2,599.99 regular MSRP).
* **Best Buy** (`bestbuy-product-reviews`): Daily review sentiment, verified purchase flag, and rating tracking.
* **Google Shopping** (`google-shopping-scraper`): 60+ live competitor listings across US retail merchants.
* **Amazon & Keepa** (`amazon-product-keepa`): Bestseller rank and historical buy-box seller mix.
* **Newegg** (`newegg-scraper`): Marketplace seller pricing and stock availability.
