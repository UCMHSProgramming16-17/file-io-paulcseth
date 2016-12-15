file = open('list.txt','w')

count = 0 
while count <=10:
    user = input("What's in your list?")
    file.write(user+'\n')
    count += 1
    
file.close()