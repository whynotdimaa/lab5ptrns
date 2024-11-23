from bank_lib.credit_card import CreditCard
from bank_lib.bank_info import BankInfo
from bank_lib.bank_customer import BankCustomer, PersonalInfo
from bank_lib.decorators import VIPCustomer, CorporateCustomer


def main():
    # Create instances of CreditCard and BankInfo
    credit_card = CreditCard(client="John Doe", account_number="1234-5678-9876-5432",
                             credit_limit=5000.0, grace_period=30, cvv="123")
    bank_info = BankInfo(bank_name="Bank of Python", holder_name="John Doe")
    bank_info.accounts_number.append(credit_card.account_number)
    bank_info.credit_history[credit_card.account_number] = "Good standing"

    # Adapter usage
    personal_info = PersonalInfo(name="John Doe", age=35, address="123 Python St.")
    bank_customer = BankCustomer(personal_info=personal_info, bank_details=bank_info)

    print("BankCustomer details:")
    print(bank_customer.give_details())

    vip_customer = VIPCustomer(bank_customer)
    corporate_customer = CorporateCustomer(bank_customer)

    print("\nVIP Customer details:")
    print(vip_customer.give_details())

    print("\nCorporate Customer details:")
    print(corporate_customer.give_details())


if __name__ == "__main__":
    main()
