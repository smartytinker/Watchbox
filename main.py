import subprocess
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
from log_parser import convert
from report_builder import parse_csv
from malware_runner import run_sample
from tkinter import messagebox

malware_path = None

def run_procmon(duration =30):
	threading.Thread(target = subprocess.run(f'"run_procmon.bat" {duration}', shell = True)).start()
	logbox.insert(tk.END, f"Procmon started\n")
	logbox.see(tk.END)

def ex():
	root.destroy()

def openwindow():
	global malware_path
	malware_path = filedialog.askopenfilename()
	if malware_path:
		entry1.delete(0, tk.END)
		entry1.insert(0, malware_path)

def star():
	def runn():
		if malware_path:
			run_sample(malware_path)
			run_procmon(30)
			if convert():
				report = parse_csv()
				logbox.insert(tk.END, "Malware Behaviour Summary")
		
				logbox.insert(tk.END, "\n[Files Written]\n")
				for item in report["files written"][:10]:
					logbox.insert(tk.END, f" - {item}\n")

				logbox.insert(tk.END, "\n[Registery Modified]\n")
				for item in report["registry mods"][:10]:
					logbox.insert(tk.END, f" - {item}\n")

				logbox.insert(tk.END, "\n[Network Access]\n")
				for item in report["network access"][:10]:
					logbox.insert(tk.END, f" - {item}\n")		
				logbox.see(tk.END)
		else:
			messagebox.showerror("Error!", "Please select the Malware Path !")
			
	threading.Thread(target = runn).start()
	 
		
root = tk.Tk()

root.title("Analyzer")

root.state('zoomed')

button = tk.Button(root, text = "Select File",  command = openwindow)
button.pack(pady = 20)

button = tk.Button(root, text = "Exit",  command = ex)
button.pack(pady = 20)

button = tk.Button(root, text = "Start", command = star)
button.pack(pady = 20)

label1 = tk.Label(root, text = ' ')
label1.pack(pady = 20)

entry1 = tk.Entry(root, width = 60)
entry1.pack(pady = 40)

logbox = tk.Text(root, bg = "black", height = 15, fg = "lime")
logbox.pack(padx = 40, pady = 40)

root.mainloop()	