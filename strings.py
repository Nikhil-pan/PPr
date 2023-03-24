import datetime
 
today = datetime.datetime.now()
print(f"{today:%B %d, %Y}")
print(today)

var='now'

print(f"we gotta do it {var}, if not {var}, then when?")

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print ("Ah, so your name is {nam}, your quest is {ques}, " \
"and your favorite color is {colr}.".format(nam=name,ques=quest,colr=color))

print('This isn\'t flying, this is falling with style!')

print(bool(1))


