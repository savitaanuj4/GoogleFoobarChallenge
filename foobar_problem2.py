def solution(l):
    # Your code here
    l = [i.split('.') for i in l]
    l = [[int(j) for j in i] for i in l]
    l.sort()
    l = [[str(j) for j in i] for i in l]

    l = ['.'.join(i) for i in l]
    temp_string = ''
    
    return ','.join(l)

print solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])