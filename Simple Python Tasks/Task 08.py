txt= input('write ur msg: ').split(' ')
emoji = {
    ':)':'sexy',
    ':(':'☹️'
}
output= ''
for ch in txt:
    output += emoji.get(ch,ch)+ ' '
print(output)
