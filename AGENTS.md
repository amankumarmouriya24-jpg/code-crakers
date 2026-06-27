# Agent Notes

This repository contains a Flask-based Budget Trip Planner.

## Project Map

- `app.py` defines the Flask routes and budget/itinerary helpers.
- `templates/` contains the Jinja pages rendered by the app.
- `static/css/style.css` and `static/js/script.js` contain frontend assets.
- `data/` stores destination, hotel, and transport data as JSON.
- `docs/` contains presentation material.

## Development Notes

- Keep the app dependency-light; currently it only requires Flask.
- Prefer updating JSON data files for destination and recommendation changes.
- Keep route names and template names simple and consistent.
- Preserve the existing data fields unless the templates and docs are updated together.

## Verification

Run these checks after changes:

```bash
python -m compileall app.py
python app.py
```

Then manually open the home, planner, itinerary, recommendations, and about pages.

## Handoff

If future work changes user-facing behavior, update `README.md` and `USER_MANUAL.md`. If it changes contributor workflow, update `CONTRIBUTING.md`.
