from posixpath import split


str = open("log.txt","r").read()
lista=str.split("commit")

alt = lista [5]
alt2= alt.split("Date")
alt3= alt2[1]
alt4= alt3.split("\n")
alt5= alt4[1:]
print(alt5)
# print(alt2)
# print(alt)
# print(len(lista)-1)