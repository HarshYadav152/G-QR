import tkinter as tk
from tkinter import messagebox
import qrcode

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("G-QR")

        self.label = tk.Label(master, text="Enter text to generate QR Code:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack()

        self.qr_code_label = tk.Label(master)
        self.qr_code_label.pack()

    def generate_qr(self):
        text = self.entry.get()
        if text:
            qr = qrcode.make(text)
            qr.save("qr_code.png")
            self.qr_code_label.config(text="QR Code generated and saved as 'qr_code.png'")
        else:
            messagebox.showwarning("Input Error", "Please enter some text to generate a QR Code.")

def run_gui():
    root = tk.Tk()
    qr_code_generator = QRCodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
