import tkinter as tk
from tkinter import messagebox


class BipartiteMatchingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bipartite Matching")

        self.graph = []
        self.rows = 0
        self.cols = 0

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.input_frame, text="Enter 0/1 for connections between applicants and jobs:")
        self.label.grid(row=0, columnspan=2, pady=(0, 10))

        self.rows_entry = tk.Entry(self.input_frame, width=5)
        self.rows_entry.grid(row=1, column=0, padx=(0, 5))
        self.rows_entry.insert(0, "6")  # default value
        self.rows_label = tk.Label(self.input_frame, text="Applicants")
        self.rows_label.grid(row=1, column=1)

        self.cols_entry = tk.Entry(self.input_frame, width=5)
        self.cols_entry.grid(row=2, column=0, padx=(0, 5))
        self.cols_entry.insert(0, "6")  # default value
        self.cols_label = tk.Label(self.input_frame, text="Jobs")
        self.cols_label.grid(row=2, column=1)

        self.generate_button = tk.Button(self.input_frame, text="Generate Graph", command=self.generate_graph)
        self.generate_button.grid(row=3, columnspan=2, pady=(10, 0))

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=(10, 0))

    def generate_graph(self):
        try:
            self.rows = int(self.rows_entry.get())
            self.cols = int(self.cols_entry.get())

            self.graph_frame = tk.Frame(self.root)
            self.graph_frame.pack()

            self.entries = []
            for i in range(self.rows):
                row_entries = []
                for j in range(self.cols):
                    entry = tk.Entry(self.graph_frame, width=5)
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    row_entries.append(entry)
                self.entries.append(row_entries)

            self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_max_bpm)
            self.calculate_button.pack(pady=(10, 0))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for rows and columns.")

    def calculate_max_bpm(self):
        try:
            self.graph = [[int(entry.get()) for entry in row] for row in self.entries]
            g = GFG(self.graph)
            max_applicants = g.maxBPM()
            self.result_label.config(text=f"Maximum number of applicants that can get job is {max_applicants}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


class GFG:
    def __init__(self, graph):
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    def bpm(self, u, matchR, seen):
        for v in range(self.jobs):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxBPM(self):
        matchR = [-1] * self.jobs
        result = 0
        for i in range(self.ppl):
            seen = [False] * self.jobs
            if self.bpm(i, matchR, seen):
                result += 1
        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = BipartiteMatchingGUI(root)
    root.mainloop()
