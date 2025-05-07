from pathlib import Path
import csv

DESKTOP = Path.home() / "Desktop"

PROJECT_DIR = DESKTOP / "Project 1"
CSV_PATH = PROJECT_DIR / "capture.csv"

def parse_csv():
    results = {"files written": [], "registry mods": [], "network access": []}

    with open(CSV_PATH, newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            
            path = row.get("Path", "")
            op = row.get("Operation", "")

            
            if "WriteFile" in op:
                results["files written"].append(path)
            elif "RegSetValue" in op or "RegCreateKey" in op:
                results["registry mods"].append(path)
            elif "TCP" in op or "UDP" in op:
                results["network access"].append(path)
    
    return results	
