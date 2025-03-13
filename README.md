# Animal Information Web Generator

## Overview

The Animal Information Web Generator is a Python-based application that fetches animal data from an API, processes it, and generates a well-formatted HTML page displaying the information. This project is designed to help users easily visualize and access detailed information about various animals.

## Features

- Fetches animal data from an external API.
- Processes and formats the data into a readable HTML structure.
- Includes additional animal characteristics if available.
- Generates an HTML file with a clean and user-friendly design.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:densenden/My-Zootopia.git
    cd animal-info-web-generator
    ```

2. Install the required Python packages:
    ```sh
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the project root directory and add your API key:
    ```env
    API_KEY=your_api_key_here
    ```

## Usage

1. Fetch animal data and generate the HTML file:
    ```sh
    python animals_web_generator.py
    ```

2. Open the generated `animals.html` file in your web browser to view the animal information.

## Project Structure

- `data_fetcher.py`: Contains the function to fetch animal data from the API.
- `animals_web_generator.py`: Contains functions to process the data and generate the HTML file.
- `animals_templates.html`: HTML template file used to format the animal information.
- `animals_data.json`: Example JSON file containing animal data (used for testing).
- `README.md`: Project documentation.

## Example

Here is an example of the generated HTML structure:

```html
<li class="cards__item">
  <div class="card__title">American Foxhound</div>
  <p class="card__text">
    <ul>
      <li><strong>Diet</strong> Omnivore</li>
      <li><strong>Location</strong> United States</li>
      <li><strong>Type</strong> Hound</li>
      <li><strong>Distinctive Feature</strong> Long legs and wide, flat ears</li>
      <li><strong>Temperament</strong> Mix of affectionate, loving, and stubborn</li>
      <li><strong>Training</strong> Medium</li>
      <li><strong>Average Litter Size</strong> 7</li>
      <li><strong>Common Name</strong> American Foxhound</li>
      <li><strong>Slogan</strong> Sweet, kind, loyal, and very loving!</li>
      <li><strong>Group</strong> Dog</li>
      <li><strong>Color</strong> BlackWhiteTan</li>
      <li><strong>Skin Type</strong> Hair</li>
      <li><strong>Lifespan</strong> 10 to 12 years</li>
    </ul>
  </p>
</li>