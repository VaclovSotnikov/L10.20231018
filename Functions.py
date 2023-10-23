
# def add_two_number(a, b):
#     print(a + b)

# add_two_number(5, 6) 

# add_two_number(85, 76) 

# add_two_number(5, 14) 

# def write_wellcome():
#     print("labas")

# write_wellcome()

# def add_two_numbers(a, b):
#     return a + b

# nr_sum = add_two_numbers(4777, 566)

# print(nr_sum)

#Create a function that takes string as parameter and returns number of letters from that string.

# def number_of_letters(text):
#     return len(text and str.split(" ", ""))

# text = input("enter text: ")
# print(len(text))

# def count_letters(in_string: str):
#     return len(in_string.replace(" ", ""))

# def add_two_number(a: str, b: str) -> str: #butinai irasyti type
#     return a + b

# def sqrt_two_numbers(a: int) ->int:
#    ## print("first function: ", a)
#     return a ** 2

# def make_a_string(text: str, x: int) -> str:
#    ## print("second function: ", x)
#     number = sqrt_two_numbers(x)
#     return text + str(number)

# print(make_a_string("betkas", 5))

#1

# def number_multiplication(a: int, b: int) ->int:
#     return a * b
# multiplication = number_multiplication(704, 455)

# print(multiplication)

# def get_even_number(numbers: int) ->int:
#     even_nums = [num for num in numbers if not num % 2]
#     return even_nums
# print(get_even_number([5, 4, 41, 236, 57, 86]))

# from typing import Optional, Union, List, Dict


# def union_type(a: Union[int, float]) -> Union[int, str]:
#     if type(a) == "int":
#         return a
#     else:
#         return str(a)


# def optional_type(a: Union[int, float]) -> Optional(int):
#     if type(a) == "int":
#         return a
#     return None

# my_list: List[Union[str, int, float]] = ["ffff", 1, 1.56]

# my_dict: Dict[str,Optional(Union[int,float])]= {"A":1, "B":1.23, "C": None}


#2

# from typing import List, Union


# def add_string_ending_to_list_elements(list: List[str], ending_str: str) ->List:
#     result = []
#     for item in list:
#         result.append(item + ending_str)
#     return result

#3

# from typing import Union, Tuple


# Number_a = float(input("enter number: "))
# Number_b = float(input("enter number: "))

# def input_two_numbers_to_calculate(Number_a: Union[int, float], Number_b:Union[int, float]) ->Tuple[float]:
#     addition = Number_a + Number_b
#     subtraction = Number_a - Number_b
#     multiplication = Number_a * Number_b
        
#     if Number_b != 0:
#         division = Number_a / Number_b
#     else:
#         division = "Division by zero is not allowed."

#     return addition, subtraction, multiplication, division


#4

# from typing import List

# simbol = input("Please enter words with spec simbol: ")

# def find_word(in_text: str) -> List[str]:
#     unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-"]
#     splited_words: List[str] = in_text.split(" ")
#     unique_words: List[str] = [word for word in splited_words if any(simb in word for simb in unique_chars)]
#     return unique_words

# print(find_word(simbol))


#1 namu darbai      
# Create a mini program that takes 10 random numbers in one input ("1,2,5 76,89 ...etc")
# Write functions to: calculate their sum, multiplication of highest and lowest numbers
# and the function which makes a new string where numbers are positioned from highest to lowest.


#1

# from typing import List, Optional


# my_numbers = input("Enter 10 random numbers: ")
# my_list = [float(num) for num in my_numbers.split(",")]

# def calculate_sum(numbers: List[float]) -> float:
#     return sum(numbers)

# new_sum = calculate_sum(my_list)
# print(new_sum)

# def calculate_multiplication(numbers: List[float]) -> float:
#     return min(numbers) * max(numbers)

# new_multiplication = calculate_multiplication(my_list)
# print(new_multiplication)

# def sort_numbers(numbers: List[float]) ->float:
#     sorted_numbers = sorted (numbers, reverse=True)
#     sorted_stirng = ",".join(map(str, sorted_numbers))
#     return sorted_stirng

# sorted_numbers_str = sort_numbers(my_list)
# print(sorted_numbers_str)


# User enters two names separated by comma : for example :('Mindaugas PiktasDestytojas, Mindaugas Juokauja') 
# Create a function that would swipe surnames and will prduxe new name surname and 
# another function funtion that will swap names.



# from typing import List


# input_names = input("Enter 2 names and surnames separated by coma: ")

# def swap_surnames(names: List[str]) ->List:
#     name_list = names.split(',')
    
#     if len(name_list) == 2:
#         first_name, second_name = name_list[0].strip(), name_list[1].strip()
        
#         first_surname = first_name.split()[-1]
#         second_surname = second_name.split()[-1]
        
#         new_name = f"{first_name.replace(first_surname, second_surname)} {second_name.replace(second_surname, first_surname)}"
        
#         return new_name

# swapped_names = swap_surnames(input_names)
# print(swapped_names)

# from typing import List

# input_names = input("Enter 2 names and surnames separated by comma: ")

# def swap_names(names: List[str]) ->str:
#     name_list = names.split(',')
    
#     if len(name_list) == 2:
#         first_name, second_name = name_list[0].strip(), name_list[1].strip()
        
#         first_first_name = first_name.split()[0]
#         second_first_name = second_name.split()[0]
        
#         new_name = f"{second_first_name} {first_name.replace(first_first_name, second_first_name)}," \
#                    f" {first_first_name} {second_name.replace(second_first_name, first_first_name)}"
        
#         return new_name

# swapped_names = swap_names(input_names)
# print(swapped_names)

# 2 namu darbai
# Create a program , which takes 3 different sentences. 
# The input should have all error checking in mind. 
# The program then should create a dictionary of whith key values corresponding to words `long` (more than 9 letters in a words) `medium`(7 letters)
# `short` (5 words). 
# Then the pgrogram should create a new sentences (if 3 provided, 3 new sentences should be returned) 
# with following rules attached:
# All sentences should have same (or less) words amount as entered one;
# The most frequent letter from the sentence (from input) should be dominated in a new sentence as well.

# The program should return new sentences with statitstics of ratio how many words was used from all sections 
# (as for exmpale: long 10%,medium 25%, short <35%)