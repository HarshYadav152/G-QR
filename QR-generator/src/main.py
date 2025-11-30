import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr_code():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate QR code.")
        return
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")
    
    messagebox.showinfo("Success", "QR code generated and saved as 'qr_code.png'.")

app = tk.Tk()
app.title("G-QR")

label = tk.Label(app, text="Enter data for QR Code:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=20)

app.mainloop()
