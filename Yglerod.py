import customtkinter
from tkinter import ttk
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
text_info='    Для расчета углеродного следа заполните все ячейкии нажмите кнопку "Рассчитать"\n После расчета углородного следа здания, Вам будет дана оценка выделения углеродного следа в атмосеру.'
app = customtkinter.CTk()
app.geometry("500x500")
app.resizable(width=False, height=False)
app.title("Калькулятор углеродного следа строительного проекта")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

label_info = customtkinter.CTkLabel(master=frame_1, wraplength=450, justify=customtkinter.LEFT, text=text_info)
label_info.grid(row=1, columnspan=2, pady=5, padx=10)

label_people = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='ГСОП (С*сут):')
label_people.grid(row=2, column=0, padx=(20, 5), pady=(5, 5))
entry_people = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_people.grid(row=2, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")


label_0 = customtkinter.CTkLabel(master=frame_1,  font=("Arial", 18), text='Калькулятор углеродного следа здания')
label_0.grid(row=0, columnspan=2, pady=0, padx=0, )

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='Нормируемая удельная х-ка (Вт/м^3*С):')
label_1.grid(row=3, column=0, padx=(20, 5), pady=(5, 5))
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_1.grid(row=3, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")

label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='Коэффициент эмиссии ((УЕ*10^3)/Гкал):')
label_2.grid(row=4, column=0, padx=(20, 5), pady=(5, 5))
entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
entry_2.grid(row=4, column=1, padx=(5, 20), pady=(5, 5), sticky="nsew")



str_text = customtkinter.StringVar()

label_result = customtkinter.CTkLabel(master=frame_1, font=("Arial", 14), textvariable=str_text)
label_result.grid(row=6, columnspan=3, pady=0, padx=0)



def calculation():
    Ka = int(entry_2.get()) * 0.000001*24
    e = int(entry_1.get())
    p = int(entry_people.get())
    result = Ka * e * p
    result_str = 'Углеродный след равен ' + str(round(result, 3)) + ' тонн CO2 в год.'

    if result <= 100:
        result_str += '\n Ваш углеродный след ниже среднего значения. Вы молодец!'
    elif result > 100 and result <=160:
        result_str += '\n Ваш углеродный след находится с среднем значении.\n Следует чаще проводить проверку.'
    else:
        result_str += '\n Ваш углеродный след превышает среднего значение выброса \n в атмосферу.  Необходимо в кратчайшие сроки \n сократить выброс и произвести проверку снова!!! '
    return str_text.set(result_str)

button_1 = customtkinter.CTkButton(master=frame_1, command=calculation, text='Рассчитать')
button_1.grid(row=5, columnspan=2, pady=10, padx=10, sticky="s")

if __name__ == '__main__':
    app.mainloop()