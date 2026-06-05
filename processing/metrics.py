import math

def log_list(lyst):
    for index in range(len(lyst)):
      lyst[index] = math.log(lyst[index])
    return lyst

states_data = {}
def gen_states_data(states_pops):
  for currentState, currentPops in states_pops.items():
    rank = list(range(1, len(currentPops) + 1))
    size = currentPops
    size.sort(reverse = "True")

    rank = log_list(rank)
    size = log_list(size)

    states_data[currentState] = {"rank": rank, "size": size}
  return states_data
