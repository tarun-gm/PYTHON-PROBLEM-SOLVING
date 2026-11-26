import argparse
import re
from collections import Counter
from pathlib import Path


def word_report(path, top=20):
    text = Path(path).read_text(encoding="utf-8", errors="replace").lower()
    words = re.findall(r"[a-z]+(?:'[a-z]+)?", text)
    counts = Counter(words)
    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": counts.most_common(top),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()
    print(word_report(args.file, args.top))


if __name__ == "__main__":
    main()
