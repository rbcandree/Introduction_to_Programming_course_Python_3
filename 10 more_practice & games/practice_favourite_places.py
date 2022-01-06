placesAbby = str(input("Abby, write your three favourite places: "))
placesJohn = str(input("John, write your three favourite places: "))
placesEmily = str(input("Emily, write your three favourite places: "))

favourite_places  = {"Abby": placesAbby, "John": placesJohn, "Emily": placesEmily}
for name, liked_places in favourite_places.items():
    print(name + " has three favourite places: " + liked_places + ".")