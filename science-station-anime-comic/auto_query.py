import time
import pyautogui
import pyperclip

# Delay aman
pyautogui.PAUSE = 0.2

ITEMS = [
    # Tier 0 & 1
    "Science Station",
    "Toxic Waste Barrel",
    "Military Radio",
    # Tier 2
    "Acid",
    "Barrel",
    "Biohazard Sign",
    "Sharp Piano",
    # Tier 3
    "Cactus",
    "Plumbing",
    "Super Crate Box",
    "Dungeon Door",
    "Danger Sign",
    "Orange Block",
    "Piano Note",
    "Death Spikes",
    # Tier 4 & Base
    "Bush",
    "Bathtub",
    "Toilet",
    "White Block",
    "Crappy Sign",
    "Brown Block",
    "Mushroom",
    "Green Block",
    "Door",
    "Window",
    "Dirt",
    "Sign",
    "Lava",
    "Pointy Sign",
    "Bricks",
    "Poppy",
    "Rose"
]

def countdown(seconds=5):
    print("\n" + "="*55)
    print(f"SIAP-SIAP! KLIK KOLOM CHAT DISCORD SEKARANG!")
    print("="*55)
    for i in range(seconds, 0, -1):
        print(f"Mulai dalam {i} detik...")
        time.sleep(1)
    print("MULAI NGETIK!\n")

def send_harvest(item_name, item_count=2700, harvester=True, dcs=True):
    print(f"[HARVEST] Mengirim: {item_name} ({item_count}) | Harvester={harvester}, DCS={dcs}")
    
    # 1. Ketik /harvest & pilih command
    pyautogui.write("/harvest", interval=0.04)
    time.sleep(0.6)
    pyautogui.press("enter")
    time.sleep(0.5)
    
    # 2. Pill 1: item_count
    pyautogui.write(str(item_count), interval=0.03)
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.5)
    
    # 3. Pill 2: item_name
    pyperclip.copy(item_name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter") # Kunci nama item
    time.sleep(0.6)
    
    # 4. Pill 3: harvester_buff
    # Ketik 'harvester' biar Discord otomatis narget opsi harvester_buff
    pyautogui.write("harvester", interval=0.04)
    time.sleep(0.5)
    pyautogui.press("tab") # Ubah jadi pill [harvester_buff]
    time.sleep(0.5)
    if harvester:
        pyautogui.press("enter") # Pilih True
    else:
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter") # Pilih False
    time.sleep(0.6)
    
    # 5. Pill 4: dcs_buff
    # Ketik 'dcs' biar Discord otomatis narget opsi dcs_buff
    pyautogui.write("dcs", interval=0.04)
    time.sleep(0.5)
    pyautogui.press("tab") # Ubah jadi pill [dcs_buff]
    time.sleep(0.5)
    if dcs:
        pyautogui.press("enter") # Pilih True
    else:
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter") # Pilih False
    time.sleep(0.7)
    
    # 6. Submit final command
    pyautogui.press("enter")
    print(f"[HARVEST] Selesai!")

def send_break(item_name, item_count=10000):
    print(f"[BREAK] Mengirim: {item_name} ({item_count})")
    
    # 1. Ketik /break & pilih command
    pyautogui.write("/break", interval=0.04)
    time.sleep(0.6)
    pyautogui.press("enter")
    time.sleep(0.5)
    
    # 2. Pill 1: item_count
    pyautogui.write(str(item_count), interval=0.03)
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.5)
    
    # 3. Pill 2: item_name
    pyperclip.copy(item_name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter") # Kunci nama item
    time.sleep(0.6)
    
    # 4. Submit
    pyautogui.press("enter")
    print(f"[BREAK] Selesai!")

if __name__ == "__main__":
    print("=== DROID-PET DISCORD AUTO-TYPER ===")
    print("Pilihan Mode:")
    print("1. Tes 1 item (Science Station) - Full Buff (Harvester + DCS)")
    print("2. Gas semua 32 item: Full Buff (Harvester=True, DCS=True)")
    print("3. Gas semua 32 item: No Buff (Harvester=False, DCS=False)")
    
    mode = input("\nPilih mode (1/2/3): ").strip()
    
    if mode == "1":
        countdown(5)
        send_harvest("Science Station", item_count=2700, harvester=True, dcs=True)
        time.sleep(5)
        send_break("Science Station", item_count=10000)
        print("\n[SELESAI] Tes 1 item beres! Cek hasilnya di Discord.")
    elif mode == "2":
        delay_between = 5
        countdown(6)
        for idx, item in enumerate(ITEMS, 1):
            print(f"\n--- Item {idx}/{len(ITEMS)}: {item} (FULL BUFF) ---")
            send_harvest(item, item_count=2700, harvester=True, dcs=True)
            time.sleep(delay_between)
            send_break(item, item_count=10000)
            time.sleep(delay_between)
        print("\n[SELESAI] Semua 32 item FULL BUFF sudah terkirim!")
    elif mode == "3":
        delay_between = 5
        countdown(6)
        for idx, item in enumerate(ITEMS, 1):
            print(f"\n--- Item {idx}/{len(ITEMS)}: {item} (NO BUFF) ---")
            send_harvest(item, item_count=2700, harvester=False, dcs=False)
            time.sleep(delay_between)
            send_break(item, item_count=10000)
            time.sleep(delay_between)
        print("\n[SELESAI] Semua 32 item NO BUFF sudah terkirim!")
    else:
        print("Pilihan tidak valid.")
