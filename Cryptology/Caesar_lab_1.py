arr1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

arr2=[]
for i in range(len(arr1)):
    arr2.append(arr1[i])
number=int(input("Key:"))
for i in range(number):
    arr2.append(arr2[0])
    arr2.remove(arr2[0])

msg = input("text:")

msgc = ""
for i in msg:
    for j in range(len(arr1)):
        if i == arr1[j]:
            msgc += arr2[j]
print("Crypt:", msgc)

