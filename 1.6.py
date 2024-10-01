my_dict = {"Denis": 1998, "Richard": 1996, "Smit": 1995}
print("Dict: " + str(my_dict) )
print("Existing value: " + str(my_dict["Richard"]))
print("Not existing value: " + str(my_dict.get("Kamila")))
print("Deleted value: " + str(my_dict.pop("Smit")))
my_dict.update({"Kamila": 1994, "Serg": 1993})
print("Modified dictionary: " + str(my_dict) + "\n")

my_set = {1, "Pineapple", 3.14,}
print("Set: " + str(my_set))
my_set.add(5)
my_set.add(111)
my_set.add((1, 5, 6))
my_set.discard(3.14)
#my_set.remove(1)
print("Modified set: " + str(my_set))