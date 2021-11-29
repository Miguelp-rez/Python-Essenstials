import sys
print('Miguel', 'Angel', 'Perez', 'Quiroz', sep='-')

#The print function always returns None after succesful execution
print('Returned value of the print function: ', print())

#None evaluates to False
print('Boolean value of None: ', bool(None))

#The second instruction only runs if the first one evaluates to True
print('\\', end='') and print('./')

#The second instruction always runs
print(end='') or print('./')

#Output redirection
print('Error: I failed...', file=sys.stderr)

