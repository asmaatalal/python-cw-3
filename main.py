# write your code here
favorite_animals = ['dog', 'cat', 'monkey', 'rabbit' ]
for favorite_animal in favorite_animals :
    print( favorite_animal )
print(f"the second element in the list is {favorite_animals[1]}" )
favorite_animals.remove('monkey')
print(f'the favorite animals list {favorite_animals}')
favorite_animals.append('pat')
print(f'the favorit animals list {favorite_animals}')
for favorite_animal in favorite_animals :
    print('i like', favorite_animal)
numbers = [1, 2, 3, 4, 5]
numbers_sum =0
for sum in numbers :
    numbers_sum+=sum
    print(numbers_sum) 