from bank_lib.bank_customer import BankCustomer


class CustomerDecorator:
    def __init__(self, customer: BankCustomer):
        self.customer = customer

    def give_details(self) -> dict:
        return self.customer.give_details()


class VIPCustomer(CustomerDecorator):
    def give_details(self) -> dict:
        details = super().give_details()
        details["customer_type"] = "VIP"
        details["benefits"] = ["Priority support", "Exclusive offers"]
        return details


class CorporateCustomer(CustomerDecorator):
    def give_details(self) -> dict:
        details = super().give_details()
        details["customer_type"] = "Corporate"
        details["benefits"] = ["Dedicated account manager", "Custom solutions"]
        return details
