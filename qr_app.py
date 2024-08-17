import qrcode
from PIL import Image
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator and Scanner")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="QR Code Generator and Scanner", font=("Arial", 16))
        self.label.pack(pady=10)

        self.generate_button = tk.Button(self.frame, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=5)

        self.scan_button = tk.Button(self.frame, text="Scan QR Code", command=self.scan_qr_code)
        self.scan_button.pack(pady=5)

    def generate_qr_code(self):
        data = tk.simpledialog.askstring("Input", "Enter the data for the QR Code:")
        if data:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filename:
                try:
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(data)
                    qr.make(fit=True)

                    img = qr.make_image(fill='black', back_color='white')
                    img.save(filename)
                    messagebox.showinfo("Success", f"QR Code generated and saved as {filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to generate QR Code: {e}")

    def scan_qr_code(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if filename:
            try:
                img = cv2.imread(filename)
                detector = cv2.QRCodeDetector()
                data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
                if vertices_array is not None:
                    messagebox.showinfo("QR Code Data", f"QR Code data: {data}")
                else:
                    messagebox.showwarning("No QR Code", "No QR Code detected in the image.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to scan QR Code: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
