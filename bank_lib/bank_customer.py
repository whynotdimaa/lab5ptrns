from dataclasses import dataclass
from typing import Dict
from bank_lib.bank_info import BankInfo


@dataclass
class PersonalInfo:
    name: str
    age: int
    address: str


class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self) -> dict:
        transactions = {
            acc: self.bank_details.transaction_list(acc)
            for acc in self.bank_details.accounts_number
        }
        return {
            "personal_info": {
                "name": self.personal_info.name,
                "age": self.personal_info.age,
                "address": self.personal_info.address,
            },
            "bank_details": {
                "bank_name": self.bank_details.bank_name,
                "holder_name": self.bank_details.holder_name,
                "accounts_number": self.bank_details.accounts_number,
                "credit_history": self.bank_details.credit_history,
                "transactions": transactions
            }
        }
