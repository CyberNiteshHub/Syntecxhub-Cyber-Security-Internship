import socket
import threading
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# PDF support
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PortScannerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Port Scanner Pro")
        self.root.geometry("900x600")
        self.root.config(bg="#0f172a")

        self.results = []

        self.setup_ui()

    def setup_ui(self):

        # Title
        title = Label(
            self.root,
            text="PORT SCANNER PRO",
            font=("Segoe UI", 20, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )
        title.pack(pady=10)

        # Input Frame
        input_frame = Frame(self.root, bg="#0f172a")
        input_frame.pack(pady=10)

        # Target
        Label(input_frame, text="Target (IP/Domain):",
              fg="white", bg="#0f172a").grid(row=0, column=0, padx=10)

        self.target_entry = Entry(input_frame, width=25, font=("Segoe UI", 11))
        self.target_entry.grid(row=0, column=1, padx=10)

        # Start Port
        Label(input_frame, text="Start Port:",
              fg="white", bg="#0f172a").grid(row=1, column=0, padx=10)

        self.start_port = Entry(input_frame, width=10)
        self.start_port.grid(row=1, column=1, sticky="w")

        # End Port
        Label(input_frame, text="End Port:",
              fg="white", bg="#0f172a").grid(row=2, column=0, padx=10)

        self.end_port = Entry(input_frame, width=10)
        self.end_port.grid(row=2, column=1, sticky="w")

        # Buttons
        btn_frame = Frame(self.root, bg="#0f172a")
        btn_frame.pack(pady=10)

        scan_btn = Button(
            btn_frame,
            text="Start Scan",
            command=self.start_scan,
            bg="#22c55e",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            width=15
        )
        scan_btn.grid(row=0, column=0, padx=10)

        save_btn = Button(
            btn_frame,
            text="Save as PDF",
            command=self.save_pdf,
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        )
        save_btn.grid(row=0, column=1, padx=10)

        clear_btn = Button(
            btn_frame,
            text="Clear",
            command=self.clear_results,
            bg="#ef4444",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15
        )
        clear_btn.grid(row=0, column=2, padx=10)

        # Result Box with Scrollbar
        result_frame = Frame(self.root)
        result_frame.pack(pady=10, fill=BOTH, expand=True)

        scrollbar = Scrollbar(result_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.result_box = Text(
            result_frame,
            bg="#020617",
            fg="#22c55e",
            font=("Consolas", 11),
            yscrollcommand=scrollbar.set
        )
        self.result_box.pack(fill=BOTH, expand=True)

        scrollbar.config(command=self.result_box.yview)

    # Scan single port
    def scan_port(self, target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                output = f"[OPEN] Port {port}"
                self.results.append(output)
                self.result_box.insert(END, output + "\n")

            sock.close()

        except:
            pass

    # Start scanning
    def start_scan(self):

        self.clear_results()

        target = self.target_entry.get()

        try:
            start = int(self.start_port.get())
            end = int(self.end_port.get())
        except:
            messagebox.showerror("Error", "Invalid port range")
            return

        try:
            target_ip = socket.gethostbyname(target)
        except:
            messagebox.showerror("Error", "Invalid target")
            return

        self.result_box.insert(END, f"Scanning {target_ip}...\n\n")

        for port in range(start, end + 1):
            thread = threading.Thread(
                target=self.scan_port,
                args=(target_ip, port)
            )
            thread.start()

    # Clear results
    def clear_results(self):
        self.result_box.delete(1.0, END)
        self.results = []

    # Save results as PDF
    def save_pdf(self):

        if not self.results:
            messagebox.showwarning("Warning", "No results to save")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        doc = SimpleDocTemplate(file_path, pagesize=letter)
        styles = getSampleStyleSheet()

        content = []

        content.append(Paragraph(
            "Port Scan Report",
            styles['Title']
        ))

        content.append(Paragraph(
            f"Generated: {datetime.now()}",
            styles['Normal']
        ))

        for line in self.results:
            content.append(Paragraph(line, styles['Normal']))

        doc.build(content)

        messagebox.showinfo("Success", "PDF saved successfully!")


if __name__ == "__main__":
    root = Tk()
    app = PortScannerGUI(root)
    root.mainloop()
