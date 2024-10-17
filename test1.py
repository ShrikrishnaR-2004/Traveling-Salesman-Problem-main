import tkinter as tk
from tkinter import messagebox

def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items

def calculate_knapsack():
    try:
        capacity = int(capacity_entry.get())
        items_list = items_entry.get("1.0", tk.END).strip().split('\n')
        items = []
        for item in items_list:
            weight, value = map(int, item.split(','))
            items.append((weight, value))
        max_value, selected_items = knapsack(items, capacity)
        result_label.config(text=f"Maximum value: {max_value}\nSelected items: {selected_items}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Create GUI
root = tk.Tk()
root.title("Knapsack Problem Solver")

tk.Label(root, text="Capacity:").grid(row=0, column=0, sticky="e")
capacity_entry = tk.Entry(root)
capacity_entry.grid(row=0, column=1)

tk.Label(root, text="Items (weight, value):").grid(row=1, column=0, sticky="e")
items_entry = tk.Text(root, height=5, width=30)
items_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_knapsack)
calculate_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()
