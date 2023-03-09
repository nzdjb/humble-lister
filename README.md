# humble-lister

## Installation

```bash
pip install poetry
poetry install
```

## Usage

Get a JSON file of your Humble Library. Save it at `library.json`:

1. Open a web-browser.
2. Open the developer tools and go to "Network" or equivalent.
3. Login to Humble Bundle.
4. Visit "https://www.humblebundle.com/home/library".
5. Filter the requests for "orders" and wait. It may take about a minute for all the requests to run.
6. Combine the returned JSON objects into an array in `library.json`.

Run the code:

```bash
poetry run python main.py
```
