import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import threading

# Payloads
payloads = [
    "<script>alert(1)</script>",
    "'\"><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>"
]

results = []

class XSSScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("XSS Vulnerability Scanner - Cyber Nitesh")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0f172a")

        # Title
        tk.Label(root, text="WEB VULNERABILITY SCANNER (XSS)",
                 font=("Arial", 20, "bold"),
                 fg="#38bdf8", bg="#0f172a").pack(pady=10)

        # Input Frame
        frame = tk.Frame(root, bg="#0f172a")
        frame.pack(pady=10)

        tk.Label(frame, text="Target URL:", fg="white", bg="#0f172a").grid(row=0, column=0)
        self.url = tk.Entry(frame, width=50)
        self.url.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Parameter:", fg="white", bg="#0f172a").grid(row=1, column=0)
        self.param = tk.Entry(frame, width=20)
        self.param.grid(row=1, column=1, sticky="w")

        tk.Button(frame, text="Start Scan", bg="#22c55e",
                  command=self.thread_scan).grid(row=0, column=2, padx=10)

        tk.Button(frame, text="Save Report", bg="#f59e0b",
                  command=self.save_report).grid(row=0, column=3)

        # Output
        self.output = scrolledtext.ScrolledText(root, width=130, height=28,
                                                bg="black", fg="#00ff00",
                                                font=("Consolas", 10))
        self.output.pack(pady=20)

    def log(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.output.update()

    def thread_scan(self):
        t = threading.Thread(target=self.start_scan)
        t.start()

    def start_scan(self):
        url = self.url.get().strip()
        param = self.param.get().strip()

        if not url or not param:
            messagebox.showerror("Error", "Enter URL and Parameter")
            return

        self.output.delete(1.0, tk.END)
        results.clear()

        self.log(f"[START] Scanning {url}\n")

        for payload in payloads:
            test_url = f"{url}?{param}={payload}"
            try:
                res = requests.get(test_url, timeout=5)

                if payload in res.text:
                    msg = f"[VULNERABLE] {test_url}"
                    self.log(msg)
                    results.append(msg)
                else:
                    self.log(f"[SAFE] {test_url}")

            except Exception as e:
                self.log(f"[ERROR] {test_url} -> {e}")

        self.log("\n=== Scan Completed ===")

    def save_report(self):
        if not results:
            messagebox.showinfo("Info", "No vulnerabilities found")
            return

        file = filedialog.asksaveasfilename(defaultextension=".pdf")

        if not file:
            return

        doc = SimpleDocTemplate(file, pagesize=letter)
        styles = getSampleStyleSheet()

        content = []
        content.append(Paragraph("<b>XSS Scan Report</b><br/><br/>", styles["Title"]))

        for r in results:
            content.append(Paragraph(r, styles["Normal"]))

        doc.build(content)

        messagebox.showinfo("Saved", "Report saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = XSSScanner(root)
    root.mainloop()
