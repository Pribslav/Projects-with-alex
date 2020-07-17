from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
# [Corresponding genders for the data above]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)

#Get Input of Height, Weight, Shoe_Size
def get_users_input():
    height_width_shoeSize = []
    height_width_shoeSize.append(int(input("What is your height(centimers): ")))
    height_width_shoeSize.append(int(input("What is your weight(kilograms): ")))
    height_width_shoeSize.append(int(input("What is your shoe size(european): ")))
    prediction = clf.predict([height_width_shoeSize])
    print(prediction)

### if statement method
program_running = 'y'
while(program_running != 'n'):
    if(program_running == 'y'):
        get_users_input()
        program_running = input("do you want to check another person(y/n): ").lower()
    else:
        print("Sorry i didn't get that")
        program_running = input("do you want to check another person(y/n): ").lower()

### Looping Method
# program_running = 'y'
# while(program_running != 'n'):
#     get_users_input()
#     program_running = input("do you want to check another person(y/n): ").lower()
#     while(program_running != 'y' and program_running != 'n'):
#         program_running = input("do you want to check another person(y/n): ").lower()

### Recursive Method
# def check_running():
#     program_running = input("do you want to check another person(y/n): ").lower()
#     if(not (program_running == 'y' or program_running == 'n')):
#         program_running = check_running():
#     return program_running
#
# program_running = 'y'
# while(program_running != 'n'):
#     get_users_input()
#     program_running = check_running()

