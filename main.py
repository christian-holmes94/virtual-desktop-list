"""Virtual Desktop List — List Windows virtual desktops and the number of windows on the current one."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='virtual_desktop_list',
        description='List Windows virtual desktops and the number of windows on the current one.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Virtual Desktop List')
    print('Which desktop you are on.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
