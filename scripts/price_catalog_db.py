# Comprehensive Price Database for Zay Chin Catalog
# Sourced from CSO, Yangon Commodity Exchange (Bayintnaung), Citymall Myanmar, and World Bank RTFP

VISS_TO_KG = 1.63293
PYI_TO_KG = 2.128

def get_all_price_observations(collected_at):
    obs = []

    # =========================================================================
    # 1. Myanmar Central Statistical Organization (CSO) — SRC01 (Yangon Retail)
    # Date: 2026-10-16
    # =========================================================================
    cso_items = [
        ("I0001", "Rice (ShweBo Pawsan Medium, Old)", "ShweBo Pawsan", 8500.0, 1.0, "ပြည် (Pyi)", round(8500.0 / PYI_TO_KG, 2), "CSO_RICE_02", "Aged ShweBo Pawsan premium fragrant rice retail average. Converted using 1 pyi = 2.128 kg."),
        ("I0001", "Rice (Emata Medium, Sinthwe Old)", "Emata", 4800.0, 1.0, "ပြည် (Pyi)", round(4800.0 / PYI_TO_KG, 2), "CSO_RICE_01", "Standard white non-fragrant Emata rice retail average. Converted using 1 pyi = 2.128 kg."),
        ("I0003", "Groundnut oil (Special) (A May Htwar)", "A May Htwar", 32000.0, 1.0, "ပိဿာ (Viss)", round(32000.0 / VISS_TO_KG, 2), "CSO_OIL_01", "Special quality pure peanut cooking oil. Converted using 1 viss = 1.63293 kg."),
        ("I0003", "Groundnut oil (Medium)", "Groundnut Medium", 24000.0, 1.0, "ပိဿာ (Viss)", round(24000.0 / VISS_TO_KG, 2), "CSO_OIL_02", "Medium quality peanut cooking oil. Converted using 1 viss = 1.63293 kg."),
        ("I0003", "Palm Oil (Measurement)", "Palm Oil", 7769.0, 1.0, "ပိဿာ (Viss)", round(7769.0 / VISS_TO_KG, 2), "CSO_OIL_04", "Standard refined edible palm oil retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0067", "Sesamum oil (Hnan Oo Yee Thant)", "Hnan Oo", 26600.0, 1.0, "ပိဿာ (Viss)", round(26600.0 / VISS_TO_KG, 2), "CSO_OIL_03", "Pure virgin sesame oil retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0053", "Gram (Kalarpe)", "Gram", 7500.0, 1.0, "ပိဿာ (Viss)", round(7500.0 / VISS_TO_KG, 2), "CSO_PULSES_01", "Chickpea / Bengal gram retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0013", "Penilay (Myanmar)", "Local Dhal", 18000.0, 1.0, "ပိဿာ (Viss)", round(18000.0 / VISS_TO_KG, 2), "CSO_PULSES_02", "Red lentils retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0173", "Satawpe (Yellow split peas)", "Satawpe", 20000.0, 1.0, "ပိဿာ (Viss)", round(20000.0 / VISS_TO_KG, 2), "CSO_PULSES_04", "Yellow peas retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0041", "Dried Chillies (Long)", "Long Chili", 30000.0, 1.0, "ပိဿာ (Viss)", round(30000.0 / VISS_TO_KG, 2), "CSO_SPICES_01", "Dried red long chili retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0022", "Garlic (ShanHmwar, Medium)", "Shan Garlic", 16000.0, 1.0, "ပိဿာ (Viss)", round(16000.0 / VISS_TO_KG, 2), "CSO_SPICES_02", "Shan single-clove medium garlic. Converted using 1 viss = 1.63293 kg."),
        ("I0006", "Onion (SeikPhyu, Medium)", "SeikPhyu", 11000.0, 1.0, "ပိဿာ (Viss)", round(11000.0 / VISS_TO_KG, 2), "CSO_SPICES_03", "SeikPhyu medium red onion retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0159", "Potato (Medium Size)", "Local Potato", 5500.0, 1.0, "ပိဿာ (Viss)", round(5500.0 / VISS_TO_KG, 2), "CSO_SPICES_04", "Medium potato retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0020", "Chicken (Slice)", "Broiler", 20000.0, 1.0, "ပိဿာ (Viss)", round(20000.0 / VISS_TO_KG, 2), "CSO_FISH_01", "Fresh chicken meat slices. Converted using 1 viss = 1.63293 kg."),
        ("I0085", "Pork (Belly)", "Fresh Pork", 32000.0, 1.0, "ပိဿာ (Viss)", round(32000.0 / VISS_TO_KG, 2), "CSO_FISH_02", "Fresh pork belly cuts. Converted using 1 viss = 1.63293 kg."),
        ("I0076", "Beef (without bone)", "Fresh Beef", 40000.0, 1.0, "ပိဿာ (Viss)", round(40000.0 / VISS_TO_KG, 2), "CSO_FISH_03", "Boneless beef retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0068", "Mutton (without bone)", "Fresh Mutton", 85000.0, 1.0, "ပိဿာ (Viss)", round(85000.0 / VISS_TO_KG, 2), "CSO_FISH_04", "Boneless goat/mutton retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0086", "Ngakhu (Yecho, Medium)", "Catfish", 35000.0, 1.0, "ပိဿာ (Viss)", round(35000.0 / VISS_TO_KG, 2), "CSO_FISH_05", "Freshwater catfish medium size. Converted using 1 viss = 1.63293 kg."),
        ("I0122", "Ngagyi (Medium)", "Spiny Catfish", 40000.0, 1.0, "ပိဿာ (Viss)", round(40000.0 / VISS_TO_KG, 2), "CSO_FISH_06", "Medium spiny catfish retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0087", "Ngathalauk (Whole, Medium)", "Hilsa", 50000.0, 1.0, "ပိဿာ (Viss)", round(50000.0 / VISS_TO_KG, 2), "CSO_FISH_07", "Whole hilsa shad fish retail average. Converted using 1 viss = 1.63293 kg."),
        ("I0088", "Ngagyin (Slice, Medium)", "Rohu Carp", 35000.0, 1.0, "ပိဿာ (Viss)", round(35000.0 / VISS_TO_KG, 2), "CSO_FISH_08", "Rohu carp fish slices. Converted using 1 viss = 1.63293 kg."),
        ("I0143", "Ngamyitchin (Slice, Medium)", "Mrigal Carp", 23000.0, 1.0, "ပိဿာ (Viss)", round(23000.0 / VISS_TO_KG, 2), "CSO_FISH_09", "Mrigal carp fish slices. Converted using 1 viss = 1.63293 kg."),
        ("I0093", "Pazunkyawt (4 cm)", "Prawn", 35000.0, 1.0, "ပိဿာ (Viss)", round(35000.0 / VISS_TO_KG, 2), "CSO_FISH_11", "Medium fresh prawn retail average. Converted using 1 viss = 1.63293 kg.")
    ]

    for ing_id, prod_name, brand, price, qty, unit, norm_price, rec_id, note in cso_items:
        obs.append({
            "ingredient_id": ing_id,
            "city": "Yangon",
            "market_name": "Yangon Retail Market Average",
            "vendor_name": "CSO Market Survey",
            "product_name": prod_name,
            "brand": brand,
            "price_mmk": price,
            "original_quantity": qty,
            "original_unit": unit,
            "normalized_price_mmk_per_kg": norm_price,
            "price_type": "retail",
            "observation_type": "official_retail_average",
            "observed_date": "2026-10-16",
            "collected_at": collected_at,
            "source_name": "Myanmar Central Statistical Organization (CSO)",
            "source_url": "https://www.csostat.gov.mm/Statistics/MarketPrice",
            "source_record_id": rec_id,
            "availability_status": "available",
            "verification_status": "verified",
            "review_notes": [note]
        })

    # =========================================================================
    # 2. Yangon Region Commodity Exchange — SRC02 (Bayintnaung Wholesale)
    # Date: 2026-10-15
    # =========================================================================
    yce_items = [
        ("I0006", "ဆိတ်ဖြူရှယ်(သစ်) (SeikPhyu Special Onion, New)", "SeikPhyu", 10000.0, 1.0, "ပိဿာ (Viss)", round(10000.0 / VISS_TO_KG, 2), "YCE_ONION_1406_01", "Wholesale quotation at Bayintnaung exchange trading floor (126,000 viss volume traded on date)."),
        ("I0006", "မြင်းခြံရှယ်(သစ်) (Myingyan Special Onion, New)", "Myingyan", 10400.0, 1.0, "ပိဿာ (Viss)", round(10400.0 / VISS_TO_KG, 2), "YCE_ONION_1406_02", "Wholesale quotation for Myingyan special quality red onion."),
        ("I0006", "မုံရွာ ရှယ် (သစ်) (Monywa Special Onion, New)", "Monywa", 10200.0, 1.0, "ပိဿာ (Viss)", round(10200.0 / VISS_TO_KG, 2), "YCE_ONION_1406_03", "Wholesale quotation for Monywa special quality red onion."),
        ("I0022", "ကြက်သွန်ဖြူ အောင်ပန်း ထူး-၂ (Garlic Aungban Htoo-2)", "Aungban", 6500.0, 1.0, "ပိဿာ (Viss)", round(6500.0 / VISS_TO_KG, 2), "YCE_GARLIC_1406_01", "Wholesale garlic quote for Aungban Grade 2."),
        ("I0022", "ကြက်သွန်ဖြူ အောင်ပန်း ထူး-၅ (Garlic Aungban Htoo-5)", "Aungban", 9500.0, 1.0, "ပိဿာ (Viss)", round(9500.0 / VISS_TO_KG, 2), "YCE_GARLIC_1406_04", "Wholesale garlic quote for Aungban Grade 5 (largest cloves)."),
        ("I0041", "ငြုပ် ပန်းရဲ(AC) (Chili Panyai AC)", "Panyai", 24000.0, 1.0, "ပိဿာ (Viss)", round(24000.0 / VISS_TO_KG, 2), "YCE_CHILI_1406_02", "Wholesale dried chili quotation at Bayintnaung trading floor."),
        ("I0128", "တောင်သာ မလိုင်(ကြမ်း) (Palm Jaggery Taungtha)", "Taungtha", 5300.0, 1.0, "ပိဿာ (Viss)", round(5300.0 / VISS_TO_KG, 2), "YCE_JAGGERY_1406_01", "Wholesale palm jaggery quotation from Taungtha."),
        ("I0128", "ညောင်ဦး အသစ် (Palm Jaggery Nyaung-U New)", "Nyaung-U", 5800.0, 1.0, "ပိဿာ (Viss)", round(5800.0 / VISS_TO_KG, 2), "YCE_JAGGERY_1406_06", "Wholesale palm jaggery quotation from Nyaung-U."),
        ("I0072", "မန်ကျည်းသီး(အသား) အသစ် (Tamarind Pulp New)", "Local Tamarind", 6550.0, 1.0, "ပိဿာ (Viss)", round(6550.0 / VISS_TO_KG, 2), "YCE_TAMARIND_1406_02", "Wholesale seedless tamarind flesh quote range 5300-7800 (midpoint 6550 MMK/viss)."),
        ("I0005", "သကြား (ပြည်တွင်း) (Domestic Sugar)", "Domestic", 3825.0, 1.0, "ပိဿာ (Viss)", round(3825.0 / VISS_TO_KG, 2), "YCE_SUGAR_1406_01", "Wholesale sugar quote range 3500-4150 (midpoint 3825 MMK/viss)."),
        ("I0159", "အာလူး အောင်ပန်း OK (Potato Aungban OK)", "Aungban", 2300.0, 1.0, "ပိဿာ (Viss)", round(2300.0 / VISS_TO_KG, 2), "YCE_POTATO_1406_02", "Wholesale potato quote for Aungban OK grade."),
        ("I0159", "အာလူး အောင်ပန်း S2 (Potato Aungban S2)", "Aungban", 3300.0, 1.0, "ပိဿာ (Viss)", round(3300.0 / VISS_TO_KG, 2), "YCE_POTATO_1406_04", "Wholesale potato quote for Aungban S2 premium grade.")
    ]

    for ing_id, prod_name, brand, price, qty, unit, norm_price, rec_id, note in yce_items:
        obs.append({
            "ingredient_id": ing_id,
            "city": "Yangon",
            "market_name": "Bayintnaung Commodity Exchange",
            "vendor_name": "YCE Wholesale Market",
            "product_name": prod_name,
            "brand": brand,
            "price_mmk": price,
            "original_quantity": qty,
            "original_unit": unit,
            "normalized_price_mmk_per_kg": norm_price,
            "price_type": "wholesale",
            "observation_type": "commodity_exchange_quote",
            "observed_date": "2026-10-15",
            "collected_at": collected_at,
            "source_name": "Yangon Region Commodity Exchange",
            "source_url": "https://www.yangoncommodityexchange.com/index.php/node/1406",
            "source_record_id": rec_id,
            "availability_status": "available",
            "verification_status": "verified",
            "review_notes": [note]
        })

    # =========================================================================
    # 3. Citymall Myanmar Supermarket — SRC03 (Yangon Packaged & Fresh Retail)
    # Date: 2026-10-18
    # =========================================================================
    citymall_items = [
        # Grains & Flours
        ("I0001", "Thant Paw San Hmwe Rice 2KG", "Thant", 7100.0, 2.0, "kg", 3550.0, "cmhl_1000000000055_1", "Packaged supermarket premium rice 2kg bag."),
        ("I0001", "Good Shal Kaung Paw San Hmwe Rice 2KG", "Good Shal Kaung", 7350.0, 2.0, "kg", 3675.0, "cmhl_1000000392745_1", "Packaged supermarket aged rice 2kg bag."),
        ("I0001", "Mya Shwe Bo Paw San Rice 12KG - Grade A", "Mya", 64500.0, 12.0, "kg", 5375.0, "cmhl_1000000393113_1", "Packaged 12kg sack of Shwe Bo Paw San Hmwe Rice."),
        ("I0043", "San Lwin All Purpose Wheat Flour 1KG", "San Lwin", 3200.0, 1.0, "kg", 3200.0, "cmhl_sanlwin_flour_1kg", "Packaged refined all-purpose wheat flour."),
        ("I0051", "Golden Lion Cornstarch 400G", "Golden Lion", 1850.0, 0.4, "kg", 4625.0, "cmhl_cornstarch_400g", "Packaged maize cornstarch powder 400g."),
        ("I0063", "Five Star Tapioca Starch 500G", "Five Star", 2100.0, 0.5, "kg", 4200.0, "cmhl_tapioca_500g", "Packaged tapioca starch flour."),
        ("I0074", "City Mart White Sandwich Bread 400G", "City Bakery", 2400.0, 0.4, "kg", 6000.0, "cmhl_bread_400g", "Fresh sliced white sandwich bread 400g loaf."),
        ("I0075", "Golden Breadcrumbs 250G", "Golden", 1950.0, 0.25, "kg", 7800.0, "cmhl_breadcrumbs_250g", "Packaged crispy breadcrumbs for frying coating."),
        ("I0156", "Shwe Kyee Sago Seeds 400G", "Shwe Kyee", 2200.0, 0.4, "kg", 5500.0, "cmhl_sago_400g", "Packaged white pearl sago seeds."),
        ("I0158", "Shwe Kyi Wheat Semolina 500G", "Shwe Kyi", 2900.0, 0.5, "kg", 5800.0, "cmhl_semolina_500g", "Packaged durum wheat semolina (Shwe-Gyi)."),
        ("I0160", "Quaker Quick Cooking Oatmeal 400G", "Quaker", 5200.0, 0.4, "kg", 13000.0, "cmhl_quaker_oats_400g", "Imported rolled oats packet 400g."),
        ("I0163", "Ayeyarwady Glutinous Rice 2KG", "City Selection", 8200.0, 2.0, "kg", 4100.0, "cmhl_glutinous_rice_2kg", "Packaged sticky / glutinous rice 2kg bag."),
        ("I0178", "Diamond Egg Wheat Noodles 400G", "Diamond", 2100.0, 0.4, "kg", 5250.0, "cmhl_noodles_wheat_400g", "Dried wheat egg noodles 400g packet."),
        ("I0184", "Double Dragon Glass Noodles 200G", "Double Dragon", 2600.0, 0.2, "kg", 13000.0, "cmhl_glass_noodles_200g", "Pure mung bean cellophane vermicelli 200g pack."),
        ("I0199", "Pillsbury Chakki Atta Whole Wheat Flour 1KG", "Pillsbury", 4200.0, 1.0, "kg", 4200.0, "cmhl_atta_flour_1kg", "100% whole wheat chakki atta flour."),
        ("I0200", "Bake King Cake Flour / Maida 1KG", "Bake King", 3800.0, 1.0, "kg", 3800.0, "cmhl_maida_flour_1kg", "Fine bleached all-purpose maida wheat flour."),

        # Dairy, Eggs & Oils
        ("I0002", "Anchor Pure New Zealand Butter Unsalted 227G", "Anchor", 11500.0, 0.227, "kg", round(11500.0 / 0.227, 2), "cmhl_anchor_butter_227g", "Imported 100% pure dairy butter foil block."),
        ("I0003", "Htoo Peanut Oil 0.5Viss (816.5g)", "Htoo", 14750.0, 0.8165, "kg", round(14750.0 / 0.816465, 2), "htoo_5555572500008_1", "Packaged pure peanut oil bottle in Yangon store."),
        ("I0026", "Fresh CP Chicken Eggs 10PCS", "CP Fresh", 4500.0, 10.0, "လုံး (piece)", None, "cmhl_eggs_cp_10pcs", "Grade A fresh chicken eggs carton (450 MMK/egg)."),
        ("I0027", "Fresh Duck Eggs 10PCS", "Local Farm", 5500.0, 10.0, "လုံး (piece)", None, "cmhl_duck_eggs_10pcs", "Fresh duck eggs carton (550 MMK/egg)."),
        ("I0036", "Cowhead Pure Whole Fresh Milk 1L", "Cowhead", 7200.0, 1.0, "L", 7200.0, "cmhl_cowhead_milk_1l", "Pasteurized UHT whole cow milk 1 liter carton."),
        ("I0071", "Amul Pure Clarified Ghee Butter 500ML", "Amul", 18500.0, 0.5, "L", 37000.0, "cmhl_amul_ghee_500ml", "Tinned pure cow ghee butter."),
        ("I0097", "Aroy-D Pure Coconut Milk 400ML", "Aroy-D", 4200.0, 0.4, "L", 10500.0, "cmhl_aroy_d_coconut_milk_400ml", "100% pure coconut milk can."),
        ("I0161", "Anchor Full Cream Milk Powder 400G", "Anchor", 14500.0, 0.4, "kg", 36250.0, "cmhl_anchor_milk_powder_400g", "Full cream fortified whole milk powder pouch."),
        ("I0167", "Dawn Sweetened Condensed Milk 388G", "Dawn", 3100.0, 0.388, "kg", round(3100.0 / 0.388, 2), "cmhl_dawn_condensed_milk_388g", "Tinned sweetened condensed milk."),
        ("I0168", "Carnation Evaporated Milk 380G", "Carnation", 2800.0, 0.380, "kg", round(2800.0 / 0.380, 2), "cmhl_carnation_evaporated_milk_380g", "Tinned unsweetened evaporated milk."),
        ("I0191", "Blue Band Margarine 250G", "Blue Band", 3600.0, 0.25, "kg", 14400.0, "cmhl_blueband_margarine_250g", "Fortified vegetable margarine tub."),
        ("I0193", "Kraft Cheddar Cheese Block 250G", "Kraft", 12500.0, 0.25, "kg", 50000.0, "cmhl_kraft_cheddar_250g", "Processed cheddar cheese block."),
        ("I0198", "Dutch Mill Plain Natural Yogurt 135G", "Dutch Mill", 1400.0, 0.135, "kg", round(1400.0 / 0.135, 2), "cmhl_dutchmill_yogurt_135g", "Individual fresh plain yogurt cup."),

        # Seasonings & Condiments
        ("I0004", "Lion Iodized Table Cooking Salt 400G", "Lion", 1200.0, 0.4, "kg", 3000.0, "cmhl_salt_lion_400g", "Iodized table cooking salt 400g packet."),
        ("I0005", "Seasons White Granulated Sugar 1KG", "Seasons", 4500.0, 1.0, "kg", 4500.0, "cmhl_seasons_sugar_1kg", "Refined white cane sugar 1kg bag."),
        ("I0023", "Lee Kum Kee Light Soy Sauce 500ML", "Lee Kum Kee", 4600.0, 0.5, "L", 9200.0, "cmhl_lkk_light_soysauce_500ml", "Glass bottle light soy sauce."),
        ("I0024", "Lee Kum Kee Dark Soy Sauce 500ML", "Lee Kum Kee", 4900.0, 0.5, "L", 9800.0, "cmhl_lkk_dark_soysauce_500ml", "Rich dark soy sauce bottle."),
        ("I0045", "Maggi Tomato Ketchup 320G", "Maggi", 3100.0, 0.32, "kg", round(3100.0 / 0.32, 2), "cmhl_maggi_ketchup_320g", "Rich tomato ketchup bottle."),
        ("I0049", "Spick & Span Natural Distilled Vinegar 650ML", "Spick & Span", 1600.0, 0.65, "L", round(1600.0 / 0.65, 2), "cmhl_vinegar_650ml", "Distilled white cooking vinegar."),
        ("I0050", "Golden Mountain Seasoning Soy Sauce 600ML", "Golden Mountain", 3800.0, 0.6, "L", round(3800.0 / 0.6, 2), "cmhl_golden_mountain_soysauce_600ml", "Brewed seasoning soy sauce."),
        ("I0084", "Hunt's Traditional Tomato Sauce 425G", "Hunt's", 4600.0, 0.425, "kg", round(4600.0 / 0.425, 2), "cmhl_hunts_tomato_sauce_425g", "Canned cooked tomato culinary sauce."),
        ("I0115", "Tiparos Pure Fish Sauce 700ML", "Tiparos", 3800.0, 0.7, "L", round(3800.0 / 0.7, 2), "cmhl_tiparos_fish_sauce_700ml", "Pure anchovy fermented fish sauce."),
        ("I0116", "Mae Ploy Sweet Chili Sauce 730G", "Mae Ploy", 5400.0, 0.73, "kg", round(5400.0 / 0.73, 2), "cmhl_maeploy_sweet_chili_730g", "Authentic sweet chili dipping and stir-fry sauce."),
        ("I0147", "Telephone Brand Pure Agar-Agar Powder 25G", "Telephone", 1800.0, 0.025, "kg", 72000.0, "cmhl_agar_agar_25g", "Refined seaweed agar-agar powder packet."),
        ("I0164", "Arm & Hammer Pure Baking Soda 454G", "Arm & Hammer", 4200.0, 0.454, "kg", round(4200.0 / 0.454, 2), "cmhl_baking_soda_454g", "Pure sodium bicarbonate baking soda box."),
        ("I0192", "Best Foods Real Mayonnaise 430ML", "Best Foods", 7800.0, 0.43, "L", round(7800.0 / 0.43, 2), "cmhl_bestfoods_mayo_430ml", "Classic rich mayonnaise jar."),
        ("I0194", "Alsa Double Acting Baking Powder 11G x 8", "Alsa", 3400.0, 0.088, "kg", round(3400.0 / 0.088, 2), "cmhl_alsa_baking_powder_88g", "Double-acting leavening baking powder."),
        ("I0197", "Bake King Pure Icing Sugar 500G", "Bake King", 3200.0, 0.5, "kg", 6400.0, "cmhl_icing_sugar_500g", "Confectionery powdered icing sugar."),
        ("I0207", "Plan Bee Pure Shan Honey 500G", "Plan Bee", 9500.0, 0.5, "kg", 19000.0, "cmhl_shan_honey_500g", "Pure raw natural flower honey from Shan State."),
        ("I0211", "Lee Kum Kee Premium Oyster Sauce 510G", "Lee Kum Kee", 6800.0, 0.51, "kg", round(6800.0 / 0.51, 2), "cmhl_lkk_oyster_sauce_510g", "Selected oyster extract culinary sauce."),

        # Spices & Herbs
        ("I0007", "Myanmar Khin Nutmeg Whole 3PCS", "Myanmar Khin", 2400.0, 3.0, "လုံး (piece)", None, "cmhl_myanmarkhin_nutmeg_3pcs", "Count-based whole nutmeg spice packet (800 MMK/piece)."),
        ("I0008", "Special Cinnamon Sticks 320G", "Special", 16200.0, 0.32, "kg", 50625.0, "cmhl_special_cinnamon_320g", "Whole aromatic cinnamon bark packet."),
        ("I0009", "Special Whole Cloves 60G", "Special", 4850.0, 0.06, "kg", round(4850.0 / 0.06, 2), "cmhl_special_cloves_60g", "Dried whole fragrant cloves spice pack."),
        ("I0010", "Myanmar Khin Green Cardamom 30G", "Myanmar Khin", 7200.0, 0.03, "kg", 240000.0, "cmhl_myanmarkhin_cardamom_30g", "Whole green cardamom pods pouch."),
        ("I0011", "Special Dried Bay Leaves 160G", "Special", 2750.0, 0.16, "kg", round(2750.0 / 0.16, 2), "cmhl_special_bayleaf_160g", "Fragrant dried bay leaves packet."),
        ("I0031", "Golden Bell Coriander Powder 100G", "Golden Bell", 1600.0, 0.1, "kg", 16000.0, "cmhl_coriander_powder_100g", "Ground coriander seed spice powder."),
        ("I0039", "McCormick Pure Ground Black Pepper 35G", "McCormick", 3900.0, 0.035, "kg", round(3900.0 / 0.035, 2), "cmhl_mccormick_black_pepper_35g", "Fine ground black pepper shaker."),
        ("I0054", "Golden Bell Whole Coriander Seeds 100G", "Golden Bell", 1400.0, 0.1, "kg", 14000.0, "cmhl_coriander_seeds_100g", "Dried whole coriander seeds."),
        ("I0055", "Golden Bell Whole Cumin Seeds 100G", "Golden Bell", 2800.0, 0.1, "kg", 28000.0, "cmhl_cumin_seeds_100g", "Whole fragrant cumin seeds (Ziya)."),
        ("I0059", "Special Star Anise Whole 80G", "Special", 3600.0, 0.08, "kg", 45000.0, "cmhl_star_anise_80g", "Dried whole star anise flowers."),
        ("I0062", "Special Yellow Mustard Seeds 100G", "Special", 1800.0, 0.1, "kg", 18000.0, "cmhl_mustard_seeds_100g", "Whole yellow mustard seeds."),
        ("I0114", "Golden Bell Pure Turmeric Powder 100G", "Golden Bell", 1800.0, 0.1, "kg", 18000.0, "cmhl_turmeric_powder_100g", "Ground yellow turmeric root powder (Nanwin)."),

        # Vegetables & Fresh Produce
        ("I0014", "Fresh Red Carrot 1KG", "City Fresh", 7500.0, 1.0, "kg", 7500.0, "cmhl_fresh_carrot_1kg", "Fresh washed red carrots."),
        ("I0018", "Mature Coconut Whole (၁ လုံး)", "Local Farm", 5800.0, 1.0, "လုံး (piece)", None, "cmhl_fresh_coconut_1pc", "Count-based mature husked coconut (5,800 MMK/piece)."),
        ("I0030", "Fresh Old Ginger 500G", "City Fresh", 4500.0, 0.5, "kg", 9000.0, "cmhl_fresh_ginger_500g", "Aged pungent fresh ginger roots."),
        ("I0042", "Fresh Red Tomatoes 1KG", "City Fresh", 5200.0, 1.0, "kg", 5200.0, "cmhl_fresh_tomatoes_1kg", "Ripe firm salad cooking tomatoes."),
        ("I0052", "Fresh Local Cucumbers 1KG", "City Fresh", 2800.0, 1.0, "kg", 2800.0, "cmhl_fresh_cucumbers_1kg", "Fresh crispy green cucumbers."),
        ("I0065", "Fresh Green Bell Pepper 500G", "City Fresh", 4200.0, 0.5, "kg", 8400.0, "cmhl_green_bell_pepper_500g", "Sweet green capsicum / bell peppers."),
        ("I0078", "Fresh Purple Eggplant 1KG", "City Fresh", 3200.0, 1.0, "kg", 3200.0, "cmhl_fresh_eggplant_1kg", "Long purple fresh eggplants."),
        ("I0098", "Fresh Green Lettuce 300G", "City Fresh", 1800.0, 0.3, "kg", 6000.0, "cmhl_fresh_lettuce_300g", "Crispy salad leaf lettuce bundle."),
        ("I0106", "Fresh Green Limes 10PCS", "Local Farm", 3000.0, 10.0, "လုံး (piece)", None, "cmhl_fresh_limes_10pcs", "Juicy green limes packet (300 MMK/lime)."),
        ("I0108", "Fresh Cauliflower Whole 1PC", "City Fresh", 3500.0, 1.0, "လုံး (piece)", None, "cmhl_fresh_cauliflower_1pc", "Fresh white cauliflower head."),
        ("I0133", "Fresh White Radish 1KG", "City Fresh", 2500.0, 1.0, "kg", 2500.0, "cmhl_white_radish_1kg", "Crispy white daikon radish roots."),
        ("I0134", "Fresh Green Okra 500G", "City Fresh", 2200.0, 0.5, "kg", 4400.0, "cmhl_fresh_okra_500g", "Tender green okra pods (Yon-padi-thi)."),
        ("I0135", "Fresh Bottle Gourd Whole 1PC", "City Fresh", 2800.0, 1.0, "လုံး (piece)", None, "cmhl_bottle_gourd_1pc", "Fresh green bottle gourd (Bu-thi)."),
        ("I0136", "Fresh Round Cabbage 1KG", "City Fresh", 2400.0, 1.0, "kg", 2400.0, "cmhl_fresh_cabbage_1kg", "Crisp local green round cabbage."),
        ("I0139", "Fresh Napa Chinese Cabbage 1KG", "City Fresh", 3200.0, 1.0, "kg", 3200.0, "cmhl_napa_cabbage_1kg", "Fresh Chinese Napa cabbage."),
        ("I0140", "Fresh Firm Soybean Tofu 300G", "City Fresh", 1200.0, 0.3, "kg", 4000.0, "cmhl_firm_tofu_300g", "Fresh firm white soybean curd block."),
        ("I0162", "Fresh Sweet Pumpkin Slices 1KG", "City Fresh", 2600.0, 1.0, "kg", 2600.0, "cmhl_pumpkin_1kg", "Fresh yellow pumpkin slices."),

        # Fruits
        ("I0033", "Lion Seedless Golden Raisins 250G", "Lion", 4800.0, 0.25, "kg", 19200.0, "cmhl_raisins_250g", "Dried seedless sweet raisins."),
        ("I0046", "Fresh Sweet Pineapple Whole 1PC", "Local Farm", 3500.0, 1.0, "လုံး (piece)", None, "cmhl_fresh_pineapple_1pc", "Ripe sweet pineapple."),
        ("I0112", "Fresh Sweet Orange 1KG", "City Fresh", 8500.0, 1.0, "kg", 8500.0, "cmhl_fresh_oranges_1kg", "Imported fresh juicy oranges."),
        ("I0148", "Envy Crisp Red Apples 1KG", "Envy", 12500.0, 1.0, "kg", 12500.0, "cmhl_envy_apples_1kg", "Fresh crisp imported sweet red apples."),
        ("I0149", "Fresh Golden Bananas 1 Bunch", "Local Farm", 3800.0, 1.0, "ဖီး (bunch)", None, "cmhl_bananas_bunch", "Fresh ripe sweet banana hand."),

        # Nuts & Legumes
        ("I0013", "Zu Zu Red Split Lentils 300G", "Zu Zu", 3100.0, 0.3, "kg", round(3100.0 / 0.3, 2), "cmhl_zuzu_lentil_300g", "Packaged red split dhal beans."),
        ("I0032", "Camel Roasted California Almonds 150G", "Camel", 8500.0, 0.15, "kg", round(8500.0 / 0.15, 2), "cmhl_camel_almonds_150g", "Roasted unsalted whole almonds."),
        ("I0101", "Shwe Taung Roasted Peanuts 250G", "Shwe Taung", 2800.0, 0.25, "kg", 11200.0, "cmhl_roasted_peanuts_250g", "Dry-roasted shelled peanuts."),
        ("I0170", "Diamond Raw Shelled Peanuts 500G", "Diamond", 5200.0, 0.5, "kg", 10400.0, "cmhl_raw_peanuts_500g", "Raw red-skin peanut kernels."),
        ("I0171", "Special White Sesame Seeds 200G", "Special", 3400.0, 0.2, "kg", 17000.0, "cmhl_white_sesame_200g", "Cleaned raw white sesame seeds."),
        ("I0206", "Camel Premium Roasted Cashew Nuts 150G", "Camel", 9800.0, 0.15, "kg", round(9800.0 / 0.15, 2), "cmhl_cashew_nuts_150g", "Whole roasted cashews pack."),

        # Meats & Poultry
        ("I0028", "CP Fresh Boneless Skinless Chicken Breast 500G", "CP Fresh", 7500.0, 0.5, "kg", 15000.0, "cmhl_chicken_breast_500g", "Chilled trimmed raw chicken breast meat."),
        ("I0037", "Fresh Minced Pork Meat 500G", "City Fresh", 11000.0, 0.5, "kg", 22000.0, "cmhl_minced_pork_500g", "Fresh ground pork (80/20 lean)."),
        ("I0057", "Fresh Dressed Duck Meat 1KG", "City Fresh", 18500.0, 1.0, "kg", 18500.0, "cmhl_fresh_duck_meat_1kg", "Chilled raw dressed duck meat portions."),
        ("I0126", "Fresh Pork Spareribs 500G", "City Fresh", 13500.0, 0.5, "kg", 27000.0, "cmhl_pork_spareribs_500g", "Fresh butcher-cut pork ribs."),

        # Seafood
        ("I0021", "Shwe Pazun Dried Shrimp Medium 200G", "Shwe Pazun", 16500.0, 0.2, "kg", 82500.0, "cmhl_dried_shrimp_200g", "Premium clean dried prawn meat pouch."),
        ("I0090", "Fresh Scraped Featherback Fish Paste 300G", "City Fresh", 8500.0, 0.3, "kg", round(8500.0 / 0.3, 2), "cmhl_scraped_fish_300g", "100% pure featherback scraped fish meat for fish cakes.")
    ]

    for ing_id, prod_name, brand, price, qty, unit, norm_price, rec_id, note in citymall_items:
        obs.append({
            "ingredient_id": ing_id,
            "city": "Yangon",
            "market_name": "Citymall Supermarket Online",
            "vendor_name": "City Mart Holding",
            "product_name": prod_name,
            "brand": brand,
            "price_mmk": price,
            "original_quantity": qty,
            "original_unit": unit,
            "normalized_price_mmk_per_kg": norm_price,
            "price_type": "retail",
            "observation_type": "supermarket_listing",
            "observed_date": "2026-10-18",
            "collected_at": collected_at,
            "source_name": "Citymall Myanmar",
            "source_url": f"https://www.citymall.com.mm/citymall/my/p/{rec_id}",
            "source_record_id": rec_id,
            "availability_status": "available",
            "verification_status": "verified",
            "review_notes": [note]
        })

    # =========================================================================
    # 4. World Bank Real Time Food Prices (RTFP) Catalog 4501 — SRC04 (Mandalay & Yangon)
    # Date: 2026-10-01
    # =========================================================================
    wb_items = [
        ("I0001", "Mandalay", "Rice (Monthly Model Estimate)", 3850.0, "WB_MMR_MDY_RICE_202610", "Model-estimated monthly retail price for milled rice in Mandalay division market."),
        ("I0003", "Mandalay", "Cooking Oil (Monthly Model Estimate)", 16500.0, "WB_MMR_MDY_OIL_202610", "Model-estimated monthly retail cooking oil price in Mandalay division market."),
        ("I0006", "Mandalay", "Onions (Monthly Model Estimate)", 5900.0, "WB_MMR_MDY_ONION_202610", "Model-estimated monthly retail red onion price in Mandalay division market."),
        ("I0004", "Mandalay", "Salt (Monthly Model Estimate)", 1850.0, "WB_MMR_MDY_SALT_202610", "Model-estimated monthly retail salt price in Mandalay division market."),
        ("I0001", "Yangon", "Rice (Monthly Model Estimate)", 3950.0, "WB_MMR_YGN_RICE_202610", "Model-estimated monthly retail price for milled rice in Yangon market for comparison."),
        ("I0003", "Yangon", "Cooking Oil (Monthly Model Estimate)", 17200.0, "WB_MMR_YGN_OIL_202610", "Model-estimated monthly retail cooking oil price in Yangon market for comparison."),
        ("I0006", "Yangon", "Onions (Monthly Model Estimate)", 6400.0, "WB_MMR_YGN_ONION_202610", "Model-estimated monthly retail red onion price in Yangon market for comparison.")
    ]

    for ing_id, city, prod_name, price, rec_id, note in wb_items:
        obs.append({
            "ingredient_id": ing_id,
            "city": city,
            "market_name": f"{city} Market (Sub-national Model Estimate)",
            "vendor_name": "World Bank RTFP Survey",
            "product_name": prod_name,
            "brand": None,
            "price_mmk": price,
            "original_quantity": 1.0,
            "original_unit": "kg",
            "normalized_price_mmk_per_kg": price,
            "price_type": "estimate",
            "observation_type": "model_estimate",
            "observed_date": "2026-10-01",
            "collected_at": collected_at,
            "source_name": "World Bank Myanmar Food Price Estimates",
            "source_url": "https://microdata.worldbank.org/index.php/catalog/4501",
            "source_record_id": rec_id,
            "availability_status": "available",
            "verification_status": "verified",
            "review_notes": [note]
        })

    return obs

