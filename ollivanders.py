counter = 0
number_wands = 0
elder = 0
hawthorn = 0 
willow = 0
holly = 0
client = input("Are there any clients? (yes/no)")

while client == "yes":
  counter += 1
  wand = input("Has a wand been sold? (yes/no)")
  if wand == "yes":
    print("1. Elder Wand 2. Hawthorn wand 3. Willow wand 4.Holly Wand")

  type_of_wand = int(input("Which wand has been bought?"))
  if type_of_wand == 1:
    elder += 1
    client = input("Are there any clients (yes/no)") 
  elif type_of_wand == 2: 
    hawthorn += 1
    client = input("Are there any clients (yes/no)") 
  elif type_of_wand == 3:
    willow += 1
    client = input("Are there any clients (yes/no)") 
  elif type_of_wand == 4:
    holly += 1
    client = input("Are there any clients (yes/no)") 
  else:
    print("Invalid wand type")
    client = input("Are there any clients (yes/no)")
    break

print(f"This number of costumers came today {counter}")
print(f"Number of elder Wands sold: {elder}")
print(f"Number of hawthorn Wands sold: {hawthorn}")
print(f"Number of willow Wands sold: {willow}")
print(f"Number of holly Wands sold: {holly}")
