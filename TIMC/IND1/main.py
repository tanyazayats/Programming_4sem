import tkinter as tk
from tkinter import messagebox
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_data():
    try:
        k = int(entry_k.get())
        var_type = var_choice.get()
        
        if var_type == "Дискретна":
            data = np.random.randint(k, k+10, 50)
            title = "Дискретна вибірка"
        else:
            distribution = dist_choice.get()
            if distribution == "Рівномірний":
                data = np.random.uniform(k, k+10, 50)
                title = "Рівномірний розподіл"
            elif distribution == "Нормальний":
                data = np.random.normal(k+5, 2, 50)
                title = "Нормальний розподіл"
            else:
                data = np.random.exponential(2, 50) + k
                title = "Експоненційний розподіл"

        show_statistics(data, title)
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректне значення для k.")

def show_statistics(data, title):
    sorted_data = np.sort(data)
    mean = np.mean(data)
    median = np.median(data)
    mode = pd.Series(data).mode().values
    variance = np.var(data)

    # Відображення характеристик
    stats_text = f"Середнє: {mean:.2f}\nМедіана: {median:.2f}\nМода: {mode}\nДисперсія: {variance:.2f}"
    messagebox.showinfo("Статистичні характеристики", stats_text)

    # Побудова графіків
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.histplot(data, bins=10, kde=True, ax=axes[0], color='blue')
    axes[0].set_title("Гістограма")

    sns.ecdfplot(data, ax=axes[1], color='red')
    axes[1].set_title("Емпірична функція розподілу")

    plt.suptitle(title)
    plt.show()

# Графічний інтерфейс
root = tk.Tk()
root.title("Генерація вибірки")

tk.Label(root, text="Введіть номер варіанту (k):").pack(pady=5)
entry_k = tk.Entry(root)
entry_k.pack(pady=5)

var_choice = tk.StringVar(value="Дискретна")
tk.Label(root, text="Оберіть тип змінної:").pack(pady=5)
tk.Radiobutton(root, text="Дискретна", variable=var_choice, value="Дискретна").pack()
tk.Radiobutton(root, text="Неперервна", variable=var_choice, value="Неперервна").pack()

dist_choice = tk.StringVar(value="Рівномірний")
tk.Label(root, text="Оберіть розподіл (для неперервної змінної):").pack(pady=5)
tk.Radiobutton(root, text="Рівномірний", variable=dist_choice, value="Рівномірний").pack()
tk.Radiobutton(root, text="Нормальний", variable=dist_choice, value="Нормальний").pack()
tk.Radiobutton(root, text="Експоненційний", variable=dist_choice, value="Експоненційний").pack()

tk.Button(root, text="Згенерувати вибірку", command=generate_data).pack(pady=10)

root.mainloop()
