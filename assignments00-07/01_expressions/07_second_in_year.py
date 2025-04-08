days_per_year:int=360
hours_per_day:int=24
mins_per_hour=60
secs_per_min:int=60

def main():

    # Calculate total secods in a year
    total_seconds:int= days_per_year * hours_per_day * mins_per_hour * secs_per_min

    # Print answer
    print(f"There are {total_seconds} seconds in a year!")

if __name__ == '__main__':
    main()