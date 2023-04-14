"""
No.1
There is a saying that "Data scientists spend 80% of their time cleaning data,
and 20% of their time complaining about cleaning data." Let's see if you can write a function 
to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. 
For our purposes, a valid zip code is any string consisting of exactly 5 digits.
"""

def is_valid_zip(zip_code):
    # Returns whether the input string is a valid (5 digit) zip code
    
    num_str = ['0','1','2','3','4','5','6','7','8','9']
    if all(num in num_str for num in zip_code) and len(zip_code) == 5:
        return True
    return False

"""
2.
A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

Your function should meet the following criteria:

Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.
"""

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.
    """
    result = []
    for i in doc_list:
        
        # split the sentence in to word list (tokenization)
        tokens = i.split()
        
        # remove symbol then lowercasing all characters (normalization)
        normalized = [token.rstrip(".,").lower() for token in tokens]
        
        #check
        check = any(keyword in normalized for word in normalized)
        if check == True:
            result.append(doc_list.index(i))
      
    return result
