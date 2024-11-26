import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def browse_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)

        #Descriptive Statistics
        def describe_column(df, column_name):
            print(f"Descriptive Statistics for {column_name}:")
            print(df[column_name].describe())
            print("-" * 20)

        if 'math score' in data.columns: describe_column(data, 'math score')
        if 'reading score' in data.columns: describe_column(data, 'reading score')
        if 'writing score' in data.columns: describe_column(data, 'writing score')


        # Histograms
        plt.figure(figsize=(12, 4))
        if 'math score' in data.columns:
            plt.subplot(1, 3, 1)
            sns.histplot(data['math score'], kde=True)
            plt.title('Math Score Distribution')
        if 'reading score' in data.columns:
            plt.subplot(1, 3, 2)
            sns.histplot(data['reading score'], kde=True)
            plt.title('Reading Score Distribution')
        if 'writing score' in data.columns:
            plt.subplot(1, 3, 3)
            sns.histplot(data['writing score'], kde=True)
            plt.title('Writing Score Distribution')
        plt.tight_layout()
        plt.show()


        # Box plots (example using gender if the column exists)
        if 'gender' in data.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='gender', y='math score', data=data)
            plt.title('Math Score by Gender')
            plt.show()

        # Add more visualizations as needed...

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "The file is empty.")
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Error parsing the CSV file.  Please check its format.")
    except KeyError as e:
        messagebox.showerror("Error", f"Column not found: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# --- Main Tkinter window ---
root = tk.Tk()
root.title("Student Performance Analyzer")

browse_button = tk.Button(root, text="Browse CSV File", command=lambda: analyze_data(browse_file()))
browse_button.pack(pady=20)

root.mainloop()