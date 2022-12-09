#!/usr/bin/python

import sys

salesTotal = 0
oldSale = None
def mayor(coste):
    max = 0
    if coste > max:
        max = coste

    return max

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldSale and oldSale != thisSale:
        print(str(salesTotal))
        oldSale = thisSale
        salesTotal = 0

    oldSale = thisSale
    salesTotal += float(thisSale)

# Escribe o ultimo par, unha vez rematado o bucle
if oldSale != None:
    print(str(salesTotal))
