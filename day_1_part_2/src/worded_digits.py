import re

class CalibrationDocument:
    def __init__(self, filename):
        self.filename = filename

    def get_lines(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def get_all_digits(self):
        print("Entering the loop in get_all_digits")
        all_digits_list = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                reader = CalibrationReader(line)
                digits_for_each_line = reader.read()
                all_digits_list.append(digits_for_each_line)

        return all_digits_list

    def get_first_and_last_digits(self):
        print("Before calling get_all_digits in get_first_and_last_digits")
        all_digits_list = self.get_all_digits()

        # Add a print statement just before the loop
        print("Entering the loop in get_first_and_last_digits")

        first_and_last_digits = []
        for digits in all_digits_list:
            if isinstance(digits, int):
                # If only one digit, use it as both first and last
                first_and_last_digits.append(digits * 11)
            elif digits:
                first_and_last_digits.append(digits[0])
                if len(digits) > 1:
                    first_and_last_digits.append(digits[-1])

        print("First and Last Digits List:", first_and_last_digits)
        return first_and_last_digits


    def sum(self):
        all_digits_list = self.get_first_and_last_digits()
        total_sum = sum(all_digits_list)
        return total_sum

class CalibrationReader:
    def __init__(self, calibration_line):
        self.calibration_line = calibration_line

    def read(self):
        digits = [int(digit) for digit in re.findall(r'\d', self.calibration_line)]
        worded_numbers = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine)\b', self.calibration_line)
        worded_digit_values = [worded_digits[word] for word in worded_numbers]

        # Combine both digit lists
        all_digits = digits + worded_digit_values

        result_digits = []
        result_digits.append(all_digits[0])
        result_digits.append(all_digits[-1])
        # Concatenate digits into a single number
        single_number_per_line = int(''.join(map(str, result_digits)))
        print(single_number_per_line)
        return single_number_per_line


worded_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# Example usage
calibration_doc = CalibrationDocument("all_lines.txt")
first_and_last_digits_list = calibration_doc.get_first_and_last_digits()

# Print the result for each line
for i, digits in enumerate(first_and_last_digits_list, start=1):
    print(f"Line {i} First and Last Digits:", digits)

# 1 assign worded numbers to digit
# 2 find these worded numbers and convert them to int
# 3 find last and first digit
# 4 sum the new digits
