import sqlite3


class Inventory:
    def __init__(self, path="inventory.db"):
        self.path = path
        with self.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS products (sku TEXT PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL CHECK(price >= 0), quantity INTEGER NOT NULL CHECK(quantity >= 0))")

    def connect(self):
        return sqlite3.connect(self.path)

    def add_product(self, sku, name, price, quantity):
        with self.connect() as db:
            db.execute("INSERT INTO products VALUES (?, ?, ?, ?)", (sku, name, price, quantity))

    def adjust_stock(self, sku, delta):
        with self.connect() as db:
            cursor = db.execute("UPDATE products SET quantity = quantity + ? WHERE sku = ? AND quantity + ? >= 0", (delta, sku, delta))
            if cursor.rowcount != 1:
                raise ValueError("product missing or stock would become negative")

    def search(self, phrase):
        with self.connect() as db:
            return db.execute("SELECT sku, name, price, quantity FROM products WHERE name LIKE ? ORDER BY name", (f"%{phrase}%",)).fetchall()

    def inventory_value(self):
        with self.connect() as db:
            return db.execute("SELECT COALESCE(SUM(price * quantity), 0) FROM products").fetchone()[0]


if __name__ == "__main__":
    store = Inventory()
    store.add_product("KB-01", "Mechanical Keyboard", 2499, 12)
    store.adjust_stock("KB-01", -2)
    print(store.search("keyboard"))
    print(store.inventory_value())
