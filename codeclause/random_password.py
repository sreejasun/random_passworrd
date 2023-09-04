import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"','<',',','>','.','?','/']
print("Welcome to Password Generator")
n_letters=int(input("how many letters would you like to have in your password? "))
n_symbols=int(input("how many symbols would you like to have in your password? "))
n_numbers=int(input("how many numbers would you like to have in your password? "))
password_list=[]
for char in range(1,n_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,n_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1,n_numbers+1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
print(''.join(map(str,password_list)))