
print("How many times should I break free?")
num = int(input())
count = 1
# while count < num:
#     print(f"…{num - count}: this is the part when I break free")
#     count += 1

for count in range(num-1, 0, -1):
  print(f"{count}:this is the part when I break free")
print(" 'Cause I can't resist it no more!")