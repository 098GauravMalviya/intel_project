# NVIDIA RTX Spark Competitive Intelligence Dashboard & Datasets

Intel x NVIDIA RTX Spark Competitive Intelligence POC (BridgeAI).

This repository contains the interactive intelligence dashboard and all 6 collected competitive intelligence Excel workbooks (data period: 20 May – 20 Nov 2026).

---

## Repository Structure

```
├── RTX_Spark_All_Data_v1.xlsx             # Master compiled workbook (78 sheets: CI, EX, SC, CO)
├── RTX_Spark_CI_Data_v1_latest.xlsx       # Latest CI data pull (includes 48 reviews & 217 Q&As)
├── RTX_Spark_CI_Data_v1.xlsx              # Baseline CI dataset
├── RTX_Spark_Company_Intel_v1.xlsx        # OEM partners, executive profiles, YouTube & transcripts
├── RTX_Spark_Scraper_Data_v1.xlsx         # Explorium firmographics, intent data, and technographics
├── RTX_Spark_Stock_Exchange_Data_v1.xlsx  # Stock quotes, SEC 10-K/10-Q filing hits, Taiwan revenue
├── rtxsparkintelligence/
│   └── rtx-spark-intelligence/
│       ├── index.html                     # Complete single-page app (verified data loaded)
│       ├── README.md                      # Front-end documentation
│       └── src/
│           ├── app.template.html          # Application source template
│           ├── build.py                   # Rebuilds index.html
│           └── data.js                    # Verified laptop configurations & source links
└── rtxsparkintelligence.zip               # Standalone distribution zip
```

---

## Running the Dashboard

The dashboard is a static single-page web app with zero dependencies.

### Option 1: Direct File
Open `rtxsparkintelligence/rtx-spark-intelligence/index.html` directly in any modern web browser.

### Option 2: Local HTTP Server
Run from the root or the web folder:
```bash
python -m http.server 8080 --directory rtxsparkintelligence/rtx-spark-intelligence
```
Then navigate to `http://localhost:8080` in your browser.

*Note on Sign-in:* Any email and password can be entered on the initial demo gate.

---

## Verified Data Summary
The dashboard datasets have been synchronized and verified against the collected Excel intelligence:
* **SKU Landscape**: 9 launch laptops ($2,599.99 to $3,799.99) verified against official retailer listings.
* **Advertising**: 709 ad creatives across Meta Ad Library, LinkedIn, and Google Ads Transparency.
* **Sentiment & Social**: 10,339 sentiment observations across Reddit, YouTube, Instagram, X, and TikTok.
* **Customer Voice**: 265 customer reviews and shopper Q&A threads from Amazon and Best Buy.
* **Retail & Pricing**: Observed discounts and promotions from Micro Center, Newegg, Best Buy, and OEM stores.
