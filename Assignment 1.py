"""
Shahad AlHabsi
Assignment1: Introduction to programming & problem solving.


1) a certain steel is graded according to the following conditions:
    i.Rockwell hardness > 50 
    ii.Carbon content > 0.7 
    iii.Tensile strength > 5600 kg/cm2 
The steel is graded as follows: 
    a. Grade 10, if all the conditions are satisfied 
    b. Grade 9, if conditions (i) and (ii) are satisfied 
    c. Grade 8, if conditions (ii) and (iii) are satisfied 
    d. Grade 7, if conditions (i) and (iii) are satisfied 
    e. Grade 0, otherwise
Draw the flow chart and algorithm steps to solve this problem
"""
# condition_1 = float(input("Enter the rockwell hardness: "))
# condition_2 = float(input("Enter the carbon content: "))
# condition_3 = float(input("Enter the tensile strength: "))
# 
# if (condition_1 > 50  and condition_2 > 0.7 and condition_3 > 5600):
#     print("Grade 10")
# else:
#     if (condition_1 > 50  and condition_2 > 0.7  ):
#         print("Grade 9")
#     elif (condition_2 > 0.7  and condition_3 > 5600):
#         print("Grade 8")
#     elif (condition_1 > 50  and condition_3 > 5600):
#         print("Grade 7")
#     else:
#         print("Grade 0")



"""
2) Suppose that the tuition for a university is $10,000 this year and increases 5% every year.
In one year, the tuition will be $10,500. Write a program that computes the tuition in ten years 
and the total cost of four years’ worth of tuition after the tenth year
"""
# tuition = 10000
# tuition_after_10_years = 0
# for years in range(1,15):
#     tuition += (tuition*5/100)
#     
#     # the tuition in 10 years:
#     if years==10:
#         print("Tuition in ten years = $%.2f"%(tuition))
#         
#     # total tuition of 4 years after the 10th year(the total of the 11th, 12th, 13th and 14th year)
#     if years > 10:
#         tuition_after_10_years += tuition
#         
# print("Total cost of four years worth of tuition after the tenth year = $%.2f"%(tuition_after_10_years))




"""
Write a nested for loop that prints the following output:
                  1
                1 2 1
              1 2 4 2 1
            1 2 4 8 4 2 1
         1 2 4 8 16 8 4 2 1
      1 2 4 8 16 23 16 8 4 2 1
   1 2 4 8 16 23 46 23 16 8 4 2 1
1 2 4 8 16 23 46 128 46 23 16 8 4 2 1
"""