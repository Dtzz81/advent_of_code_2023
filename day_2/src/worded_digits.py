class CalibrationDocument:
    def __init__(self, filename):
        self.filename = filename

    def get_lines(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def sum(self):
        sum = 0
        with open(self.filename, 'r') as file:
            for line in file:

                reader = CalibrationReader(line)
                digits_for_each_line = reader.read()

                sum += digits_for_each_line
        return sum

class CalibrationReader:
    def __init__(self, calibration_line):
        self.calibration_line = calibration_line

    def read(self):
      
        digits = []
        for char in self.calibration_line:
            if char.isdigit():
                digits.append(char)

        first_and_last_digits = digits[0] + digits[-1]
        return int(first_and_last_digits)


calibration_doc = CalibrationDocument("all_lines.txt")
total_sum = calibration_doc.sum()

