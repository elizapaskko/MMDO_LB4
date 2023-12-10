import tkinter as tk

class MatrixInputApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Input")
        
        self.label_size = tk.Label(self.master, text="Введіть розмірність квадратної матриці:")
        self.label_size.pack(pady=5)
        
        self.entry_size = tk.Entry(self.master)
        self.entry_size.pack(pady=5)
        
        self.button = tk.Button(self.master, text="Ввести", command=self.create_matrix)
        self.button.pack(pady=10)

       

    def create_matrix(self):
        try:
            size = int(self.entry_size.get())
            if size > 0:
                self.master.iconify()
                self.show_matrix_input(size)
            else:
                self.show_error("Розмірність повинна бути додатнім числом.")
        except ValueError:
            self.show_error("Введено некоректне значення.")

    def show_matrix_input(self, size):
        matrix_input_frame = tk.Frame(self.master)
        matrix_input_frame.pack()

        matrix = []
        probabilities = []

        for i in range(size):
            row = []
            for j in range(size):
                entry = tk.Entry(matrix_input_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row.append(entry)
            matrix.append(row)

            prob_entry = tk.Entry(matrix_input_frame, width=5)
            prob_entry.grid(row=size, column=i, padx=5, pady=5)
            probabilities.append(prob_entry)

        submit_button = tk.Button(matrix_input_frame, text="Готово", command=lambda: self.get_matrix_values(matrix, probabilities, size))
        submit_button.grid(row=size + 1, columnspan=size, pady=10)

         # Додаємо поле для виведення результатів
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def get_matrix_values(self, matrix, probabilities, size):
        values = []
        for row in matrix:
            row_values = []
            for entry in row:
                try:
                    value = float(entry.get())
                    row_values.append(value)
                except ValueError:
                    self.show_error("Введено некоректне числове значення.")
                    return
            values.append(row_values)

        prob_values = []
        for prob_entry in probabilities:
            try:
                prob_value = float(prob_entry.get())
                prob_values.append(prob_value)
            except ValueError:
                self.show_error("Введено некоректне числове значення для ймовірності.")
                return

        result_text = f"A: стратегія 1\n B: стратегія 1"

        # Виводимо результат під матрицею
        self.result_label.config(text=result_text)

    def show_error(self, message):
        error_label = tk.Label(self.master, text=message, fg="red")
        error_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixInputApp(root)
    root.mainloop()
