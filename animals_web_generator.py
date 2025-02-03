import data_fetcher


def animal_reader(animal):
    name = animal["name"]
    location = ", ".join(animal["locations"])
    characteristics = animal["characteristics"]
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    return name, diet, location, animal_type


def string_creator(data, animal_name):
    if not data:
        return f'<h2>The animal "{animal_name}" doesn’t exist.</h2>'

    animals_string = ''
    for animal in data:
        name, diet, location, animal_type = animal_reader(animal)
        animals_string += (
            f'<li class="cards__item">\n'
            f'  <div class="card__title">{name}</div>\n'
            f'  <p class="card__text">\n'
            f'    <ul>\n'
            f'      <li>Diet: {diet}</li>\n'
            f'      <li>Location: {location}</li>\n'
            f'      <li>Type: {animal_type}</li>\n'
            f'    </ul>\n'
            f'  </p>\n'
            f'</li>\n'
        )
    return animals_string


def html_replacer(animals_data, animal_name):
    with open("animals_templates.html", "r") as html_object:
        placeholder = html_object.read()

    new_content = placeholder.replace("__REPLACE_ANIMALS_INFO__", string_creator(animals_data, animal_name))

    with open("animals.html", "w") as new_file:
        new_file.write(new_content)


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    html_replacer(animals_data, animal_name)


if __name__ == "__main__":
    main()