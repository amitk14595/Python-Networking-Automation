ip= '192.168.5.5'

parts= ip.split('.')
print (parts)

part_0 = parts[0]
part_1 = parts[1]
part_2 = parts[2]
part_3 = parts[3]

print ("_" *60)

print('part: 0', part_0)
print('part: 1', part_1)
print('part: 2', part_2)
print('part: 3', part_3)

print("_" *60)

sep= "."

for x in range (1, 256):
        print(part_0 + sep + part_1 + sep + part_2 + sep + str(x))
