cubes=[]
print("-----List by Loop-----")
for value in range(1,11):
        cube=value**3
        cubes.append(cube)
print(cubes)

print("-----List Comprehension-----")
cubes=[value**3 for value in range(1, 11)]
print(cubes)
