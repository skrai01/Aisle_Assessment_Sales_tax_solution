from Inputs import getInput
from ItemType import getTaxStatus
from ItemTax import getItemTax

while True:
    filename = raw_input('Enter \'Filename\' or \'Done\' to exit\t')
    print "\n"
    if filename.lower()=='done':
        break
    all_items = getInput(filename)

    total_without_tax = 0
    total_with_tax = 0

    for item in all_items:
        qty = int(item[0][0])
        taxStatus, imported = getTaxStatus(item[0]) # Returns True if tax is applied on item and True if item is imported.
        itemTax = getItemTax(qty, taxStatus, imported, item[1])
        total_without_tax += float(item[1])
        total_with_tax += float(itemTax)
        print item[0], " : ", itemTax

    salesTax = total_with_tax - total_without_tax
    salesTax = format(salesTax, '.2f')
    total_with_tax = format(total_with_tax, '.2f')
    print "Sales Taxes : ", salesTax

    print "Total : ", total_with_tax,"\n"
