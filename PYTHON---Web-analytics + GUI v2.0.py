import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_website_usage(log_file):
    # Load the log file into a DataFrame
    df = pd.read_csv(log_file)
    
    results = ""
    
    # Counting unique users
    if 'user_id' in df.columns:
        unique_users = df['user_id'].nunique()
        results += f"Number of unique users: {unique_users}\n"
    
    # Counting total visits
    if 'timestamp' in df.columns:
        total_visits = df['timestamp'].count()
        results += f"Total number of visits: {total_visits}\n"
    
    # Counting visits per day
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        visits_per_day = df.groupby(df['timestamp'].dt.date).size()
        results += "Visits per day:\n"
        results += visits_per_day.to_string() + "\n"
    
    return results

def browse_file():
    file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        results = analyze_website_usage(file_path)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, results)

# Setting up the main application window
root = tk.Tk()
root.title("Website Usage Analyzer")

# Creating the GUI elements
label = tk.Label(root, text="Select the website log file:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, height=20, width=60)
result_text.pack(pady=10)

# Run the application
root.mainloop()
