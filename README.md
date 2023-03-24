# humble-lister

## Installation

```bash
pip install poetry
poetry install
```

## Usage

Get your _simpleauth_sess cookie. Save it at `humble.cookie`:

1. Open a web-browser.
2. Login to Humble Bundle.
3. Open the developer tools in your browser.
4. Go to Storage then Cookies and copy the value of _simpleauth_sess to humble.cookie.

Run the code:

```bash
poetry run python main.py
```
