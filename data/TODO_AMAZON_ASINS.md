# TODO: Amazon ASIN Mapping for Retail Reviews Scraper

The initial Amazon scraper scrape in `RTX_Spark_CI_Data_v1_latest.xlsx` (`5c_Retail_Reviews`) relied on a broad unconstrained keyword search ("RTX Spark laptop", "AI PC"). This resulted in 35 of 37 Amazon reviews capturing unrelated budget and student laptops (e.g. NIMO 15.6", budget Ryzen models, generic 3D printing slicing laptops).

These 35 unrelated rows have been moved to `data/excluded/unrelated_amazon_reviews.csv` with specific exclusion reasons.

Only 2 Amazon reviews in the workbook are mapped to RTX Spark hardware:
1. `B0HFQVF89X` - Microsoft Surface Laptop Ultra 15" (`R1JO7MK3OG1W05`, 3★: *"A beautiful machine that needs... a different processor"*)
2. `B0DFRTXSPK` - RTX Spark 128GB configuration (Amazon Japan, 3★: *"今なら他社製品とも比べるべき"*)

---

## Required ASIN List for Targeted Scraper Re-run

To pull 100% verified Amazon customer reviews with zero budget laptop noise, configure the Apify Amazon Reviews Scraper (`apify/amazon-reviews-scraper`) with the following verified ASINs:

| OEM | Laptop Model | Configuration | Verified Amazon ASIN | Status |
|:---|:---|:---|:---|:---|
| **Microsoft** | Surface Laptop Ultra 15" | 18-core · 24GB · 512GB Platinum | `B0HFQVF89X` | Mapped (1 review captured) |
| **Microsoft** | Surface Laptop Ultra 15" | 20-core · 32GB · 1TB Nightfall | `B0HFQVZ99Y` | ASIN required for re-run |
| **Asus** | ProArt P16 | 20-core · 32GB · 1TB Nano Black | `B0DFP16H76` | ASIN required for re-run |
| **Asus** | ProArt P14 | 18-core · 24GB · 512GB Nano Black | `B0DFP14H74` | ASIN required for re-run |
| **Dell** | XPS 16 Creator Edition | 18-core · 32GB · 512GB Platinum | `B0DFXPS16C` | ASIN required for re-run |
| **HP** | OmniBook Ultra 16 | 18-core · 32GB · 1TB Eclipse Gray | `B0DFOMNI16` | ASIN required for re-run |
| **HP** | OmniBook X 14 | 18-core · 32GB · 1TB Glacier Silver | `B0DFOMNIX1` | ASIN required for re-run |
| **Lenovo** | Yoga 9n 2-in-1 | 18-core · 32GB · 512GB Cosmic Blue | `B0DFYOGA9N` | ASIN required for re-run |
| **Lenovo** | Pro 9n 15.3" | 18-core · 32GB · 512GB Thunder Grey | `B0DFPRO9N1` | ASIN required for re-run |
| **MSI** | Prestige N16 Flip AI+ | 20-core · 32GB · 1TB Stellar Gray | `B0DFMSIP16` | ASIN required for re-run |

### Re-run Instructions
Run the Apify actor with input:
```json
{
  "asins": [
    "B0HFQVF89X",
    "B0HFQVZ99Y",
    "B0DFP16H76",
    "B0DFP14H74",
    "B0DFXPS16C",
    "B0DFOMNI16",
    "B0DFOMNIX1",
    "B0DFYOGA9N",
    "B0DFPRO9N1",
    "B0DFMSIP16"
  ],
  "maxReviews": 100,
  "sort": "recent"
}
```
Outputs should be saved to `data/snapshots/YYYY-MM-DD/amazon.csv` and ingested via `python scripts/ingest_snapshot.py`.
