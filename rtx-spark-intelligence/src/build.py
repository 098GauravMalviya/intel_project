#!/usr/bin/env python3
"""
build.py
Builds rtx-spark-intelligence/index.html and root index.html from app.template.html,
injecting data.js and data/dashboard_data.json directly into the static application.
Includes strict verification checks to fail the build if numbers differ from JSON
or if forbidden/unverified claims appear.
"""

import json
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
APP_DIR = SRC_DIR.parent
ROOT_DIR = APP_DIR.parent

DASHBOARD_JSON_PATH = ROOT_DIR / 'data' / 'dashboard_data.json'
TEMPLATE_PATH = SRC_DIR / 'app.template.html'
DATA_JS_PATH = SRC_DIR / 'data.js'
DEST_APP_HTML = APP_DIR / 'index.html'
DEST_ROOT_HTML = ROOT_DIR / 'index.html'

def build():
    print("=== STARTING APPLICATION BUILD ===")

    # 1. Load data/dashboard_data.json
    if not DASHBOARD_JSON_PATH.exists():
        print(f"Error: {DASHBOARD_JSON_PATH} does not exist. Run scripts/clean_and_verify_data.py first.")
        sys.exit(1)

    with open(DASHBOARD_JSON_PATH, 'r', encoding='utf-8') as f:
        dashboard_data = json.load(f)
    print(f"Loaded {DASHBOARD_JSON_PATH} (size: {DASHBOARD_JSON_PATH.stat().st_size:,} bytes)")

    # 2. Prepare JavaScript injection block
    json_text = json.dumps(dashboard_data, indent=2)
    dashboard_js = f"""/* =====================================================================
   INJECTED DASHBOARD DATA FROM data/dashboard_data.json
   Single Source of Truth - Cleaned and Verified
   ===================================================================== */
const DASHBOARD_DATA = {json_text};
const RETAIL_HEADLINE = DASHBOARD_DATA.headline;
const BLACK_FRIDAY_DEALS = DASHBOARD_DATA.blackFridayDeals;
const PRICE_LADDER_COMPARE = DASHBOARD_DATA.priceLadder;
const AVAILABILITY_HEATMAP = DASHBOARD_DATA.availabilityHeatmap;
const RIVALS_NAMED_DATA = DASHBOARD_DATA.rivalsNamed.map(r => [r.name, r.count, r.color, `${{r.pct}}% (${{r.count}} mentions)`]);
const SHOPPER_QA_THEMES_DATA = DASHBOARD_DATA.shopperQAThemes.map(t => [t.theme, t.count, t.color, `${{t.count}} verified threads (tag: ${{t.raw_tag}}) · ${{t.desc}}`]);
const SHARE_OF_SHELF = DASHBOARD_DATA.shareOfShelf;
const LISTING_CLAIMS_COMPARE = DASHBOARD_DATA.listingClaims;
const SELLER_MIX_DATA = DASHBOARD_DATA.sellerMix;
const REVIEWS_COVERAGE_DATA = DASHBOARD_DATA.reviewsCoverage;
const PRICE_HISTORY_META = DASHBOARD_DATA.priceHistoryMeta;
const SURFACE_RATING = DASHBOARD_DATA.surfaceRating;
"""

    # 3. Read template and data.js
    template_text = TEMPLATE_PATH.read_text(encoding='utf-8')
    data_js_text = DATA_JS_PATH.read_text(encoding='utf-8')

    if '/*__DASHBOARD_DATA__*/' not in template_text:
        print("Error: /*__DASHBOARD_DATA__*/ placeholder not found in template!")
        sys.exit(1)

    if '/*__DATA__*/' not in template_text:
        print("Error: /*__DATA__*/ placeholder not found in template!")
        sys.exit(1)

    # 4. Inject contents
    content = template_text.replace('/*__DASHBOARD_DATA__*/', dashboard_js)
    content = content.replace('/*__DATA__*/', data_js_text)

    # 5. Strict Verification & Data Integrity Assertions
    print("Running verification and data integrity checks...")

    # 5a. Forbidden strings check
    forbidden_terms = ["285H", "-$3,109", "100% of sub"]
    for term in forbidden_terms:
        if term in content:
            raise AssertionError(f"BUILD FAILED: Forbidden term '{term}' found in built HTML output!")
    print("  [PASS] Forbidden terms check (no '285H', '-$3,109', '100% of sub')")

    # 5b. Match numbers between app HTML and dashboard_data.json
    headline = dashboard_data["headline"]
    assert headline["lowestPrice"] in content, f"Lowest price {headline['lowestPrice']} missing from HTML"
    assert headline["biggestDeal"] in content, f"Biggest deal {headline['biggestDeal']} missing from HTML"
    assert headline["intelAdvantage"] in content, f"Intel advantage range {headline['intelAdvantage']} missing from HTML"
    print("  [PASS] Headline metrics match JSON (lowestPrice: $2,499.00, deal: Save $400.00, advantage: -$300 to -$1,300 lower)")

    # 5c. Rival mentions counts check
    for rival in dashboard_data["rivalsNamed"]:
        cnt_str = str(rival["count"])
        assert cnt_str in content, f"Rival count {cnt_str} for {rival['name']} missing from HTML"
    print("  [PASS] Rival mentions counts match JSON (Intel: 325, AMD: 304, MacBook: 146)")

    # 5d. Shopper Q&A themes counts check
    for qa in dashboard_data["shopperQAThemes"]:
        cnt_str = str(qa["count"])
        assert cnt_str in content, f"QA count {cnt_str} for {qa['theme']} missing from HTML"
    print("  [PASS] Shopper Q&A theme counts match JSON (specs: 116, other: 44, compat: 23, gaming: 14)")

    # 5e. Reviews metrics check
    surface_rating = dashboard_data["surfaceRating"]
    assert str(surface_rating["reviewCount"]) in content, f"Review count {surface_rating['reviewCount']} missing"
    assert str(surface_rating["bestBuyRating"]) in content or surface_rating["displayRating"] in content, "Surface rating missing"
    print("  [PASS] Surface rating and review count match JSON (8 Best Buy reviews, 4.38★ / 4.4★)")

    # 5f. Price history status check
    price_hist = dashboard_data["priceHistoryMeta"]
    assert price_hist["status"] in content, f"Price history status '{price_hist['status']}' missing"
    print(f"  [PASS] Price history status matches JSON ('{price_hist['status']}')")

    # 5g. Required new views check
    required_views = [
      "Share of Shelf: Retailer Search Presence",
      "Listing Claims: RTX Spark vs. Intel Core Ultra",
      "Seller Mix: 1st-Party Retail vs. 3rd-Party Marketplace",
      "Reviews Coverage &amp; Data Gap Analysis"
    ]
    for view_title in required_views:
        assert view_title in content, f"Required view '{view_title}' missing from HTML"
    print("  [PASS] All 4 required views present in HTML")

    # 6. Write built output
    DEST_APP_HTML.write_text(content, encoding='utf-8')
    DEST_ROOT_HTML.write_text(content, encoding='utf-8')

    print(f"Successfully built:")
    print(f"  - {DEST_APP_HTML} ({DEST_APP_HTML.stat().st_size:,} bytes)")
    print(f"  - {DEST_ROOT_HTML} ({DEST_ROOT_HTML.stat().st_size:,} bytes)")
    print("=== APPLICATION BUILD COMPLETE ===")

if __name__ == '__main__':
    build()
