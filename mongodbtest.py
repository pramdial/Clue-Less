from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
#Step1: connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('localhost', 27017)
db=client.clueless

#Step 2: Create sample data
Suspects = ["Miss Scarlet",
            "Colonel Mustard",
            "Mrs. White", 
            "Mr. Green",
            "Mrs. Peacock",
            "Professor Plum"]

Locations = ["Study",
            "Study - Hall",
            "Hall",
            "Hall - Lounge",
            "Lounge",
            "Study - Library",
            "Hall - Billiard Room",
            "Lounge - Dining Room",
            "Library",
            "Library - Billiard Room",
            "Billiard Room",
            "Billiard Room - Dining Room",
            "Dining Room",
            "Library - Conservatory",
            "Billiard Room - Ballroom",
            "Dining Room - Kitchen",
            "Conservatory",
            "Conservatory - Ballroom",
            "Ballroom",
            "Ballroom - Kitchen",
            "Kitchen"]


for location in Locations:
    # location_tokens = {}
    if location == "Hall - Lounge": 
        location_tokens = {"Location" : location, "Suspects" : Suspects[0], "Weapons" : []}
    elif location == "Lounge - Dining Room":
        location_tokens = {"Location" : location, "Suspects" : [Suspects[1]], "Weapons" : []}
    elif location == "Library - Billiard Room":
        location_tokens = {"Location" : location, "Suspects" : [Suspects[2]], "Weapons" : []}
    elif location == "Ballroom - Kitchen":
        location_tokens = {"Location" : location, "Suspects" : [Suspects[3]], "Weapons" : []}
    elif location == "Conservatory - Ballroom":
        location_tokens = {"Location" : location, "Suspects" : [Suspects[4]], "Weapons" : []}
    elif location == "Study - Library":
        location_tokens = {"Location" : location, "Suspects" : [Suspects[5]], "Weapons" : []}
    else:
        location_tokens = {"Location" : location, "Suspects" : [], "Weapons" : []}

    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=db.clueless.insert_one(location_tokens)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} as {1}'.format(location,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating ClueLess ')


# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

#Step 6: Test 
person_of_interest = db.clueless.find_one({"Location": "Hall - Lounge"})
print(person_of_interest)

person_of_interest = db.clueless.find_one({"Location": "Study"})
print(person_of_interest)