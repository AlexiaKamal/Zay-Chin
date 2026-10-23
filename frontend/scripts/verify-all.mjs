import assert from "node:assert";
import { getLocalRecipeDetail, queryLocalRecipes, getLocalCategories } from "../src/lib/local-recipes.ts";
import { getLocalMarkets, getLocalMealPlan, getLocalMealReplacements, getLocalGroceryList } from "../src/lib/local-services.ts";

console.log("=============================================================");
console.log("ZAY CHIN VERIFICATION: RECIPES, NUTRITION, PRICES, SERVICES");
console.log("=============================================================\n");

let passed = 0;
let total = 0;

function test(name, fn) {
  total++;
  try {
    fn();
    console.log(`[PASS] ${name}`);
    passed++;
  } catch (err) {
    console.error(`[FAIL] ${name}`);
    console.error("       ", err);
  }
}

// 1. Recipe Detail & Instructions
test("R0001 (Butter Rice) detail has all 7 cooking instructions in MM & EN", () => {
  const recipe = getLocalRecipeDetail("R0001", 10, "Yangon");
  assert.ok(recipe, "Recipe must exist");
  assert.strictEqual(recipe.id, "R0001");
  assert.strictEqual(recipe.name_mm, "ထောပတ်ထမင်း");
  assert.strictEqual(recipe.name_en, "Butter Rice");

  assert.ok(Array.isArray(recipe.instructions), "Instructions must be array");
  assert.strictEqual(recipe.instructions.length, 7, "Must have exactly 7 instructions");
  assert.strictEqual(recipe.instructions[0].step_number, 1);
  assert.ok(recipe.instructions[0].instruction_mm.includes("ဆန်ကို"), "Instruction 1 MM must contain authentic text");
  assert.ok(recipe.instructions[0].instruction_en.includes("Clean and wash the rice"), "Instruction 1 EN must contain authentic text");
});

// 2. Nutrition Breakdown
test("R0001 nutrition breakdown has per_serving and recipe_total macro/micronutrients", () => {
  const recipe = getLocalRecipeDetail("R0001", 10, "Yangon");
  assert.ok(recipe.nutrition_breakdown, "nutrition_breakdown must be present");
  const ps = recipe.nutrition_breakdown.per_serving;
  assert.ok(ps.calories_kcal > 200, `Calories should be realistic (got ${ps.calories_kcal})`);
  assert.ok(ps.protein_g > 5, `Protein should be realistic (got ${ps.protein_g})`);
  assert.ok(ps.fat_g > 5, `Fat should be realistic (got ${ps.fat_g})`);
  assert.ok(ps.carbohydrates_g > 30, `Carbohydrates should be realistic (got ${ps.carbohydrates_g})`);
  assert.ok(recipe.nutrition_breakdown.weighted_ingredients_ratio, "weighted_ingredients_ratio should be present");
  assert.ok(recipe.nutrition_breakdown.disclaimer.includes("USDA FoodData Central"), "Disclaimer should be present");
});

// 3. Dynamic Live Prices & October 2026 Observations
test("R0001 live price breakdown has authentic October 2026 dates and sources", () => {
  const recipe = getLocalRecipeDetail("R0001", 10, "Yangon");
  assert.ok(recipe.cost_breakdown, "cost_breakdown must be present");
  assert.ok(recipe.cost_breakdown.estimated_cost_mmk > 10000, `Cost for 10 servings should be realistic (got ${recipe.cost_breakdown.estimated_cost_mmk})`);
  
  // Verify ingredient breakdown
  const items = recipe.cost_breakdown.ingredient_breakdown;
  assert.ok(items.length >= 10, "Must have all ingredients in breakdown");
  
  // Rice
  const rice = items.find((i) => i.ingredient_id === "I0001");
  assert.ok(rice, "Rice must be in breakdown");
  assert.ok(rice.is_priced, "Rice must be priced");
  assert.ok(rice.observation_date && rice.observation_date.startsWith("2026-10"), `Rice date must be Oct 2026 (got ${rice.observation_date})`);
  assert.ok(rice.observation_source.includes("CSO") || rice.observation_source.includes("Citymall"), `Source must be CSO or Citymall (got ${rice.observation_source})`);
  
  // Water
  const water = items.find((i) => i.ingredient_id === "I0012");
  assert.ok(water, "Water must be in breakdown");
  assert.ok(water.is_zero_cost_utility, "Water must be zero-cost utility");
  assert.strictEqual(water.item_cost_mmk, 0, "Water cost must be 0 MMK");
});

