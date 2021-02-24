def solution(i):
    # Your code here
    temp_str = ''
    count =1
    while(len(temp_str)<i+5):
        if isPrime(count):
            temp_str += str(count)
        count+=1
        
    return temp_str[i:i+5]

def isPrime(num):
    if num > 1:
        for i in range(2, num//2 +1):
                if (num % i) == 0:
                    return False
                    break
        else:
            return True
    return False

print solution(3)
