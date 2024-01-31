if __name__ == '__main__':
	t = int(input())
	for i in range(t):
            b = input()
            a = []
            a.append(b[0])

            index = 1
            while index < len(b):
                a.append(b[index])
                index += 2
            # a.append(b[-1])
            a = ''.join(a)
            print(a)
                
                
                
	
