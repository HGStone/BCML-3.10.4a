import aamp
import rstb
import os
import sys
from pathlib import Path

def gather_files_from_pkg(pkg_module, patterns):
    base = Path(os.path.dirname(pkg_module.__file__))
    found = []
    for pat in patterns:
        for p in base.glob(pat):
            if p.is_file():
                found.append(str(p))
    return found

def main():
    all_files = []

    # aamp: .txt data files
    try:
        aamp_files = gather_files_from_pkg(aamp, ["*.txt"])
        if not aamp_files:
            print(f"WARNING: no .txt files found in aamp at {os.path.dirname(aamp.__file__)}", file=sys.stderr)
        all_files.extend(aamp_files)
    except ImportError:
        print("ERROR: aamp not installed or not found.", file=sys.stderr)
        sys.exit(1)

    # rstb: TSV/TXT data files
    try:
        rstb_files = gather_files_from_pkg(rstb, ["*.tsv", "*.txt"])
        if not rstb_files:
            print(f"WARNING: no TSV/TXT files found in rstb at {os.path.dirname(rstb.__file__)}", file=sys.stderr)
        all_files.extend(rstb_files)
    except ImportError:
        print("ERROR: rstb not installed or not found.", file=sys.stderr)
        sys.exit(1)

    if not all_files:
        print("ERROR: no runtime data files collected.", file=sys.stderr)
        sys.exit(1)

    for f in sorted(set(all_files)):
        print(f.strip())

if __name__ == "__main__":
    main()
