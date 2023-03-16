from tkinter import *
import math


def leftClickButton(event):
    print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100,2))
    labelResult.configure(text=float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))

    bmi = format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    bmiShow = ""

    if float(bmi) <= 18.5:
        bmiShow = "ผอมเกินไป น้อยกว่า 18.5"

    elif float(bmi) > 18.5 and float(bmi) <= 22.9:
        bmiShow = "น้ำหนักปกติ เหมาะสม 18.6 - 22.9"

    elif float(bmi) >= 23 and float(bmi) <= 24.9:
        bmiShow = "น้ำหนักเกิน 23.0 - 24.9"

    elif float(bmi) >= 25 and float(bmi) <= 29.9:
        bmiShow = "อ้วน 25.0 - 29.9"

    elif float(bmi) >= 30:
        bmiShow = "อ้วนมาก 30.0 ขึ้นไป"

    labelResult.configure(text=bmiShow)


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง(cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก(kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="ผลลัพธ์")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ดัชนีมวลกาย(BMI)")
labelResult.grid(row=2, column=1)

MainWindow.mainloop()