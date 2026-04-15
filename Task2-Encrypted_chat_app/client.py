import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from cryptography.fernet import Fernet

class CyberChatPro:
    def __init__(self, root):
        self.root = root
        self.root.title("CRYPT-NET EXTREME v2.0 | SECURE NODE")
        
        # Professional Full Screen Layout
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="#020617")

        # AES Key (Must be same for all clients to talk)
        self.key = b'v-9R_O7E0_N9W_9XQZp0vU9q-jP0z-G8yY2Z1A7-oY4=' 
        self.cipher = Fernet(self.key)

        # Connection Setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 5555))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Server se connect nahi ho paya: {e}")
            self.root.destroy()
            return

        self.create_widgets()
        
        # Start Receiver Thread
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def create_widgets(self):
        # Top Bar
        top_bar = tk.Frame(self.root, bg="#1e293b", height=60)
        top_bar.pack(fill="x", side="top")
        
        tk.Label(top_bar, text="🛡️ END-TO-END ENCRYPTED TERMINAL", fg="#38bdf8", bg="#1e293b", 
                 font=("Courier New", 18, "bold")).pack(pady=15)

        # Main Layout (Split Screen)
        container = tk.Frame(self.root, bg="#020617")
        container.pack(fill="both", expand=True, padx=30, pady=20)

        # Left Side: Tools & Keys
        left_panel = tk.Frame(container, bg="#0f172a", width=400, bd=2, relief="flat")
        left_panel.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(left_panel, text="ENCRYPTION STATUS", fg="#22c55e", bg="#0f172a", font=("Arial", 12, "bold")).pack(pady=20)
        
        # Key Display
        tk.Label(left_panel, text="Active Session Key:", fg="#94a3b8", bg="#0f172a").pack()
        key_box = tk.Entry(left_panel, bg="#020617", fg="#38bdf8", font=("Consolas", 10), bd=0)
        key_box.insert(0, self.key.decode())
        key_box.config(state="readonly")
        key_box.pack(pady=10, padx=20, fill="x")

        # Input Area
        tk.Label(left_panel, text="TYPE MESSAGE:", fg="white", bg="#0f172a", font=("Arial", 10)).pack(pady=(30, 0))
        self.msg_entry = tk.Text(left_panel, height=10, bg="#020617", fg="white", font=("Arial", 12), insertbackground="white")
        self.msg_entry.pack(pady=10, padx=20, fill="x")

        send_btn = tk.Button(left_panel, text="SECURE SEND", command=self.send_data, 
                             bg="#2563eb", fg="white", font=("Arial", 12, "bold"), pady=10, cursor="hand2")
        send_btn.pack(pady=20, padx=20, fill="x")

        # Right Side: Real-time Decrypted Logs
        right_panel = tk.Frame(container, bg="#020617")
        right_panel.pack(side="right", fill="both", expand=True)

        tk.Label(right_panel, text="SECURE TRAFFIC LOG", fg="#38bdf8", bg="#020617", font=("Arial", 12)).pack(anchor="w")
        self.display = scrolledtext.ScrolledText(right_panel, bg="#000000", fg="#00ff41", font=("Consolas", 12))
        self.display.pack(fill="both", expand=True, pady=10)

    def send_data(self):
        msg = self.msg_entry.get("1.0", tk.END).strip()
        if msg:
            encrypted_msg = self.cipher.encrypt(msg.encode())
            self.client_socket.send(encrypted_msg)
            self.display_message(f"[YOU]: {msg}")
            self.msg_entry.delete("1.0", tk.END)

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(2048)
                if data:
                    decrypted = self.cipher.decrypt(data).decode()
                    self.display_message(f"[INCOMING]: {decrypted}")
            except:
                break

    def display_message(self, text):
        self.display.insert(tk.END, f"{text}\n")
        self.display.insert(tk.END, "-"*60 + "\n")
        self.display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberChatPro(root)
    root.mainloop()
