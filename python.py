import pyttsx3
name=input("what is your name ")
print(name)
aishwarya= pyttsx3.init()
aishwarya.say(f"hello {name} how are you ")
aishwarya.runAndWait()