// 4. Market Finder Directory
test("Market Finder returns 5 verified locations across Yangon & Mandalay", () => {
  const allMarkets = getLocalMarkets();
  assert.strictEqual(allMarkets.length, 5, "Must return 5 verified markets");
  
  const ygn = getLocalMarkets("Yangon");
  assert.strictEqual(ygn.length, 4, "Must return 4 Yangon markets");
  
  const mdy = getLocalMarkets("Mandalay");
  assert.strictEqual(mdy.length, 1, "Must return 1 Mandalay market");
  
  for (const m of allMarkets) {
    assert.ok(m.latitude && m.longitude, `Market ${m.id} must have GPS coordinates`);
    assert.ok(m.recorded_price_observations_count > 0, `Market ${m.id} must have recorded observations`);
  }
});

// 5. Intelligent Meal Planner
test("Meal Planner generates 7-day schedule with 21 meals and daily nutrition", () => {
  const plan = getLocalMealPlan({
    city: "Yangon",
    household_size: 3,
    weekly_budget_mmk: 120000,
    meals_per_day: 3,
    plan_duration_days: 7,
  });
  
  assert.strictEqual(plan.schedule.length, 21, "Must generate 21 meal slots (7 days * 3 meals)");
  assert.strictEqual(plan.daily_summaries.length, 7, "Must generate 7 daily summaries");
  assert.ok(plan.estimated_total_cost_mmk > 0, "Estimated cost must be positive");
  assert.ok(plan.average_daily_calories_per_person > 1500, "Daily calories per person must be realistic");
  assert.ok(plan.average_daily_protein_per_person > 40, "Daily protein per person must be realistic");
  assert.ok(plan.budget_status_message_en.length > 0, "Must have English budget message");
  assert.ok(plan.budget_status_message_mm.length > 0, "Must have Myanmar budget message");
});

// 5b. Strict Budget Constraints Test
test("Meal Planner strictly respects weekly budget constraints without blowing budget", () => {
  const budgetTest60k = getLocalMealPlan({
    city: "Yangon",
    household_size: 2,
    weekly_budget_mmk: 60000,
    meals_per_day: 3,
    plan_duration_days: 7,
  });

  assert.ok(
    budgetTest60k.estimated_total_cost_mmk <= 60000,
    `Budget 60,000 MMK must not be exceeded: got ${budgetTest60k.estimated_total_cost_mmk}`
  );
  assert.strictEqual(budgetTest60k.is_budget_exceeded, false, "60,000 MMK plan should not be marked exceeded");
  assert.ok(
    budgetTest60k.budget_status_message_en.includes("Generated within your budget"),
    "Budget success message must be rendered"
  );

  const budgetTest90k = getLocalMealPlan({
    city: "Mandalay",
    household_size: 2,
    weekly_budget_mmk: 90000,
    meals_per_day: 3,
    plan_duration_days: 7,
  });

  assert.ok(
    budgetTest90k.estimated_total_cost_mmk <= 90000,
    `Budget 90,000 MMK must not be exceeded: got ${budgetTest90k.estimated_total_cost_mmk}`
  );
  assert.strictEqual(budgetTest90k.is_budget_exceeded, false, "90,000 MMK plan should not be marked exceeded");
});

// 6. Meal Replacement Candidates
test("Planner replacement returns alternative options with cost deltas", () => {
  const replacements = getLocalMealReplacements({
    city: "Yangon",
    household_size: 2,
    day_of_week: 1,
    meal_type: "lunch",
    current_recipe_id: "R0001",
  });
  
  assert.ok(replacements.length >= 3, "Must return at least 3 replacement candidates");
  for (const r of replacements) {
    assert.notStrictEqual(r.recipe_id, "R0001", "Replacement cannot be current recipe");
    assert.ok(typeof r.cost_difference_mmk === "number", "Must have cost difference");
    assert.ok(r.calories_kcal > 0, "Must have calories");
  }
});

// 7. Grocery List Aggregation
test("Grocery list aggregates ingredients, groups by aisles, and calculates subtotals", () => {
  const grocery = getLocalGroceryList({
    city: "Yangon",
    household_size: 4,
    recipe_ids: ["R0001", "R0002", "R0003"],
  });
  
  assert.ok(grocery.total_items_count > 0, "Must have aggregated items");
  assert.ok(grocery.groups.length >= 3, "Must group into multiple shopping aisles");
  assert.ok(grocery.estimated_total_mmk > 0, "Estimated total MMK must be positive");
  
  for (const g of grocery.groups) {
    assert.ok(g.category_id, "Group must have category_id");
    assert.ok(g.category_name_en, "Group must have English category name");
    assert.ok(g.category_name_mm, "Group must have Myanmar category name");
    assert.ok(g.items.length > 0, "Group must have items");
  }
});

