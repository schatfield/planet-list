planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(3, "Earth")
planet_list.insert(4,"Venus")
planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_list.append("Pluto")
rocky_planets = planet_list[:4]
print(rocky_planets)
del planet_list[-1]
print(planet_list)

#mercury, venus, earth, mars
# SLICE example from class:
# create a new list from a subset of values in another list with slice
# my_list = [1, 2, 4, "hello", "monkey"]
# my_subset = my_list[0:3]
# my_subset = my_list[1:3]
# my_subset = my_list[:3]
# my_subset = my_list[2:]
# my_subset = my_list[2:34]
# my_subset = my_list[2:-1]
# print(my_subset)
# print(my_list)

#Use append() to add Jupiter and Saturn at the end of the list.
#Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
#Use insert() to add Earth, and Venus in the correct order.
#Use append() again to add Pluto to the end of the list.
#Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
#Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.