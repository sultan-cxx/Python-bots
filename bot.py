import time
from colorama import Fore, Style, init
init(autoreset=True)
print('hello')

def speak(msg):
    print(Fore.GREEN + 'Complex BOT:  '+ msg)
def ask(prompt):
    return input(Fore.CYAN + prompt + '\nYOU:  ').strip()
def highlight(msg):
    print(Fore.YELLOW + msg)
def error(msg):
    print(Fore.RED + msg)

#welcoming note
speak('''Hello there welcome to complex company  you number one trusted partner in tech enterpreneurship
Please feel at home as we continue on this tech voyage''')

name = ask(' May I know your name please')

#service
service = ['Trade', 'Banking', 'Investiment', 'Any Other Business']
speak(f''' {name} Here at  complex we offer many services
These services include: ''')
for i, s in enumerate(service, start=1):
    print(Fore.MAGENTA + f"{i}. {s}")

#selection
while True:
    action = ask('\nplease select a service with a number or index(eg; 1)').strip()
    if not action.isdigit():
       error('Invalid choice. Integers only.')
       continue

    index = int(action) - 1
    if 0 <= index < len(service):
        chosen_service = service[index]
        break
    else:
        highlight('''Value out of range (range = 1 to 4) ''')
error('*'*78)
        
      #TRADE WING
      
if chosen_service == 'Trade':
    highlight( '\n '*3 + '          Accessing please wait.........')
    time.sleep(2)
    print(Fore.BLUE, '\nCOMPLEX TRADE PLATFORM')
    time.sleep(1)
    speak(f'''{name} Welcome to our trade platform here is where all our supply is held
We have to main cartegories of products: ''')
    products = ['Digital products', 'Physical products']
    for i, s in enumerate(products, start = 1):
        print(Fore.MAGENTA, f'{i}. {s}')
     
   #product selection
    while True:
        action1 = ask('What products would you like today? ')
        
        if not action1.isdigit():
              error('Invalid choice. Enter a number.')
              continue

        index = int(action1) - 1
        if 0 <= index < len(products):
             chosen_product = products[index]
             break
        else:
              highlight('Value out of range')
        if chosen_product == 'Digital products':
            speak('digital product menu is being initialised please wait....')
            time.sleep(1)
            highlight('\nDIGITAL PRODUCTS')          
    
            d_pdcts =['apps', 'websites', 'security tools', 'gadgets']
        for i,s in enumerate(d_pdcts, start =1):
            print(Fore.MAGENTA, f'{i}. {s}')
        
        #selling
        while True:
             action2 = ask('Please select one by index')
             if not action2.isdigit():
                 error('Invalid choice. Enter a number.')
                 continue

             index = int(action2) - 1
             if 0 <= index < len(d_pdcts):
                 chosen_pdcts = d_pdcts[index]
                 break
             else:
                 highlight('Value out of range')
        if chosen_d_pdct == 'apps':
            speak('please pick app cartegory that suits you')
            
 

elif chosen_service =='Banking':
            print('damn')
            