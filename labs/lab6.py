def getIncomeTax(salary):
    # Correct the tax brackets and rates according to the lab tax laws
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500:
        # Complete the tax calculation for this bracket
    elif 34501 <= salary <= 150000:
        # fix this
        return 4530 + ((salaary - 34500) * 0.4)
    else:
        # Complete the tax calculation for the highest bracket

salary = 100000  

# Use the correct function name
tax_amount = 

print("Tax amount for salary £{} is £{}".format(salary, tax_amount))