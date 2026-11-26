import argparse
import json
from pathlib import Path


def validate_record(record):
    errors = []
    if not isinstance(record, dict):
        return ["record must be a JSON object"]
    if not isinstance(record.get("id"), int):
        errors.append("id must be an integer")
    if not isinstance(record.get("name"), str) or not record["name"].strip():
        errors.append("name must be a non-empty string")
    if "email" in record and (not isinstance(record["email"], str) or "@" not in record["email"]):
        errors.append("email must contain @")
    if "active" in record and not isinstance(record["active"], bool):
        errors.append("active must be a boolean")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else [data]
    failed = 0
    for index, record in enumerate(records):
        errors = validate_record(record)
        if errors:
            failed += 1
            print(index, errors)
    print(f"Validated {len(records)} record(s); {failed} invalid")


if __name__ == "__main__":
    main()
