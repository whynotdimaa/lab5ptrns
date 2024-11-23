from typing import List


class BankInfo:
    def __init__(self, bank_name: str, holder_name: str):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = []
        self.credit_history = {}

    def transaction_list(self, account_number: str) -> List[str]:
        return [f"Transaction {i} for {account_number}" for i in range(1, 6)]
