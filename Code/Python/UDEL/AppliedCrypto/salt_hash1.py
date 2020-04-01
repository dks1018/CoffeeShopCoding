import bcrypt, hashlib,time

# encryption funciton
def encryptPass(password):
    #print("Hash this value:",password)
    salt = bcrypt.gensalt()
    hash_enc = hashlib.sha512(password.encode('utf8') + salt)
    return hash_enc.hexdigest()
    

# Variables and user input
counter = 0 # counter for how many times to hash it in the while loop
hash_val = str(input("Enter the string you want to hash: ")) # string to hash
num_hashes = int(input("Enter the number of times to hash: ")) # this is the amount of time to call the encrypt function
pass_count = 1 # add a number so you know how many times the hash has been run
start_time = time.time() # start the timer

# loop with function call
while counter < num_hashes:
    tryThis = encryptPass(hash_val)
    hash_val = tryThis # After calling the function when it returns set the new hash equal to hash val
    #print(pass_count,"The password is:",tryThis, "\n") # print out the new password hash so we know what is being run in the program
    counter += 1 # simple counter to keep track of amount of hashes
    pass_count +=1 # simple hash counter on to print
print(pass_count,"The password is:",tryThis, "\n")
endtime = time.time() - start_time # end the timer after the loop
print("This program took:",endtime,"seconds!") # print how much time it took




# starttime = timeit.default_timer()
# print("The start time is:",starttime)
# print(starttime)
#print("The time difference is :",timeit.default_timer() - starttime)