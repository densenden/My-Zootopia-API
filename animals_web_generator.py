import json

def load_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing animal data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)

def animal_reader(animal):
    """
    Extract relevant information from an animal dictionary.

    Args:
        animal (dict): A dictionary containing animal information.

    Returns:
        tuple: A tuple containing the extracted animal information.
    """
    name = animal["name"]
    location = ", ".join(animal["locations"])
    characteristics = animal["characteristics"]
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    distinctive_feature = characteristics.get("distinctive_feature")
    temperament = characteristics.get("temperament")
    training = characteristics.get("training")
    average_litter_size = characteristics.get("average_litter_size")
    common_name = characteristics.get("common_name")
    slogan = characteristics.get("slogan")
    group = characteristics.get("group")
    color = characteristics.get("color")
    skin_type = characteristics.get("skin_type")
    lifespan = characteristics.get("lifespan")
    return (name, diet, location, animal_type, distinctive_feature, temperament, training,
            average_litter_size, common_name, slogan, group, color, skin_type, lifespan)

def string_creator(data):
    """
    Create an HTML string representation of the animal data.

    Args:
        data (list): A list of dictionaries containing animal information.

    Returns:
        str: An HTML string representation of the animal data.
    """
    animals_string = ''
    for animal in data:
        (name, diet, location, animal_type, distinctive_feature, temperament, training,
         average_litter_size, common_name, slogan, group, color, skin_type, lifespan) = animal_reader(animal)
        animals_string += (
            f'<li class="cards__item">\n'
            f'  <div class="card__title">{name}</div>\n'
            f'  <p class="card__text">\n'
            f'    <ul>\n'
        )
        if diet:
            animals_string += f'      <li><strong>Diet</strong> {diet}</li>\n'
        if location:
            animals_string += f'      <li><strong>Location</strong> {location}</li>\n'
        if animal_type:
            animals_string += f'      <li><strong>Type</strong> {animal_type}</li>\n'
        if distinctive_feature:
            animals_string += f'      <li><strong>Distinctive Feature</strong> {distinctive_feature}</li>\n'
        if temperament:
            animals_string += f'      <li><strong>Temperament</strong> {temperament}</li>\n'
        if training:
            animals_string += f'      <li><strong>Training</strong> {training}</li>\n'
        if average_litter_size:
            animals_string += f'      <li><strong>Average Litter Size</strong> {average_litter_size}</li>\n'
        if common_name:
            animals_string += f'      <li><strong>Common Name</strong> {common_name}</li>\n'
        if slogan:
            animals_string += f'      <li><strong>Slogan</strong> {slogan}</li>\n'
        if group:
            animals_string += f'      <li><strong>Group</strong> {group}</li>\n'
        if color:
            animals_string += f'      <li><strong>Color</strong> {color}</li>\n'
        if skin_type:
            animals_string += f'      <li><strong>Skin Type</strong> {skin_type}</li>\n'
        if lifespan:
            animals_string += f'      <li><strong>Lifespan</strong> {lifespan}</li>\n'
        animals_string += (
            f'    </ul>\n'
            f'  </p>\n'
            f'</li>\n'
        )
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
    """
    Main function to load data, generate HTML content, and save it to a file.
    """
    file_path = "animals_data.json"
    animals_data = load_data(file_path)
    html_replacer(animals_data)

if __name__ == "__main__":
    main()