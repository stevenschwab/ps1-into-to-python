#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:54:09 2025

@author: stevenschwab
"""

# Program to calculate how many months it will take you to save up enough money for a down payment

# Get user inputs and cast to floats
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary raise, as a decimal: "))

# Initialize variables
portion_down_payment = 0.25 # 25% down payment
total_down_payment = total_cost * portion_down_payment
current_savings = 0 # Start with no savings
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved # Monthly contribution from salary
r = 0.04 # Annual return rate
num_of_months = 0

# Loop until savings meet or exceed down payment
while current_savings < total_down_payment:
    # Increment months first to track time
    num_of_months += 1
    
    # Apply semi-annual raise before calculating savings for this month
    if num_of_months % 6 == 1 and num_of_months > 1:
        annual_salary *= (semi_annual_raise + 1)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved
    
    # Calculate monthly return and update savings
    roi = current_savings * (r / 12) # Monthly return on investment
    current_savings += monthly_savings + roi # Add savings and return
    
    

# Output result
print("Number of months:", num_of_months)