# My Zootopia API

## Description
This project generates a website with information about animals fetched from an API.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/densenden/My-Zootopia-API.git
    cd My-Zootopia-API
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory with your API key:
    ```
    API_KEY=your_actual_api_key
    ```

## Usage

1. Run the `animals_web_generator.py` script:
    ```sh
    python animals_web_generator.py
    ```

2. Enter the name of an animal when prompted:
    ```
    Enter a name of an animal: Fox
    ```

3. The website will be generated and saved to `animals.html`.

## License
This project is licensed under the MIT License.