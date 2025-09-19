import getpass


class BankAccount:
    def __init__(self, owner: str, pin: str, balance: int = 0) -> None:
        self.owner = owner
        self._pin = pin
        self.balance = balance

    def check_pin(self, pin: str) -> bool:
        return pin == self._pin

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak")
        if amount > self.balance:
            raise ValueError("Hisobda yetarli mablag' yo'q")
        self.balance -= amount


def menu() -> None:
    account = BankAccount(owner="Foydalanuvchi", pin="1234", balance=100_000)
    print("Bankomat simulyatori. Standart PIN: 1234")
    tries = 3
    while tries:
        pin = getpass.getpass("PIN kiriting: ")
        if account.check_pin(pin):
            break
        tries -= 1
        print(f"Noto'g'ri PIN. Qolgan urinishlar: {tries}")
    else:
        print("Kirish bloklandi.")
        return

    while True:
        print("\n1) Balans  2) Pul qo'yish  3) Pul yechish  4) Chiqish")
        choice = input("Tanlov: ").strip()
        try:
            if choice == "1":
                print(f"Balans: {account.balance} so'm")
            elif choice == "2":
                amount = int(input("Miqdor: "))
                account.deposit(amount)
                print("Pul qo'yildi.")
            elif choice == "3":
                amount = int(input("Miqdor: "))
                account.withdraw(amount)
                print("Pul yechildi.")
            elif choice == "4":
                print("Chiqildi.")
                break
            else:
                print("Noto'g'ri tanlov.")
        except ValueError as ex:
            print("Xato:", ex)


if __name__ == "__main__":
    menu()


