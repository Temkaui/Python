import md5 # imports the md5 module to generate a hash
import os, binascii
salt = binascii.b2a_hex(os.urandom(15))
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password + salt).hexdigest()
print salt
print hashed_password