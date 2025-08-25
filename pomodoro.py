
# pomodoro.py
# A Pomodoro timer you can run in your terminal.
# Pomodoro = focus for a set time, then take a short break. Repeat!
#
# How it works (simple version):
# 1) You type how many minutes to work, how many to break, and how many cycles.
# 2) The script counts down and prints the remaining time every second.
# 3) It beeps (\a) and tells you when to switch between work/break.
#
# Tips:
# - Press Ctrl+C to stop early.
# - Leave a prompt blank to use the default.

import time

def parse_int_or_default(prompt: str, default: int) -> int:
    """Ask the user for a number. If blank or invalid, use the default."""
    raw = input(f"{prompt} (default {default}): ").strip()
    if raw == "":
        print(f"Using default: {default}\n")
        return default
    try:
        value = int(raw)
        if value < 0:
            print(f"Negative values aren't allowed. Using default {default}.\n")
            return default
        return value
    except ValueError:
        print(f"That's not a whole number. Using default {default}.\n")
        return default

def countdown(seconds: int, label: str) -> None:
    """Count down from 'seconds' to 0, updating one line in the terminal."""
    try:
        while seconds >= 0:
            mins = seconds // 60
            secs = seconds % 60
            # \r returns the cursor to the beginning of the line so we overwrite it
            print(f"\r{label}: {mins:02d}:{secs:02d} remaining", end="", flush=True)
            time.sleep(1)
            seconds -= 1
    except KeyboardInterrupt:
        # Let the caller know we were interrupted
        print("\nTimer interrupted.")
        raise
    finally:
        print()  # move to a new line

def beep(times: int = 2) -> None:
    """Make a simple terminal beep (might be silent in some terminals)."""
    for _ in range(times):
        print("\a", end="", flush=True)
        time.sleep(0.2)
    print()  # newline

def main() -> None:
    print("\n=== Pomodoro Timer ===\n")
    print("A 'Pomodoro' is one work session followed by a short break.\n")

    work_mins = parse_int_or_default("Work minutes", 25)
    break_mins = parse_int_or_default("Break minutes", 5)
    cycles     = parse_int_or_default("Number of cycles", 4)

    work_seconds  = work_mins * 60
    break_seconds = break_mins * 60

    try:
        for cycle in range(1, cycles + 1):
            print(f"\nCycle {cycle}/{cycles}: Focus time!")
            countdown(work_seconds, label="Work")
            beep()
            print("Work session done. Time for a break!\n")

            # Don't do a break after the last work session
            if cycle < cycles:
                countdown(break_seconds, label="Break")
                beep()
                print("Break over. Back to work!")

        print("\nAll cycles finished — great job!\n")
    except KeyboardInterrupt:
        print("\n\nStopped early. See you next time!\n")

if __name__ == "__main__":
    main()
