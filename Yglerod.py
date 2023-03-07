import customtkinter
from tkinter import ttk
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
text_info='    Для расчета углеродного следа ведите потребление каждого вида энергии и нажмите кнопку "Рассчитать"\n    Индивидуальный "углеродный след" человека рассчитывается делением количества энергии на количество человек в домохозяйстве.\n'
app = customtkinter.CTk()
app.geometry("500x500")
app.resizable(width=False, height=False)
app.title("Расчет углеродного следа здания")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

label_info = customtkinter.CTkLabel(master=frame_1, wraplength=450, justify=customtkinter.LEFT, text=text_info)
label_info.grid(row=1, columnspan=2, pady=5, padx=10)

label_people = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='Количество человек:')
label_people.grid(row=2, column=0, padx=(20, 5), pady=(5, 5))
entry_people = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_people.grid(row=2, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")


label_0 = customtkinter.CTkLabel(master=frame_1,  font=("Arial", 18), text='Калькулятор углеродного следа здания')
label_0.grid(row=0, columnspan=2, pady=0, padx=0, )

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='Тепловая энергия(kWh):')
label_1.grid(row=3, column=0, padx=(20, 5), pady=(5, 5))
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_1.grid(row=3, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")

label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='Электрическая энергия(kWh):')
label_2.grid(row=4, column=0, padx=(20, 5), pady=(5, 5))
entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_2.grid(row=4, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")



str_text = customtkinter.StringVar()

label_result = customtkinter.CTkLabel(master=frame_1, font=("Arial", 16), textvariable=str_text)
label_result.grid(row=6, columnspan=2, pady=0, padx=0)

def calculation():
    KCo2 = int(entry_2.get()) * 0.3302
    e = int(entry_1.get()) * 0.1838
    p = int(entry_people.get())
    result = (KCo2 + e)/p/1000
    result_str = 'Углеродный след равен '+str(round(result, 3))+' тонн CO2'
    return str_text.set(result_str)

button_1 = customtkinter.CTkButton(master=frame_1, command=calculation, text='Рассчитать')
button_1.grid(row=5, columnspan=2, pady=10, padx=10, sticky="s")

if __name__ == '__main__':
    app.mainloop()