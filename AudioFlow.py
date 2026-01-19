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
        ⏩ Ctrl + Right: Skip current track.
        ⏪ Ctrl + Left: Go back to previous track.
        🔊 Ctrl + Up: Increase volume (+1, max 100).
        🔉 Ctrl + Down: Decrease volume (-1, min 0).
        ❌ Esc: Quit the player.
        """.split("\n")))
    print(f"{Fore.CYAN}", end="")
    for m in msg: print(m) if m else 1
    print(f"{Fore.BLUE}{"-"*30}")

def setting():

    path = input("Enter Path: ")
    choice = 1 if input("Listen to audio only? `YES`: ").strip().lower() == "yes" else 0

    image = (".jpg", ".png", ".jpeg")
    video = (".mp4", ".mkv", ".avi", ".mov")
    files = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if not f.lower().endswith(image)
    ]

    player = vlc.MediaPlayer()
    volume = 50
    player.audio_set_volume(volume)

    return files, None, choice, video, player, volume, [], 0

def playing(user):

    files, first_audio, choice, video, player, volume, history, pointer = user
    item = random.choice(files) if not first_audio else first_audio

    clear_screen()
    guide()
    print(f"{Fore.RED}{" "*7}🎧 Playing...\n")
    print(f"{Fore.CYAN}▶️", os.path.basename(item))

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
            return [files, first_audio, choice, video, player, volume, history, pointer]
        elif keyboard.is_pressed("ctrl+right"):
            pointer += 1
            if pointer <= len(history) - 1:
                first_audio = history[pointer]
            else: pointer = len(history); first_audio = None
            player.stop()
            print("⏩ Skipped")
            return [files, first_audio, choice, video, player, volume, history, pointer]
        elif keyboard.is_pressed("ctrl+left"):
            pointer -= 1
            pointer = min(max(0, pointer), len(history) - 1)
            first_audio = history[pointer]
            player.stop()
            print("⏩ Back")
            return [files, first_audio, choice, video, player, volume, history, pointer]
        elif keyboard.is_pressed("ctrl+up"):
            volume = min(100, volume + 1)
            player.audio_set_volume(int(volume))
            print(f"🔊 Volume: {volume}")
        elif keyboard.is_pressed("ctrl+down"):
            volume = max(0, volume - 1)
            player.audio_set_volume(int(volume))
            print(f"🔊 Volume: {volume}")
        elif keyboard.is_pressed("esc"): return 0
        time.sleep(0.1)

def main():
    clear_screen()
    user = setting()
    while user: user = playing(user)
    print(f"{Fore.CYAN}\nExiting Program... 👋")
    time.sleep(3)
main()