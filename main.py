import tkinter as tk
from tkinter import messagebox
import requests

def shorten_url():
    api_key = api_key_entry.get()
    url = url_entry.get()

    if not api_key:
        messagebox.showerror("Error", "Please enter your API Key")
        return

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    shorten_button.config(text="Shortening...", state=tk.DISABLED)
    
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    response = requests.get(api_url).json()

    if response["url"]["status"] == 7:
        shortened_url = response["url"]["shortLink"]
        result_label.config(text="Shortened URL:", fg="#4caf50")
        shortened_result.config(text=shortened_url)
    else:
        error_message = response["url"]["error"]["msg"]
        result_label.config(text="Error:", fg="#f44336")
        shortened_result.config(text=error_message)

    shorten_button.config(text="Shorten URL", state=tk.NORMAL)

# Create the main application window
app = tk.Tk()
app.title("URL Shortener")
app.geometry("400x300")
app.resizable(False, False)

# Dark theme styling
app.configure(bg="#212121")
font = ("Helvetica", 12)
foreground_color = "#ffffff"
input_bg = "#333"
button_bg = "#2196f3"
button_fg = "#ffffff"

# Create and place UI components
title_label = tk.Label(app, text="URL Shortener", font=("Helvetica", 18, "bold"), bg="#212121", fg=foreground_color)
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

api_key_label = tk.Label(app, text="API Key:", font=font, bg="#212121", fg=foreground_color)
api_key_label.grid(row=1, column=0, padx=10, sticky="w")

api_key_entry = tk.Entry(app, font=font, bg=input_bg, fg=foreground_color)
api_key_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

url_label = tk.Label(app, text="Enter URL:", font=font, bg="#212121", fg=foreground_color)
url_label.grid(row=2, column=0, padx=10, sticky="w")

url_entry = tk.Entry(app, font=font, bg=input_bg, fg=foreground_color)
url_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")

shorten_button = tk.Button(app, text="Shorten URL", font=font, bg=button_bg, fg=button_fg, command=shorten_url)
shorten_button.grid(row=3, columnspan=2, pady=15)

result_label = tk.Label(app, text="", font=("Helvetica", 12, "bold"), bg="#212121", fg=foreground_color)
result_label.grid(row=4, column=0, padx=10, sticky="w")

shortened_result = tk.Label(app, text="", font=("Helvetica", 12), bg="#212121", fg=foreground_color)
shortened_result.grid(row=4, column=1, padx=10, pady=5, sticky="e")

# Start the GUI event loop
app.mainloop()
