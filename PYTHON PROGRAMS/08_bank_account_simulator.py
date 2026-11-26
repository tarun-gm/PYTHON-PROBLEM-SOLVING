from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal


@dataclass
class BankAccount:
    owner: str
    balance: Decimal = Decimal("0.00")
    transactions: list = field(default_factory=list)

    def _record(self, action, amount):
        self.transactions.append({
            "action": action,
            "amount": str(amount),
            "balance": str(self.balance),
            "time": datetime.now(timezone.utc).isoformat()
        })

    def deposit(self, amount):
        amount = Decimal(str(amount)).quantize(Decimal("0.01"))
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self._record("deposit", amount)

    def withdraw(self, amount):
        amount = Decimal(str(amount)).quantize(Decimal("0.01"))
        if amount <= 0 or amount > self.balance:
            raise ValueError("invalid withdrawal")
        self.balance -= amount
        self._record("withdrawal", amount)

    def statement(self):
        return list(self.transactions)


if __name__ == "__main__":
    account = BankAccount("Tarun")
    account.deposit("1500")
    account.withdraw("275.50")
    print(account.balance)
    print(account.statement())
