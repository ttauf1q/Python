def ch(msg):
    emoji = {
        ':)' : '🙂',
        ':(' : '☹️'
    }
    output=''
    for xx in msg:
        output+=emoji.get(xx,xx)+' '
    return output


msg=input('enter ur msg: ').split()

print(f'\n {ch(msg)} \n')