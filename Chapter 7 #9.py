# population_analysis.py

def main():
    start_year = 1950

    # Population data you provided (in thousands)
    population = [
        151868, 153982, 156393, 158956, 161884, 165069, 168088, 171187, 174149,
        177135, 179979, 182992, 185771, 188483, 191141, 193526, 195576, 197457,
        199399, 201385, 203984, 206827, 209284, 211357, 213342, 215465, 217563,
        219760, 222095, 224567, 227225, 229466, 231664, 233792, 235825, 237924,
        240133, 242289, 244499, 246819, 249623
    ]

    # Calculate year-to-year population changes
    changes = []
    for i in range(1, len(population)):
        change = population[i] - population[i - 1]
        changes.append(change)

    # Calculate average annual change
    avg_change = sum(changes) / len(changes)

    # Find greatest and smallest increase and corresponding years
    greatest_increase = max(changes)
    smallest_increase = min(changes)
    year_greatest = start_year + changes.index(greatest_increase) + 1
    year_smallest = start_year + changes.index(smallest_increase) + 1

    # Display results
    print(f"Average annual change in population: {avg_change:.2f} thousand")
    print(f"Year with greatest increase: {year_greatest} ({greatest_increase} thousand)")
    print(f"Year with smallest increase: {year_smallest} ({smallest_increase} thousand)")

if __name__ == "__main__":
    main()
