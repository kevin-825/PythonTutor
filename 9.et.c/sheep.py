#this is example of yield kerword, how the generator function work

def main():
    N=10
    for s in sheep1(N):
          print(s)
    
    for s in sheep2(N):
          print(s)

def count_to_n(N):
    n=0
    while n < N:
        yield n 
        n += 1

def sheep1(n):
    print("sheep1")
    sheeps=[]
    for i in range(n):
        sheeps.append("s"*i)
        print(f"sheep1 in loop {i}")
    print("sheep1 conting whole fluck of sheeps done")
    return sheeps

def sheep2(n):
    print("sheep2")
    for i in range(n):
        yield "s"*i
        print(f"sheep2 in loop {i}")
    print("sheep2 conting whole fluck of sheeps done")

if __name__ == "__main__":
    main()
