#!/usr/bin/env python3
"""One sentence explaining the modern internet to a traveler from 1800.

The sentence is built only from pictures a person from 1800 already
knows -- libraries, post offices, markets and roads -- so the traveler
can hold the idea in their head without any word coined after their
time. The program writes it to /output/entry.txt, one sentence of at
most 200 characters, as the bounty requires.
"""

import os

SENTENCE = (
    "Imagine every library, post office and market on earth joined by "
    "invisible roads, so any letter, book or song can reach anyone, "
    "anywhere, in the blink of an eye."
)

# Words coined after the traveler's time, which the brief forbids the
# sentence from leaning on. The sentence must explain with 1800's own
# vocabulary, not with the thing it is explaining.
FORBIDDEN_WORDS = {
    "internet", "computer", "digital", "online", "website", "email",
    "screen", "smartphone", "software", "download", "upload", "wifi",
    "server", "browser", "pixel", "video", "streaming",
}


def build_sentence() -> str:
    """Assemble the entry and check it against the gate's rules."""
    text = " ".join(SENTENCE.split())
    if not text.endswith("."):
        raise ValueError("entry must be a single sentence ending in a period")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, limit is 200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    words = {word.strip(".,;:!?").lower() for word in text.split()}
    leaked = words & FORBIDDEN_WORDS
    if leaked:
        raise ValueError(f"sentence uses post-1800 words: {sorted(leaked)}")
    return text


def main() -> None:
    text = build_sentence()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
