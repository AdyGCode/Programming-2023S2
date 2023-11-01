from os.path import exists

FILENAME = "data.txt"

# Change these values when testing
location = "York"
temperature = 27.8

# check to see if the file "FILENAME" exists,
# if not, set header to "Location, Temperature"
header = None

file_exists = exists(FILENAME)
if not file_exists:
    header = "Location, Temperature"

file_handle = open(FILENAME, "a")
if not file_exists:
    print(header, file=file_handle)

print(f"\"{location}\", {temperature}", file=file_handle)
file_handle.close()
