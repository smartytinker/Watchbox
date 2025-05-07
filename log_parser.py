from pathlib import Path
import subprocess

DESKTOP = Path.home() / "Desktop"
PROJECT_DIR = DESKTOP / "Project 1"
CSV_PATH = PROJECT_DIR / "capture.csv"
PML_PATH = PROJECT_DIR / "procmon_log.pml"
PROC_PATH = PROJECT_DIR / "Procmon64a.exe"

def convert():
    if not PML_PATH.exists():
        print(f"No PML log found at {PML_PATH}")
        return False

    print(f"PML file found at {PML_PATH}, now converting...")

    result = subprocess.run([PROC_PATH, "/OpenLog", str(PML_PATH), "/SaveAs", str(CSV_PATH)],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0 or not CSV_PATH.exists():
        print("Error during conversion:")
        print(result.stderr.decode(errors="ignore"))
        print(result.stdout.decode(errors="ignore"))
        return False

    print(f"CSV saved to {CSV_PATH}")
    return True
