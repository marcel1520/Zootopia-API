import requests
import json


API_KEY = "xyFODdLjB3Sc18vg4Ro2rw==6shJ5CyYvlDCOHad"


def get_user_animal(user_animal):
    animal_url = f"https://api.api-ninjas.com/v1/animals?name={user_animal}"
    res = requests.get(animal_url, headers={"X-Api-Key": API_KEY})
    animals = res.text
    return animals


def create_animal_json(user_animal_json):
    with open("user_animal_file.json", "w") as animal_file:
        animal_file.write(user_animal_json)
        return animal_file


def read_json(user_animal_file_path):
    with open(user_animal_file_path, "r") as animal_file:
        animal_content = json.load(animal_file)
        return animal_content


def write_json(user_animal_file_path, animal_file_content):
    formatted_json = json.dumps(animal_file_content, indent=4)
    with open(user_animal_file_path, "w") as animal_json_formatted:
        animal_json_formatted.write(formatted_json)
        return animal_json_formatted


def main():
    user_input = input("Enter an animal: ")
    user_animal_get = get_user_animal(user_input)
    create_animal_json(user_animal_get)
    json_read = read_json("user_animal_file.json")
    write_json("user_animal_file.json", json_read)


if __name__ == "__main__":
    main()