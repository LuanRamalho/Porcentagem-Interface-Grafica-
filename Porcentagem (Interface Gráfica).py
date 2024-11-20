import tkinter as tk
from tkinter import messagebox

class PerCentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Percentual")
        self.root.geometry("500x400")
        self.root.config(bg="#1E2A47")  # Fundo escuro para dar contraste

        # Título
        self.title_label = tk.Label(self.root, text="Calculadora Percentual", font=("Arial", 20, "bold"), fg="white", bg="#1E2A47")
        self.title_label.pack(pady=20)

        # Descrição
        self.desc_label = tk.Label(self.root, text="Escolha a operação desejada", font=("Arial", 14), fg="white", bg="#1E2A47")
        self.desc_label.pack(pady=10)

        # Opções de operação
        self.operation_var = tk.StringVar()
        self.operation_var.set("1")  # Default is Acréscimo/Descrécimo
        
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, 
                                            "1 - Acréscimo/Descrécimo",
                                            "2 - Descobrir Valor Percentual", 
                                            "3 - Descobrir Valor Numérico")
        self.operation_menu.config(font=("Arial", 12), bg="#FDCB82", fg="black", width=25)
        self.operation_menu.pack(pady=20)

        # Botão de Iniciar
        self.start_button = tk.Button(self.root, text="Iniciar Cálculo", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.start_calculation, relief="flat", width=20)
        self.start_button.pack(pady=20)

        # Resultados
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16), bg="#1E2A47", fg="white")
        self.result_label.pack(pady=10)

    def start_calculation(self):
        op = self.operation_var.get()

        if op == "1 - Acréscimo/Descrécimo":
            self.acrescimo_descrécimo()
        elif op == "2 - Descobrir Valor Percentual":
            self.valor_percentual()
        elif op == "3 - Descobrir Valor Numérico":
            self.valor_numerico()

    def acrescimo_descrécimo(self):
        def calculate():
            try:
                num = float(entry_num.get())
                p = float(entry_percent.get())
                result = num + (num * p) / 100
                self.result_label.config(text=f"Resultado: {result:.0f}", fg="#2ECC71")
            except ValueError:
                messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

        # Janela de operação Acréscimo/Descrécimo
        top = tk.Toplevel(self.root)
        top.title("Acréscimo/Descrécimo")
        top.geometry("400x300")
        top.config(bg="#34495E")

        tk.Label(top, text="Digite um número:", font=("Arial", 12), bg="#34495E", fg="white").pack(pady=10)
        entry_num = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_num.pack(pady=10)

        tk.Label(top, text="Digite o valor percentual:", font=("Arial", 12), bg="#34495E", fg="white").pack(pady=10)
        entry_percent = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_percent.pack(pady=10)

        calc_button = tk.Button(top, text="Calcular", font=("Arial", 12), bg="#F39C12", fg="white", command=calculate, width=20)
        calc_button.pack(pady=20)

    def valor_percentual(self):
        def calculate():
            try:
                num1 = float(entry_num1.get())
                num2 = float(entry_num2.get())
                result = (num1 / num2) * 100
                self.result_label.config(text=f"Resultado: {result:.2f}%", fg="#F39C12")
            except ValueError:
                messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

        # Janela de operação Valor Percentual
        top = tk.Toplevel(self.root)
        top.title("Valor Percentual")
        top.geometry("400x300")
        top.config(bg="#8E44AD")

        tk.Label(top, text="Digite o 1º número:", font=("Arial", 12), bg="#8E44AD", fg="white").pack(pady=10)
        entry_num1 = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_num1.pack(pady=10)

        tk.Label(top, text="Digite o 2º número:", font=("Arial", 12), bg="#8E44AD", fg="white").pack(pady=10)
        entry_num2 = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_num2.pack(pady=10)

        calc_button = tk.Button(top, text="Calcular", font=("Arial", 12), bg="#F39C12", fg="white", command=calculate, width=20)
        calc_button.pack(pady=20)

    def valor_numerico(self):
        def calculate():
            try:
                num = float(entry_num.get())
                p = float(entry_percent.get())
                result = (num * p) / 100
                self.result_label.config(text=f"Resultado: {result:.0f}", fg="#E74C3C")
            except ValueError:
                messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")

        # Janela de operação Valor Numérico
        top = tk.Toplevel(self.root)
        top.title("Valor Numérico")
        top.geometry("400x300")
        top.config(bg="#2980B9")

        tk.Label(top, text="Digite um número:", font=("Arial", 12), bg="#2980B9", fg="white").pack(pady=10)
        entry_num = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_num.pack(pady=10)

        tk.Label(top, text="Digite o valor percentual:", font=("Arial", 12), bg="#2980B9", fg="white").pack(pady=10)
        entry_percent = tk.Entry(top, font=("Arial", 14), relief="solid", width=20)
        entry_percent.pack(pady=10)

        calc_button = tk.Button(top, text="Calcular", font=("Arial", 12), bg="#F39C12", fg="white", command=calculate, width=20)
        calc_button.pack(pady=20)

# Inicia a aplicação
root = tk.Tk()
app = PerCentApp(root)
root.mainloop()
