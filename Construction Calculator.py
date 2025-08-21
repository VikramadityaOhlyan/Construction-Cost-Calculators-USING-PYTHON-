# Construction Cost Calculator (per square foot) WITHOUT Finishing

def construction_calculator(area_sqft):
    """
    Calculate construction material requirements & costs
    based on area in square feet (only structural materials).
    """

    # Approximate material requirements per sq. foot
    cement_bags_per_sqft = 0.037   # bags per sqft
    tmt_kg_per_sqft = 0.42         # kg per sqft
    sand_cft_per_sqft = 0.0046     # cubic feet per sqft
    bricks_per_sqft = 0.74         # bricks per sqft

    # Prices (can be updated as per local market)
    cement_bag_price = 350        # INR per bag (50kg)
    tmt_price_per_kg = 65         # INR per kg
    sand_price_per_cft = 55       # INR per cubic feet
    brick_price = 9               # INR per brick

    # Calculations
    cement_bags = cement_bags_per_sqft * area_sqft
    tmt_kg = tmt_kg_per_sqft * area_sqft
    sand_cft = sand_cft_per_sqft * area_sqft
    bricks = bricks_per_sqft * area_sqft

    cement_cost = cement_bags * cement_bag_price
    tmt_cost = tmt_kg * tmt_price_per_kg
    sand_cost = sand_cft * sand_price_per_cft
    brick_cost = bricks * brick_price

    total_cost = cement_cost + tmt_cost + sand_cost + brick_cost

    return {
        "Area (sqft)": area_sqft,
        "Cement (bags)": round(cement_bags, 2),
        "Cement cost": round(cement_cost, 2),
        "TMT (kg)": round(tmt_kg, 2),
        "TMT cost": round(tmt_cost, 2),
        "Sand (cft)": round(sand_cft, 2),
        "Sand cost": round(sand_cost, 2),
        "Bricks (pcs)": round(bricks, 2),
        "Brick cost": round(brick_cost, 2),
        "Total Estimated Cost": round(total_cost, 2)
    }


# Example usage
if __name__ == "__main__":
    area = float(input("Enter the area of construction in square feet: "))
    result = construction_calculator(area)

    print("\n--- Construction Cost Estimate (Structural Only) ---")
    for k, v in result.items():
        print(f"{k}: {v}")
