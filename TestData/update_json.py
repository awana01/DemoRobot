import os,time,json
from faker import Faker
from datetime import datetime


# JSON data:
x = { "organization": "GeeksForGeeks",
       "city": "Noida",
       "country": "India"
      }

def update_json_value_in_file():
    """ python object to be appended [append single value to json dict """
    z = {"pin": 110096}

    data= None
    # Opening JSON file
    with open('update1.json', 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)

        # # parsing JSON string:
        # z = json.loads(x)

        # appending the data
        file_data.update(z)

        # the result is a JSON string:
        # print(json.dumps(z))
        file.seek(0)
        json.dump(file_data,file,indent=4)



# function to add to JSON
def write_json(new_data, filename='update2.json'):
    jsonFile = os.getcwd()+'/TestData/'+filename

    with open(jsonFile, 'r+') as file:

        file_data = json.load(file)                # First we load existing data into a dict.
        file_data["userdetails"].append(new_data)  # Join new_data with file_data inside emp_details
        file.seek(0)                               # Sets file's current position at offset.
        
        json.dump(file_data, file, indent=4)       # convert back to json.

    # python object to be appended


def read_json_data(testNode='',filename='update2.json'):
    """read json test data and return testnode"""
    jsonFileToRead = os.getcwd()+'/TestData/'+filename
        
    # Opening JSON file
    with open(jsonFileToRead) as json_file:
         data = json.load(json_file)
         # Print the type of data variable
         print("Type:", type(data))

         # Print the data of dictionary
         print("\nTotal length of data under user1",len(data["userdetails"]))
         print("\nUser1:", data["userdetails"])

    return data["userdetails"]

fake = Faker('en_US')
currentDate1 = datetime.today().strftime("%Y-%m-%d")   #"2022-11-28"
currentDate2 = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")   #"2022-11-28_22:24:01"
currentDate3 = datetime.today().strftime("%a-%b-%Y-%m-%d_%H:%M:%S") #"Mon-Nov-2022-11-28_22:24:01"
currentDate4 = datetime.today().strftime("%Y-%m-%d_%I:%M:%S-%p")  #"2022-11-28_10:27:11-PM"  12 hour format






y = {"name": fake.first_name(),
     "email": "nikhil@geeksforgeeks.org",
     "Created_On":currentDate4
     }


# update_json_value_in_file()
write_json(y)
listItems = read_json_data()
print(listItems[5]["name"])
# print(os.curdir)
print(os.getcwd())





