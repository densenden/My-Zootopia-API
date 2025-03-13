from data_fetcher import fetch_data

def string_creator(animal_data):
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
    animal_name = "Fox"
    animal_data = fetch_data(animal_name)
    html_replacer(animal_data)

if __name__ == "__main__":
    main()