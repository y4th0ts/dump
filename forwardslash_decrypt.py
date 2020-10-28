def encrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in key:
        for i in range(len(msg)):
            if i == 0:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[-1])
            else:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[i-1])

            while tmp > 255:
                tmp -= 256
            msg[i] = chr(tmp)
    return ''.join(msg)

def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)

#msg = 'Is this message long enough or should I keep typing? How about now? Hmm. Maybe this is long enough.'
#key = 'Sup3rS3cur3k3y'

#print encrypt(key, msg)
#print decrypt('REDACTED', encrypt('REDACTED', 'REDACTED'))

# Opens a file for outputing results.
outfile = open("decrypted_msg","a")

# Imports ciphertext string.
with open("ciphertext","r") as f:
    ciphertext = f.read().rstrip()

keys = []
# Imports wordlist to a list.
with open("/usr/share/wordlists/rockyou.txt","r") as f:
    for line in f:
        for word in line.split():
            keys.append(word)

# Bruteforces using words from rockyou.txt as keys. If 'chiv', 'pain', 'pass', or 'key'. is found,
# It breaks out of the loop and prints out the results on the terminal as well as in a file ' decrypted_msg'.
for i in range(len(keys)):
    print "Trying key: {}".format(keys[i])
    out = decrypt(keys[i], ciphertext)
    if 'chiv' in out.lower():
        outfile.write("Decrypted msg:\n "+out)
        outfile.write("\nKey Found: "+keys[i]+"\n")
        print "KEY FOUND: {}".format(keys[i])
        print "Decrypted msg: \n{}".format(out)
        break
    elif 'pain' in out.lower():
        outfile.write("Decrypted msg:\n "+out)
        outfile.write("\nKey Found: "+keys[i]+"\n")
        print "KEY FOUND: {}".format(keys[i])
        print "Decrypted msg: \n{}".format(out)
        break
    elif 'pass' in out.lower():
        outfile.write("Decrypted msg:\n "+out)
        outfile.write("\nKey Found: "+keys[i]+"\n")
        print "KEY FOUND: {}".format(keys[i])
        print "Decrypted msg: \n{}".format(out)
        break
    elif 'key' in out.lower():
        outfile.write("Decrypted msg:\n "+out)
        outfile.write("\nKey Found: "+keys[i]+"\n")
        print "KEY FOUND: {}".format(keys[i])
        print "Decrypted msg: \n{}".format(out)
        break

outfile.close()
