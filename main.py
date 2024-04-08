# Built-in imports
def reverse(text):
    '''
    Return text string reversed 
    '''
    if len(text) <= 1:
        return text 
    else:
        return reverse(text[1:]) + text[0]            

def is_palindrome(text):
    ''' 
    Tests if text is a palindrome
    '''
    text = text.lower()
    text = text.strip()
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for i in punctuation:
        text = text.replace(i, '')
        if len(text) <= 1:
            return True  
        elif len(text) == 2:
            return text[0] == text[1]
        else:
            if text[0] == text[-1]:
                return is_palindrome(text[1:-1])
            else:
                return False
            
    
        
        

