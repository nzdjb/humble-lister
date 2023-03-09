# humble-lister

## Installation

```bash
pip install poetry
poetry install
```

## Usage

Get a JSON file of your Humble Library. Save it at `library.json`.

To do this, open a web-browser, open the developer tools and go to "Network" or equivalent.
Login to Humble Bundle and visit "https://www.humblebundle.com/home/library".
Filter the requests for "orders". Combine the returned JSON objects into an array in `library.json`.

Run the code:

```bash
poetry run python main.py
```
