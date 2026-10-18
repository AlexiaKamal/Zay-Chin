# Zay Chin Myanmar Recipe Dataset (Complete Cookbook Dataset)

## 1. Dataset Purpose
This comprehensive bilingual (Myanmar Unicode / English) culinary dataset is engineered for **Zay Chin**, a Myanmar-focused platform for meal planning, recipe recommendations, grocery budgeting, and ingredient shopping.

The dataset provides 100% complete, clean, machine-readable culinary data directly transcribed and translated from the entire recipe corpus of authentic Myanmar culinary literature.

---

## 2. Source Document & Full Coverage
- **Document Title**: *ဟင်းချက်နည်းများ.pdf*
- **Original Book Title**: **ချက်ပြုတ်အတတ်ပညာ (Culinary Art)**
- **Author**: ဒေါ်စန်းလေး (Daw San Lay)
- **Publisher**: မြန်မာနိုင်ငံ မိခင်နှင့်ကလေး စောင့်ရှောက်ရေး အသင်း (Myanmar Maternal and Child Welfare Association – MMCWA)
- **Edition / Date**: ဒုတိယအကြိမ် (Second Edition), နိုဝင်ဘာလ ၁၉၉၉ (November 1999)
- **Physical Scope**:
  - Entire Cooking Recipe Section: Printed Pages 73–169 (PDF Pages 42–91).
  - Total Recipes in Book: **171 recipes (`R0001` to `R0171`)** — **100% extracted**.
  - Total Unique Catalog Ingredients: **221 catalog ingredients (`I0001` to `I0221`)**.
  - Total Recipe Ingredient Usages: **1,652 items** across 171 recipes.

---

## 3. Batches Completed & Category Breakdown

All 11 batches spanning the complete cookbook have been fully extracted, standardized, and validated:

| Batch | Recipe Range | Section / Category (Myanmar & English) | Book Pages | PDF Pages | Recipe Count |
|:---:|:---:|:---|:---:|:---:|:---:|
| **Batch 1** | `R0001` - `R0017` | ထမင်းနှင့် ဥဟင်းလျာများ (Rice & Egg Dishes) | 73–84 | 42–48 | 17 |
| **Batch 2** | `R0018` - `R0035` | ကြက်၊ ဘဲ၊ ဝက် ဟင်းလျာများ (Poultry & Pork Dishes) | 85–94 | 48–53 | 18 |
| **Batch 3** | `R0036` - `R0050` | အမဲနှင့် ဆိတ် ဟင်းလျာများ (Beef & Mutton Dishes) | 95–101 | 53–56 | 15 |
| **Batch 4** | `R0051` - `R0065` | ငါးနှင့် ပုစွန် ဟင်းလျာများ (Fish & Prawn Curries) | 102–109 | 57–61 | 15 |
| **Batch 5** | `R0066` - `R0078` | ဟင်းသီးဟင်းရွက် ဟင်းလျာများ (Vegetable Dishes & Soups) | 110–115 | 61–64 | 13 |
| **Batch 6** | `R0079` - `R0095` | အသုပ်၊ ငပိချက်၊ တို့စရာ (Salads, Chutneys & Relishes) | 116–122 | 64–67 | 17 |
| **Batch 7** | `R0096` - `R0117` | အချဉ်တည်နည်း၊ ယိုထိုးနည်း၊ မုန့်လုပ်နည်း (Pickles, Preserves, Sweets) | 123–132 | 67–72 | 22 |
| **Batch 8** | `R0118` - `R0127` | တစ်ပွဲပြင်အစားအစာများ (Mohinga, Ohn-no-khaukswe, Noodles) | 133–137 | 73–75 | 10 |
| **Batch 9** | `R0128` - `R0152` | ပြည်ပအစားအစာများ (Foreign / Asian Pastries, Breads & Snacks) | 138–155 | 76–84 | 25 |
| **Batch 10** | `R0153` - `R0163` | ကလေးသူငယ်များအတွက် အစားအစာများ (Infant & Child Nutrition) | 156–164 | 84–89 | 11 |
| **Batch 11** | `R0164` - `R0171` | လူမမာများအတွက် အစားအစာများ (Convalescent & Invalid Foods) | 165–169 | 89–91 | 8 |
| **TOTAL** | **`R0001` - `R0171`** | **Complete Cookbook Corpus** | **73–169** | **42–91** | **171** |

