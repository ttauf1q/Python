while True:

    class special():
        def common(self):
            com = []
            for num in number:
                if number.count(num) > 1:
                    if num not in com:
                        com.append(num)
            print(f'\n{com}\n')


        def unique(self):
            uniq = []
            for num in number:
                if num not in uniq:
                    uniq.append(num)
            print(f'\n{uniq}\n')


        def minimum(self):
            min = number[0]
            for num in number:

                if min > num:
                    min = num
            print(f'\n{min}\n')


        def maximum(self):
            max = number[0]
            for num in number:

                if max < num:
                    max = num
            print(f'\n{max}\n')


        def even(self):
            ev = []
            for num in number:
                if int(num) % 2 == 0:
                    if num not in ev:
                        ev.append(num)
            print(f'\n{ev}\n')


        def odd(self):
            od = []
            for num in number:
                if int(num) % 2 != 0:
                    if num not in od:
                        od.append(num)
            print(f'\n{od}\n')


        def prime(self):
            pr = []
            for num in number:
                c = 0
                for i in range(1, int(num)):
                    if int(num) % i == 0:
                        c += 1
                if c == 1:
                    if num not in pr:
                        pr.append(num)
            print(f'\n{pr}\n')


        def srt(self):
            print(f'\n{sorted(number)}\n')


        def rev(self):

            number.sort(reverse=True)
            print(number)

        def error(self):
            print("\nWRONG INPUT!! please enter the right keyword: (repeat/unique/minimum/maximum/odd/even/prime/ascending/descending)\n")


    number = input('Enter your numbers: ').split()

    gg = input("what u want to find (repeat/unique/minimum/maximum/odd/even/prime/ascending/descending): ")

    tt = special()

    if gg.lower() == 'repeat':
        tt.common()
        break

    elif gg.lower() == 'unique':
        tt.unique()
        break

    elif gg.lower() == 'minimum':
        tt.minimum()
        break

    elif gg.lower() == 'maximum':
        tt.maximum()
        break

    elif gg.lower() == 'even':
        tt.even()
        break

    elif gg.lower() == 'odd':
        tt.odd()
        break

    elif gg.lower() == 'prime':
        tt.prime()
        break

    elif gg.lower() == 'ascending':
        tt.srt()
        break

    elif gg.lower() == 'descending':
        tt.rev()
        break

    else:
        tt.error()


