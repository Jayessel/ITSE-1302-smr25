#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale

locale.setlocale(locale.LC_ALL, 'us')

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    shipping_cost = subtotal * Decimal(".085")
    shipping_cost = shipping_cost.quantize(Decimal("1.00"),ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax + shipping_cost
    
    group = f"grouping=\'thousands_sep\'"
    tf = '>10'
    fo = '10,'
    # display the results
    # print(f"Order total:        {order_total:10,}")
    print(f"Order total:        {locale.currency(order_total,group):{tf}}")
    print(f"Discount amount:    {discount:{fo}}")
    print(f"Subtotal:           {subtotal:{fo}}")
    print(f"Shipping cost:      {shipping_cost:{fo}}")
    print(f"Sales tax:          {sales_tax:{fo}}")
    print(f"Invoice total:      {locale.currency(invoice_total,group):{tf}}")
    # print(f"Invoice total:      {invoice_total:10,}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
