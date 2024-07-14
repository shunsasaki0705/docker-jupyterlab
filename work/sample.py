import math
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python sample.py <number>")
        sys.exit(1)

    try:
        val = float(sys.argv[1])
        print(f"The provided value is {val}")
    except ValueError:
        print("Please provide a valid number.")
        sys.exit(1)

if __name__ == "__main__":
  main()