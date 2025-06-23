** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    dash_count = 0
    operation = []
    longest = 0
    addsub = 0
    output1 = ''
    output2 = ''
    dashes = ''
    answers = ''
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else: 
        for problem in problems:
            operation = problem.split(' ')
            if len(operation[0]) > 4 or len(operation[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if operation[1] == '+':
                longest = 2 + max(len(operation[0]),len(operation[2]))
                try:
                    addsub = int(operation[0]) + int(operation[2])
                except:
                    return 'Error: Numbers must only contain digits.'
                output1 += operation[0].rjust(longest) + '    '
                output2 += '+' + operation[2].rjust(longest - 1) + '    '
            
                while dash_count < longest:
                    dashes += '-'
                    dash_count += 1
                dashes += '    '
                dash_count = 0
                answers += str(addsub).rjust(longest) + '    '
            elif operation[1] == '-':
                longest = 2 + max(len(operation[0]),len(operation[2]))
                try:
                    addsub = int(operation[0]) - int(operation[2])
                except:
                    return 'Error: Numbers must only contain digits.'
                output1 += operation[0].rjust(longest) + '    '
                output2 += '-' + operation[2].rjust(longest - 1) + '    '
                
                while dash_count < longest:
                    dashes += '-'
                    dash_count += 1
                dashes += '    '
                dash_count = 0
                answers += str(addsub).rjust(longest) + '    '
            else:
                return "Error: Operator must be '+' or '-'."
    if show_answers:
        return output1.rstrip() + '\n' + output2.rstrip() + '\n' + dashes.rstrip() + '\n' + answers.rstrip()
    else:
        return output1.rstrip() + '\n' + output2.rstrip() + '' + '\n' + dashes.rstrip()
    

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print('  3801      123\n-    2    +  49\n------    -----')

** end of main.py **

