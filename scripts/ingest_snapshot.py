#!/usr/bin/env python3
"""
ingest_snapshot.py
Ingests dated snapshot folders from data/snapshots/YYYY-MM-DD/,
normalizes stock, merges UK into GB, separates search/category pages from price views,
and compiles/appends to data/price_history.csv.
"""

import csv
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / 'data'
SNAPSHOTS_ROOT = DATA_DIR / 'snapshots'
PRICE_HISTORY_FILE = DATA_DIR / 'price_history.csv'

def normalize_stock(val):
    if not val:
        return 'No Data'
    v = str(val).strip().lower()
    if any(k in v for k in ['in stock', 'in_stock', 'active', 'left in stock']):
        return 'In Stock'
    if any(k in v for k in ['pre-order', 'pre_order', 'will be released', 'dispatched within 3 to 7 months']):
        return 'Pre-Order'
    if any(k in v for k in ['limited', 'dispatched within 2 to 3 days']):
        return 'Limited'
    if any(k in v for k in ['out of stock', 'out_of_stock', 'temporarily out of stock']):
        return 'Out of Stock'
    return 'In Stock'

def parse_price(val):
    if not val:
        return None
    s = str(val).replace('$', '').replace(',', '').strip()
    try:
        return float(s)
    except ValueError:
        m = re.search(r'([0-9]+\.?[0-9]*)', s)
        return float(m.group(1)) if m else None

def ingest_all():
    print("=== INGESTING SNAPSHOTS ===")
    
    # Standard columns for price_history.csv
    fieldnames = [
        'captured_at',
        'snapshot_date',
        'source',
        'laptop',
        'brand',
        'country',
        'retailer',
        'title',
        'price',
        'list_price',
        'discount_pct',
        'stock',
        'seller',
        'url',
        'page_type'
    ]
    
    all_records = []
    snapshot_dates = sorted([d.name for d in SNAPSHOTS_ROOT.iterdir() if d.is_dir()])
    print(f"Found snapshot directories: {snapshot_dates}")
    
    for s_date in snapshot_dates:
        s_dir = SNAPSHOTS_ROOT / s_date
        
        # 1. Walmart
        wm_file = s_dir / 'walmart.csv'
        if wm_file.exists():
            with open(wm_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    price = parse_price(r.get('price'))
                    was_p = parse_price(r.get('wasPrice') or r.get('wasPriceValue'))
                    disc = float(r.get('discountPercent') or 0.0)
                    
                    # Deduce laptop model
                    name = r.get('name', '')
                    laptop = 'RTX Spark Laptop'
                    brand = 'Unknown'
                    if 'Surface' in name:
                        laptop = 'Surface Laptop Ultra'
                        brand = 'Microsoft'
                    elif 'OmniBook X' in name:
                        laptop = 'OmniBook X 14'
                        brand = 'HP'
                    elif 'Pro 9n' in name:
                        laptop = 'Pro 9n'
                        brand = 'Lenovo'
                    elif 'Prestige' in name:
                        laptop = 'Prestige N16 Flip AI+'
                        brand = 'MSI'
                    elif 'ProArt P16' in name:
                        laptop = 'ProArt P16'
                        brand = 'Asus'
                    elif 'ProArt P14' in name:
                        laptop = 'ProArt P14'
                        brand = 'Asus'
                        
                    all_records.append({
                        'captured_at': r.get('captured_at') or f"{s_date}T00:00:00Z",
                        'snapshot_date': s_date,
                        'source': 'walmart',
                        'laptop': laptop,
                        'brand': brand,
                        'country': 'US',
                        'retailer': 'Walmart',
                        'title': name,
                        'price': price,
                        'list_price': was_p if was_p else price,
                        'discount_pct': disc,
                        'stock': normalize_stock(r.get('availabilityStatus') or ('in stock' if r.get('inStock') == 'true' else 'out of stock')),
                        'seller': r.get('seller') or 'Walmart.com',
                        'url': r.get('url', ''),
                        'page_type': 'product_listing'
                    })
                    
        # 2. Google Shopping
        gs_file = s_dir / 'google_shopping.csv'
        if gs_file.exists():
            with open(gs_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    p = parse_price(r.get('price'))
                    wp = parse_price(r.get('withoutDiscountPrice'))
                    t = r.get('productName', '')
                    k = r.get('searchKeyword', '')
                    
                    brand = 'Unknown'
                    if 'ASUS' in k: brand = 'Asus'
                    elif 'HP' in k: brand = 'HP'
                    elif 'MSI' in k: brand = 'MSI'
                    elif 'Lenovo' in k: brand = 'Lenovo'
                    
                    all_records.append({
                        'captured_at': r.get('captured_at') or f"{s_date}T00:00:00Z",
                        'snapshot_date': s_date,
                        'source': 'google_shopping',
                        'laptop': k,
                        'brand': brand,
                        'country': 'US',
                        'retailer': r.get('merchantName', 'Google Shopping'),
                        'title': t,
                        'price': p,
                        'list_price': wp if wp else p,
                        'discount_pct': round((wp - p)/wp * 100, 1) if (wp and p and wp > p) else 0.0,
                        'stock': 'In Stock',
                        'seller': r.get('merchantName', ''),
                        'url': r.get('productLink', ''),
                        'page_type': 'product_listing'
                    })
                    
        # 3. Newegg, Best Buy, Amazon
        for src_name in ['bestbuy', 'newegg', 'amazon']:
            f_path = s_dir / f"{src_name}.csv"
            if f_path.exists():
                with open(f_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for r in reader:
                        country = r.get('country', 'US')
                        if country == 'UK': country = 'GB'
                        pt = r.get('page_type', 'retailer listing')
                        
                        all_records.append({
                            'captured_at': r.get('captured_at') or f"{s_date}T00:00:00Z",
                            'snapshot_date': s_date,
                            'source': src_name,
                            'laptop': r.get('laptop', ''),
                            'brand': r.get('brand', ''),
                            'country': country,
                            'retailer': r.get('retailer_or_site', src_name),
                            'title': r.get('title', ''),
                            'price': parse_price(r.get('price_usd_equiv') or r.get('price_local')),
                            'list_price': parse_price(r.get('list_price_local')),
                            'discount_pct': float(r.get('discount_pct') or 0.0),
                            'stock': normalize_stock(r.get('stock')),
                            'seller': r.get('seller') or r.get('retailer_or_site', ''),
                            'url': r.get('url', ''),
                            'page_type': 'search_category_page' if 'category/search page' in str(pt).lower() else 'product_listing'
                        })

    print(f"Total normalized records ingested: {len(all_records)}")
    
    # Write price_history.csv
    with open(PRICE_HISTORY_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_records)
        
    print(f"Wrote price history to: {PRICE_HISTORY_FILE}")
    
    # Metadata for dashboard
    unique_dates = sorted(list(set(r['snapshot_date'] for r in all_records)))
    print(f"Unique snapshot dates: {unique_dates} (Count: {len(unique_dates)})")
    
    meta = {
        'totalRecords': len(all_records),
        'uniqueDates': unique_dates,
        'dateCount': len(unique_dates),
        'status': 'Collecting: needs 2+ snapshots' if len(unique_dates) < 2 else 'Active Historical Trajectory',
        'statusNote': '1 daily snapshot captured on 2026-11-22 across 5 sources (Walmart, Best Buy, Google Shopping, Newegg, Amazon). Trend lines activate automatically once 2+ dated snapshots exist.' if len(unique_dates) < 2 else f'Tracking {len(unique_dates)} dates across daily retailer snapshots.'
    }
    
    return meta

if __name__ == '__main__':
    ingest_all()