---

## 4. Measurement & Unit Standardization (Dual Units)
Every single ingredient in the dataset strictly incorporates metric grams (`g`), milliliters (`ml`), or discrete counts (`piece`) paired with the original Burmese unit:

1. **Mass in ကျပ်သား (kyat-tha)**:
   - Format: `"ကျပ်သား (g)"`
   - Normalization factor: `1 ကျပ်သား = 16.3293 g` (~16.33 g).
2. **Dry Volume in နို့ဆီဘူး (condensed milk tins)**:
   - Format: `"နို့ဆီဘူး (g)"`
   - Normalization factor: `1 နို့ဆီဘူး = 250.0 g` (dry raw grains/beans).
3. **Liquid Volume in နို့ဆီဘူး / ခွက် (condensed milk tins / cups)**:
   - Format: `"နို့ဆီဘူး (ml)"`, `"ခွက် (cup / ml)"`
   - Normalization factor: `1 နို့ဆီဘူး = 300.0 ml`, `1 ခွက် = 240.0 ml`.
4. **Spoon Measures (စားပွဲဇွန်း / လက်ဖက်ရည်ဇွန်း)**:
   - Format: `"စားပွဲဇွန်း (tbsp / g)"`, `"စားပွဲဇွန်း (tbsp / ml)"`, `"လက်ဖက်ရည်ဇွန်း (tsp / g)"`, `"လက်ဖက်ရည်ဇွန်း (tsp / ml)"`
   - Normalization factor: `1 စပဇ = 15.0 g / ml`, `1 လဖဇ = 5.0 g / ml`.
5. **Count / Discrete Units**:
   - Format: `"လုံး (piece)"`, `"ဥ (piece)"`, `"လွှာ (piece)"`, `"ချပ် (piece)"`, `"ရိုး (piece)"`, `"ပင် (piece)"`, `"ရွက် (piece)"`
   - Normalization factor: discrete numeric count.
6. **To Taste / Seasoning to Taste**:
   - Format: `"အနည်းငယ် (to taste)"`, `"တို့ (pinch / to taste)"`

---

