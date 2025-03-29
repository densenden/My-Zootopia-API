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
            animals_string += ( f"<li><strong>{key.replace('_', ' ').title()}"
                                f"</strong>: {value}</li>"
                                )


        for key, value in animal['taxonomy'].items():
            animals_string += ( f"<li><strong>{key.replace('_', ' ').title()}"
                                f"</strong>: {value}</li>"
                                )

        animals_string += f"""
              <li><strong>Locations</strong>: {', '.join(animal['locations'])}</li>
            </ul>
          </p>
        </li>
        """
    return animals_string


def html_replacer(animals_data=None, error_message=None):
    """
    Replace the placeholder in the HTML template with the animal data or an error message.
    """
    with open("animals_templates.html", "r", encoding='utf-8') as html_object:
        placeholder = html_object.read()

    if error_message:
        new_content = placeholder.replace("__REPLACE_ANIMALS_INFO__", f"<h2>{error_message}</h2>")
    else:
        new_content = placeholder.replace("__REPLACE_ANIMALS_INFO__", string_creator(animals_data))

    with open("animals.html", "w", encoding='utf-8') as new_file:
        new_file.write(new_content)


def main():
    while True:
        animal_name = input("Enter a name of an animal: ")
        animal_data = fetch_data(animal_name)
        if animal_data:
            html_replacer(animals_data=animal_data)
            print(f"Website was successfully generated to the file animals.html for {animal_name}.")
            break
        else:
            error_message = f'The animal "{animal_name}" doesn\'t exist.'
            html_replacer(error_message=error_message)
            print(f"No data found for the given animal name {animal_name}. Please try again.")


if __name__ == "__main__":
    main()