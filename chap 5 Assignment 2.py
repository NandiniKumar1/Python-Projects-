def compute_cost(area, price_per_gallon):
    # Constants given
    sqft_per_gallon = 112
    labor_hours_per_gallon = 8
    labor_cost_per_hour = 35.00

    # Calculate gallons needed 
    gallons_needed = -(-area // sqft_per_gallon)

    # Calculate hours of labor needed
    labor_hours = gallons_needed * labor_hours_per_gallon

    # Calculate cost of paint
    paint_cost = gallons_needed * price_per_gallon

    # Calculate labor charges
    labor_charges = labor_hours * labor_cost_per_hour

    # Calculate total cost
    total_cost = paint_cost + labor_charges

    # Return all calculated values
    return gallons_needed, labor_hours, paint_cost, labor_charges, total_cost

# Example usage:
area = 500
price_per_gallon = 25.00

result = compute_cost(area, price_per_gallon)
print(f"Gallons of paint required: {result[0]}")
print(f"Hours of labor required: {result[1]}")
print(f"Cost of paint: ${result[2]:.2f}")
print(f"Labor charges: ${result[3]:.2f}")
print(f"Total cost of the paint job: ${result[4]:.2f}")
