number = input('enter the numbers:')
phone= {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
output= ''
for num in number:
    output+=phone.get(num)+'  '
print(output)
