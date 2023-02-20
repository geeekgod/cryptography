import math
from sympy import *

def is_prime(num):
  if num == 1:
    return False
  range_of_num = range(2, num-1)
  for i in range_of_num:
    if num%i == 0:
      return False
  return True


def key_gen():
  public_key = {}
  private_key = {}
  global n, e, d

  # default values
  p,q = 3,7

  while True:
    p_raw = input("Enter the value of p: ")
    try:
      p = int(p_raw)
    except ValueError:
      print("Please enter a number!")
    else:
      if is_prime(p):
        break
      else:
        print("Please enter a prime number!")


  while True:
    q_raw = input("Enter the value of q: ")
    try:
      q = int(q_raw)
    except ValueError:
      print("Please enter a number!")
    else:
      if is_prime(q):
        break
      else:
        print("Please enter a prime number!")

  n = p*q
  e=2
  phi = (p-1)*(q-1)

  while (e < phi):

    if(math.gcd(e, phi) == 1):
      break
    else:
      e = e+1

  k = 2
  d = (1 + (k*phi))/e

  print(e,n)
  public_key[e]=n
  private_key[d]=n
  print("Public key : {p_k}\nPrivate Key: {pr_k}".format(p_k=public_key,pr_k=private_key))

def cryptography():
  key_gen()
  print(n,d,e)
  plain_text=input("Enter the plain text: ")
  plain_text_list = []
  cipher_list = []
  decipher_list=[]
  for i in plain_text:
    ascii_code_of_char = ord(i)
    plain_text_list.append(ascii_code_of_char)

  print("Plain text: ", plain_text)
  print("Plain text list: ", plain_text_list)

  for i in plain_text_list:
    cipher = pow(i, e)
    cipher = math.fmod(cipher, n)
    cipher_list.append(int(cipher))

  cipher_text = "".join(map(lambda x: str(x), cipher_list))

  print("Cipher text: ", cipher_text)
  print("Cipher text list: ", cipher_list)

  for i in cipher_list:
    decipher = pow(float(i), d)
    decipher = math.fmod(decipher, n)
    decipher_list.append(int(decipher))

  decipher_text = "".join(map(lambda x: str(x), decipher_list))

  print("Decipher text: ", decipher_text)
  print("Decipher text list: ", decipher_list)

cryptography()
print(n,d,e)
