import hashlib
from pathlib import Path
from collections import defaultdict


def digest(path, chunk_size=1024 * 1024):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            result.update(chunk)
    return result.hexdigest()


def find_duplicates(folder):
    candidates = defaultdict(list)
    for path in Path(folder).rglob("*"):
        if path.is_file():
            candidates[path.stat().st_size].append(path)
    duplicates = []
    for same_size in candidates.values():
        if len(same_size) < 2:
            continue
        by_hash = defaultdict(list)
        for path in same_size:
            by_hash[digest(path)].append(str(path))
        duplicates.extend(group for group in by_hash.values() if len(group) > 1)
    return duplicates


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    args = parser.parse_args()
    for group in find_duplicates(args.folder):
        print("\n".join(group))
        print()
