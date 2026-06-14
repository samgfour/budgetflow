#!/usr/bin/env python3
"""
BudgetFlow - Income allocator based on the 15/20/30/35 rule
"""

def print_header():
    print("\n" + "="*50)
    print(" " * 15 + "BUDGETFLOW")
    print("="*50)
    print("15% Invest • 20% Save • 30% Pay Yourself • 35% Spend\n")

def calculate_budget(income):
    income = float(income)
    return {
        "Pay Yourself": int(0.30 * income),
        "Savings":     int(0.20 * income),
        "Expenses":    int(0.35 * income),
        "Investing":   int(0.15 * income)
    }

def main():
    print_header()
    
    while True:
        try:
            income_input = input("Enter your monthly income: ").strip()
            if not income_input:
                print("Please enter a valid amount.\n")
                continue
                
            income = float(income_input.replace(",", ""))
            if income <= 0:
                print("Income must be greater than zero.\n")
                continue
                
            budget = calculate_budget(income)
            total = sum(budget.values())
            
            print(f"\n📊 Income: ${income:,.2f}\n")
            for category, amount in budget.items():
                print(f"• {category:15} ${amount:,.2f}")
            
            print(f"\n{'─'*50}")
            print(f"Total Allocated: ${total:,.2f} (100%)")
            print("="*50)
            
        except ValueError:
            print("❌ Please enter a valid number.\n")
            continue
        
        again = input("\nCalculate another income? (y/n): ").strip().lower()
        if again != 'y':
            print("\nStay consistent. Your future self will thank you 💪\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
