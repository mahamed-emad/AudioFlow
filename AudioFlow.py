from colorama import Fore
import os, random, vlc, keyboard, time, platform

def clear_screen():
    system_name = platform.system().lower()
    os.system("cls" if system_name == "windows" else "clear")
    print(f"{Fore.BLUE}{"-"*30}")
    print(f"{Fore.GREEN}{" "*6}Free Palestine") # 🇵🇸
    print(f"{Fore.RED}{" "*2}Dev By ❤️ Mahamed Emad")
    print(f"{Fore.BLUE}{"-"*30}")

def guide():
    msg = list(map(str.strip, """
        ⏸️ ` + Space: Stop track.
        ⏩ ` + Right: Skip track.
        ⏪ ` + Left: back previous track.
        🔊 ` + Up: Increase volume +1.
        🔉 ` + Down: Decrease volume -1.
        ❌ ` + Esc: Quit the player.
        """.split("\n")))
    print(f"{Fore.CYAN}", end="")
    for m in msg: print(m) if m else 1
    print(f"{Fore.BLUE}{"-"*30}")

def setting():

    path = input("Enter Path: ")
    choice = 1 if input("Listen to audio only? `YES`: ").strip().lower() == "yes" else 0

    video = (".mp4", ".mkv", ".avi", ".mov")
    audio = (".mp3", ".wav", ".ogg", ".flac")
    try:
        files = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith(video + audio)
        ]
        if not files: assert ""

        player = vlc.MediaPlayer("--quiet")
        volume = 50
        player.audio_set_volume(volume)
        vlc.Instance("--quiet")
        return True, files, None, choice, video, player, volume, [], 0, 0
    except: return ["empty"]

def screen(item):
    clear_screen()
    guide()
    print(f"{Fore.RED}{" "*7}🎧 Playing...\n")
    name = os.path.basename(item)
    print(f"{Fore.CYAN}▶️", name if len(name) <= 20 else name[:20] + "...")

def playing(user):

    order, files, first_audio, choice, video, player, volume, history, pointer, last_oper = user
    if order == "empty": return [order]
    item = random.choice(files) if not first_audio else first_audio

    screen(item)
    if last_oper: print(last_oper)

    media = vlc.Media(item)
    if item.lower().endswith(video) and choice: media.add_option(":no-video")
    player.set_media(media)

    if pointer == len(history) or history[pointer] != item:
        if pointer == len(history): pointer += 1
        history.append(item)

    player.play()
    time.sleep(0.1)

    while True:
        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Stopped, vlc.State.Error]: 
            pointer = len(history); first_audio = False
            return [order, files, first_audio, choice, video, player, volume, history, pointer, last_oper]
        elif keyboard.is_pressed(41) and keyboard.is_pressed("right"):
            pointer += 1
            if pointer <= len(history) - 1:
                first_audio = history[pointer]
            else: pointer = len(history); first_audio = None
            player.stop()
            screen(item)
            last_oper = "⏩ Skipped"
            return [order, files, first_audio, choice, video, player, volume, history, pointer, last_oper]
        elif keyboard.is_pressed(41) and keyboard.is_pressed("left"):
            pointer -= 1
            pointer = min(max(0, pointer), len(history) - 1)
            first_audio = history[pointer]
            player.stop()
            screen(item)
            last_oper = "⏩ Back"
            return [order, files, first_audio, choice, video, player, volume, history, pointer, last_oper]
        elif keyboard.is_pressed(41) and keyboard.is_pressed("up"):
            volume = min(100, volume + 1)
            player.audio_set_volume(int(volume))
            print(f"\r🔊 Volume: {volume}", end=" ", flush=True)
        elif keyboard.is_pressed(41) and keyboard.is_pressed("down"):
            volume = max(0, volume - 1)
            player.audio_set_volume(int(volume))
            print(f"\r🔊 Volume: {volume}", end=" ", flush=True)
        elif keyboard.is_pressed(41) and keyboard.is_pressed("space"):
            if player.is_playing():
                player.pause()
                print("\r⏸️ Paused", end=" ", flush=True)
            else:
                player.play()
                print("\r▶️ Resumed", end=" ", flush=True)
        elif keyboard.is_pressed(41) and keyboard.is_pressed("esc"):
            player.pause()
            return [0]
        time.sleep(0.2)

while True:
    clear_screen()
    user = setting()
    while user[0] is True: user = playing(user)
    clear_screen()
    msg_empty = "❌ No media found ❌\n-Type `YES` to another path: "
    if user[0] == "empty" and input(msg_empty).strip().lower() in ["y", "yes"]: continue
    print(f"{Fore.CYAN}\n    Exiting Program... 👋\n\n\n")
    time.sleep(3)
    break
