import tkinter as tk
from tkinter import messagebox
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight

    def dijkstra(self, start):
        if start not in self.graph:
            return "Start node is not in the graph"
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current_node = min((node for node in self.graph if node not in visited), key=lambda x: distances[x])
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        return distances

    def bellman_ford(self, start):
        if start not in self.graph:
            return "Start node is not in the graph"
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        for u in self.graph:
            for v, weight in self.graph[u].items():
                if distances[u] + weight < distances[v]:
                    return "Graph contains a negative weight cycle"

        return distances


class ShortestPathApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Shortest Path Visualizer")
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.graph = Graph()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter edges and weights (comma-separated):")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.dijkstra_button = tk.Button(self.master, text="Dijkstra's Shortest Path", command=self.perform_dijkstra)
        self.dijkstra_button.pack()

        self.bellman_ford_button = tk.Button(self.master, text="Bellman-Ford Shortest Path",
                                             command=self.perform_bellman_ford)
        self.bellman_ford_button.pack()

    def perform_dijkstra(self):
        try:
            edges = self.entry.get().strip().split(",")
            for edge in edges:
                u, v, weight = edge.strip().split()
                self.graph.add_edge(u, v, int(weight))
            start_node = 'A'  # Change this to the desired start node
            dijkstra_result = self.graph.dijkstra(start_node)
            total_cost = sum(dijkstra_result.values())
            formatted_result = ", ".join(f"{node}: {distance}" for node, distance in dijkstra_result.items())
            self.result_label.config(text=f"Dijkstra's Shortest Path Result from node {start_node}: {formatted_result}. Total cost: {total_cost}")
        except ValueError:
            messagebox.showinfo("Error", "Invalid input. Please enter edges and weights in the correct format.")

    def perform_bellman_ford(self):
        try:
            edges = self.entry.get().strip().split(",")
            for edge in edges:
                u, v, weight = edge.strip().split()
                self.graph.add_edge(u, v, int(weight))
            start_node = 'A'  # Change this to the desired start node
            bellman_ford_result = self.graph.bellman_ford(start_node)
            if isinstance(bellman_ford_result, str):
                self.result_label.config(text=f"{bellman_ford_result}")
            else:
                total_cost = sum(bellman_ford_result.values())
                formatted_result = ", ".join(f"{node}: {distance}" for node, distance in bellman_ford_result.items())
                self.result_label.config(text=f"Bellman-Ford Shortest Path Result from node {start_node}: {formatted_result}. Total cost: {total_cost}")
        except ValueError:
            messagebox.showinfo("Error", "Invalid input. Please enter edges and weights in the correct format.")


root = tk.Tk()
app = ShortestPathApp(root)
root.mainloop()

# A B 3, B C 4, A D 5, C D 2