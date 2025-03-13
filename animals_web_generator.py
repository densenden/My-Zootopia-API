from data_fetcher import fetch_data

def string_creator(animal_data):
    """
    Create a string with the animal data to be inserted in the HTML template.
    """
    animals_string = ""
    for animal in animal_data:
        animals_string += f"""
        <li class="cards__item">
          <div class="card__title">{animal['name']}</div>
          <p class="card__text">
            <ul>
        """
        for key, value in animal['characteristics'].items():
            animals_string += f"<li><strong>{key.replace('_', ' ').title()}</strong>: {value}</li>"

        for key, value in animal['taxonomy'].items():
            animals_string += f"<li><strong>{key.replace('_', ' ').title()}</strong>: {value}</li>"

        animals_string += f"""
              <li><strong>Locations</strong>: {', '.join(animal['locations'])}</li>
            </ul>
          </p>
        </li>
        """
    return animals_string

def html_replacer(animals_data):
    """
    Replace the placeholder in the HTML template with the animal data.

    Args:
        animals_data (list): A list of dictionaries containing animal information.
    """
    with open("animals_templates.html", "r") as html_object:
        placeholder = html_object.read()

    new_content = placeholder.replace("__REPLACE_ANIMALS_INFO__", string_creator(animals_data))

    with open("animals.html", "w") as new_file:
        new_file.write(new_content)

def main():
    while True:
        animal_name = input("Enter a name of an animal: ")
        animal_data = fetch_data(animal_name)
        if animal_data:
            html_replacer(animal_data)
            print(f"Website was successfully generated to the file animals.html for {animal_name}.")
            break
        else:
            print(f"No data found for the given animal name {animal_name}. Please try again.")


if __name__ == "__main__":
    main()