import os
import tempfile
import subprocess
import winreg
import time
import requests	

def create_fake_exe():
    fake_dir = os.path.join(os.getenv("APPDATA"), "FakeMalware")
    os.makedirs(fake_dir, exist_ok=True)
    fake_exe = os.path.join(fake_dir, "evil.exe")
    with open(fake_exe, "w") as f:
        f.write("This is a fake malware executable.")
    return fake_exe

def add_registry_persistence(exe_path):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Run",
                                 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "FakeMalware", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"Registry write failed: {e}")

def create_temp_files():
    for i in range(5):
        temp_file = os.path.join(tempfile.gettempdir(), f"fake_file_{i+1}.tmp")
        with open(temp_file, "w") as f:
            f.write(f"Fake content {i+1}")
        time.sleep(0.3)

def simulate_network():
    try:
        requests.get("http://example.com", timeout=2)
    except Exception:
        print("[*] Network sim failed (expected)")

def spawn_process():
    subprocess.Popen(["notepad.exe"])

def main():
    print("[*] Starting fake malware simulation...")

    exe_path = create_fake_exe()
    add_registry_persistence(exe_path)
    create_temp_files()
    simulate_network()
    spawn_process()

    print("[*] Simulation complete.")

if __name__ == "__main__":
    main()
