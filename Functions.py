
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