from src.finding_numbers import CalibrationReader

def test_read_calibration_line():
    calibration_line = "1abc2"          #input
    expected_calibration_value = 12             #output
    calibration_reader = CalibrationReader()  #process
    #every class has an empty constractor as default
    actual_calibration_value = calibration_reader.read(calibration_line)
    assert expected_calibration_value == actual_calibration_value

