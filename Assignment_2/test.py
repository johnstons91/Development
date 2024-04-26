print('Hello, valuable client of our multinational corporation. In order to receive a monthly discount on our products, you need to register on our website. Please, sign up.') #Greetengs
while True:
    u = input('Please, create Username. The username must begin with a lowercase letter and can only contain letters, numbers, and underscores.', )
    print(u)
    if u[0].islower() and u.isidentifier(): #Checking that three requirements are met (first lowercase letter, no other characters except letters, numbers and underscores)
        print('Username meets requirements')
        break