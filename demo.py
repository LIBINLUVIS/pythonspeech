import pyttsx3
s=input("enter the limit")
mul = 1
res = 1
t=s+1

for x in range(res, t, mul):
 engine = pyttsx3.init()
 engine.say(x)
 engine.runAndWait()