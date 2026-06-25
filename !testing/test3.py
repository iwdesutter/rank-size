import csv

def get_indicators(file, state_header, pop_header):
  
  text = []
  with open(file, "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file)

    counter = 0
    for line in csv_reader:
      text.append(line)
      counter += 1
  ##    if counter > 1000:
  ##      break

  header = text.pop(0)
  indexState = header.index(state_header)
  indexIndicator = header.index(pop_header)

  indicatorsDict = {}
  for row in text:
    currentState = row[indexState]
    currentIndicator = row[indexIndicator].replace(",","")
    print(currentState, currentIndicator)

    # checks current indicator, converts to float
    if currentIndicator.replace(".","").isnumeric():
      currentIndicator = float(currentIndicator)
    else:
      continue

    # creates/adds country with pops to list
    indicatorsDict[currentState] = currentIndicator

    # print(currentState, currentPop)

  # return statesDict
  return indicatorsDict

data_lyst = [
  ['State', 'Reg Slope', 'Reg Int', 'R', 'R2', 'Pattern'],
  ['ARG', -0.9035581772038387, 14.957180389508219, -0.9775545335240566, 0.955612866013436, 'primate'],
  ['BOL', -1.0181784994358043, 13.949869457907655, -0.9083976329640749, 0.8251862595747342, 'binary'],
  ['BRA', -0.8121718699311918, 15.829136393408662, -0.997701779280241, 0.9954088403789586, 'binary'],
  ['CAN', -0.7500515016436988, 14.335433416261898, -0.9617915794823204, 0.9250430423630966, 'log-normal'],
  ['CHL', -0.8835318766859175, 14.15346223542076, -0.9018638164426288, 0.8133583434084637, 'primate']
]


indicatorsDict = get_indicators("C:/Users/eatyo/OneDrive/Desktop/Rank-Size/!testing/HDR25_Composite_indices_complete_time_series.csv", "iso3", "hdi_2023")
# print(indicatorsDict)
for row in data_lyst:
  currentState = row[0]
  if currentState in indicatorsDict:
    row.append(indicatorsDict[currentState])
  else:
    row.append("")
print(indicatorsDict)
print(data_lyst)

input("Enter to close program.")