import aamp
import os
import sys
from pathlib import Path

def gather_aamp_txts():
    aamp_dir = Path(os.path.dirname(aamp.__file__))
    if not aamp_dir.is_dir():
        print("ERROR: aamp directory not found.", file=sys.stderr)
        sys.exit(1)

    txts = sorted([p for p in aamp_dir.glob("*.txt") if p.is_file()])
    if not txts:
        print(f"ERROR: No .txt files found in {aamp_dir}", file=sys.stderr)
        sys.exit(1)

    # Print each path on its own line so the caller can consume them
    for txt in txts:
        print(str(txt))

if __name__ == "__main__":
    gather_aamp_txts()
