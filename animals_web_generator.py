import requests
import json
import os
from dotenv import load_dotenv



load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

print(API_KEY)


def get_user_animal(user_animal):
    '''gets users animal of choice upon user animal input'''
    animal_url = f"https://api.api-ninjas.com/v1/animals?name={user_animal}"
    res = requests.get(animal_url, headers={"X-Api-Key": API_KEY})
    animals = res.text
    return animals


def create_animal_json(user_animal_json):
    '''creates animal json file of users choice'''
    with open("user_animal_file.json", "w") as animal_file:
        animal_file.write(user_animal_json)
        return animal_file


def read_json(user_animal_file_path):
    '''reads animal json file'''
    with open(user_animal_file_path, "r") as animal_file:
        animal_content = json.load(animal_file)
        return animal_content


def write_json(user_animal_file_path, animal_file_content):
    '''writes animal json file again in a formatted version'''
    formatted_json = json.dumps(animal_file_content, indent=4)
    with open(user_animal_file_path, "w") as animal_json_formatted:
        animal_json_formatted.write(formatted_json)
        return animal_json_formatted


def serialize_animal_data(animal):
    '''serialize animal data'''
    animal_info = ""
    animal_name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = ", ".join(map(str, animal["locations"]))
    character = animal["characteristics"]
    if "type" in character:
        character_type = character["type"]
        animal_info += ("<li class='cards__item'>\n"
                        f"<div class='card__title'>{animal_name}</div>"
                        f"<strong>Diet:</strong> {diet}<br/>\n"
                        f"<strong>Location:</strong> {location}<br/>\n"
                        f"<strong>Type:</strong> {character_type}<br/>\n"
                        '</li>\n')
    else:
        animal_info += ("<li class='cards__item'>\n"
                        f"<div class='card__title'>{animal_name}</div>"
                        f"<strong>Diet:</strong> {diet}<br/>\n"
                        f"<strong>Location:</strong> {location}<br/>\n"
                        '</li>\n')
    return animal_info


def get_animal_data(animal_list):
    '''retrieving animal info'''
    animal_info = ""
    for animal in animal_list:
        animal_info += serialize_animal_data(animal)
    return animal_info


def read_html_file(html_animal):
    '''reads html file'''
    with open(html_animal, "r") as html_animal_file:
        animal_html = html_animal_file.read()
        return animal_html


def replace_string(old_string, new_string):
    '''replaces target string from html file with animal info'''
    string_to_replace = "__REPLACE_ANIMALS_INFO__"
    text_to_replace = old_string
    html_with_replace = text_to_replace.replace(string_to_replace, new_string)
    return html_with_replace


def write_animal_html(animal_html_replaced):
    '''writes html file with animal data in class'''
    animal_html = "animal.html"
    with open(animal_html, "w") as new_animal_file:
        new_animal_file.write(animal_html_replaced)
        return new_animal_file


def main():
    '''loads animal data, creates animal string, reads html,
    replaces html target string with animal data'''
    user_input = input("Enter an animal: ")
    user_animal_get = get_user_animal(user_input)
    create_animal_json(user_animal_get)
    json_read = read_json("user_animal_file.json")
    write_json("user_animal_file.json", json_read)
    animal_data_get = get_animal_data(json_read)
    if len(animal_data_get) > 0:
        html_file_read = read_html_file("animals_template.html")
        string_replace = replace_string(html_file_read, animal_data_get)
        write_animal_html(string_replace)
    else:
        error_message = "<h1 style='color:red;'>!!! typo alert !!!</h1>"
        html_file_read = read_html_file("animals_template.html")
        string_replace = replace_string(html_file_read, error_message)
        write_animal_html(string_replace)


if __name__ == "__main__":
    main()


