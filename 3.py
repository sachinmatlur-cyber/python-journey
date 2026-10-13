while True :
  print ('Who are you?')
  name = input()
  if name != 'joe':
    continue
  print ('Hello, joe. What is the password? (It is a fish.)')
  password = input()
  if password == 'swordfish':
    break
print ('Access granted.')