from re import *


horizon = [
  "http://www.google.com/",
  "http://www.bing.com/",
  "http://www.yahoo.com/",
  "http://www.duckduckgo.com/",
  "http://www.aol.com/",
  "http://www.msn.com/"
]
start_array = [1,2,3,4,5,6,7,8,9,10]
results_array = []
end_array = []

def manipulate_array_data():
  array_size = len(horizon)
  for i in range(0, array_size):
    placeholder = horizon.pop(0)
    print("pinging: " + str(placeholder))
    calc = calculation(placeholder)
    results_array.append(calc)
    end_array.insert(0, placeholder)

def calculation(data):
  return data[11:15]

manipulate_array_data()

print("start array: " + str(horizon))
print("results: " + str(results_array))
print("end array: " + str(end_array))

#do ping stuff here
for index in start_array:
  print(start_array.index(index))
