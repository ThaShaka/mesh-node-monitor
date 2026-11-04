import time
import subprocess
import sys
from datetime import datetime

NODES = {
    "Studentski-Gateway": "10.129.154.23",
    "Javni-DNS (Google)": "8.8.8.8", 
    "Sensor-Node-Na-Terenu": "10.129.154.99"  
}

def ping_node(ip):
    param = "-n" if sys.platform.startswith("win") else "-c"
    command = ["ping", param, "1", "-W", "1", ip]
    
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

def main():
    print("=== MESHPOINT SIMULATOR: Krizni mrežni monitor pokrenut ===")
    print(f"Nadzirem {len(NODES)} čvorova. Pritisni Ctrl+C za izlaz.\n")
    
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(stat_line := f"[{timestamp}] Provjera statusa mreže...")
            
            for name, ip in NODES.items():
                is_alive = ping_node(ip)
                if is_alive:
                    print(f"  [ONLINE]  {name} ({ip}) - Veza stabilna.")
                else:
                    print(f"  [ALERT!]  {name} ({ip}) - ISPAD VEZE DETEKTIRAN!")
            
            print("-" * 50)
            time.sleep(5)  
    except KeyboardInterrupt:
        print("\nMonitor zaustavljen od strane korisnika")

if __name__ == "__main__":
    main()
