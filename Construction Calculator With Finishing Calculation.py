# Full Construction Cost Calculator (per square foot) WITH Finishing

def construction_calculator(area_sqft):
    """
    Calculate construction material requirements & costs
    including structural + finishing costs.
    """

    # --- STRUCTURAL MATERIALS (per sqft) ---
    cement_bags_per_sqft = 0.037   # bags per sqft
    tmt_kg_per_sqft = 0.42         # kg per sqft
    sand_cft_per_sqft = 0.0046     # cubic feet per sqft
    bricks_per_sqft = 0.74         # bricks per sqft

    # Prices (adjust as per local market)
    cement_bag_price = 350        # INR per bag (50kg)
    tmt_price_per_kg = 65         # INR per kg
    sand_price_per_cft = 55       # INR per cubic feet
    brick_price = 9               # INR per brick

    # --- FINISHING COST (per sqft estimates in INR) ---
    plastering_rate = 70      # Rs/sqft
    flooring_rate = 120       # Rs/sqft
    painting_rate = 60        # Rs/sqft
    electrical_rate = 80      # Rs/sqft
    plumbing_rate = 100       # Rs/sqft
    doors_windows_rate = 150  # Rs/sqft

    # --- STRUCTURAL CALCULATIONS ---
    cement_bags = cement_bags_per_sqft * area_sqft
    tmt_kg = tmt_kg_per_sqft * area_sqft
    sand_cft = sand_cft_per_sqft * area_sqft
    bricks = bricks_per_sqft * area_sqft

    cement_cost = cement_bags * cement_bag_price
    tmt_cost = tmt_kg * tmt_price_per_kg
    sand_cost = sand_cft * sand_price_per_cft
    brick_cost = bricks * brick_price

    structural_cost = cement_cost + tmt_cost + sand_cost + brick_cost

    # --- FINISHING CALCULATIONS ---
    plastering_cost = plastering_rate * area_sqft
    flooring_cost = flooring_rate * area_sqft
    painting_cost = painting_rate * area_sqft
    electrical_cost = electrical_rate * area_sqft
    plumbing_cost = plumbing_rate * area_sqft
    doors_windows_cost = doors_windows_rate * area_sqft

    finishing_cost = (
        plastering_cost + flooring_cost + painting_cost +
        electrical_cost + plumbing_cost + doors_windows_cost
    )

    # --- TOTAL COST ---
    total_cost = structural_cost + finishing_cost

    return {
        "Area (sqft)": area_sqft,
        "STRUCTURAL COSTS": {
            "Cement (bags)": round(cement_bags, 2),
            "Cement cost": round(cement_cost, 2),
            "TMT (kg)": round(tmt_kg, 2),
            "TMT cost": round(tmt_cost, 2),
            "Sand (cft)": round(sand_cft, 2),
            "Sand cost": round(sand_cost, 2),
            "Bricks (pcs)": round(bricks, 2),
            "Brick cost": round(brick_cost, 2),
            "Structural Cost": round(structural_cost, 2)
        },
        "FINISHING COSTS": {
            "Plastering": plastering_cost,
            "Flooring": flooring_cost,
            "Painting": painting_cost,
            "Electrical": electrical_cost,
            "Plumbing": plumbing_cost,
            "Doors & Windows": doors_windows_cost,
            "Finishing Cost": finishing_cost
        },
        "TOTAL CONSTRUCTION COST": round(total_cost, 2),
        "Cost per sqft": round(total_cost / area_sqft, 2)
    }


# Example usage
if __name__ == "__main__":
    area = float(input("Enter the area of construction in square feet: "))
    result = construction_calculator(area)

    print("\n--- Construction Cost Estimate (With Finishing) ---")
    for section, data in result.items():
        if isinstance(data, dict):
            print(f"\n{section}:")
            for k, v in data.items():
                print(f"  {k}: {v}")
        else:
            print(f"{section}: {data}")
