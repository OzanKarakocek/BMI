import tkinter

window = tkinter.Tk()
window.title("BMI Hesaplama")
window.minsize(width=300, height=250)
window.resizable(width=False, height=False)


def click_button():
    try:
        kilo = float(entry1.get())
        boy = float(entry2.get())
        boy = boy / 100
        bmi = kilo / (boy * boy)
        bmi_label.config(text=f"Hesaplanan BMI: {bmi:.2f}")

        if bmi <= 18.5:
            label3.config(text="Zayıf")
        elif 18.5 < bmi <= 24.9:
            label3.config(text="Normal Kilo")
        elif 25 <= bmi <= 29.9:
            label3.config(text="Fazla Kilolu")
        elif 30 <= bmi <= 39.9:
            label3.config(text="Obezite")
        elif bmi >= 40:
            label3.config(text="Aşırı Obezite")
    except ValueError:
        label3.config(text="Lütfen geçerli bir sayı giriniz!")
        bmi_label.config(text="")

        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        entry1.focus()

label1 = tkinter.Label(text="Kilonuzu Giriniz (kg):", padx="3", pady="3")
label1.pack()

entry1 = tkinter.Entry()
entry1.pack()

label2 = tkinter.Label(text="Boyunuzu Giriniz (cm):", padx="3", pady="3")
label2.pack()

entry2 = tkinter.Entry()
entry2.pack()

button1 = tkinter.Button(text="Hesaplamak İçin Basınız", padx="3", pady="3", command=click_button)
button1.pack()

bmi_label = tkinter.Label(text="Hesaplanan BMI: ", padx="3", pady="3")
bmi_label.pack()

label3 = tkinter.Label()
label3.pack(side="bottom")

window.mainloop()
