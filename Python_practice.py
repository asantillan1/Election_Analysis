#  counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# for county in counties:
#     print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


#Prints Keys and values fron a disctionary using for loop and items()
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(county + " county has", str(voters) + " registered voters")
##Code using f string and Formatting using f'{value:{width},.{precision}}
#for county, voters in counties_dict.items():
     #print(f"{county} county has {voters:,} registered voters.")

# use the range() function to iterate over the list of dictionaries and print the counties in voting_data
#for i in range(len(voting_data)):
    ##prints Registered voters
    #print(voting_data[i]['registered_voters'])
    ##Prints "Arapahoe county has 422,829 registered voters" formatted skill drill
    #print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")     
    
      

#Nested For loop Get the Values from a List of Dictionaries
# for county_dict in voting_data:
#     for value in county_dict.values():
#      print(value)
