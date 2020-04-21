#!/usr/bin/python3
# Create a custom Module and imported
from imported_module import var, DoThis

print(var)
DoThis()


# Python default class imported
from decimal import Decimal


print(Decimal('3.5') + Decimal(3.5))
