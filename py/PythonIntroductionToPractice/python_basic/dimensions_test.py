dimensions = ( 200, 50 )
#dimensions[0] = 150  'tuple object does not support item assignment
for dimension in dimensions:
    print(dimension)
#if you want to modify the 'tuple' you can redefinition the tuple
dimensions = (150, 50)
for dimension in dimensions:
    print(dimension)