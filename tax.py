from __future__ import print_function
from bisect import bisect
import sys




def eprint(*argv, **kwargs):
    print (file=sys.stderr, *argv, **kwargs)

old_input = input
def input(fmt = None):
    if fmt:
        eprint(fmt)
    return old_input()

rates = [0, 2, 6, 10, 14, 17]   # 10%  20%  30%

brackets = [0, 50000, 100000, 150000, 200000]

base_tax = [0, 1000, 4000, 9000, 16000]

def single_tax(income, combined = False):

    if (combined):
        allowance = 264000
    else:
        allowance = 132000
    mpf = MPF(income)
    nci = income - mpf - allowance
    total_tax = 0
    if nci > 85200:
        if mpf >= 18000:
            eprint("You have to pay $18000 MPF.")
            pre_charge = nci - 18000
            net_charge = pre_charge - 132000
            if net_charge > 0:
                i = bisect(brackets, int(net_charge))
                if not i:
                    return i == 0
                rate = rates[i]
                bracket = brackets[i - 1]
                income_in_bracket = net_charge - bracket
                tax_in_bracket = income_in_bracket * rate / 100
                total_tax = base_tax[i - 1] + tax_in_bracket
            else:
                total_tax = 0
                eprint("You have only pay MPF, no taxation.")

        else:
            eprint("You have to pay $" + str(mpf) + " MPF.")
            pre_charge = nci - mpf
            # print(pre_charge)
            net_charge = pre_charge - 132000
            # print(net_charge)
            if net_charge > 0:
                i = bisect(brackets, int(net_charge))
                # print(i)
                if not i:
                    return i == 0
                rate = rates[i]
                # print(rate)
                bracket = brackets[i - 1]
                # print(bracket)
                income_in_bracket = net_charge - bracket
                # print(income_in_bracket)
                tax_in_bracket = income_in_bracket * rate / 100
                # print(tax_in_bracket)
                total_tax = int(base_tax[i - 1] + tax_in_bracket)
                # return total_tax

            else:
                total_tax = 0
                eprint("You have only pay MPF, no taxation.")

    else:
        total_tax = 0
        print("You have nothing to pay.")

    return total_tax

def MPF(total_income):
    total_income = int(total_income)
    if total_income < 7100 * 12:
        return 0
    return min(18000, int(total_income * 0.05))

def progressive(net_income, combined = False):
    net_charge = net_income - 132000 * (int(combined) + 1)
    if net_charge <= 0:
        return 0

    i = bisect(brackets, int(net_charge))
    if not i:
        return i == 0
    rate = rates[i]
    bracket = brackets[i - 1]
    income_in_bracket = net_charge - bracket
    tax_in_bracket = income_in_bracket * rate / 100
    total_tax = base_tax[i - 1] + tax_in_bracket
    return int(total_tax)


def standard(net_income):
    return int(net_income * 0.15)

def merried_progressive(first_income, second_income):
    eprint("*************Seperate Payment**************")
    total_mpf = MPF(first_income) + MPF(second_income)
    eprint("Total mpf: " + str(total_mpf))
    nci = (first_income + second_income) - total_mpf - 264000
    if nci > 0:
        i = bisect(brackets, int(nci))
        if not i:
            return i == 0
        rate = rates[i]
        bracket = brackets[i - 1]
        income_in_bracket = nci - bracket
        tax_in_bracket = income_in_bracket * rate / 100
        total_tax = int(base_tax[i - 1] + tax_in_bracket)
    else:
        total_tax = 0
        eprint("You have only pay MPF, no taxation.")
    return total_tax

def net_income(total_income):
    return total_income - MPF(total_income)


def single_standard(income):
    mpf = 18000
    eprint("You have to pay $18000 MPF.")
    net_charge = income - mpf
    tax = net_charge * 0.15
    eprint("Tax chargeable: ", end="")
    print (tax)

# ---------------------------------------------------------------------------------

eprint("-------------------------------------------")
eprint("              Tax Calculator")
eprint("-------------------------------------------")
status = input("Are you in Single or Married (s/m): ")
# status = ["s", "m"].index(status[0].lower())
if status == "s":
    income = int(input("What is your yearly income? "))
    eprint("-------------------------------------------")
    if income > 2022000:
        single_standard(income)
    else:
        single_tax(income)
elif status == "m":
    first_income = int(input("What is your yearly income? "))
    second_income = int(input("What is your spouse yearly income? "))
    # total_income = first_income + second_income
    # merried_progressive(first_income, second_income)
    total_incomes = [first_income, second_income]
    mpfs = list(map(MPF, total_incomes))
    eprint(mpfs)
    net_incomes = list(map(net_income, total_incomes))
    def tax(net_income):
        return min([standard(net_income), progressive(net_income)])
    individual_taxes = map(tax, net_incomes)
    values = [sum(individual_taxes), standard(sum(net_incomes)), progressive(sum(net_incomes), combined=True)]
    # eprint (values)
    total_tax = min(values)

    eprint("-------------------------------------------")
    eprint("Tax payable: ", end="")
    print(total_tax)
