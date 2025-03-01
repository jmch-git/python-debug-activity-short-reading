from glob import glob


offense = False
defense = False
rule_changes = False

def get_offense():
    global offense
    offense = True

def get_defense():
    global defense
    defense = True
    num1 = 10
    num2 = 50

    def add_nums():
      nonlocal num2 # get a variable from the scope above that is not a global scope
      num2 = num2 + num1

    def print_num():
      print("num2 is", num2)

    add_nums()
    print_num()  

    def get_rule_changes():
      global rule_changes
      rule_changes = True

    if offense and defense:
        get_rule_changes()

get_offense()
get_defense()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
  print("We're going to the Super Bowl!")
else:
  print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")