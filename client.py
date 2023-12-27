import tkinter as tk
from tkinter import filedialog
import requests

class FileShareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sharing App")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="Select a file to upload:")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.download_button = tk.Button(root, text="Download File", command=self.download_file)
        self.download_button.pack(pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            files = {'file': open(file_path, 'rb')}
            response = requests.post('http://localhost:5000/upload', files=files)
            print(response.text)

    def download_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
        if filename:
            filename = filename.split("/")[-1]  # Extract only the filename
            response = requests.get(f'http://localhost:5000/download/{filename}')
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f'File downloaded as {filename}')

if __name__ == "__main__":
    root = tk.Tk()
    app = FileShareApp(root)
    root.mainloop()
