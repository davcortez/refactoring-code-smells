class TaxCalculator:
    def calculate_tax(income):
        deductions = income * 0.1
        taxable_income = income - deductions
        tax = calculate_high_income_tax(taxable_income)
        tax += calculate_medium_income_tax(taxable_income)
        tax += calculate_low_income_tax(taxable_income)
        return tax


    def calculate_high_income_tax(taxable_income):
        if taxable_income > 50000:
            return 0.3 * (taxable_income - 50000)
        return 0


    def calculate_medium_income_tax(taxable_income):
        if taxable_income > 20000:
            return 0.2 * min(taxable_income - 20000, 30000)
        return 0


    def calculate_low_income_tax(taxable_income):
        if taxable_income > 10000:
            return 0.1 * min(taxable_income - 10000, 10000)
        return 0
