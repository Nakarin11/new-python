#num = int(input("Enter a number: "))

#def prime(n):
#    if n < 2:
#        return False
#    for i in range(2, int(n ** 0.5) + 1):
#        if n % i == 0:
#            return False
#    return True
#
#primeNum = [i for i in range(2, num + 1) if prime(i)]
#print(primeNum)

#------------------------------------------------------------------------#

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(generate_primes(10))
print(generate_primes(20))
print(generate_primes(1))
print(generate_primes(2))
