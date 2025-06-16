import time
import tkinter as tk
import math
from tkinter import ttk, messagebox
from tkinter import filedialog
from SHA_256_fernet import FernetEncryptor as fernet
from SHA_256_fernet import hash_sha256
from faker import Faker # type: ignore

#--------------------------#
# Omar Alnabilsi 322598558
# Neev Penkar 341119501
#--------------------------#

### --- GUI MODULES --- ###
def clamp(val, min_val=0, max_val=255):
    return max(min_val, min(val, max_val))

class CustomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enctyption Tools")
        self.root.geometry("800x600")
        self.start_time = time.time()

        # Top level containers
        self.create_logo("Omar Alnabilsi & Neev Penkar\n322598558        341119501")
        self.create_nav_buttons()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.animate_background()

    def create_logo(self, text):
        self.logo = tk.Label(self.root, text=text, font=("Arial", 20), fg="yellow", justify="center")
        self.logo.pack(pady=5)
    
    def create_nav_buttons(self):
        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(pady=5)

        self.buttons = {
            "Hash": self.render_hash_ui,
            "Encrypt": self.render_encrypt_ui,
            "Fake": self.render_fake_ui,
            "URL Scrape": self.render_scrape_ui,
            "DDOS" : self.render_ddos_ui,
            "Caesar" : self.render_caesar_ui,
            "Vigenere" : self.render_vigenere_ui,
        }

        for label, command in self.buttons.items():
            b = tk.Button(self.nav_frame, text=label, command=command)
            b.pack(side=tk.LEFT, padx=5)

    def animate_background(self):
        t = time.time() - self.start_time

        # r = int((math.sin(t * 0.5) + 1) * 64)
        # g = int((math.sin(t * 0.7 + 2) + 1) * 64)
        # b = int((math.sin(t * 0.9 + 4) + 1) * 128 + 64) 

        # # Clamp values to [0, 255]
        # r, g, b = clamp(r), clamp(g), clamp(b)
        r = 10  # low red
        g = 20  # low green

    # Animate blue in a smooth wave between 64 and 128
        b = int((math.sin(t * 1.0) + 1) * 32 + 64)
        hex_color = f'#{r:02x}{g:02x}{b:02x}'

        # Apply background
        self.root.configure(bg=hex_color)
        self.logo.configure(bg=hex_color)
        self.nav_frame.configure(bg=hex_color)
        self.main_frame.configure(bg=hex_color)

        self.root.after(50, self.animate_background)

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def attach_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=file_path)
            try:
                with open(file_path, 'rb') as f:
                    self.file_content = f.read()
            except Exception as e:
                messagebox.showerror("File Error", str(e))
                self.file_content = b""   

    #### WORKING WELL ####
    def render_hash_ui(self):
        self.clear_main()

        # Data entry
        tk.Label(self.main_frame, text="Data").pack()
        data_entry = tk.Text(self.main_frame, height=3)
        data_entry.pack()

        # Attach file
        attach_button = tk.Button(self.main_frame, text="Attach Key", command=self.attach_file)
        attach_button.pack()

        self.file_label = tk.Label(self.main_frame, text="No key selected")
        self.file_label.pack()

        # Output area
        tk.Label(self.main_frame, text="Output").pack()
        output = tk.Text(self.main_frame, height=3, state="disabled")
        output.pack()

        # Algorithm selector
        algo = tk.StringVar()
        algo.set("Fernet")
        algo_menu = ttk.Combobox(self.main_frame, textvariable=algo, values=["Fernet", "SHA256"])
        algo_menu.pack(pady=5)

        # Go button logic
        def on_go():
            try:
                data = data_entry.get("1.0", tk.END).strip().encode()

                if algo.get() == "Fernet":
                    if not self.file_content:
                        raise ValueError("You must attach a key file for Fernet encryption.")
                    f = fernet()
                    result = f.encrypt(data, str)
                else:
                    result = hash_sha256(data, str)

                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, result)
                output.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####

    #### WORKING WELL ####
    def render_ddos_ui(self):
        self.clear_main()

        tk.Label(self.main_frame, text="Target IP").pack()
        target_entry = tk.Text(self.main_frame, height=1, width=14)
        target_entry.pack()

        tk.Label(self.main_frame, text="Port number").pack()
        port_entry = tk.Text(self.main_frame, height=1, width=14)
        port_entry.pack()

        tk.Label(self.main_frame, text="Message to send").pack()
        msg_entry = tk.Text(self.main_frame, height=4, width=14)
        msg_entry.pack()

        tk.Label(self.main_frame, text="Number of threads").pack()
        threads_entry = tk.Text(self.main_frame, height=1, width=14)
        threads_entry.pack()

        tk.Label(self.main_frame, text="Number of runs").pack()
        runs_entry = tk.Text(self.main_frame, height=1, width=14)
        runs_entry.pack()

        tk.Label(self.main_frame, text="Output").pack()
        output = tk.Text(self.main_frame, height=3, state="disabled")
        output.pack(pady=5)

        from ddos import run_attack
        def on_go():
            try:
                GivvenIP = target_entry.get("1.0", tk.END).strip()
                GivvenPort = int(port_entry.get("1.0", tk.END).strip())
                GivvenMSG = msg_entry.get("1.0", tk.END).strip()
                ThreadsNum = int(threads_entry.get("1.0", tk.END).strip())
                runs = int(runs_entry.get("1.0", tk.END).strip())

                print("STARTING A DDOS ATTACK\n")
                
                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, "DDOSing...")  # display int or str
                output.config(state="disabled")
                output.update_idletasks()
                from time import sleep
                sleep(0.5)
                
                run_attack(GivvenIP, GivvenPort, GivvenMSG, ThreadsNum, runs)

                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, "DONE ATTACKING")  # display int or str
                output.config(state="disabled")

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####
   
    #### WORKING WELL ####
    def render_encrypt_ui(self):
        self.clear_main()

        import tkinter as tk
        from tkinter import messagebox
        from MSSP import mssp_decode

        tk.Label(self.main_frame, text="Data").pack()
        data_entry = tk.Text(self.main_frame, height=3)
        data_entry.pack(pady=5)

        # Frame for keys
        keys_frame = tk.Frame(self.main_frame)
        keys_frame.pack(pady=5)

        # Keyn
        frame1 = tk.Frame(keys_frame)
        frame1.pack(side='left', padx=10)
        tk.Label(frame1, text="Keyn").pack()
        key1_entry = tk.Text(frame1, height=2, width=20)
        key1_entry.pack()

        # Keyd
        frame2 = tk.Frame(keys_frame)
        frame2.pack(side='left', padx=10)
        tk.Label(frame2, text="Keyd").pack()
        key2_entry = tk.Text(frame2, height=2, width=20)
        key2_entry.pack()

        # Output
        tk.Label(self.main_frame, text="Output").pack()
        output = tk.Text(self.main_frame, height=3, state="disabled")
        output.pack(pady=5)

        def on_go():
            try:
                UsersNum = data_entry.get("1.0", tk.END).strip()
                keyn_raw = key1_entry.get("1.0", tk.END).strip()
                keyd_raw = key2_entry.get("1.0", tk.END).strip()

                # Validate UsersNum is digits only
                if not UsersNum.isdigit():
                    raise ValueError("Data must contain only digits.")

                # Convert and validate keys
                if not (keyn_raw.isdigit() and keyd_raw.isdigit()):
                    raise ValueError("Keyn and Keyd must be valid integers.")

                keyn = int(keyn_raw)
                keyd = int(keyd_raw)

                result = mssp_decode(UsersNum, keyn, keyd)

                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, str(result))  # display int or str
                output.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####

    #### WORKING WELL ####
    def render_scrape_ui(self):
        self.clear_main()
        
        tk.Label(self.main_frame, text="URL").pack()
        url_entry = tk.Text(self.main_frame, height=3)
        url_entry.pack()

        tk.Label(self.main_frame, text="Target").pack()
        target_entry = tk.Text(self.main_frame, height=3)
        target_entry.pack()

        from request_URL import highlight_word_in_url_with_parsing, show_html_with_highlight

        def on_go():
            try:
                url = url_entry.get("1.0", tk.END).strip()
                target = target_entry.get("1.0", tk.END).strip()
                highlight_word_in_url_with_parsing(f"{url}", f"{target}")
                show_html_with_highlight(f"{url}", f"{target}")
                messagebox.showinfo("Info", f"Scraping initiated for {target}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####
    
    #### WORKING WELL ####
    def render_fake_ui(self):
        import tkinter as tk
        from tkinter import ttk, messagebox
        from fake_data import generate_fake_data

        self.clear_main()

        # Language to locale mapping (same as your CLI version)
        locale_map = {
            "English": "en_US",
            "Hebrew": "he_IL",
            "Italian": "it_IT",
            "Japanese": "ja_JP",
            "Arabic": "ar_SA"
        }

        # Language selector
        tk.Label(self.main_frame, text="Select Language").pack(pady=(5, 0))
        algo = tk.StringVar(value="English")
        algo_menu = ttk.Combobox(
            self.main_frame,
            textvariable=algo,
            values=list(locale_map.keys()),
            state="readonly"
        )
        algo_menu.current(0)
        algo_menu.pack(pady=5)

        # Helper function to create a labeled text field
        def create_output_field(label_text):
            tk.Label(self.main_frame, text=label_text).pack()
            text_widget = tk.Text(self.main_frame, height=3, state="disabled", wrap=tk.WORD)
            text_widget.pack(pady=5)
            return text_widget

        # Create and store output fields
        self.output_fields = {
            "Name": create_output_field("Name"),
            "Address": create_output_field("Address"),
            "Email": create_output_field("Email"),
            "Phone": create_output_field("Phone"),
            "Company": create_output_field("Company")
        }

        # Button click action
        def on_go():
            try:
                selected_language = algo.get()
                locale = locale_map.get(selected_language)

                if not locale:
                    messagebox.showwarning("Invalid Selection", "Please select a valid language.")
                    return

                fake = Faker(locale)
                result = generate_fake_data(fake)  # Should return [name, address, email, phone, company]

                if len(result) != 5:
                    raise ValueError("generate_fake_data must return exactly 5 values.")

                for key, value in zip(self.output_fields.keys(), result):
                    widget = self.output_fields[key]
                    widget.config(state="normal")
                    widget.delete("1.0", tk.END)
                    widget.insert("1.0", value)
                    widget.config(state="disabled")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

        # "Go" button
        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=10)
    #### WORKING WELL ####

    #### WORKING WELL ####
    def render_caesar_ui(self):
        self.clear_main()

         # Algorithm selector
        algo = tk.StringVar()
        algo.set("Encrypt")
        algo_menu = ttk.Combobox(self.main_frame, textvariable=algo, values=["Encrypt", "Decrypt"])
        algo_menu.pack(pady=5)
        
        tk.Label(self.main_frame, text="Data").pack()
        data_entry = tk.Text(self.main_frame, height=3)
        data_entry.pack(pady=5)

        tk.Label(self.main_frame, text="key").pack()
        shift_entry = tk.Text(self.main_frame, height=3)
        shift_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Output").pack()
        output = tk.Text(self.main_frame, height=13, state="disabled")
        output.pack(pady=5)

        from Caesar import encrypt_caesar_cipher, decrypt_caesar_cipher
        def on_go():
            try:
                Data = data_entry.get("1.0", tk.END).strip()
                shift = shift_entry.get("1.0", tk.END).strip()

                if algo.get() == "Encrypt":
                    result = encrypt_caesar_cipher(f"{Data}", int(shift))
                else:
                    result, res0 , res1 = decrypt_caesar_cipher(f"{Data}")

                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, str(f"{result}\n\n"))
                output.insert(tk.END, str(f"{res0}\n"))
                output.insert(tk.END, str(f"{res1}\n"))  # display int or str
                output.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####

    #### WORKING WELL ####
    def render_vigenere_ui(self):
        self.clear_main()

        # Algorithm selector
        algo = tk.StringVar()
        algo.set("Encrypt")
        algo_menu = ttk.Combobox(self.main_frame, textvariable=algo, values=["Encrypt", "Decrypt"])
        algo_menu.pack(pady=5)
        
        tk.Label(self.main_frame, text="Data").pack()
        data_entry = tk.Text(self.main_frame, height=3)
        data_entry.pack(pady=5)

        tk.Label(self.main_frame, text="key").pack()
        shift_entry = tk.Text(self.main_frame, height=3)
        shift_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Output").pack()
        output = tk.Text(self.main_frame, height=13, state="disabled")
        output.pack(pady=5)

        from Vigenere import encrypt_vigenere, decrypt_vigenere
        def on_go():
            try:
                Data = data_entry.get("1.0", tk.END).strip()
                shift = shift_entry.get("1.0", tk.END).strip()

                if algo.get() == "Encrypt":
                    result = encrypt_vigenere(f"{Data}", f"{shift}")
                else:
                    result= decrypt_vigenere(f"{Data}", f"{shift}")

                output.config(state="normal")
                output.delete("1.0", tk.END)
                output.insert(tk.END, str(f"{result}\n\n"))
                output.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.main_frame, text="Go", command=on_go).pack(pady=5)
    #### WORKING WELL ####

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    root.mainloop()
