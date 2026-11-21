# RTX Spark Intelligence: front-end prototype

Prototype web app for the Intel x NVIDIA RTX Spark competitive-intelligence POC (BridgeAI).
Single-page app: plain HTML, CSS and JavaScript. No framework, no build step needed to run it.

## Run it
Open `index.html` in a browser. Any email and password works on the sign-in page (demo gate only).

## Files
| File | What it is |
|---|---|
| `index.html` | The complete app, ready to open or deploy as a static site |
| `src/app.template.html` | The app source, with a `/*__DATA__*/` placeholder |
| `src/data.js` | Verified data: the nine laptops, prices, sources, sourced insights |
| `src/build.py` | Rebuilds `index.html` from the template and `data.js` (`python3 src/build.py`) |

## How the app is organised
- **Sign-in page**: always the first page; a deep link (e.g. `#shelf`) opens after sign-in.
- **Sidebar**: Ask or search (⌘K or /), 7 top tabs, two "Supporting analysis" dropdowns, "For Intel" (Implications, Sources & evidence), Present.
- **Routing**: hash-based (`#overview`, `#shelf`, `#sov`, `#lenses`, `#switchers`, `#rebuttals`, `#partners`, `#laptops`, `#retail`, `#reviews`, `#advertising`, `#social`, `#implications`, `#sources`, `#present`, `#ask`).
- **Every page** opens with a three-part strip: What's happening / What it means for Intel / What Intel should do (`TAKES` in the source).
- **Filters** are per page (`FKEYS` lists which filters each page shows).
- **Tooltips**: the ⓘ text for each card is in `HELP` and `KPI_HELP`.
- **Presentation mode**: 11 slides built from the same data (`SLIDES`); narrated-deck link goes in `NARRATOR_URL`.

## Real vs sample data
- Green "Verified" tags: real, sourced data (laptop line-up, US prices, retailer listings, sourced insights, real quotes).
- Orange "Sample" tags: placeholder numbers until the live data feeds are wired in.
- Sample datasets are the constants near the top of the script (e.g. `ADS_W`, `MENTIONS`, `SOV_CH`, `REBUT`, `PARTNERS`, `SIB`, `PLAT_SENT`). Replace these with the collected data (RTX_Spark_All_Data_v1.xlsx) and switch the tag to "Verified".
- Intel sibling model names in Shelf view are placeholders to confirm.

## Deploy
Static site: deploy the folder as-is (e.g. Vercel, "Other" framework, no build command, output directory = root). Add password protection in the host for the client.
