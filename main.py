import tkinter as tk
import requests
from IPython.display import display
import ipywidgets as widgets

api_key = "1cfca0cea63d4584869144562b207f7d" #api i used from open-exchange-rates
base_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

root = tk.Tk()
root.title("Abdullah Currency Converter")

amount_label = tk.Label(root, text="Amount:", font=("Arial", 14))
amount_label.grid(row=0, column=0, padx=5, pady=5)

from_label = tk.Label(root, text="From:", font=("Arial", 14))
from_label.grid(row=1, column=0, padx=5, pady=5)

to_label = tk.Label(root, text="To:", font=("Arial", 14))
to_label.grid(row=2, column=0, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="#008080")
result_label.grid(row=3, column=0, padx=5, pady=5)

amount_entry = tk.Entry(root, font=("Arial", 14))
amount_entry.grid(row=0, column=1, padx=5, pady=5)

from_currency = tk.StringVar()
from_currency_dropdown = tk.OptionMenu(root, from_currency, "USD", "EUR", "GBP", "PKR", "CAD")
from_currency_dropdown.grid(row=1, column=1, padx=5, pady=5)
from_currency.set("USD")

to_currency = tk.StringVar()
to_currency_dropdown = tk.OptionMenu(root, to_currency, "USD", "EUR", "GBP", "PKR", "CAD")
to_currency_dropdown.grid(row=2, column=1, padx=5, pady=5)
to_currency.set("USD")

def convert_currency():
    # used to get exchange rates using API
    try:
        response = requests.get(base_url)
        exchange_rates = response.json()["rates"]
        from_rate = exchange_rates[from_currency.get()]
        to_rate = exchange_rates[to_currency.get()]

        amount = float(amount_entry.get())
        result = amount * (to_rate / from_rate)
        result_label.config(text=f"{result:.2f} {to_currency.get()}")
    except ValueError:
        result_label.config(text="Please enter a valid amount.")

    except:

        result_label.config(text="An error occurred.")


convert_button = tk.Button(root, text="Convert", command=convert_currency, font=("Arial", 14),
                            bg="#008080", fg="white")
convert_button.grid(row=3, column=1, padx=5, pady=5, sticky="W")

reset_button = tk.Button(root, text="Reset", command=lambda: [amount_entry.delete(0, tk.END), from_currency.set("USD"), to_currency.set("USD"), result_label.config(text="")], font=("Arial", 14), bg="#C0C0C0",
                            fg="blue")
reset_button.grid(row=3, column=1, padx=5, pady=5, sticky="E")

#  display it in the notebook
result_widget = widgets.Output()
display(result_widget)
with result_widget:
    display(result_label)

root.mainloop()
