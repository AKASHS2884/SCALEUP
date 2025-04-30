import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("AI Drug Analyzer")
root.geometry("400x600")
root.configure(bg='white')

# Header
header = tk.Label(root, text="DRUG ANALYSER", bg="#4B0082", fg="white", font=("Helvetica", 16, "bold"), pady=10)
header.pack(fill=tk.X)

# Logo Placeholder
logo = tk.Label(root, text="[LOGO]", bg="white", font=("Helvetica", 20), pady=20)
logo.pack()

# Subtitle
subtitle = tk.Label(root, text="AI ANALYSE EITHER YOUR DRUG WILL BE\nDESIRED OR NOT BY ITS FEED DATA", 
                    bg="white", fg="black", font=("Helvetica", 10, "bold"), justify="center")
subtitle.pack(pady=(0, 20))

# Input fields
input1 = ttk.Entry(root, width=40)
input1.insert(0, "Enter Drug Name")
input1.pack(pady=10)

input2 = ttk.Entry(root, width=40)
input2.insert(0, "Enter Molecular Data")
input2.pack(pady=10)

input3 = ttk.Entry(root, width=40)
input3.insert(0, "Enter SMILES or Compound ID")
input3.pack(pady=10)

# Check button
def check_drug():
    drug = input1.get()
    molecule = input2.get()
    smiles = input3.get()
    print(f"Drug: {drug}, Molecular Data: {molecule}, SMILES: {smiles}")
    # Add your AI logic here

check_btn = ttk.Button(root, text="✔  CHECK NOW", command=check_drug)
check_btn.pack(pady=30)

# Start the application
root.mainloop()
