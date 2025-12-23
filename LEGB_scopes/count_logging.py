count = 10
def foot():
    count= 11
    print(count)
foot()
print(count)

logging_level = 'DEBUG'
def log_message(message):
    logging_level = 'INFO'
    print(f'[{logging_level}] {message}') 
    message("Thanks for coming...")
    
    (message)