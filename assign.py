#question 1
list = ['a','b','c']
list1 = ['p','q','r']

i = 0
while i <= 2:
    print(list[i] + list1[i],end=" ")
    i += 1
print("")

#question 2
list2 = ['a','b','','']
list3 = ['p','q','r','s']

j = 0
while j <= 3:
    print(list2[j] + list3[j],end=" ")
    j += 1
print(" ")

#question 3
list4 = ['p','q','','']
list5 = ['a','b','c','d']

k = 0
while k <= 3:
    print(list4[k] + list5[k],end=" ")
    k += 1
print(" ")

#question 4, 5 and 6

def gcd (str1,str2):
    if(len(str1)<len(str2)):
        return gcd(str2,str1)
    elif(not str1.startswith(str2)):
        return ""
    elif(len(str2) == 0):
        return str1
    else :
        return gcd(str1[len(str2):],str2)
    
str1 = "ABABAB"    #"ABCABC"   #"LEET"
str2 = "AB"        #"ABC"      #"CODE"
result = gcd(str1,str2)
print(result)

