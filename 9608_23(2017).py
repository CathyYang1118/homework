#5
'''
def search_file(login_event):
    f = open('LoginFile.txt','r')
    ID = input('input an user ID')
    line = f.readlines()
    l = 0
    for line:
        if line[0:5] == ID:
            LoginEvents[l,0] = f[5:9]
            LoginEvents[l,1] = f[9:23]
            l += 1
    f.closefile()
'''

#6
'''
def VaidatePassword():
    num = ['0','1','2','3','4','5','6','7','8','9']
    num_n = 0
    num_l = 0
    num_u = 0
    
    resoult = False
    password = input('input a password')
    
    for item in password:
        if ord(item)>=65 and ord(item)<=90:
            num_u += 1
        elif ord(item)>= 97 and ord(item) <= 122:
            num_l += 1
        else:
            for i in num:
                if i == item:
                    num_n += 1
                else:
                    return resoult
        if num_l >= 2 and num_u >= 2 and num_n >= 3:
            resoult = True
        return resoult
'''  
