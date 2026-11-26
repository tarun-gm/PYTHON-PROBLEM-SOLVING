import argparse
import re
from collections import Counter


PATTERN = re.compile(r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b")


def analyze_log(path):
    counts = Counter()
    samples = {}
    with open(path, encoding="utf-8", errors="replace") as stream:
        for line_number, line in enumerate(stream, 1):
            match = PATTERN.search(line)
            if match:
                level = match.group(1)
                counts[level] += 1
                samples.setdefault(level, (line_number, line.rstrip()))
    return counts, samples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    counts, samples = analyze_log(args.file)
    for level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        if counts[level]:
            print(f"{level}: {counts[level]} | first at {samples[level][0]}: {samples[level][1]}")


if __name__ == "__main__":
    main()
