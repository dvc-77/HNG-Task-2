import requests
import json
import random

#Testing the Create Operation
def create_person(name: str):
    api = "http://127.0.0.1:8000/api"
    payload = {
        "name": name
    }

    payload = json.dumps(payload)
    response = requests.post(api, data=payload)
    print(response.status_code, response.content)

def get_person(user_id: int):
    api = f"http://127.0.0.1:8000/api/{user_id}"
    response = requests.get(api)
    print(response.status_code, response.content)

def update_person(user_id: int, name: str):
    api = f"http://127.0.0.1:8000/api/{user_id}"

    payload = {
            "name": name
    }

    payload = json.dumps(payload)
    response = requests.patch(api, data=payload)
    print(response.status_code, response.content)

def delete_person(user_id: int):
    api = f"http://127.0.0.1:8000/api/{user_id}"

    response = requests.delete(f"http://127.0.0.1:8000/api/{user_id}")
    print(response.status_code, response.content)


if __name__ == "__main__":
    NAME_REPLACEMENT = "OLAMIDE BADOO"
    names = ["Mark Essien", "Idee", "Bolarinwa Aje"]
    number_of_user = len(names)
    FIRST_ID = 1

    # Create users in the database
    print("-------------------------CREATING USERS-----------------------------")
    for name in names:
        create_person(name)
        print()
    print()

    print("-------------------------GET USER-----------------------------")
    #Select random user (by id) to perfom the read, update and delete operation on
    selected_id = random.randint(FIRST_ID, number_of_user)

    #Getting the user whose id matches the selected id    
    get_person(selected_id)
    print()

    print("-------------------------UPDATE USER-----------------------------")
    #Updating the name of the selected user
    update_person(selected_id, NAME_REPLACEMENT)
    print()

    print("-------------------------DELETE USER-----------------------------")
    #Deleting the selected user
    delete_person(selected_id)
    print()
