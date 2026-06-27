from __future__ import annotations

import json
import os
from pathlib import Path

from flask import Flask, abort, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

app = Flask(__name__)


def load_json(filename: str) -> list[dict]:
    with (DATA_DIR / filename).open(encoding="utf-8") as file:
        return json.load(file)


def find_destination(slug: str) -> dict | None:
    return next((item for item in load_json("destinations.json") if item["slug"] == slug), None)


def build_budget(destination: dict, days: int, travelers: int, style: str) -> dict:
    style_multiplier = {"budget": 0.85, "comfort": 1.0, "premium": 1.35}.get(style, 1.0)
    daily_total = destination["daily_cost"] * days * travelers * style_multiplier
    transport_total = destination["transport_cost"] * travelers
    emergency_buffer = (daily_total + transport_total) * 0.1

    return {
        "daily": round(daily_total),
        "transport": round(transport_total),
        "buffer": round(emergency_buffer),
        "total": round(daily_total + transport_total + emergency_buffer),
    }


def build_itinerary(destination: dict, days: int) -> list[dict]:
    activities = destination["activities"]
    itinerary = []

    for day in range(1, days + 1):
        activity = activities[(day - 1) % len(activities)]
        itinerary.append(
            {
                "day": day,
                "title": activity["title"],
                "description": activity["description"],
                "tip": activity["tip"],
            }
        )

    return itinerary


@app.route("/")
def index():
    destinations = load_json("destinations.json")
    return render_template("index.html", destinations=destinations[:3])


@app.route("/planner", methods=["GET", "POST"])
def planner():
    destinations = load_json("destinations.json")

    if request.method == "POST":
        slug = request.form.get("destination", "")
        destination = find_destination(slug)
        if destination is None:
            abort(404)

        days = max(1, min(int(request.form.get("days", 3)), 21))
        travelers = max(1, min(int(request.form.get("travelers", 1)), 12))
        style = request.form.get("style", "comfort")
        budget = build_budget(destination, days, travelers, style)
        itinerary = build_itinerary(destination, days)

        return render_template(
            "itinerary.html",
            budget=budget,
            days=days,
            destination=destination,
            itinerary=itinerary,
            style=style,
            travelers=travelers,
        )

    return render_template("planner.html", destinations=destinations)


@app.route("/recommendations")
def recommendations():
    destinations = load_json("destinations.json")
    hotels = load_json("hotels.json")
    transport = load_json("transport.json")
    return render_template(
        "recommendations.html",
        destinations=destinations,
        hotels=hotels,
        transport=transport,
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG") == "1",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
    )