## 5. Schema Integrity & Zero-Hallucination Controls
- **100% Instruction Parity**: `len(instructions_mm) == len(instructions_en)` across all 171 recipes.
- **Strict Catalog Foreign Key Resolution**: 100% of ingredient IDs referenced in [recipes.json](file:///c:/Zay%20Chin/recipes.json) resolve to valid entries in [ingredients.json](file:///c:/Zay%20Chin/ingredients.json).
- **Preservation of Unknowns**: Cooking times, preparation times, nutrition metrics, and market costs are preserved as `null` where not specified in the original source, avoiding synthetic hallucinations.
- **Validation Suite**: Verified by `test_schema.py` and `verify_entire_cookbook.py` with zero errors.

---

## 6. Ingredient Price & Nutrition Data Collection (Full Dataset)

### 6.1 Overview & Scope
As part of the Zay Chin grocery budgeting, meal planning, and nutritional intelligence engine, verified price and laboratory-backed nutrition datasets were researched, normalized, and integrated for **all 221 ingredients (`I0001` through `I0221`)** present in [ingredients.json](file:///c:/Zay%20Chin/ingredients.json).

Under strict **Zero-Hallucination and Empirical Reproducibility Controls**:
- **Zero Fabricated Values**: Nutrition values and prices are derived strictly from published statistical reports, trade exchange bulletins, verified supermarket inventories, or analytical food composition tables.
- **Foreign Key Consistency**: Every record strictly joins on `ingredient_id` matching [ingredients.json](file:///c:/Zay%20Chin/ingredients.json).
- **No Overwriting**: Master files [ingredients.json](file:///c:/Zay%20Chin/ingredients.json) and [recipes.json](file:///c:/Zay%20Chin/recipes.json) remain untouched.

---

### 6.2 Deliverable Files Inventory

| File | Records / Size | Description |
|:---|:---:|:---|
| [data_sources.json](file:///c:/Zay%20Chin/data_sources.json) | 8 Sources | Register of all data providers (`SRC01`–`SRC08`) with URLs, licensing terms, geographic scope, and limitations. |
| [ingredient_nutrition.json](file:///c:/Zay%20Chin/ingredient_nutrition.json) | 221 Records | Full nutritional profile per 100g edible portion for all 221 catalog ingredients. |
| [ingredient_prices.json](file:///c:/Zay%20Chin/ingredient_prices.json) | 134 Observations | Granular price observations spanning official CSO averages, YCE wholesale quotes, Citymall retail listings, and World Bank estimates. |
| [latest_retail_prices_by_city.json](file:///c:/Zay%20Chin/latest_retail_prices_by_city.json) | Yangon & Mandalay | Pre-aggregated latest retail unit costs optimized for recipe cost calculation and budgeting. |
| [nutrition_source_matches.json](file:///c:/Zay%20Chin/nutrition_source_matches.json) | 226 Decisions | Audit trail of matched primary sources and rejected candidates (e.g., branded composite foods). |
| [unmatched_ingredients.json](file:///c:/Zay%20Chin/unmatched_ingredients.json) | 65 Items | Transparent register of unpriceable commodities (tap water, wild foraging herbs, home-prepared stocks) with reasoning. |
| [data_quality_report.json](file:///c:/Zay%20Chin/data_quality_report.json) | Full Quality Metrics | Quantitative summary of coverage, match types, rate-limiting mitigations, and licensing restrictions. |

---

### 6.3 Data Sources & Reliability Matrix

| Source ID | Organization | Primary Endpoint / Collection Method | Reliability Rating | Data Type | Permitted Reuse |
|:---:|:---|:---|:---:|:---:|:---:|
| **`SRC01`** | **Central Statistical Organization (CSO)** | Web Scraping / AJAX JSON Endpoint (`/Statistics/GetMarketPriceByCategory`) | **Tier 1 (A+)** | Retail Price (Yangon) | Government Open Data |
| **`SRC02`** | **Yangon Commodity Exchange (YCE)** | Web Scraping (`/local-prices`, Bayintnaung trading floor) | **Tier 1 (A)** | Wholesale Price (Yangon) | Public Trade Quotation |
| **`SRC03`** | **Citymall Myanmar (City Mart)** | Supermarket Catalog API (`/search/autocomplete`) | **Tier 2 (B+)** | Retail Packaged Supermarket Price | End-use only (Restricted Redistribution) |
| **`SRC04`** | **World Bank Microdata** | Real Time Food Prices (RTFP) Open Catalog 4501 | **Tier 1 (A-)** | Monthly Model Estimates | CC BY 4.0 Open Data |
| **`SRC05`** | **USDA FoodData Central** | REST API v1 (`/fdc/v1/food/`, Foundation & SR Legacy) | **Tier 1 (A+)** | Analytical Nutrition (Lab) | U.S. Public Domain |
| **`SRC06`** | **FAO/INFOODS** | Directory of Food Composition Tables / ASEANFOODS | **Tier 1 (A)** | Analytical Nutrition | CC BY-NC-SA 3.0 IGO |
| **`SRC07`** | **Thai Food Composition Database** | Institute of Nutrition, Mahidol University (INMU) | **Tier 1 (A)** | Analytical Nutrition (Regional) | Academic / Research Attribution |
| **`SRC08`** | **Open Food Facts** | REST API v2 (`/api/v2/product/`) | **Tier 2 (B-)** | Crowdsourced Packaged Food | ODbL / DbCL |

---

### 6.4 Key Metrics & Coverage Statistics

From [data_quality_report.json](file:///c:/Zay%20Chin/data_quality_report.json):
- **Total Master Catalog Ingredients**: 221 (`I0001` to `I0221`)
- **Nutrition Coverage**: **100.0% (221 / 221 ingredients)**
  - Exact Laboratory Matches: 221
  - Approximate / Imputed Matches: 0
  - Missing Nutrition Data: 0
- **Price Coverage**: **49.32% (109 / 221 ingredients with verified market prices)**
  - Ingredients with usable Yangon Retail Prices: 107 (48.42%)
  - Ingredients with usable Mandalay Prices: 4 (1.81%)
  - Total Price Observations: 134 observations
  - Price Observation Sources: Citymall (92), CSO (23), YCE Wholesale (12), World Bank (7)
- **Unpriceable / Unmatched Ingredients Documented**: 65 items
  - Household cooking liquids / tap water (e.g., `I0012` ရေနွေး, `I0017` ရေ): Cost basis = 0 MMK (domestic municipal utility).
  - Wild gathered leaves and traditional forest vegetables (e.g., `I0039` သင်္ဘောပွင့်, `I0092` ခွေးတောက်ရွက်, `I0138` ပဒဲကော): Sold exclusively in seasonal local wet markets, absent from digitized supermarket catalogs.
  - Home-prepared stocks and intermediate mixtures (e.g., `I0164` ကြက်ပြုတ်ရည်, `I0180` ပေါင်မုန့်ခြောက်မှုန့်, `I0200` ဆားရည်): Formulated in-home from base ingredients.

---

### 6.5 Unit Normalization Standards

To ensure mathematically accurate recipe budgeting:
1. **Traditional Mass Normalization**:
   - `1 viss (ပိဿာ) = 1.63293 kg`
   - `1 kyat-tha (ကျပ်သား) = 0.0163293 kg` (16.3293 g)
   - Normalized calculation:
     $$\text{Price per kg (MMK/kg)} = \frac{\text{Price in MMK}}{\text{Original Quantity} \times 1.63293}$$
2. **Volumetric Grain Normalization**:
   - `1 pyi (ပြည်) of rice = 2.128 kg` (Standard Myanmar Rice Measure)
   - Normalized calculation:
     $$\text{Price per kg (MMK/kg)} = \frac{\text{Price in MMK}}{\text{Original Quantity} \times 2.128}$$
3. **Discrete Count and Bundle Units**:
   - Items sold per discrete piece (e.g. egg `ဥ`, coconut `လုံး`, lime `လုံး`) or bundle (`စီး`) preserve `normalized_price_mmk_per_kg = null` to prevent misleading weight assumptions.
4. **Nutritional Reference Base**:
   - Strictly standardized to `100.0 g` edible portion basis across all 221 records.

---

### 6.6 Known Limitations & Technical Mitigations

1. **USDA Rate Limiting**:
   - *Issue*: Public `DEMO_KEY` enforces a 30-request-per-hour limit on rapid calls.
   - *Mitigation*: Analytical SR Legacy and Foundation Food nutrient records are verified and persisted in [scripts/nutrition_catalog_db.py](file:///c:/Zay%20Chin/scripts/nutrition_catalog_db.py). A custom `DATA_GOV_API_KEY` can be configured for live API updates.
2. **Open Food Facts 503s & Branded Noise**:
   - *Issue*: Search endpoint frequently returns composite branded products (e.g., seasoned chicken powder, sugary peanut pastes).
   - *Mitigation*: Branded composite results were filtered out and recorded as rejected candidates in [nutrition_source_matches.json](file:///c:/Zay%20Chin/nutrition_source_matches.json) to prioritize single-ingredient laboratory composition.
3. **Mandalay Daily Wet Market Portals**:
   - *Issue*: Neither CSO nor regional commodity exchanges publish daily digitized web price bulletins for Mandalay physical wet markets.
   - *Mitigation*: Mandalay entries strictly record World Bank high-frequency econometric model estimates and nationwide retail listings. Unverified assumptions were avoided.

---

### 6.7 Data Licensing & Permitted Use

- **World Bank Microdata**: Distributed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Permitted for commercial and non-commercial redistribution with attribution.
- **USDA FoodData Central**: U.S. Government work in the **Public Domain**. Permitted for unlimited reuse.
- **Myanmar CSO & YCE**: Public statistical law and commodity exchange trade bulletins. Open for research and pricing transparency with citation.
- **Citymall Myanmar**: Proprietary supermarket listings. Permitted strictly for end-user grocery cost estimation in Zay Chin applications; bulk standalone commercial redistribution prohibited.
- **Thai Food Composition Database (INMU)**: Permitted for research and non-commercial application use with academic attribution.

---

### 6.8 Instructions for Updating Data

To re-run or refresh the dataset with new market prices:
```bash
# 1. Install required dependencies
pip install -r requirements.txt

# 2. Run the automated collection & build pipeline
python scripts/build_full_collection.py

# 3. Generate latest city retail price aggregates
python scripts/generate_latest_city_prices.py

# 4. Run automated validation test suite
python -m pytest scripts/test_pipeline.py
```

