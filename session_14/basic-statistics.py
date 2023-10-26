# Read data from data.txt
# find location in dictionary
#   add temperature to the total
#   add one to count
# { "location":[ count, total ], ... }

import csv

FILENAME = "data.txt"
STATS_FILENAME = "stats.txt"

data_dictionary = {}

with open(FILENAME, mode='r') as file:
    csvFile = csv.reader(file)
    count = 0
    for line in csvFile:
        print(count, ":", line)
        # ignore the first (header) line
        if count > 0:
            location = line[0]
            temperature = line[1]
            current_count = 0
            current_total = 0
            if location in data_dictionary:
                current_total = data_dictionary[location]["total"]
                current_count = data_dictionary[location]["count"]
            current_total = current_total + float(temperature)
            current_count = current_count + 1
            data_dictionary.update({location: {"count": current_count, "total": current_total}})
        print(data_dictionary)
        count = count + 1
# Auto-close file due to the WITH statement

with open(STATS_FILENAME, mode='w') as stats_file:
    # for location in data_dictionary:
    #     data = data_dictionary[location]
    #     total = data["total"]
    #     count = data["count"]
    for location, data in data_dictionary.items():
        total = data["total"]
        count = data["count"]
        print(f"Location: {location:15} Average (Mean) Temp: {total / count:6.2f}",
              file=stats_file)
