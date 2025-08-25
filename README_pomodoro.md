
# Pomodoro Timer

A **Pomodoro** timer you run in your terminal.
Pomodoro = focus for a set time, then take a short break. Repeat!

## Features
- Simple text prompts (leave blank for defaults)
- Clear countdown in `MM:SS`
- Little beep and message at the end of each session
- Press `Ctrl + C` any time to stop

## Quickstart

1. **Check you have Python 3.** In a terminal run:
   ```bash
   python --version
   # or on some systems
   python3 --version
   ```
2. **Download** `pomodoro.py` to a folder you like.
3. **Run** it:
   ```bash
   # Windows (often)
   python pomodoro.py

   # macOS / Linux (often)
   python3 pomodoro.py
   ```
4. **Enter values** when prompted, or press Enter to accept defaults (25/5 minutes, 4 cycles).

## Notes
- The beep uses the terminal bell (`\a`). Some terminals keep it silent by default.
