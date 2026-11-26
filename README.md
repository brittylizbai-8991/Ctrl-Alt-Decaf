# Ctrl-Alt-Decaf

CSC-154 Semester Project: Coffee Shop Ordering System

A console-based prototype for a campus coffee shop ordering system, written in Python. Customers can place orders, baristas manage the queue, and managers handle menu changes and discounts.

## How to run

1. Install Python 3.
2. Download or clone this repo.
3. In a terminal, go to the project folder and run:

   python3 main.py

You can also open the folder in PyCharm and run `main.py`.

## What it does

- **Customer (no sign-in):** browse the categorized menu, customize a drink (size, milk, flavor, toppings), pick a pick-up time, and confirm or cancel the order.
- **Barista (PIN sign-in):** view the order queue, mark orders done, and mark items in or out of stock. Three wrong PINs locks sign-in for 30 seconds.
- **Manager:** change menu prices, set daily deals, apply discounts, refund orders, and review orders by employee.

Orders and menu changes are not saved. They reset when the program closes.

## Demo barista PINs

- Nicholas: 6889
- Ryatt: 2143
- Ryley: 9187

## Out of scope

Delivery, loyalty/rewards, online payments, and supplier ordering are not part of this prototype.

## Documents

- Test plan: `CtrlAltDecaf_Test_Plan_and_Run_Sheet.pdf`
- Prototype plan: `docs/prototype_plan.md`