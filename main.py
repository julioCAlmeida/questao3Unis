import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_bmi():
    patient_name = entry_patient_name.get()
    full_address = entry_full_address.get()

    if not patient_name or not full_address:
        messagebox.showerror("Error", "Favor entrar com os campos Nome e Endereço Completo.")
        return

    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, insira valores numéricos válidos para Peso e Altura.")
        return

    bmi = ((weight * 100) / (height ** 2)) * 100

    if bmi < 17:
        situation = "Muito abaixo do peso"
    elif 17 <= bmi < 18.5:
        situation = "Abaixo do peso"
    elif 18.5 <= bmi < 25:
        situation = "Peso normal "
    elif 25 <= bmi < 30:
        situation = "Acima do peso"
    elif 30 <= bmi < 35:
        situation = "Obesidade I "
    elif 35 <= bmi < 40:
        situation = "Obesidade II (severa)"
    else:
        situation = "Obesidade III (mórbida)"

    result_text = f"{patient_name.upper()}\nIMC: {bmi:.2f}\nSituation: {situation}"
    label_result.config(text=result_text)

def reset_fields():
    entry_patient_name.delete(0, tk.END)
    entry_full_address.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    label_result.config(text="")

def close_program():
    window.destroy()


window = tk.Tk()
window.title("Cálculo de IMC - índice de Massa Corporal")


label_patient_name = ttk.Label(window, text="Nome do Paciente:")
label_patient_name.grid(row=0, column=0, padx=10, pady=10)
entry_patient_name = ttk.Entry(window)
entry_patient_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

label_full_address = ttk.Label(window, text="Endereço Completo:")
label_full_address.grid(row=1, column=0, padx=10, pady=10)
entry_full_address = ttk.Entry(window)
entry_full_address.grid(row=1, column=1, padx=10, pady=10)

label_weight = ttk.Label(window, text="Peso (kg):")
label_weight.grid(row=2, column=0, padx=10, pady=10)
entry_weight = ttk.Entry(window)
entry_weight.grid(row=2, column=1, padx=10, pady=10)

label_height = ttk.Label(window, text="Altura (cm):")
label_height.grid(row=3, column=0, padx=10, pady=10)
entry_height = ttk.Entry(window)
entry_height.grid(row=3, column=1, padx=10, pady=10)


button_calculate = ttk.Button(window, text="Calcular IMC", command=calculate_bmi)
button_calculate.grid(row=5, column=0, columnspan=2, pady=10)

button_reset = ttk.Button(window, text="Reiniciar", command=reset_fields)
button_reset.grid(row=5, column=2, columnspan=2, pady=10)

button_close = ttk.Button(window, text="Sair", command=close_program)
button_close.grid(row=5, column=4, columnspan=2, pady=10)


frame_result = ttk.Frame(window)
frame_result.grid(row=2, column=2, rowspan=2, columnspan=2, pady=10, padx=10)

label_result = ttk.Label(frame_result, text="")
label_result.pack(expand=True, fill="both")

window.mainloop()