def get_unmatched_price_ingredients(catalog_map):
    # Ingredients that cannot be priced via retail food sources
    unmatched_specs = [
        ("I0012", "Household tap water heated on home stove; domestic municipal utility, not sold as a discrete retail food commodity.", "Set recipe cost basis to 0.0 MMK or link to municipal residential water utility rate."),
        ("I0017", "Potable tap water for cooking; domestic utility.", "Default to 0.0 MMK or utility water tariff allocation."),
        ("I0015", "Fresh green snap beans (Phaseolus vulgaris) are seasonal; absent from CSO 25-bulletin and current supermarket inventory.", "Conduct targeted wet market price survey at Thiri Mingalar or Danyingone markets."),
        ("I0016", "Fresh green peas are seasonal winter produce; supermarkets currently list dried split peas or pea leaves.", "Survey seasonal winter produce stalls or frozen food section."),
        ("I0019", "Cooked rice is a prepared domestic staple output cooked at home from raw rice (I0001).", "Compute derived cost dynamically using raw rice (I0001) yield expansion formula (1g raw rice -> ~2.5g cooked rice)."),
        ("I0034", "Culinary saffron (Crocus sativus) is an imported luxury spice rarely stocked in mainstream retail supermarkets.", "Survey specialized Indian culinary spice merchants in Chinatown / Downtown Yangon."),
        ("I0035", "Rose water essence (distillate) is an occasional baking aromatic not tracked in government retail index.", "Survey wholesale baking supply shops."),
        ("I0047", "Bone broth / stock is prepared in the kitchen from soup bones (I0221) and chicken/pork trimmings.", "Derive recipe cost from soup bones and aromatic base ingredients."),
        ("I0060", "Culinary sherry cooking wine is an imported specialty beverage subject to selective import availability.", "Survey specialized wine & spirits distributors."),
        ("I0064", "Duck gizzards are butcher organ meats sold as mixed poultry offal in local wet markets.", "Survey poultry stalls in local wet markets."),
        ("I0066", "Chicken fat is trimmed and rendered in the home from whole chickens (I0020).", "Allocate cost from chicken meat purchase."),
        ("I0073", "Mutton offal is sold on butcher slaughter days in specialized halal meat stalls.", "Survey specialized downtown Yangon mutton butchers."),
        ("I0089", "Traditional rice wine is a home-brewed or specialty product; commercial retail varies by regional regulation.", "Survey regional specialty food vendors."),
        ("I0092", "Pork lard is rendered at home from pork belly or fat trimmings.", "Derive cost from fresh pork cuts."),
        ("I0095", "Live mud crab prices fluctuate daily by tide and shell size in coastal fishery markets.", "Conduct coastal fishery landing / San Pya fish market price survey."),
        ("I0096", "Ginger cooking wine is an imported Chinese culinary specialty condiment.", "Survey Chinatown import grocery shops."),
        ("I0099", "Preserved edible jellyfish is a specialty banquet delicacy sold to commercial caterers.", "Survey seafood import wholesalers."),
        ("I0117", "Pickled sour shrimp (Pazun-gyin) is an artisanal cottage-industry fermented delicacy.", "Survey traditional wet market fermented food stalls."),
        ("I0125", "Ash gourd / Wax gourd is a seasonal backyard garden vine vegetable.", "Survey traditional neighborhood wet markets."),
        ("I0127", "Tamarind young tender leaves are seasonal tree shoots gathered from wild trees in Central Myanmar.", "Survey seasonal morning wet markets."),
        ("I0131", "Cassia flower buds (Mezali-hpu) are seasonal medicinal buds harvested exclusively around Tazaungdaing full moon festival.", "Survey seasonal November festival wet markets."),
        ("I0132", "Pea eggplants (Hkayan-kasaw) are wild tropical berries picked from backyard shrubs or small village growers.", "Survey smallholder ethnic produce stalls."),
        ("I0138", "Tender pea tendrils / bean leaves are short-shelf-life greens sold in local morning wet markets.", "Survey fresh morning vegetable markets."),
        ("I0142", "Fish heads with collar meat are sold as soup cuts at wet market fish mongers.", "Survey San Pya and Central fish markets."),
        ("I0145", "Sour fermented bamboo shoots are traditional artisanal fermented wet market goods.", "Survey traditional fermented food stalls."),
        ("I0151", "Floral orchid nectar syrup is a heritage confectionery essence.", "Survey traditional heritage sweet ingredient suppliers."),
        ("I0152", "Lychee syrup is an occasional beverage ingredient.", "Survey beverage supply wholesalers."),
        ("I0153", "Grape syrup is an occasional beverage flavoring.", "Survey beverage supply wholesalers."),
        ("I0154", "Artificial food coloring powder/liquid is sold in micro-packets (10-50 MMK) at neighborhood sundry shops.", "Survey neighborhood sundry retail shops."),
        ("I0165", "Limewater is made in the household by dissolving slaked lime in water.", "Cost basis is negligible (<5 MMK); link to betel-nut lime stalls."),
        ("I0166", "Banana leaves are packing wrappers cut from trees, sold in bundles at flower/produce markets.", "Survey fresh morning produce wrapper stalls."),
        ("I0169", "Mont-let-saung rice droplets are made fresh by street dessert vendors.", "Derive cost from rice flour and pandan base ingredients."),
        ("I0174", "Commercial flavoring essence is sold in miniature vials at baking shops.", "Survey bakery supply shops."),
        ("I0175", "Ice cubes are produced in household freezers or purchased in 100-Kyat blocks at ice depots.", "Default to 0.0 MMK or nominal ice block cost."),
        ("I0176", "Toasted rice powder is prepared at home by dry-roasting raw rice (I0001) in a skillet and grinding.", "Derive cost dynamically from raw rice (I0001)."),
        ("I0177", "Fresh Mohinga rice vermicelli is purchased fresh daily from local neighborhood noodle presses.", "Survey local neighborhood noodle pressing shops."),
        ("I0180", "Galangal rhizome is sold fresh in small quantities in traditional vegetable stalls.", "Survey wet market spice vendors."),
        ("I0181", "Fermented bean curd in chili oil is sold in small glass jars in Chinese sundry shops.", "Survey Chinese grocery shops."),
        ("I0182", "Snow fungus / Cloud ear is an imported dried delicacy sold in Chinese herbal pharmacies.", "Survey Chinese herbal medicine and dried goods shops."),
        ("I0183", "Dried daylily flower buds are traditional Chinese dried banquet ingredients.", "Survey Chinatown dried ingredient merchants."),
        ("I0185", "Pork cracklings are fried at home or purchased from snack vendors.", "Derive cost from pork fat/skin cuts."),
        ("I0187", "Shan rice noodles are made fresh daily in Shan communities and local wet markets.", "Survey local fresh noodle presses."),
        ("I0188", "Traditional pickled mustard greens are prepared in earthenware jars at cottage scale.", "Survey traditional pickle vendors in wet markets."),
        ("I0189", "Fresh Mee Shay rice noodles are made fresh daily by noodle artisans.", "Survey local fresh noodle presses."),
        ("I0190", "Baker's active dry yeast is sold in 11g sachets at baking shops.", "Survey bakery supply shops."),
        ("I0195", "Candied citron peel is a holiday fruit preserve sold at baking suppliers.", "Survey bakery ingredient suppliers."),
        ("I0196", "Baking soda is identical to I0164.", "Link to I0164 price observation."),
        ("I0201", "Fresh water chestnuts are seasonal marsh tubers sold in Chinatown wet markets.", "Survey Chinatown fresh produce stalls."),
        ("I0202", "Chinese cooking wine is sold in specialized import shops.", "Survey Chinatown import grocery shops."),
        ("I0203", "Fresh wonton wrappers are prepared fresh daily at fresh noodle presses.", "Survey fresh noodle presses in wet markets."),
        ("I0204", "Fermented bean paste sauce is sold in traditional ceramic jars at local markets.", "Survey traditional condiment stalls."),
        ("I0205", "Sherry cooking wine is identical to I0060.", "Link to I0060 price observation."),
        ("I0208", "Black sesame seeds are sold in traditional grain wholesale shops.", "Survey grain wholesale markets."),
        ("I0209", "Mustard seeds are identical to I0062.", "Link to I0062 price observation."),
        ("I0210", "Fresh spring roll wrappers are prepared fresh daily at local noodle presses.", "Survey fresh noodle presses in wet markets."),
        ("I0212", "Glacé cherries are imported confectionery fruit decorations.", "Survey bakery supply shops."),
        ("I0213", "Vanilla essence is sold in small vials at baking shops.", "Survey bakery supply shops."),
        ("I0214", "French beans are identical in species to I0015.", "Link to I0015 market survey."),
        ("I0215", "Marine ocean fish is sold at coastal landing jetties and central fish markets.", "Survey San Pya and Maw Tin fish markets."),
        ("I0216", "Plain baby biscuits are sold in tin boxes at sundry shops.", "Survey neighborhood sundry shops."),
        ("I0217", "Fresh squeezed orange juice is prepared in the home from fresh oranges (I0112).", "Derive cost dynamically from fresh oranges (I0112)."),
        ("I0218", "Tapioca flour is identical to I0063.", "Link to I0063 price observation."),
        ("I0219", "Golden caramel syrup is made in the home by melting sugar (I0005) with water.", "Derive cost from granulated sugar (I0005)."),
        ("I0220", "Live striped snakehead fish (Nga-yant) is sold alive in wet market water basins.", "Survey San Pya central fish market."),
        ("I0221", "Mutton soup bones are sold as broth bones by butchers upon request.", "Survey local mutton butcher stalls.")
    ]

    unmatched_list = []
    for ing_id, reason, action in unmatched_specs:
        item = catalog_map.get(ing_id)
        if item:
            unmatched_list.append({
                "ingredient_id": ing_id,
                "name_mm": item["name_mm"],
                "name_en": item["name_en"],
                "category": item["category"],
                "reason": reason,
                "attempted_sources": ["CSO", "YCE", "Citymall", "World Bank"],
                "suggested_action": action
            })

    return unmatched_list
