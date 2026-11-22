# RTX Spark Intelligence: Front-End Application

Web application for the Intel x NVIDIA RTX Spark competitive-intelligence POC (BridgeAI).
Single-page web application built with HTML, CSS and vanilla JavaScript with zero external runtime dependencies.

## Quick Start
Open `index.html` directly in any modern browser, or run a local static server:
```bash
python -m http.server 8080
```
Any email and password can be entered on the demo sign-in gate.

## Files
| File | Description |
|---|---|
| `index.html` | Complete built application, ready to open or deploy to static hosts (Vercel) |
| `src/app.template.html` | Application HTML/JS template containing view rendering and verified datasets |
| `src/data.js` | Verified laptop configurations, visibility metrics, and source links |
| `src/build.py` | Build script that compiles `app.template.html` and `data.js` into `index.html` |

## Rebuilding
Run from the repository root:
```bash
python rtx-spark-intelligence/src/build.py
```

## Verified Data Feeds
All data components in this application are synchronized with verified datasets from `RTX_Spark_All_Data_v1.xlsx`, `RTX_Spark_CI_Data_v1_latest.xlsx`, and live retail scrapers in `data/`:
- **Retail & Black Friday Tracker**: Live snapshots from Walmart, Best Buy, Newegg, and OEM stores (deals through 28 Nov 2026).
- **Price Ladder vs Intel & Mac M5**: Verified tier comparisons based on 60 Google Shopping search listings and official retailer pages.
- **Availability Heatmap**: 26 verified regional cells with 19 unmonitored cells transparently noted as "No Data".
- **Competitor Mentions**: Verified counts across 2,091 listings (Intel 325, AMD 304, MacBook 146).
- **Shopper Q&A Themes**: 217 questions mapped to verified raw tags (specs 116, other/portability 44, compatibility 23, gaming 14, price 9, battery 7, display 4).
- **Buyer Ratings & Complaints**: 8 verified Best Buy reviews for Surface Laptop Ultra (4.38★ / 4.4★ avg) and mapped Amazon reviews.
