import json

def generate_latest_retail_summary():
    with open("ingredient_prices.json", "r", encoding="utf-8") as f:
        prices = json.load(f)

    # Filter for retail or model estimates (prioritizing verified retail)
    city_summary = {"Yangon": {}, "Mandalay": {}}

    for p in prices:
        city = p["city"]
        if city not in city_summary:
            continue
        ing_id = p["ingredient_id"]
        
        current = city_summary[city].get(ing_id)
        # We prefer retail over estimate, and newer date over older date
        is_retail = p["price_type"] == "retail"
        
        if current is None:
            city_summary[city][ing_id] = p
        else:
            current_is_retail = current["price_type"] == "retail"
            if is_retail and not current_is_retail:
                city_summary[city][ing_id] = p
            elif is_retail == current_is_retail:
                if (p["observed_date"] or "") >= (current["observed_date"] or ""):
                    city_summary[city][ing_id] = p

    # Format into clean array
    output = {
        "generated_at": prices[0]["collected_at"] if prices else None,
        "description": "Derived summary of latest usable retail food prices by city for Zay Chin budgeting and recommendation engine.",
        "cities": {}
    }

    for city, ings in city_summary.items():
        output["cities"][city] = [
            {
                "ingredient_id": p["ingredient_id"],
                "name_mm": p["ingredient_name_mm"],
                "name_en": p["ingredient_name_en"],
                "latest_product_name": p["product_name"],
                "latest_brand": p["brand"],
                "price_mmk": p["price_mmk"],
                "unit": p["original_unit"],
                "normalized_price_mmk_per_kg": p["normalized_price_mmk_per_kg"],
                "price_type": p["price_type"],
                "observation_type": p["observation_type"],
                "observed_date": p["observed_date"],
                "source_name": p["source_name"],
                "source_record_id": p["source_record_id"]
            }
            for p in sorted(ings.values(), key=lambda x: x["ingredient_id"])
        ]

    with open("latest_retail_prices_by_city.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("Exported latest_retail_prices_by_city.json.")

if __name__ == "__main__":
    generate_latest_retail_summary()
