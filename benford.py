import json
import sys

import matplotlib.pyplot as plt
import requests

key = "area"
url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-surface-area.json"

response = requests.get(url)
json_data = None

if response.status_code == 200:
    json_data = response.text  # Get the content of the response
else:
    print("Failed to retrieve the content")
    sys.exit()


def count_numbers_starting_with_digit(num_list, digit):
    count = 0
    for num in num_list:
        # Convert number to string and check if it starts with the specified digit
        if str(num).startswith(str(digit)):
            count += 1
    return count


jsn = json.loads(json_data)
data = [int(x[key]) for x in jsn if x[key] is not None]

x = [x for x in range(1, 10)]
y = [count_numbers_starting_with_digit(data, x) for x in range(1, 10)]

plt.plot(x, y, color="blue")
plt.bar(x, y, color="green")
plt.plot()

plt.title("Benford's Law Chart")
plt.show()
