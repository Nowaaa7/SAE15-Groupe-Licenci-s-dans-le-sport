#!/usr/bin/python3

def draw(table):
    max_number = max(table[1])
    n = len(table[1])
    symbol = "█"
    MAX_LEN = 40
    filling = [None for i in range(n)]
    filling_len = [None for i in range(n)]
    lines = [None for i in range(n)]

    for i in range(n):
        lines[i] = ' ' * (len(str(n)) - len(str(i + 1))) + str(i + 1) + ':  '
    
    for i in range(n): #creating [████████████████████████████████________] style chart filling for each line
        filling_len[i] = int(table[1][i] / max_number * MAX_LEN)
        filling[i] = '[' + (filling_len[i] * symbol) + ((MAX_LEN - filling_len[i]) * '_') + ']'

    for i in range(n):
        lines[i] += table[0][i]

                #Aligning lines and adding numbers
    lines_lens = [len(lines[i]) for i in range(n)]
    max_len = max(lines_lens)
    for i in range(n):
        lines[i] += ' ' * (max_len - len(lines[i])) + ' : ' + str(table[1][i]) + '  '
        
                #Aligning lines after numbers, adding chart filling
    lines_lens = [len(lines[i]) for i in range(n)]
    max_len = max(lines_lens)
    for i in range(n):
        lines[i] += ' ' * (max_len - len(lines[i])) + filling[i]

                #Printing chart
    for i in range(n):
        print(lines[i])

    return
