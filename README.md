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
