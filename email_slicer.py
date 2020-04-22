'''
The email slicer is a handy program to get the username and domain name from an email address. 
You can customize and send a message to the user with this information.
'''

# imports
import re

document_to_slice = 'benny lives in juja and ian@gsad ben2020.com yy291Y@yahoo.com istan@gmasi com his email address is bennyhinnpotieno@gmail.com john has an emialj302sd@hotmail.com'

# TODO: WORK ON THE PATTERN - .COM PART
# Function to get email from strings of words/document.
def email_slicer(document_to_slice):
    '''
    Takes an document(string) argument and returns a list of email matches.
    '''

    # Generate email pattern
    pattern = re.compile(r'''(
    [a-zA-Z0-9]+                # benny or bera200 or hiHsad334
    @                # @
    [a-zA-Z0-9.]+     # gmail or live or hotmail or asd332 plus .
    [a-zA-Z]{,6}                # last part - com/co
    
    )''',re.VERBOSE)

    # searching for pattern
    found_pattern = pattern.findall(document_to_slice)
    print(found_pattern) 
    print('--'*20) 
    for email in found_pattern:
        print(email)


if __name__ == '__main__':
    email_slicer(document_to_slice)