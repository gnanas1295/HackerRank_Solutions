import sys

input_data = sys.stdin.read().strip()

final_dict = []
count = 1
ini_data = int(input_data[0])
# print(ini_data)

for data in input_data[1:]:
    # print(f"GS: {data}")
    if int(data) == ini_data:
        count += 1
    else:
        final_dict.append(f"({count}, {ini_data})")
        ini_data = int(data)
        count = 1
        # print(f"Coming Here: {final_dict}")
final_dict.append(f"({count}, {ini_data})")
print(" ".join(final_dict))