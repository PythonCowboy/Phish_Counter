import tkinter as tk
from datetime import datetime

# Set the stored date variable
# At the moment, need to configure this manually
stored_date_str = "2024-04-20"
stored_date_obj = datetime.strptime(stored_date_str, "%Y-%m-%d")

# Create GUI window
root = tk.Tk()
root.title("IT")

# Calculate the number of days since the stored date
delta = datetime.now() - stored_date_obj
days_since = delta.days

# Create a label for the title
title_label = tk.Label(root, text=f"Days since last Phished:", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a label for the stored date
stored_date_label = tk.Label(root, text=f"{days_since}", font=("Helvetica", 12))
stored_date_label.pack()

# Mainly used as a padding placeholder for now
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()