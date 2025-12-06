# 🚴‍♂️ Berlin Bicycle Route Optimization  
A Python-based routing system that models real Berlin locations as a weighted graph and computes optimised bicycle delivery routes using classical graph algorithms (Dijkstra and A*). Includes multi-stop route sequencing and route visualisation.

---

## 📘 Project Overview

Urban bicycle couriers often rely on intuition or generic navigation tools that are not optimised for multi-stop delivery routes. This project demonstrates how computational methods—specifically weighted graphs and shortest-path algorithms—can be used to generate efficient delivery routes across Berlin.

The system uses **real geographic coordinates** for 10 locations across Berlin (Mitte + surrounding districts), builds a simplified weighted graph using Haversine distance, and computes routes using:

- **Dijkstra’s Algorithm**  
- **A\* Search (with distance heuristic)**  
- **Nearest-Neighbour Multi-Stop Sequencing**

This project was developed as part of a computer science research assignment and is designed to be **clear, modular, and industry-aligned**.

---

## 🗺️ Features

- Real Berlin GPS coordinates  
- Weighted graph with Haversine distance  
- Dijkstra and A\* shortest path computation  
- Multi-stop delivery route optimisation  
- Route visualisation using Matplotlib  
- Clean, modular Python code structure  
- Simple to extend with more advanced routing or ML-based prediction techniques  

---

## 📍 Real Berlin Locations Used

The graph contains the following landmarks:

- Brandenburg Gate  
- Potsdamer Platz  
- Checkpoint Charlie  
- Unter den Linden  
- Museum Island  
- Hackescher Markt  
- Alexanderplatz  
- Treptower Park  
- Berlin Hauptbahnhof  
- Mauerpark  

These locations provide a realistic mix of dense city-centre navigation and outer delivery zones.

---

## 🧠 Algorithms Used

### **Dijkstra’s Algorithm**
Classic weighted shortest-path algorithm used as the baseline.

### **A\* Search**
A more efficient shortest-path method that uses a **Heuristic Function** (straight-line Haversine distance).

### **Nearest-Neighbour Heuristic**
Used to build efficient multi-stop courier routes.

---

## 🏗️ Project Structure

```text
bicycle-routing/
├─ src/
│  ├─ graph_data.py        # Coordinates + edge definitions
│  ├─ graph_builder.py     # Builds weighted Berlin graph
│  ├─ routing.py           # Dijkstra & A* implementations
│  ├─ multi_stop.py        # Multi-stop route sequencing
│  ├─ visualize.py         # Graph + route plotting
│  └─ main.py              # Example scenarios
├─ requirements.txt
└─ README.md
