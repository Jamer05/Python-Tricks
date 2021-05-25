import sys
import time 
import os 
import requests
import hashlib

from time import sleep


# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "loading IYPP..."
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 40): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
banner = r'''
   ___   ___                         
      / /\\    / / //   ) ) //   ) ) 
     / /  \\  / / //___/ / //___/ /  
    / /    \\/ / / ____ / / ____ /   
   / /      / / //       //          
__/ /___   / / //       //           
                      
Is Your Password Pawned?
Author: Jamer05
'''
#colours
def p_green(skk): print("\033[92m {}\033[00m" .format(skk),end="")
def p_red(skk): print("\033[91m {}\033[00m" .format(skk),end="")  
red = "\033[91m {}\033[00m"
p_red(banner)


p_green("\nChecking the password!...")



runs = 10
for run_num in range(runs):
    time.sleep(.1)
    print("",end="")
  

if len(sys.argv) == 1:
	print(f'Usage: "python3 pwn.py <PASSWORD>"\n(Use "-h" option for more info)')
	sys.exit()
if '-h' in sys.argv or '--help' in sys.argv:
	print('''
Example usage: python3 pwn.py 1234 
-h                     To show this message''')
	sys.exit()


def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)
  


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
             print('\n')
             p_green("Password")
             p_red(f'"{password}"''\n')
             p_green("Result:")
             p_red('***Pwned***')
             p_green('\n'+" Note:")
             p_red(f'This password has been seen {count} times before \nyou better to change your password immedietly\n')
        else:
            print('\n')
            print(f'\n{password} was not found in any kind of Data breaches . Congrats!')           

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

