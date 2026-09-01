indian = ['dal','samosa','naan']
chinese = ['noodles','pot sticker','fried rice']
italian = ['pizza'],'pasta','risotto'
dish = input('enter a dish: ')
if dish in indian:
    print(f'{dish} in indian')
elif dish in chinese:
    print(f'{dish} in chinese')
elif dish in italian:
    print(f'{dish} in italian')
else:
    print("i don't know from which dish it is ")