import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog


def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))


def nearest_neighbor(graph, start):
    unvisited = set(range(len(graph)))
    path = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: graph[current][city])
        path.append(nearest_city)
        unvisited.remove(nearest_city)
        current = nearest_city
    return path


def total_cost(graph, path):
    cost = 0
    for i in range(len(path)):
        cost += graph[path[i - 1]][path[i]]
    return cost


def plot_graph(graph, path, cost):
    x = [city[0] for city in graph]
    y = [city[1] for city in graph]
    plt.plot(x, y, 'bo')
    for i in range(len(graph)):
        plt.text(x[i], y[i], str(i), fontsize=12)
    for i in range(len(path) - 1):
        plt.plot([graph[path[i]][0], graph[path[i + 1]][0]],
                 [graph[path[i]][1], graph[path[i + 1]][1]], 'r-')
        distance = euclidean_distance(graph[path[i]], graph[path[i + 1]])
        plt.text((graph[path[i]][0] + graph[path[i + 1]][0]) / 2,
                 (graph[path[i]][1] + graph[path[i + 1]][1]) / 2,
                 f"{round(distance, 2)}", fontsize=10, horizontalalignment='center')
    plt.plot([graph[path[-1]][0], graph[path[0]][0]],
             [graph[path[-1]][1], graph[path[0]][1]], 'r-')
    distance = euclidean_distance(graph[path[-1]], graph[path[0]])
    plt.text((graph[path[-1]][0] + graph[path[0]][0]) / 2,
             (graph[path[-1]][1] + graph[path[0]][1]) / 2,
             f"{round(distance, 2)}", fontsize=10, horizontalalignment='center')

    plt.text(min(x) + 0.1, min(y) + 0.1, f"Total Cost: {round(cost, 2)}", fontsize=12)

    plt.title('TSP Using Nearest Neighbor')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Display time complexity
    complexity = f"Time Complexity: O(n^2)"
    plt.text(min(x) + 0.1, max(y) - 0.1, complexity, fontsize=12)

    plt.show()


def get_cities():
    cities = []
    root = tk.Tk()
    root.withdraw()
    num_cities = simpledialog.askinteger("Input", "Enter the number of cities:")
    for i in range(num_cities):
        city = simpledialog.askstring("Input", f"Enter the coordinates for city {i} (x,y):")
        city = tuple(map(float, city.split(',')))
        cities.append(city)
    return cities


# Example usage
# Define cities interactively
cities = get_cities()

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Run nearest neighbor algorithm
start_city = 0
path = nearest_neighbor(distance_matrix, start_city)

# Calculate total path cost
cost = total_cost(distance_matrix, path)

# Plot the graph with the path, distances, and total cost
plot_graph(cities, path, cost)

print("Path:", path)
print("Total cost:", cost)
