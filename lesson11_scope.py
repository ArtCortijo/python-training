# Lesson 11
# global scope (in file)
name = 'Art'
count = 1


def another():
    # local  scope
    color = 'blue'

    global count
    count += 1
    print(count)

    def greeting(name):
        # use nonlocal to change the value of a variable in an outer scope
        nonlocal color
        color = 'red'
        print(color)
        print(name)

    greeting('Bro')


another()
