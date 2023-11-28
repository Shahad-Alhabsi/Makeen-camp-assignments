"""
Shahad Al Habsi
Assignment 3: Introduction to programming & problem solving.

"""
# 1. Crap Game
def CrapGame():
    points = 0
    Roll = True
    possible_values = [1,2,3,4,5,6]
    n1, n2 = 0,0 # for now
    while Roll:
        prev_sum = n1+n2
        try:
            n1 = int(input("\nRoll the first die --> "))
            n2 = int(input("Roll the second die --> "))
        
        except Exception as exc:
            print("Error: ", type(exc))
        
        if n1 in possible_values and n2 in possible_values:
            sum_ = n1+n2
            if points == 0:
                if sum_ in [2,3,12]:
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    return "you lose"
                
                elif sum_ in [7,11]:
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    return "you win"
                else:
                    points += sum_
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    print("points = ", points)
            else:
                if sum_ == prev_sum:
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    return "you win"
                
                elif sum_ == 7:
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    return "you lose"
                else:
                    points += sum_
                    print("you rolled {} + {} = {}".format(n1,n2,n1+n2))
                    print("points = ", points)            

        else:
            print("The dies have only 6 faces")
            continue
        
print(CrapGame())



########################################################
# 2. Find the index of the smallest element
def index_of_smallest_element(List):
    min_ind = 0
    for i in range(len(List)):
        if List[i] < List[min_ind]:
            min_ind = i
    return min_ind

def test():
    while True:
        try:
            nums = input("\nEnter ten integers: ")
            nums = [int(i) for i in nums.split()]    
        except:
            print("Error: Invalid input")
         
        if len(nums) != 10:
            print("You must enter exactly ten integers")
            continue
        else:   
            smallest_index = index_of_smallest_element(nums)
            print("the index of the smallest element is ", smallest_index)
            break
    
test()



########################################################
# 3. Eliminate duplicates
def eliminate_duplicates(List):
    return(list(set(List)))  
    
def test():
    while True:
        try:
            nums = input("\nEnter ten integers: ")
            nums = [int(i) for i in nums.split()]        
        except:
            print("Error: Invalid input\n")
         
        if len(nums) != 10:
            print("You must enter exactly ten integers")
            continue
        else:   
            no_duplicates = eliminate_duplicates(nums)
            print("The distinct numbers are: ", end="")
            for i in no_duplicates:
                print(i , end=" ")
            break
    
test()
