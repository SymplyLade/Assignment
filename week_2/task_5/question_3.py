# Tuple Operations
states = tuple(input(f"Enter state{i+1}: ") for i in range (5))
print("first state:", states[0])
print("last state:", states[-1])
if "lagos" in states:
      print("Yes")
else:
    print("No")
print("Number of states entered:", len(states))
