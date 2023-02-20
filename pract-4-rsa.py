import math


def is_prime(num):
  if num == 1:
    return False
  range_of_num = range(2, num-1)
  for i in range_of_num:
    if num%i == 0:
      return False
  return True

p,q = 0,0

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
e = 2
phi = (p-1)*(q-1)

while (e < phi):

	if(math.gcd(e, phi) == 1):
		break
	else:
		e = e+1

k = 2
d = (1 + (k*phi))/e

msg = 0
while True:
  msg_raw = input("Enter the plain text: ")
  try:
    msg = int(msg_raw)
  except ValueError:
    print("Please enter a number!")
  else:
    break

print("Plain Text: ", msg)

c = pow(msg, e)
c = math.fmod(c, n)
print("Cipher Text: ", c)

m = pow(c, d)
m = math.fmod(m, n)
print("Decipher Text: ", m)



