import re

number: float = -130.2422468426
# number: float = -130
number_list = [
	-13.043,
	2424.2193183,
	-11223.0,
	111,
	12342.248248924,
	11.322442,
]
for number in number_list:
	number_str = str(number)
	print(f"{number_str} | ", end="")
	match = re.search(r"\.\d+", number_str)
	if match:
		if len(match.group()) > 5:
			print("Display irreducible fraction")
		else:
			print("Display full decimal")
	else:
		print("No match")
