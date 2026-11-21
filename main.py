import os
from pathlib import Path

LINES = [
    "His hand hovered over SEND for an hour.",
    "One word would end it \u2014 sorry, or goodbye.",
    "He set the phone down, screen still lit,",
    "and went to tell her in person.",
]

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_bytes(("\n".join(LINES) + "\n").encode("utf-8"))
