# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:17:51 2022

@author: SKUP
"""

"""
Assuming that we have some email addresses in the "username@companyname.com" 
format, please write program to print the user name of a given email address.
 Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
"""

import re
pattern = "(\w+)@\w+.com"

pattern1 = "(\w+)@((\w+\.)(com))"

string = "suma@google.com"


res = re.findall(pattern, string)


res1 = re.match(pattern1,string)

print(res)

print(res1.group(2))