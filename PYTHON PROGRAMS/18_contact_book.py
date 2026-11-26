import json
from pathlib import Path


class ContactBook:
    def __init__(self, path="contacts.json"):
        self.path = Path(path)
        self.contacts = json.loads(self.path.read_text()) if self.path.exists() else {}

    def save(self):
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(json.dumps(self.contacts, indent=2), encoding="utf-8")
        temporary.replace(self.path)

    def add(self, name, phone, email=""):
        key = name.strip().casefold()
        if not key or not phone.strip():
            raise ValueError("name and phone are required")
        if key in self.contacts:
            raise ValueError("contact already exists")
        self.contacts[key] = {"name": name.strip(), "phone": phone.strip(), "email": email.strip()}
        self.save()

    def search(self, phrase):
        phrase = phrase.casefold()
        return [item for key, item in self.contacts.items() if phrase in key or phrase in item["phone"]]

    def delete(self, name):
        removed = self.contacts.pop(name.casefold(), None)
        if removed is not None:
            self.save()
        return removed is not None


if __name__ == "__main__":
    book = ContactBook()
    print("Contact book loaded:", len(book.contacts))
    print("Use ContactBook.add(), search(), and delete() from Python.")
