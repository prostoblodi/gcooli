from bs4 import BeautifulSoup
import requests
from tkinter import Tk, Label, Entry, Button

class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        response = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD")
        soup = BeautifulSoup(response.content, 'html.parser')
        rate_element = soup.find(class_='sc-708e65be-1 chuBHG')
        return float(rate_element.text.strip().replace(' US Dollars', ''))

    def convert_to_usd(self, local_amount):
        return local_amount / self.usd_rate

# Графічний інтерфейс
class CurrencyConverterApp:
    def __init__(self):
        self.converter = CurrencyConverter()
        self.window = Tk()
        self.window.geometry("300x100")
        self.window.title("Конвертер Валюти")

        self.label_input = Label(self.window, text="Сума у EUR:")
        self.label_input.pack()

        self.entry_amount = Entry(self.window)
        self.entry_amount.pack()

        self.button_convert = Button(self.window, text="Конвертувати", command=self.convert)
        self.button_convert.pack()

        self.label_result = Label(self.window, text="")
        self.label_result.pack()

    def convert(self):
        local_amount = float(self.entry_amount.get())
        usd_amount = self.converter.convert_to_usd(local_amount)
        self.label_result.config(text=f"Сума в USD: {usd_amount:.2f}")

    def run(self):
        self.window.mainloop()

app = CurrencyConverterApp()
app.run()
