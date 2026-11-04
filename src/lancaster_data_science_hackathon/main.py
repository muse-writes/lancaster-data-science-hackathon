"""Skeleton main entrypoint file."""

import sys

import pandas as pd

def main() -> None:
    """Main function."""
    print( "  -- ✨ DATA SCIENCE HACKATHON ✨ --")
    print( "        Nov. 2026")
    print()
    print( " pandas version:")
    print(f"   {pd.__version__}")
    print( " Python version:")
    print(f"   {sys.version}")


if __name__ == "__main__":
    main()
