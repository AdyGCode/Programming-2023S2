counts = [0]*24

# for line in handle
string = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
split_up_line = string.split(" ")
time_section = split_up_line[6]
(hours, minutes, seconds) = time_section.split(":")
counts[int(hours)] += 1
# end of for

# now display results
for count in range(0,24):
    print(f"{count:02} {counts[count]}")

