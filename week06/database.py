with open ('week06/life-expectancy.csv') as file:
    for line in file:
        lowest_life = float('inf')
highest_life = float('-inf')
lowest_country = ""
lowest_year = ""
highest_country = ""
highest_year = ""

target_year = input("Enter the year of interest: ")

year_count = 0
year_sum = 0
year_min = float('inf')
year_max = float('-inf')
year_min_country = ""
year_max_country = ""

with open('week06/life-expectancy.csv') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        country = parts[0]
        year = parts[2]
        life_expectancy = float(parts[3])
        
        if life_expectancy < lowest_life:
            lowest_life = life_expectancy
            lowest_country = country
            lowest_year = year
            
        if life_expectancy > highest_life:
            highest_life = life_expectancy
            highest_country = country
            highest_year = year
            
        if year == target_year:
            year_sum += life_expectancy
            year_count += 1
            
            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_country = country
                
            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_country = country

print(f"\nThe overall highest life expectancy is: {highest_life:.3f} from {highest_country} in {highest_year}")
print(f"The overall lowest life expectancy is: {lowest_life:.3f} from {lowest_country} in {lowest_year}")

if year_count > 0:
    year_avg = year_sum / year_count
    print(f"\nFor the year {target_year}:")
    print(f"The average life expectancy was: {year_avg:.3f}")
    print(f"The maximum life expectancy was in {year_max_country} with {year_max:.3f}")
    print(f"The minimum life expectancy was in {year_min_country} with {year_min:.3f}")
else:
    print(f"\nNo data found for the year {target_year}")