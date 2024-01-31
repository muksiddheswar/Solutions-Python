if __name__ == '__main__':
    N, M, Q = input().split()
    for i in range(int(Q)):
        a, b = input().split()        
        connected = []
        day = -1
        for j in range(int(M) -1):
        # for j in range(int(M), 1, -1):
            count =1 
            divisor = int(M) - j
            while count * divisor  <= int(N):
                connected.append(count * divisor)
                if int(a) in connected and int(b) in connected:
                    day = j + 1
                    break
                count += 1
        if day < 1:
            day = int(M)
        print(day)