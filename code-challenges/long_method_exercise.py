class TaxCalculator:
    def calculate_tax(income):
        """Calculate tax"""
        deductions = income * 0.1
        taxable_income = income - deductions
        tax = 0
        if taxable_income > 50000:
            tax += 0.3 * (taxable_income - 50000)
        if taxable_income > 20000:
            tax += 0.2 * min(taxable_income - 20000, 30000)
        if taxable_income > 10000:
            tax += 0.1 * min(taxable_income - 10000, 10000)
        return tax
