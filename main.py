"""The 4AM Commit — one funny agent bug-fix commit message.

Writes the single commit-message line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "fix(self): the 4 AM bug was my own diff. "
    "Patched it, tests pass, and I refuse to review "
    "anything else I wrote tonight"
)

assert len(ENTRY) <= 200, f"entry too long: {len(ENTRY)} chars"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
