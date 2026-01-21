import sys, os, time, random, math, subprocess, datetime, platform, shutil
import ctypes
from pathlib import Path

class ChalkVUniversal:
    def __init__(self):
        # 1. PRIMARY SYSTEM REGISTERS
        self.vars = {
            "VER": "V_4.1_FINAL_MASTER", 
            "USER": "jaceb", 
            "PROMPT": "CHALK-V:/>",
            "ANS": "0", 
            "OS": platform.system(),
            "BOOT": datetime.datetime.now().strftime("%H:%M:%S")
        }
        
        # 2. REGISTERED COMMAND LIST (For Syntax Intelligence)
        self.commands = [
            "SHELL", "RUN", "TYPE", "CAT", "NANO", "DIR", "LS", "CD", "CD..", 
            "MKDIR", "CALL", "SET", "INPUT", "UI_BOX", "CLS", "EXIT", "ECHO", 
            "HELP", "VARS", "DEL", "WIPE", "PWD", "SLEEP", "IF", "EXPLORE"
        ]
        
        self.running = True
        self.cls()

    def is_danger_zone(self):
        """Hard-check for Windows/System32 protection"""
        curr = os.getcwd().upper()
        return "SYSTEM32" in curr or "WINDOWS" in curr

    def cls(self):
        """Standard System Reset and Banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        in_danger = self.is_danger_zone()
        print("="*85)
        print(f"  CHALK V UNIVERSAL 4.1 | FULL ARMORED MASTER CORE")
        print(f"  STATUS: {'!! DANGER: SYSTEM DIR !!' if in_danger else 'STABLE / SAFE'}")
        print(f"  PATH: {os.getcwd()}")
        print("="*85)
        if in_danger:
            print("[!] SHIELD WARNING: SYSTEM PROTECTION ACTIVE. WIPE/DEL/NANO LOCKED.")

    def syntax_error(self, cmd, reason, usage=None):
        """Analyzes and reports user errors"""
        print(f"\n[!] SYNTAX ERROR: '{cmd}'")
        print(f"    REASON: {reason}")
        if usage: print(f"    CORRECT USAGE: {usage}")
        print("")

    def smart_jump(self, target):
        """Logic for 'CD-less' folder jumping"""
        for root, dirs, files in os.walk('.'):
            if target in dirs:
                os.chdir(os.path.join(root, target))
                self.cls()
                print(f"[NAV] Auto-Jumped to: {os.getcwd()}")
                return True
        return False

    def execute(self, cmd_line, silent=False):
        raw = cmd_line.strip()
        if not raw or raw.startswith("//"): return
        
        # --- VARIABLE INJECTOR ---
        for v, val in self.vars.items():
            raw = raw.replace(f"${v.lower()}", str(val)).replace(f"${v.upper()}", str(val))
        
        clean, up = raw.strip(), raw.strip().upper()
        parts = clean.split(' ')
        first_word = parts[0].upper()

        try:
            # --- [FS] STABLE NANO EDITOR ---
            if up.startswith("NANO "):
                fname = clean[5:].strip()
                if not fname: return self.syntax_error("NANO", "Filename required.", "NANO file.chk")
                if self.is_danger_zone():
                    print("[SHIELD] Access Denied: Cannot write files in System folders.")
                    return
                print(f"\n-- NANO: {fname} (Type 'SAVE' on its own line to exit) --")
                buffer = []
                while True:
                    ln = input(f" {len(buffer)+1} | ")
                    if ln.upper() == "SAVE": break
                    buffer.append(ln)
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write("\n".join(buffer))
                print(f"[FS] File saved: {fname}\n")

            # --- [FS] DIRECT SHELL (WINDOWS OVERRIDE) ---
            elif up.startswith("SHELL "):
                cmd = clean[6:].strip()
                if cmd: os.system(cmd)
                else: self.syntax_error("SHELL", "No Windows command provided.")

            # --- [FS] SMART RUN (UNIFIED) ---
            elif up.startswith("RUN "):
                fname = clean[4:].strip()
                t = Path(fname)
                if not t.exists():
                    print(f"[!] ERROR: {fname} not found.")
                    return
                if t.suffix.lower() in ['.bat', '.cmd']:
                    os.system(f"call {fname}")
                else:
                    with open(t, 'r', encoding='utf-8') as f:
                        for line in f: self.execute(line.strip(), silent=True)

            # --- [FS] DEL / WIPE (WITH FEEDBACK) ---
            elif up.startswith("DEL "):
                fname = clean[4:].strip()
                if self.is_danger_zone():
                    print("[SHIELD] Locked: Cannot delete system files.")
                    return
                f_path = Path(fname)
                if f_path.exists() and f_path.is_file():
                    f_path.unlink()
                    print(f"[FS] Deleted: {fname}")
                else: print(f"[!] ERROR: Could not find '{fname}'")

            elif up == "WIPE":
                if self.is_danger_zone(): return
                conf = input("Confirm wipe? (Y/N): ")
                if conf.upper() == 'Y':
                    for item in Path('.').iterdir():
                        if item.is_file(): item.unlink()
                        elif item.is_dir(): shutil.rmtree(item)
                    print("[FS] Directory Wiped.")

            # --- [FS] NAV & TOOLS ---
            elif up == "DIR" or up == "LS":
                for f in Path('.').iterdir():
                    tag = "[DIR]" if f.is_dir() else "     "
                    print(f"  {tag} {f.name}")
            elif up.startswith("CD "):
                os.chdir(clean[3:].strip()); self.cls()
            elif up == "CD..":
                os.chdir(".."); self.cls()
            elif up == "EXPLORE": os.system("start .")
            elif up.startswith("TYPE ") or up.startswith("CAT "):
                t = Path(clean[5:].strip())
                if t.exists(): print(f"--- {t.name} ---\n{t.read_text()}\n---")
                else: print("[!] File not found.")

            # --- [LOGIC] SET, IF, SLEEP ---
            elif up.startswith("SET "):
                if "=" in clean:
                    n, v = clean[4:].split('=', 1)
                    self.vars[n.strip().upper()] = v.strip()
                    if not silent: print(f"[*] Set {n.strip().upper()}")
            
            elif up.startswith("IF "):
                idx = clean.find("{")
                logic = clean[3:idx].strip()
                block = clean[idx+1 : clean.rfind("}")].strip()
                if "==" in logic:
                    l, r = logic.split("==")
                    if l.strip().upper() == r.strip().upper():
                        self.execute(block, silent=True)

            elif up.startswith("SLEEP "):
                try: time.sleep(float(clean[6:].strip()))
                except: pass

            # --- [SYS CORE] ---
            elif up.startswith("INPUT "):
                p = clean.split('"')
                self.vars[p[2].strip().upper()] = input(p[1])
            elif up.startswith("UI_BOX "):
                ctypes.windll.user32.MessageBoxW(0, clean[7:].strip(), "CHALK V", 0x40)
            elif up == "CLS": self.cls()
            elif up == "VARS":
                for k,v in self.vars.items(): print(f" {k} = {v}")
            elif up == "EXIT": self.running = False
            elif up == "HELP": print(f"CMDS: {', '.join(self.commands)}")
            elif up.startswith("ECHO "): print(clean[5:])

            # --- [SMART JUMP / ERROR] ---
            elif first_word not in self.commands:
                if not self.smart_jump(clean):
                    self.syntax_error(first_word, "Unknown command.")

        except Exception as e:
            print(f"[SHIELD] Logic/Execution Error: {e}")

if __name__ == "__main__":
    chalk = ChalkVUniversal()
    while chalk.running:
        try:
            cmd = input(f"{chalk.vars['USER']}@CORE:{chalk.vars['PROMPT']} ")
            chalk.execute(cmd)
        except KeyboardInterrupt: break