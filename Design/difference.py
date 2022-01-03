import library

allTables = library.importDirectory("data/raw")

# Loop through the top level of the list
t = 0
for table in allTables:
    t += 1
    # Loop through the second level of the list
    i = 0
    j = 0
    for row in table:
        # Loop through the third level of the list
        if row[8] == "11:00":
            row_of_11 = i
            temp_of_11 = row[9]
        if row[8] == "21:00":
            row_of_21 = j
            temp_of_21 = row[9]

            difference = float(temp_of_11) - float(temp_of_21)
            day = round(i / 24)
            wind_speed_21 = row[19]
            if t == 1:
                a = "May"
            elif t == 2:
                a = "June"
            elif t == 3:
                a = "August"
            elif t == 4:
                a = "March"
            elif t == 5:
                a = "September"
            elif t == 6:
                a = "October"
            elif t == 7:
                a = "February"
            elif t == 8:
                a = "April"
            elif t == 9:
                a = "July"
            processed_data = [a, day, difference, wind_speed_21]
            print(processed_data)
        i += 1
        j += 1
