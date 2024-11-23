from flask import Flask, request, jsonify
from bank_lib.credit_card import CreditCard
from bank_lib.bank_info import BankInfo
from bank_lib.bank_customer import BankCustomer, PersonalInfo
from bank_lib.decorators import VIPCustomer, CorporateCustomer
app = Flask(__name__)

# Mock data
credit_card = CreditCard(client="John Doe", account_number="1234-5678-9876-5432",
                         credit_limit=5000.0, grace_period=30, cvv="123")
bank_info = BankInfo(bank_name="Bank of Python", holder_name="John Doe")
bank_info.accounts_number.append(credit_card.account_number)
bank_info.credit_history[credit_card.account_number] = "Good standing"
personal_info = PersonalInfo(name="John Doe", age=35, address="123 Python St.")
bank_customer = BankCustomer(personal_info=personal_info, bank_details=bank_info)

@app.route('/customer/details', methods=['GET'])
def get_customer_details():
    return jsonify(bank_customer.give_details())

@app.route('/customer/vip', methods=['GET'])
def get_vip_customer_details():
    vip_customer = VIPCustomer(bank_customer)
    return jsonify(vip_customer.give_details())

@app.route('/customer/corporate', methods=['GET'])
def get_corporate_customer_details():
    corporate_customer = CorporateCustomer(bank_customer)
    return jsonify(corporate_customer.give_details())

if __name__ == '__main__':
    app.run(debug=True)