// 8. Real-World Retail Packaging & Discrete Rounding
test("Real-world retail packaging rounds discrete items (0.6 cucumber -> 1 piece) and packages salt/sugar", async () => {
  const { calculateRetailPurchasing, isPantryStaple } = await import("../src/lib/retail-packaging.ts");

  // Discrete cucumber piece test: 0.6 cucumber must purchase 1 whole piece
  const cucumber = calculateRetailPurchasing({
    ingredient_id: "I0088", // Cucumber
    name_en: "Cucumber",
    name_mm: "သခွားသီး",
    unit: "piece",
    quantity: 0.6,
    unit_price_mmk: 800,
    normalized_price_per_kg: 800,
    observation_package_unit: "piece",
    observation_package_price: 800,
  });

  assert.strictEqual(cucumber.purchasable_quantity, 1, "0.6 cucumber must round up to 1 whole piece");
  assert.strictEqual(cucumber.purchasable_unit, "piece");
  assert.strictEqual(cucumber.retail_package_price_mmk, 800, "Store package price must be for 1 whole piece (800 MMK)");
  assert.strictEqual(cucumber.portion_cost_mmk, 480, "Portion cost must be prorated: 0.6 * 800 = 480 MMK");

  // Packaged pantry staple: Salt (I0004) - 3 tbsp (22.5g)
  const salt = calculateRetailPurchasing({
    ingredient_id: "I0004", // Salt
    name_en: "Salt",
    name_mm: "ဆား",
    unit: "g",
    quantity: 22.5,
    unit_price_mmk: 3000,
    normalized_price_per_kg: 3000,
    observation_package_unit: "kg",
    observation_package_price: 3000,
  });

  assert.strictEqual(salt.is_pantry_staple, true, "Salt must be flagged as a pantry staple");
  assert.strictEqual(salt.purchasable_quantity, 1, "Store purchase quantity must be 1 pack");
  assert.strictEqual(salt.package_description, "1 pack (400g)", "Salt pack description should be 1 pack (400g)");
  assert.strictEqual(salt.retail_package_price_mmk, 1200, "400g salt pack at 3000 MMK/kg is 1,200 MMK");
  assert.strictEqual(salt.portion_cost_mmk, 68, "Portion cost of 22.5g salt is ~68 MMK");
});

// 9. Dual-Tier Grocery Budgeting & Pantry Toggle
test("Grocery list dual-tier totals: retail_total_mmk >= estimated_total_mmk and pantry deduction works", () => {
  const grocery = getLocalGroceryList({
    city: "Yangon",
    household_size: 2,
    recipe_ids: ["R0001", "R0002"],
  });

  assert.ok(grocery.retail_total_mmk > 0, "Retail total MMK must be calculated");
  assert.ok(grocery.retail_total_mmk >= grocery.estimated_total_mmk, "Retail store checkout cost must be >= portion cost");
  assert.ok(grocery.pantry_adjusted_total_mmk > 0, "Pantry adjusted total must be calculated");
  assert.ok(grocery.pantry_adjusted_total_mmk <= grocery.retail_total_mmk, "Pantry adjusted total must be <= full retail cost");
  assert.ok(grocery.pantry_items_count > 0, "Must identify pantry items in recipes");

  // Verify each grocery item has retail packaging attributes
  let foundPackagedStaple = false;
  for (const group of grocery.groups) {
    for (const item of group.items) {
      if (!item.is_zero_cost_utility) {
        assert.ok(item.purchasable_quantity >= 1, `Item ${item.name_en} purchasable_quantity must be >= 1`);
      }
      assert.ok(item.package_description, `Item ${item.name_en} must have package_description`);
      assert.ok(item.retail_package_price_mmk !== undefined, `Item ${item.name_en} must have retail_package_price_mmk`);
      if (item.is_pantry_staple) {
        foundPackagedStaple = true;
      }
    }
  }
  assert.ok(foundPackagedStaple, "Should find at least one pantry staple in grocery list");
});

console.log(`\nResults: ${passed}/${total} tests passed!`);
if (passed === total) {
  console.log("✓ ALL TESTS PASSED SUCCESSFULLY!");
  process.exit(0);
} else {
  console.error("✗ SOME TESTS FAILED!");
  process.exit(1);
}
