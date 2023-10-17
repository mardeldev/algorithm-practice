def countdown(i):
    if i < 1: # The base case 
        return
    else: # The recursive case
        print(i)
        countdown(i-1)

    
countdown(10)

x = -1
z = 0
y = 1
match True:
    case True if x < 0:
        print('negative')
    case True if z > 0:
        print('positive')
    case True if y is 0:
        print('zero')

