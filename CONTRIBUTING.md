# Contributing

Thanks for helping improve Code Crakers Budget Trip Planner. This project is a small Flask application, so changes are easiest to review when they stay focused and include a quick local check.

## Local Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open `http://127.0.0.1:5000` in a browser.

## Contribution Guidelines

- Keep changes small and related to one issue or feature.
- Use clear names for routes, templates, and data fields.
- Update `README.md` or `USER_MANUAL.md` when behavior changes.
- Validate JSON files before committing changes to `data/`.
- Check that the planner form, itinerary page, and recommendations page still load.

## Suggested Checks

Before opening a merge request, run:

```bash
python -m compileall app.py
python app.py
```

Then test the main pages manually:

- Home page
- Planner form
- Generated itinerary
- Recommendations
- About page

## Reporting Issues

When reporting a bug, include:

- What you expected to happen
- What actually happened
- Steps to reproduce it
- Screenshots, if the issue is visual
