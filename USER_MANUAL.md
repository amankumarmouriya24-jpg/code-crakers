# User Manual

## Overview

Code Crakers Budget Trip Planner helps users compare affordable travel destinations, estimate costs, and build a simple day-by-day itinerary.

## Starting the App

Install the project dependencies and run the Flask server:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Pages

### Home

The home page highlights featured destinations and gives quick access to the planner.

### Planner

Use the planner form to choose:

- Destination
- Number of travel days
- Number of travelers
- Travel style

After submitting the form, the app shows:

- Daily trip estimate
- Transport estimate
- Emergency buffer
- Total estimated budget
- A day-by-day itinerary

### Recommendations

The recommendations page lists available destinations, hotel suggestions, and transport options from the project data files.

### About

The about page gives a short summary of the project and its purpose.

## Updating Travel Data

Project data is stored in JSON files under `data/`:

- `destinations.json`
- `hotels.json`
- `transport.json`

When adding or editing entries, keep the existing field names and JSON structure so the Flask routes and templates can read the data correctly.

## Troubleshooting

- If the app does not start, confirm Flask is installed with `pip install -r requirements.txt`.
- If a destination does not appear, check that it exists in `data/destinations.json`.
- If a JSON error appears, validate the edited data file and check for missing commas or brackets.
