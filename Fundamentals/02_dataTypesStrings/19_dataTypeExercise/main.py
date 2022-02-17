two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))

new_twodigit_str = str(two_digit_number)

new_output_a = two_digit_number[0]
new_output_b = two_digit_number[1]

new_a_int = int(new_output_a)
new_b_int = int(new_output_b)

new_twodigit_number = new_a_int + new_b_int
print(new_twodigit_number)