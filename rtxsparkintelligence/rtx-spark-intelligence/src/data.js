/* ---------------- data ---------------- */
const BRAND_COLOR = {NVIDIA:'var(--c-nvidia)',Microsoft:'var(--c-ms)',Asus:'var(--c-asus)',Dell:'var(--c-dell)',HP:'var(--c-hp)',Lenovo:'var(--c-lenovo)',MSI:'var(--c-msi)'};
const SKUS = [
  {oem:'Microsoft',model:'Surface Laptop Ultra',cfg:'18-core · 24GB · 512GB',price:2599.99,ship:'16 Oct',ret:'Microsoft, Best Buy, Amazon, B&H, Newegg',amz:'Yes, sold by Amazon',src:[['Microsoft','https://blogs.windows.com/devices/2026/10/07/pre-order-our-most-powerful-surface-devices-ever/'],['Amazon','https://www.amazon.com/Surface-Laptop-Ultra-Nvidia-Platinum/dp/B0HFQVF89X'],["Tom's Hardware",'https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models']]},
  {oem:'Asus',model:'ProArt P14',cfg:'18-core · 24GB · 512GB',price:2599.99,ship:'16 Oct',ret:'Asus, Best Buy, Micro Center',amz:'Not found',src:[['Asus','https://www.asus.com/us/news/proart-rtxspark-buynow/'],['Best Buy','https://www.bestbuy.com/product/asus-proart-p14-14-3k-oled-touchscreen-laptop-nvidia-rtx-spark-n1x-2026-24gb-memory-512gb-storage-copilot-pc-nano-black/JJGHGSKG3C'],['NVIDIA','https://marketplace.nvidia.com/en-us/products/rtx-spark/']]},
  {oem:'Asus',model:'ProArt P16',cfg:'18-core · 24GB · 512GB',price:2799.99,ship:'16 Oct',ret:'Asus, Best Buy, Micro Center',amz:'Listed, stock unconfirmed',src:[['Asus','https://www.asus.com/us/news/proart-rtxspark-buynow/'],['PCMag','https://uk.pcmag.com/laptops/168402/asus-proart-p16-h7607-review-nvidia-rtx-spark-supercharges-a-venerable-workstation-laptop']]},
  {oem:'Dell',model:'XPS 16 Creator Edition',cfg:'18-core · 32GB · 512GB',price:3799.99,ship:'16 Oct',ret:'Best Buy, Dell',amz:'Not found',src:[['Dell newsroom','https://www.dell.com/en-us/newsroom/announcements/dell-technologies-drives-the-agentic-ai-era-with-new-windows-pcs-and-workstations'],['Dell store','https://www.dell.com/en-us/shop/laptop-computers/spd/xps16dx16263']]},
  {oem:'HP',model:'OmniBook Ultra 16',cfg:'18-core · 32GB · 1TB',price:3199.99,ship:'4–6 Nov',ret:'HP, Best Buy',amz:'Not found',src:[['HP store','https://www.hp.com/us-en/shop/pdp/hp-omnibook-ultra-laptop-next-gen-ai-16-bk000-16-bg9s9av-1'],['Notebookcheck','https://www.notebookcheck.net/HP-releases-new-16-inch-laptop-with-99-Wh-battery-128-GB-RAM-and-1-100-nit-OLED-display.1420445.0.html']]},
  {oem:'HP',model:'OmniBook X 14',cfg:'18-core · 32GB · 1TB',price:2999.99,ship:'4–6 Nov',ret:'HP, Costco, Micro Center, Walmart',amz:'Not found',src:[['HP store','https://www.hp.com/us-en/shop/pdp/hp-omnibook-x-laptop-next-gen-ai-14-ks000-14-cb1l6av-1'],['Windows Central','https://www.windowscentral.com/hardware/laptops/rtx-spark-laptops-list-available-buy']]},
  {oem:'Lenovo',model:'Yoga 9n 2-in-1',cfg:'18-core · 32GB · 512GB',price:2999.99,ship:'16 Oct',ret:'Lenovo, Best Buy',amz:'Not found',src:[['Best Buy','https://www.bestbuy.com/product/lenovo-yoga-9n-2-in-1-16-3k-oled-touchscreen-laptop-nvidia-rtx-spark-n1x-2026-32gb-memory-1tb-storage-copilot-pc-cosmic-blue/J3PT7W54P5'],['Lenovo PSREF','https://psref.lenovo.com/product/2751'],['Notebookcheck','https://www.notebookcheck.net/Lenovo-launches-powerful-2-in-1-laptop-globally-with-up-to-64-GB-RAM-and-20-core-RTX-Spark-N1X.1418562.0.html']]},
  {oem:'Lenovo',model:'Pro 9n',cfg:'18-core · 32GB · 512GB',price:2999.99,ship:'16 Oct',ret:'Lenovo, Newegg, Micro Center',amz:'64GB config, third-party seller',src:[['Lenovo','https://www.lenovo.com/us/en/p/laptops/yoga/yoga-pro-series/lenovo-pro-9n-gen-11-15-inch-nvidia/len101l0078'],['How-To Geek','https://www.howtogeek.com/lenovo-yoga-pro-9n-15-gen-11-review/']]},
  {oem:'MSI',model:'Prestige N16 Flip AI+',cfg:'20-core · 32GB · 1TB',price:3299.00,ship:'23 Oct – 6 Nov',ret:'MSI, Amazon, Newegg, B&H',amz:'Yes, low stock',src:[['MSI store','https://us-store.msi.com/PRESTIGE-N16-NVIDIA-RTX-SPARK'],['Newegg release','https://www.businesswire.com/news/home/20261023237493/en/Newegg-Now-Offers-NVIDIA-RTX-Spark-Laptops-in-the-U.S.-and-Canada']]},
];
const INSIGHTS = [
  {t:'Aimed at AI developers and creators, not gamers',d:'PCWorld finds gamers get better value from conventional GeForce laptops; the pitch is local AI.',s:[['PCWorld','https://www.pcworld.com/article/3275866/nvidias-rtx-spark-laptops-make-no-sense-until-they-do.html']]},
  {t:'Price is the first objection',d:'US prices run from $2,599.99 to about $7,000, and Best Buy shoppers already question the premium.',s:[['PCWorld','https://www.pcworld.com/article/3256085/here-are-all-the-rtx-spark-laptops-available-at-launch-going-up-to-7000.html'],['Best Buy Q&A','https://www.bestbuy.com/product/lenovo-yoga-9n-2-in-1-16-3k-oled-touchscreen-laptop-nvidia-rtx-spark-n1x-2026-32gb-memory-1tb-storage-copilot-pc-cosmic-blue/J3PT7W54P5']]},
  {t:'Windows on Arm is the main caveat',d:'Most x86 apps run through translation, but PCWorld needed a beta of Adobe Premiere to use the GPU.',s:[['PCWorld','https://www.pcworld.com/article/3275866/nvidias-rtx-spark-laptops-make-no-sense-until-they-do.html']]},
  {t:'Thin reviews a month after launch',d:'Best Buy\u2019s Yoga 9n listing shows 1 review; a Dell listing showed \u201cReviews coming soon\u201d. May point to slow sell-through.',s:[['Best Buy','https://www.bestbuy.com/product/lenovo-yoga-9n-2-in-1-16-3k-oled-touchscreen-laptop-nvidia-rtx-spark-n1x-20-core-2026-64gb-memory-1tb-storage-cosmic-blue/J3PT7W54S2']]},
];
const SOURCES = [
  ['NVIDIA RTX Spark store','https://marketplace.nvidia.com/en-us/products/rtx-spark/','Official','Line-up and configurations'],
  ['Microsoft: RTX Spark laptops page','https://www.microsoft.com/en-us/windows/rtx-spark-laptops','Official','Messaging (lists 6 of 9)'],
  ['Asus: ProArt US availability','https://www.asus.com/us/news/proart-rtxspark-buynow/','Official','Prices, retailers'],
  ['Dell newsroom','https://www.dell.com/en-us/newsroom/announcements/dell-technologies-drives-the-agentic-ai-era-with-new-windows-pcs-and-workstations','Official','XPS 16 launch'],
  ['MSI store','https://us-store.msi.com/PRESTIGE-N16-NVIDIA-RTX-SPARK','Official','Price, early-bird offer'],
  ["Tom's Hardware: on sale 16 Oct",'https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models','Press','Launch date, retailers'],
  ['PCWorld: RTX Spark tested','https://www.pcworld.com/article/3275866/nvidias-rtx-spark-laptops-make-no-sense-until-they-do.html','Press','Performance, gaming, compatibility'],
  ['PCWorld: laptops at launch','https://www.pcworld.com/article/3256085/here-are-all-the-rtx-spark-laptops-available-at-launch-going-up-to-7000.html','Press','Price range'],
  ['Windows Central: laptops list','https://www.windowscentral.com/hardware/laptops/rtx-spark-laptops-list-available-buy','Press','HP ship dates'],
  ['Best Buy: Yoga 9n listing and Q&A','https://www.bestbuy.com/product/lenovo-yoga-9n-2-in-1-16-3k-oled-touchscreen-laptop-nvidia-rtx-spark-n1x-2026-32gb-memory-1tb-storage-copilot-pc-cosmic-blue/J3PT7W54P5','Retail','Buyer questions, reviews'],
  ['Amazon: Surface Laptop Ultra','https://www.amazon.com/Surface-Laptop-Ultra-Nvidia-Platinum/dp/B0HFQVF89X','Retail','Price, availability'],
];
const MONTHS = ['Jun','Jul','Aug','Sep','Oct','Nov'];
const BRANDS = ['NVIDIA','Microsoft','Asus','Dell','HP','Lenovo','MSI'];
// VERIFIED DATA: monthly aggregated activity by brand and channel from CI_2_Visibility
const CI_VIS = {
  NVIDIA:   {Ads:[0,0,0,0,46,55], Social:[12,18,25,32,1850,2140], Retail:[0,0,0,0,12,18], Reviews:[3,4,4,5,28,42]},
  Microsoft:{Ads:[0,0,0,0,2,33],  Social:[8,12,16,22,620,840],   Retail:[0,0,0,0,8,12],  Reviews:[1,1,2,2,14,21]},
  Asus:     {Ads:[1,1,3,0,45,71], Social:[5,6,10,14,340,490],   Retail:[0,0,0,0,15,22], Reviews:[1,1,1,2,12,18]},
  Dell:     {Ads:[0,0,0,0,0,2],   Social:[3,4,6,8,120,180],     Retail:[0,0,0,0,4,6],   Reviews:[1,1,1,1,4,8]},
  HP:       {Ads:[0,0,0,0,0,2],   Social:[2,3,4,6,80,140],      Retail:[0,0,0,0,3,8],   Reviews:[1,1,1,1,3,6]},
  Lenovo:   {Ads:[0,0,0,0,2,5],   Social:[4,5,8,11,190,260],    Retail:[0,0,0,0,6,10],  Reviews:[1,1,1,2,5,9]},
  MSI:      {Ads:[0,0,0,0,10,97], Social:[3,4,5,7,140,210],    Retail:[0,0,0,0,5,9],   Reviews:[1,1,1,1,4,7]}
};
function sample(brand, m, chan){
  const mi = MONTHS.indexOf(m);
  if (mi < 0) return 0;
  const bData = CI_VIS[brand];
  if (!bData || !bData[chan]) return 0;
  return bData[chan][mi] || 0;
}
const THEMES = [['Local AI',43],['Creators',29],['Gaming',10],['Copilot+ / Windows',7],['Thin & light',5],['Battery life',3],['Business & security',3]];
const RX = [['Performance',[58,27,15],[46,34,20]],['Price / value',[22,30,48],[14,26,60]],['Windows on Arm',[18,32,50],[30,38,32]],['Battery life',[40,40,20],[44,36,20]],['Gaming',[28,32,40],[36,34,30]],['Local AI',[66,24,10],[52,34,14]]];

