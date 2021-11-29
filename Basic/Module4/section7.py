# Section 7
# It’s better to beg for forgiveness than to ask for permission
# It's better to handle an error when it happens than to try to avoid it


try:
    # Risky code that may cause an error
    # An error here does not terminate the program,
    # instead the except block is executed
    print('a')
except:
    # This code is only run when an error hapenned in the try block
    # Do your best clean up the mess
    print('b')


# Example one
# Only one block of code will be executed
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')

# Example two: using exception names
# Only one block of code will be executed
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('Please cooperate and enter a natural number.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
    
# Example three: default exception
# Default exception is always last
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('Please cooperate and enter a natural number.')     
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
