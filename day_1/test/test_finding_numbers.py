from src.finding_numbers import CalibrationReader
from src.finding_numbers import CalibrationDocument

def test_read_calibration_line():
    calibration_line = "1abc2"          #input
    expected_calibration_value = 12             #output
    calibration_reader = CalibrationReader(calibration_line)  #process
    #every class has an empty constractor as default
    actual_calibration_value = calibration_reader.read()
    assert expected_calibration_value == actual_calibration_value

def test_go_throught_string_line_to_find_digits():
    calibration_line = "pqr3stu8vwx"
    expected_calibration_value = 38
    calibration_reader = CalibrationReader(calibration_line)
    actual_calibration_value = calibration_reader.read()
    assert expected_calibration_value == actual_calibration_value

def test_go_throught_string_line_to_find_digits_and_use_only_first_and_Last_digit():
    calibration_line = "a1b2c3d4e5f"
    expected_calibration_value = 15
    calibration_reader = CalibrationReader(calibration_line)
    actual_calibration_value = calibration_reader.read()
    assert expected_calibration_value == actual_calibration_value

def test_with_single_digit():
    calibration_line = "treb7uchet"
    expected_calibration_value = 77
    calibration_reader = CalibrationReader(calibration_line)
    actual_calibration_value = calibration_reader.read()
    assert expected_calibration_value == actual_calibration_value

def test_sum_all_lines():
    calibration_doc = CalibrationDocument("all_lines.txt")
    expected_calibration_sum = 54632 

    actual_calibration_sum = calibration_doc.sum()

    assert expected_calibration_sum == actual_calibration_sum
