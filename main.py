with open("Lance.txt",'r') as f:
  content = f.readlines()
for i in content:
  
  list = i.split(",")
  print(list[0])