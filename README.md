# Code Crakers

## Budget Trip Planner

A simple Flask web app for comparing affordable destinations, estimating trip costs, and generating a lightweight day-by-day itinerary.

## Project Description

Code Crakers helps budget-conscious travelers explore affordable destinations, compare basic hotel and transport options, and create quick itinerary estimates from curated JSON data.

## Repository Metadata

- Description: A Flask budget trip planner for affordable destination, hotel, transport, and itinerary recommendations.
- Topics: `flask`, `python`, `travel-planner`, `budget-planner`, `agplv3`

## Features

- Destination cards with daily cost, transport estimate, and best season
- Trip planner form for destination, duration, travelers, and travel style
- Budget breakdown with a 10% buffer
- Generated day-by-day itinerary
- Hotel, transport, and destination recommendation pages

## Project Structure

```text
budget-trip-planner/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- static/
|-- templates/
|-- data/
`-- docs/
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

To enable Flask debug mode locally, set:

```bash
set FLASK_DEBUG=1
python app.py
```

## Deployment

This app is ready to deploy as a Flask web service.

### Render

1. Push this repository to GitHub.
2. Open Render and create a new **Web Service** from the repository.
3. Use these settings:

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

Render can also detect `render.yaml` from this repository.

### Docker

Build and run the container locally with:

```bash
docker build -t code-crakers .
docker run -p 5000:5000 code-crakers
```

Then open `http://127.0.0.1:5000`.

## Quality Checks

The repository includes configuration for:

- Ruff formatting and linting
- Mypy type checking
- Vulture dead-code checks
- Bandit security analysis
- Pylint and Flake8 linting
- Semgrep static analysis
- Pytest with coverage threshold
- Pre-commit hooks
- GitLab CI automation

Install development dependencies with:

```bash
pip install -r requirements-dev.txt
```

Run the test suite with:

```bash
pytest
```

## Data

The planner uses JSON files in `data/`:

- `destinations.json`
- `hotels.json`
- `transport.json`

You can expand those files to add new cities, hotels, routes, and activities.

## License

This project is licensed under the GNU Affero General Public License v3.0 or later. See `LICENSE` for details.
