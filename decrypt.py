from random import randint
import sys

def gcd(a,b):
    
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    
    return a * b / gcd(a, b)

def extended_euclidean_algorithm(a, b):
    
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    
    #gives m (n * m)%p = 1.
    
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

def L(x,n):
	return ((x-1)//n)

p=17
q=19
m=0
cipher=0
#attempt at file input for Review 3
########### script for reading from file

with open('/media/sf_Shared_Docs/result.txt','r+') as f:
    data=int(f.read())
    cipher=data
    
########### script ends

if (len(sys.argv)>1):
	m=int(sys.argv[1])

if (len(sys.argv)>2):
	p=int(sys.argv[2])

if (len(sys.argv)>3):
	q=int(sys.argv[3])

if (p==q):
	print ("P and Q cannot be the same")
	sys.exit()

n = p*q

gLambda = lcm(p-1,q-1)

g = 44
r = 129


l = (pow(int(g), int(gLambda), int(n*n))-1)//n
gMu = inverse_of(l, n)

k1 = pow(g, m, n*n)
k2 = pow(r, n, n*n)

l = (pow(int(cipher), int(gLambda), int(n*n))-1) // n

mess= (l * gMu) % n
print("Data Recieved from Cloud: ", cipher)
print("Data Wrote Into File As BP: ",mess)
out=open('/media/sf_Shared_Docs/BloodPressure.txt','w')
out.write(str(mess))
out.close()
