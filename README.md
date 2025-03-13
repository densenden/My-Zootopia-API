# My Zootopia API

## Description
This project generates a website with information about animals fetched from an API.

<img width="1267" alt="Bildschirmfoto 2025-03-13 um 18 25 50" src="https://github.com/user-attachments/assets/7f5e8724-b4d8-40a2-84e2-18f58fe95a2c" />


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
