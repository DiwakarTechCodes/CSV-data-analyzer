import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_and_plot():
    file_path = filedialog.askopenfilename(
        title="CSV File Select Karo",
        filetypes=[("CSV files", "*.csv")]
    )
    
    if not file_path:
        return
    
    try:
        df = pd.read_csv(file_path)
        
        # Graph banate hain
        fig, ax = plt.subplots(figsize=(7,4))
        
        if 'Age' in df.columns:
            ax.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
            ax.set_title('Age Distribution')
            ax.set_xlabel('Age')
            ax.set_ylabel('Count')
        else:
            messagebox.showerror("Error", "CSV mein 'Age' column nahi mila!")
            return
        
        # Purana graph clear karke naya dikhao
        for widget in frame.winfo_children():
            widget.destroy()
            
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        messagebox.showinfo("Success", "Graph ban gaya! ✅")
        
    except Exception as e:
        messagebox.showerror("Error", f"Kuch gadbad ho gayi: {e}")

# Main Window
root = tk.Tk()
root.title("CSV Data Analyzer GUI")
root.geometry("750x550")

label = tk.Label(root, text="📊 CSV Data Analyzer", font=("Arial", 20, "bold"))
label.pack(pady=15)

btn = tk.Button(root, text="CSV File Select Karo", command=load_and_plot, 
                font=("Arial", 14), bg="lightblue", padx=20, pady=10)
btn.pack(pady=20)
btn2 = tk.Button(root, text="Salary ka Graph Dekho", command=lambda: plot_salary(globals().get('df')),
                font=("Arial", 14), bg="lightgreen", padx=20, pady=10)
btn2.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)
def plot_salary(df):      # ← Sirf 1 baar rahega
    if df is None:        # ← 4 space andar
        messagebox.showwarning("Ruko bhai!", "Pehle CSV File Select Karo")
        return
    if 'Salary' in df.columns:                                                   
        fig, ax = plt.subplots(figsize=(7,4))
        ax.bar(df['Name'], df['Salary'], color='lightgreen')
        ax.set_title('Salary by Name')
        ax.set_xlabel('Name')
        ax.set_ylabel('Salary')
        plt.xticks(rotation=45)
    fig.canvas.manager.window.attributes('-topmost',1)
    plt.show()
    messagebox.showerror("Error", "CSV mein 'Salary' column nahi mila!")

root.mainloop()
