name = "Hat is my fav"
print(len(name))
god ="Jai shree Ganesha \n\t"*108
print(god)
her = '''She say's "hello "'''
print(her)
this = 'this is backslash "\\"'
print(this)
for i in name:
    print(i,end="\n")

print(name.upper())
print(name.lower())
print(name.strip())
print(name[4])
print(name[0:3])
print(name[1:10:2])
print(name.find("a"))
print(name.replace("Hat","aishwarya"))

firstname = input("what is your first name ")
Secondname = input("what is your Second name ")
print(f"{firstname} {Secondname}".upper())
print(name.capitalize())
print(name.title())