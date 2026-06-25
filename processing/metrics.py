import math

def log_list(lyst):
    for index in range(len(lyst)):
      if lyst[index] <= 0:
        continue
      lyst[index] = math.log(lyst[index])
    return lyst

states_data = {}

def refine_states_pops(states_pops, popMin, popMax, citiesMin, citiesMax):
  states_pops_new = {}
  for currentState, currentPops in states_pops.items():
    
    # print(currentState, currentPops)

    currentPopsNew = currentPops
    currentPopsNew.sort(reverse = "True")
    # includes only pops w/in inputted range
    currentPops = [x for x in currentPopsNew if popMin <= int(x) <= popMax]
    # excludes states with too few cities, truncates states with too many
    if len(currentPopsNew) < citiesMin:
      continue
    elif len(currentPopsNew) > citiesMax:
      currentPopsNew = currentPopsNew[0:citiesMax]
    
    states_pops_new[currentState] = currentPopsNew
    
  return states_pops_new

def gen_states_data(states_pops):
  for currentState, currentPops in states_pops.items():
    rank = list(range(1, len(currentPops) + 1))
    size = currentPops

    rank = log_list(rank)
    size = log_list(size)

    states_data[currentState] = {"rank": rank, "size": size}
  return states_data
