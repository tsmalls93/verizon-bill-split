import re

def split_bill(tyler, daniel, mom, plan, surcharge, tax, one_time, credit, balance_forward):
    split_costs = (plan + surcharge + tax + one_time - credit + balance_forward) / 3
    tyler_cost = tyler + split_costs
    daniel_cost = daniel + split_costs
    mom_cost = mom + split_costs
    print("Tyler owes: " + str(as_currency(tyler_cost)))
    print("Daniel owes: " + str(as_currency(daniel_cost)))
    print("Mom owes: " + str(as_currency(mom_cost)))

def my_cost(phone, plan, surcharge, tax, one_time, credit, balance_forward):
    split_costs = (plan + surcharge + tax + one_time - credit + balance_forward) / 3
    return phone + split_costs

def as_currency(amount):
    return '${:,.2f}'.format(amount)

def validate(amount):
    while (not bool(re.match("^[-0-9.]*$", amount))):
        amount = raw_input("Try again: $")
    return amount

print("Welcome To Tyler's Verizon Bill Splitter")
choice = raw_input("Would you like to see what everybody owes (Enter 1) or just what you owe (Enter 2)? ")
while choice != "1" and choice != "2":
    choice = raw_input("Try again...Would you like to see what everybody owes (Enter 1) or just what you owe (Enter 2)? ")
print("Notice: The last person to pay may have to pay an extra cent depending on the amount for the charges we split since we cannot each pay a third of a cent")
if choice == '1':
    confirm = 'n'
    while confirm == 'n':
        tyler = float(validate(raw_input("Enter Tyler's phone cost: $")))
        daniel = float(validate(raw_input("Enter Daniel's phone cost: $")))
        mom = float(validate(raw_input("Enter Mom's phone cost: $")))
        plan = float(validate(raw_input("Enter plan cost: $")))
        surcharge = float(validate(raw_input("Enter surcharge: $")))
        tax = float(validate(raw_input("Enter tax: $")))
        one_time = float(validate(raw_input("Enter one-time charges: $")))
        credit = float(validate(raw_input("Enter credits: $")))
        balance_forward = float(validate(raw_input("Enter balance forward: $")))
        total = tyler + daniel + mom + plan + surcharge + tax + one_time + balance_forward - credit
        confirm = raw_input("Confirm " + str(as_currency(total)) + " is the correct total (y/n): ")
    split_bill(tyler, daniel, mom, plan, surcharge, tax, one_time, credit, balance_forward)
elif choice == '2':
    phone = float(validate(raw_input("Enter phone cost: $")))
    plan = float(validate(raw_input("Enter plan cost: $")))
    surcharge = float(validate(raw_input("Enter surcharge: $")))
    tax = float(validate(raw_input("Enter tax: $")))
    one_time = float(validate(raw_input("Enter one-time charges: $")))
    credit = float(validate(raw_input("Enter credits: $")))
    balance_forward = float(validate(raw_input("Enter balance forward: $")))
    print(str(as_currency(my_cost(phone, plan, surcharge, tax, one_time, credit, balance_forward))))
    