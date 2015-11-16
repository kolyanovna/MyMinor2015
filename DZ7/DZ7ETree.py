
words={}
for i in range(0,int(input())):
    string = input().split()
words.update(dict.fromkeys(string[1,string[0]]))
for i in range(0,int(input())):
    print(words.get(input()))
