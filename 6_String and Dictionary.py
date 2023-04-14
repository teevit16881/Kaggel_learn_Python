"""
No.1
There is a saying that "Data scientists spend 80% of their time cleaning data,
and 20% of their time complaining about cleaning data." Let's see if you can write a function 
to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. 
For our purposes, a valid zip code is any string consisting of exactly 5 digits.
"""

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    num_str = ['0','1','2','3','4','5','6','7','8','9']
    if all(num in num_str for num in zip_code) and len(zip_code) == 5:
        return True
    return False
