def arithmetic_arranger(problems, show_answers=False):
    row1 = []
    row2 = []
    ro_w = []
    res_row = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # list comprehension to do str class appending of each character in problems list
    srt = [
        str(char) if char.isnumeric() else str(char)
        for problem in problems
        for char in problem
    ]
    # whole joins the characters in the srt list and replaces whitespace with an empty string
    whole = ''.join(srt).replace(' ', '')
    for char in whole:
        if not char.isnumeric():
            if char.isalpha():
                return 'Error: Numbers must only contain digits.'
            if char != '+':
                if char != '-':
                    return "Error: Operator must be '+' or '-'."
    for problem in problems:
        for char in problem:
            if char == '+':
                ind = int(problem.index('+'))
                num1 = problem[:ind - 1]
                num2 = problem[ind + 2:]
                ans = int(num1) + int(num2)
                n1 = len(str(num1))
                n2 = len(str(num2))
                r1 = str(num1)
                r2 = str(num2)
                r3 = str(ans)
                if n1 > 4:
                    return 'Error: Numbers cannot be more than four digits.'

                elif n2 > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                if n1 > n2:
                    if n1 - n2 == 1:
                        row1.append(f'{r1.rjust(n1 + 2)}    ')
                        row2.append(f'{char} {r2.rjust(n1)}    ')
                        if len(r3) == n1:
                            res_row.append(f'  {r3.rjust(n1)}    ')
                        if len(r3) > n1:
                            res_row.append(f' {r3.rjust(n1)}    ')
                        for i in range(n1 + 2):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                    elif n2 == 1:
                        row1.append(f'  {r1}    ')
                        row2.append(f'{char} {r2.rjust(n2 + 3)}    ')
                        res_row.append(f'{r3.rjust(n1 + 2)}    ')
                        for i in range(n1 + 2):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                    elif n2 != 1 and n1 - n2 > 1:
                        row1.append(f'{r1}    ')
                        row2.append(f'{char.rjust(n1 - n2 - 1)} {r2}    ')
                        res_row.append(f'  {r3.rjust(n1)}    ')
                        for i in range(n1):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                else:
                    n = int(n2) + 2
                    row1.append(f'{r1.rjust(n)}    ')
                    row2.append(f'{char} {r2}    ')
                    for i in range(n2 + 2):
                        ro_w.append(f'-')
                    ro_w.append(f'    ')
                    if len(r3) == n2:
                        res_row.append(f'  {r3.rjust(n1)}    ')
                    elif len(r3) > n2:
                        res_row.append(f' {r3.rjust(n1)}    ')
                    elif len(r3) < n2:
                        res_row.append(f'  {r3.rjust(n1)}    ')
            elif char == '-':
                ind = int(problem.index('-'))
                num1 = problem[:ind - 1]
                num2 = problem[ind + 2:]
                ans = int(num1) - int(num2)
                n1 = len(str(num1))
                n2 = len(str(num2))
                r1 = str(num1)
                r2 = str(num2)
                r3 = str(ans)
                if n1 > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                elif n2 > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                if n1 > n2:
                    if n1 - n2 == 1:
                        row1.append(f'{r1.rjust(n1 + 2)}    ')
                        row2.append(f'{char} {r2.rjust(n1)}    ')
                        if len(r3) == n1:
                            res_row.append(f'  {r3.rjust(n1)}    ')
                        if len(r3) > n1:
                            res_row.append(f' {r3.rjust(n1)}    ')
                        for i in range(n1 + 2):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                    elif n2 == 1:
                        row1.append(f'  {r1}    ')
                        row2.append(f'{char} {r2.rjust(n2+3)}    ')
                        res_row.append(f'{r3.rjust(n1+2)}    ')
                        for i in range(n1+2):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                    elif n2 != 1 and n1 - n2 > 1:
                        row1.append(f'{r1}    ')
                        row2.append(f'{char.rjust(n1 - n2 - 1)} {r2}    ')
                        res_row.append(f'  {r3.rjust(n1)}    ')
                        for i in range(n1):
                            ro_w.append(f'-')
                        ro_w.append(f'    ')
                else:
                    n = int(n2) + 2
                    row1.append(f'{r1.rjust(n)}    ')
                    row2.append(f'{char} {r2}    ')
                    for i in range(n2 + 2):
                        ro_w.append(f'-')
                    ro_w.append(f'    ')
                    if len(r3) == n2:
                        res_row.append(f' {r3.rjust(n1)}    ')
                    elif len(r3) > n2:
                        res_row.append(f' {r3.rjust(n1)}    ')
                    elif len(r3) < n2:
                        res_row.append(f'  {r3.rjust(n1)}    ')
        l1 = (''.join(row1))
        l2 = (''.join(row2))
        l3 = (''.join(ro_w))
        arranged_problems = l1.rstrip() + '\n' + l2.rstrip() + '\n' + l3.rstrip()
        if show_answers is True:
                l4 = (''.join(res_row))
                arranged_problems += '\n' + l4.rstrip()
    return arranged_problems


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))


