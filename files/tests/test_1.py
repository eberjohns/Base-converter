# test for base_conversion.py
import pytest
from files.code.base_conversion import convert_base  # Function name

def test_valid_conversion():
    assert convert_base(10, 10, 2) == "1010"
    assert convert_base(1101, 2, 10) == "13"
    assert convert_base(16, 10, 16) == "10"
    assert convert_base(255, 10, 16) == "FF"
    assert convert_base(10, 10, 16) == "A"
    assert convert_base(1010, 2, 16) == "A"
    #assert convert_base(10, 16, 2) == "1010"
    assert convert_base(0, 10, 2) == "0"
    assert convert_base(42, 10, 16) == "2A"
    assert convert_base(27, 10, 2) == "11011"

def test_invalid_from_base():
    with pytest.raises(ValueError) as excinfo:
        convert_base(10, 1, 2)
    assert "From base must be an integer >= 2." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        convert_base(10, -1, 2)
    assert "From base must be an integer >= 2." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        convert_base(10,"string",2)
    assert "From base must be an integer >= 2." in str(excinfo.value)

def test_invalid_to_base():
    with pytest.raises(ValueError) as excinfo:
        convert_base(10, 10, 1)
    assert "To base must be an integer >= 2." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        convert_base(10, 10, -1)
    assert "To base must be an integer >= 2." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        convert_base(10,10, "string")
    assert "To base must be an integer >= 2." in str(excinfo.value)

def test_invalid_input_number():
    with pytest.raises(TypeError) as excinfo:
        convert_base("string", 10, 2)
    assert "Input number must be an integer." in str(excinfo.value)

def test_invalid_digit():
    with pytest.raises(ValueError) as excinfo:
        convert_base(22, 2, 10) #22 is not a valid binary number
    assert "Digit 2 is not valid for base 2" in str(excinfo.value)
