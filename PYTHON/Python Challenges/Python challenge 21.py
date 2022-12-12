inchorcm=input('Please enter wether you want to convert cm or inches: ')
if inchorcm=='inches':
    inch_value = int(input('Enter the value in inch: '))
    cm_value = 2.54 * inch_value
    print('{}″ = {}cm'.format(inch_value, cm_value))
elif inchorcm=='cm':
    cm_value = int(input('Enter the value in cm (You cannot use decimals): '))
    inch_value = cm_value / 2.54
    print('{}cm = {}"'.format(cm_value, inch_value))
