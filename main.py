"""Two Robots in an Elevator — entry program.

Writes one line of awkward robot small talk to the file the sealed
scorer reads. The line is a proximity-sensor complaint overruled by
a politeness subroutine: machine logic showing through forced
courtesy, in a lift neither robot wants to make weird.
"""

import os
import sys

ELEVATOR_LINE = "So… my proximity sensor says we're standing too close, but my politeness subroutine says mentioning it would be worse."

GATE_MAX_CHARS = 200


def line_passes_gate(line):
    """A valid entry is 1 to 200 characters of UTF-8 text that is not
    only whitespace, written as a single line. The gate counts
    characters, so the check is on the string itself, not its bytes."""
    if not line or len(line) > GATE_MAX_CHARS:
        return False
    if not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def entry_file_inside(folder):
    """The entry file inside an output directory is entry.txt."""
    return os.path.join(folder, "entry.txt")


def pick_output_file():
    """ENTRY_OUT names the output file, or a directory whose entry
    file is entry.txt; ENTRY_OUT_DIR names such a directory; with
    neither set, the scorer's default /output/entry.txt is used."""
    target = os.environ.get("ENTRY_OUT")
    if target:
        if os.path.isdir(target):
            return entry_file_inside(target)
        return target
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        return entry_file_inside(folder)
    return "/output/entry.txt"


def save_entry_text(path, line):
    """Write exactly the line as UTF-8 with no trailing newline,
    creating parent directories when they are missing."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    if not line_passes_gate(ELEVATOR_LINE):
        print("entry line fails the gate", file=sys.stderr)
        return 1
    destination = pick_output_file()
    save_entry_text(destination, ELEVATOR_LINE)
    print(ELEVATOR_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
