#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:54:20 2025

@author: stevenschwab
"""

# write a program to answer how much you should save each month to achieve affording a home in x years

# Get user inputs and cast to floats
starting_salary = float(input("Enter the starting salary: "))

# Initialize variables
total_cost = 1000000 # Cost of the house
portion_down_payment = 0.25 # 25% down payment
down_payment = total_cost * portion_down_payment # Target: $250,000
r = 0.04 # Annual return rate on investment
semi_annual_raise = .07 # 7% raise every 6 months
months = 36 # Goal: 36 months
tolerance = 100 # Savings must be within $100 of down payment

# Bisection search variables
low = 0 # Lower bound: 0% (0)
high = 10000 # Upper bound: 100% (10000)
steps = 0 # Track bisection search steps
best_savings_rate = 0 # To store the result

# Check if saving is possible (test with 100% savings)
current_savings = 0
annual_salary = starting_salary
for month in range(1, months + 1):
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * 1.0 # 100% savings rate
    current_savings += monthly_savings + (current_savings * (r / 12)) # Add savings and return
    if month % 6 == 0: # Apply raise after 6th, 12th, 18th, etc.
        annual_salary *= (1 + semi_annual_raise)
if current_savings < down_payment - tolerance:
    print("It is not possible to pay the down payment in three years.")
else:
    # Bisection search to find the best savings rate
    while low <= high:
        steps += 1
        guess = (low + high) // 2 # Middle point (integer for 0 to 10000)
        savings_rate = guess / 10000 # Convert to decimal (e.g., 4411 -> 0.4411)
        
        # Reset for each guess
        current_savings = 0
        annual_salary = starting_salary
        # Calculate savings over 36 months
        for month in range(1, months + 1):
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary * savings_rate
            current_savings += monthly_savings + (current_savings * (r / 12))
            if month % 6 == 0: # Apply raise after 6th, 12th, 18th, etc.
                annual_salary *= (1 + semi_annual_raise)
                
        # Check if savings is within $100 of down payment
        if abs(current_savings - down_payment) <= tolerance:
            best_savings_rate = savings_rate
            break # Found a good rate
        elif current_savings < down_payment: # Too low, increase rate
            low = guess + 1
        else: # Too high, decrease rate
            high = guess - 1

    # Output result
    print("Best savings rate:", best_savings_rate)
    print("Steps in bisection search: ", steps)