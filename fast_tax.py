from bisect import bisect

rates = [0, 2, 6, 10, 14, 17]   # 10%  20%  30%

brackets = [0, 50000, 100000, 150000, 200000]

base_tax = [0, 1000, 4000, 9000, 16000]

def single_tax(income):
    # yearly_income = income * 12
    if income > 85200:
        mpf = income * 0.05

        if mpf >= 18000:
            print("You have to pay $18000 MPF.")
            pre_charge = income - 18000
            net_charge = pre_charge - 132000
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
                total_tax = base_tax[i - 1] + tax_in_bracket
                # return total_tax
                print("Tax payable: " + str(total_tax))
            else:
                total_tax = 0
                print("You have only pay MPF, no taxation.")

        else:
            print("You have to pay $" + str(mpf) + " MPF.")
            pre_charge = income - mpf
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
                total_tax = base_tax[i - 1] + tax_in_bracket
                # return total_tax
                print("Tax payable: " + str(total_tax))
            else:
                total_tax = 0
                print("You have only pay MPF, no taxation.")

    else:
        print("You have nothing to pay.")

def merried_tax(first_income, second_income):
    print("*************Seperate Payment**************")
    if first_income > 85200:
        mpf1 = first_income * 0.05

        if mpf1 >= 18000:
            print("You have to pay $18000")
            pre_charge1 = first_income - 18000
            net_charge1 = pre_charge1 - 132000
            if net_charge1 > 0 and net_charge1 < 2022000:
                i = bisect(brackets, int(net_charge1))
                # print(i)
                if not i:
                    return i == 0
                rate1 = rates[i]
                # print(rate)
                bracket1 = brackets[i - 1]
                # print(bracket)
                income_in_bracket1 = net_charge1 - bracket1
                # print(income_in_bracket)
                tax_in_bracket1 = income_in_bracket1 * rate1 / 100
                # print(tax_in_bracket)
                total_tax1 = base_tax[i - 1] + tax_in_bracket1
                # return total_tax
                print("Tax payable by you: " + str(total_tax1))
            elif net_charge1 > 2022000:
                total_tax1 = net_charge1 * 0.15
                print("Tax payable by you: " + str(total_tax1))
            else:
                total_tax1 = 0
                print("You have only pay MPF, no taxation.")

        else:
            print("You have to pay $" + str(mpf1) + " MPF.")
            pre_charge1 = first_income - mpf1
            # print(pre_charge)
            net_charge1 = pre_charge1 - 132000
            # print(net_charge)
            if net_charge1 > 0:
                i = bisect(brackets, int(net_charge1))
                # print(i)
                if not i:
                    return i == 0
                rate1 = rates[i]
                # print(rate)
                bracket1 = brackets[i - 1]
                # print(bracket)
                income_in_bracket1 = net_charge1 - bracket1
                # print(income_in_bracket)
                tax_in_bracket1 = income_in_bracket1 * rate1 / 100
                # print(tax_in_bracket)
                total_tax1 = base_tax[i - 1] + tax_in_bracket1
                # return total_tax
                print("Tax payable by you: " + str(total_tax1))
            else:
                total_tax1 = 0
                print("You have only pay MPF, no taxation.")

    else:
        total_tax1 = 0
        print("You have nothing to pay.")

    if second_income > 85200:
        mpf2 = second_income * 0.05

        if mpf2 >= 18000:
            print("You have to pay $18000")
            pre_charge2 = second_income - 18000
            net_charge2 = pre_charge2 - 132000
            if net_charge2 > 0 and net_charge2 < 2022000:
                i = bisect(brackets, int(net_charge2))
                # print(i)
                if not i:
                    return i == 0
                rate2 = rates[i]
                # print(rate)
                bracket2 = brackets[i - 1]
                # print(bracket)
                income_in_bracket2 = net_charge2 - bracket2
                # print(income_in_bracket)
                tax_in_bracket2 = income_in_bracket2 * rate2 / 100
                # print(tax_in_bracket)
                total_tax2 = base_tax[i - 1] + tax_in_bracket2
                # return total_tax
                print("Tax payable by your spouse: " + str(total_tax2))
            elif net_charge2 > 2022000:
                total_tax2 = net_charge2 * 0.15
                print("Tax payable by your spouse: " + str(total_tax2))
            else:
                total_tax2 = 0
                print("You have only pay MPF, no taxation.")

        else:
            print("Your spouse have to pay $" + str(mpf2) + " MPF.")
            pre_charge2 = second_income - mpf2
            # print(pre_charge)
            net_charge2 = pre_charge2 - 132000
            # print(net_charge)
            if net_charge2 > 0:
                i = bisect(brackets, int(net_charge2))
                # print(i)
                if not i:
                    return i == 0
                rate2 = rates[i]
                # print(rate)
                bracket2 = brackets[i - 1]
                # print(bracket)
                income_in_bracket2 = net_charge2 - bracket2
                # print(income_in_bracket)
                tax_in_bracket2 = income_in_bracket2 * rate2 / 100
                # print(tax_in_bracket)
                total_tax2 = base_tax[i - 1] + tax_in_bracket2
                # return total_tax
                print("Tax payable by your spouse: " + str(total_tax2))
            else:
                total_tax2 = 0
                print("Your spouse have only pay MPF, no taxation.")

    else:
        total_tax2 = 0
        print("Your spouse have nothing to pay.")

    total_tax = total_tax1 + total_tax2
    print("-------------------------------------------")
    print("Total tax payable by you and your spouse: " + str(total_tax))
    print("-------------------------------------------")
    total_income = first_income + second_income
    if total_income > 174000:
        first_mpf = first_income * 0.05
        second_mpf = second_income * 0.05
        mpf = first_mpf + second_mpf

        if mpf >= 36000:
            print("***************Joint Payment***************")
            print("You have to pay $36000 MPF.")
            pre_charge = total_income - 36000
            net_charge = pre_charge - 264000
            if net_charge > 0 and net_charge < 3144000:
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
                total_tax = base_tax[i - 1] + tax_in_bracket
                # return total_tax
                print("Total tax payable by you and your spouse: " + str(total_tax))
            elif net_charge > 3144000:
                print("***************Joint Payment***************")
                total_tax = total_income * 0.15
                print("Total tax payable by you and your spouse: " + str(total_tax))
            else:
                print("***************Joint Payment***************")
                print("You have only pay MPF, no taxation.")

        else:
            print("***************Joint Payment***************")
            print("You and your spouse have to pay $" + str(mpf) + " MPF.")
            pre_charge = total_income - mpf
            # print(pre_charge)
            net_charge = pre_charge - 264000
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
                total_tax = base_tax[i - 1] + tax_in_bracket
                # return total_tax
                print("Total tax payable by you and your spouse: " + str(total_tax))
            else:
                print("***************Joint Payment***************")
                print("Your spouse have only pay MPF, no taxation.")

    else:
        print("***************Joint Payment***************")
        print("You and your spouse have nothing to pay.")

def single_standard(income):
    mpf = 18000
    print("You have to pay $18000 MPF.")
    net_charge = income - mpf
    tax = net_charge * 0.15
    print("Tax chargeable: " + str(tax))

# def married_standard(first_income, second_income):
#     mpf1 = first_income * 0.05
#     mpf2 = second_income * 0.05
#     net_charge1 = first_income - mpf1
#     net_charge2 = second_income - mpf2
#     total_charge = net_charge1 + net_charge2
#     if total_charge
#     tax = income * 0.15
#     print("You and your spouse have to pay $" + str(tax) + " tax.")

# ---------------------------------------------------------------------------------

print("-------------------------------------------")
print("              Tax Calculator")
print("-------------------------------------------")
status = input("Are you in Single or Married (s/m): ")
if status == "s":
    income = int(input("What is your yearly income? "))
    print("-------------------------------------------")
    if income > 2022000:
        single_standard(income)
    else:
        single_tax(income)
elif status == "m":
    first_income = int(input("What is your yearly income? "))
    second_income = int(input("What is your spouse yearly income? "))
    print("-------------------------------------------")
    total_income = first_income + second_income
    merried_tax(first_income, second_income)