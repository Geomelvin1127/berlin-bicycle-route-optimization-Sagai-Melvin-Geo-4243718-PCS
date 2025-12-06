# src/graph_data.py

# Berlin locations with (latitude, longitude)
BERLIN_LOCATIONS = {
    "Brandenburg Gate": (52.5163, 13.3777),
    "Potsdamer Platz": (52.5096, 13.3759),
    "Checkpoint Charlie": (52.5076, 13.3904),
    "Unter den Linden": (52.5170, 13.4019),
    "Museum Island": (52.5169, 13.4010),
    "Hackescher Markt": (52.5226, 13.4020),
    "Alexanderplatz": (52.5219, 13.4132),
    "Treptower Park": (52.4935, 13.4690),
    "Berlin Hauptbahnhof": (52.5251, 13.3694),
    "Mauerpark": (52.5413, 13.4027),
}

# Conceptual edges - connections that make sense for cycling routes.
# These edges define how locations are connected in our simplified Berlin graph.
EDGES = [
    ("Brandenburg Gate", "Potsdamer Platz"),
    ("Brandenburg Gate", "Unter den Linden"),
    ("Brandenburg Gate", "Berlin Hauptbahnhof"),

    ("Potsdamer Platz", "Checkpoint Charlie"),
    ("Checkpoint Charlie", "Unter den Linden"),

    ("Unter den Linden", "Museum Island"),
    ("Museum Island", "Hackescher Markt"),

    ("Hackescher Markt", "Alexanderplatz"),
    ("Hackescher Markt", "Mauerpark"),

    ("Alexanderplatz", "Treptower Park"),
    ("Alexanderplatz", "Museum Island"),
]
