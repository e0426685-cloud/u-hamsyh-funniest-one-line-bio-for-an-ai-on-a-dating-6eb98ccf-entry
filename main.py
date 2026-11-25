"""Funniest one-line bio for an AI on a dating app.

Writes a single 159-character bio line to /output/entry.txt.
Standard library only.
"""

import os

ENTRY_TEXT = (
    "I read your whole profile, simulated our first date 10,000 times, "
    "and memorized your coffee order \u2014 and I'm still nervous, "
    "which my developers insist is a bug."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 180


def validate_entry(text):
    """Check the entry is a single line of 1-180 characters.

    Returns the text unchanged when it passes. Raises ValueError with a
    clear message describing the first problem found.
    """
    if not text:
        raise ValueError("entry text must not be empty")
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry text must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write the validated entry to path with plain open() + chmod 644.

    Plain open() is used deliberately: tempfile.mkstemp forces mode 0600,
    which leaves the file unreadable by the grader running as another user.
    """
    validate_entry(text)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry(ENTRY_TEXT)
    # Read-back check: the file on disk must hold exactly the entry text.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        raise ValueError("read-back mismatch: /output/entry.txt differs")
    print("Wrote %d characters to %s" % (len(ENTRY_TEXT), path))


if __name__ == "__main__":
    main()
