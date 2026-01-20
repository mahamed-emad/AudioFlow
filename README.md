# 🎵 AudioFlow
AudioFlow – Stay in the work flow and get things done while enjoying podcasts, Qur'an, or music.

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**A minimalist media player that keeps you focused while working – Listen to podcasts, Qur'an, or music without interrupting your workflow**

</div>

---

## 🌟 Overview

**AudioFlow** is a lightweight, keyboard-driven media player designed for professionals and students who want to stay productive while enjoying audio content. Whether you're coding, writing, or studying, AudioFlow plays your favorite podcasts, Qur'an recitations, or music in the background without disrupting your focus.

## ✨ Features

- 🎧 **Audio-Only Mode** - Play video files with audio only, saving system resources
- ⌨️ **Keyboard Controls** - Full control without touching the mouse using backtick (`) modifier
- ⏸️ **Pause/Resume** - Pause and resume playback without losing your place
- 🔀 **Smart Playback** - Random playback with intelligent history tracking
- 📂 **Auto-Discovery** - Automatically finds all audio and video files in your folder
- 🎚️ **Volume Control** - Precise volume adjustment with instant visual feedback
- 🕒 **Navigation History** - Go back and forth through your listening history
- 🎨 **Clean Interface** - Minimal, distraction-free terminal UI with smart file name display
- 🇵🇸 **Free Palestine Support** - Built with love and solidarity

## 📋 Requirements

- **Operating System:** Windows, Linux, or macOS
- **Python:** Version 3.8 or higher
- **Required Libraries:**
  - `python-vlc`
  - `keyboard`
  - `colorama`

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mahamed-Emad/AudioFlow.git
cd AudioFlow
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** You'll also need VLC Media Player installed on your system:
- **Windows:** Download from [videolan.org](https://www.videolan.org/vlc/)
- **Linux:** `sudo apt install vlc` (Ubuntu/Debian) or `sudo dnf install vlc` (Fedora)
- **macOS:** `brew install --cask vlc`

### 3️⃣ Run the Application

```bash
python audioflow.py
```

## 🎮 Keyboard Controls

| Shortcut | Action |
|----------|--------|
| **` + Space** | ⏸️ Pause/Resume current track |
| **` + Right** | ⏩ Skip to next track |
| **` + Left** | ⏪ Go back to previous track |
| **` + Up** | 🔊 Increase volume (+1) |
| **` + Down** | 🔉 Decrease volume (-1) |
| **` + Esc** | ❌ Quit the player |

**Note:** The backtick (`) key is located above Tab and to the left of the number 1 on most keyboards.

## 📁 Project Structure

```
AudioFlow/
│
├── audioflow.py          # Main application
├── icon.ico              # Project icon
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 📦 requirements.txt Content

```txt
python-vlc>=3.0.0
keyboard>=0.13.5
colorama>=0.4.6
```

## 🎯 How to Use

1. **Run AudioFlow** using the command above
2. **Enter the folder path** containing your audio/video files
3. **Choose audio-only mode** (type "yes") or press Enter to skip for full playback
4. **Use keyboard shortcuts** to control playback
5. **Stay focused** on your work while enjoying your content!

### 📂 Supported File Formats

**Audio:** MP3, WAV, OGG, FLAC  
**Video:** MP4, MKV, AVI, MOV

## 🏷️ Releases

### v1.0.0 - First Release

**Release Date:** January 2026

**Features:**
- ✅ Audio-only mode for video files
- ✅ Keyboard-driven navigation with backtick (`) modifier
- ✅ Pause/Resume functionality with instant feedback
- ✅ Volume control with real-time display
- ✅ Playback history with back/forward navigation
- ✅ Random file selection
- ✅ Smart file name truncation for clean display
- ✅ Clean, colorful terminal interface
- ✅ Support for multiple audio/video formats
- ✅ Error handling with retry mechanism for empty folders
- ✅ VLC quiet mode to suppress unnecessary messages

## 💡 Use Cases

- 🧑‍💻 **Developers:** Listen to podcasts while coding
- 📚 **Students:** Play Qur'an or focus music while studying
- ✍️ **Writers:** Enjoy background audio during writing sessions
- 🎨 **Designers:** Stay in the flow with your favorite playlists
- 🏢 **Remote Workers:** Maintain productivity with ambient audio

## 🔧 Build Executable (Optional)

To create a standalone executable file that doesn't require Python:

```bash
pip install pyinstaller
pyinstaller --onefile --icon="icon.ico" audioflow.py
```

The executable will be created in the `dist/` folder.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Bug Reports & Feature Requests

If you encounter any issues or have suggestions for new features, please open an issue on GitHub.

## 🙏 Acknowledgments

- Built with [python-vlc](https://github.com/oaubert/python-vlc) for media playback
- Inspired by the need to stay focused while working
- Made with the intention to help others maintain their productivity

## 👨‍💻 Developer

<div align="center">

**Made With Love ❤️ By Mahamed Emad**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=social&logo=github)](https://github.com/Mahamed-Emad)

</div>

---

<div align="center">

### ⭐ If you like this project, don't forget to give it a star!

**Stay in the flow. Get things done. 🎵**

</div>
