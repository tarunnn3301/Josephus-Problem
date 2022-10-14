# My program can be compiled and executed in linux os environment.

def ProbSolve(person, k, index):
    # When one person is alive then it will print that person's name
    if len(person) == 1:
        print(person[0], "is alive")
        return

    # Finding the index of the person who is going to get killed
    index = ((index + k) % len(person))

    # Removing the person which is going to be killed and storing it in variable while popping
    target = person.pop(index)
    print(target, "gets killed")

    # recursive call for n-1 persons
    ProbSolve(person, k, index)


# Taking the input for n and k from the user

n = int(input("Please enter the value of N : "))
k = int(input("Please enter the value of K : "))

# Code proceeds further only if n and k are positive
if n <= 0 or k < 0:
    print("Please enter valid input")
    exit()

# initial index is zero
index = 0

# filling the group array with persons using for loop
group = []
for i in range(1, n + 1):
    group.append(i)

# Calling the recursive function to solve for the given input
ProbSolve(group, k, index)
