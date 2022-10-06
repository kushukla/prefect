from prefect import flow, task


## a^2+b^2+c

@task
def square(x: float):
    return x*x

@task 
def add(a: float, b: float):
    return a+b

@flow
def solve(a=[10.0, 20.0], c=30.0):
    
    x = 0.
    for b in a:
        y = square(b)
        x = add(x, y)
    z = add(x, c)
    print(f"solved: {z}")
    
if __name__ == "__main__":
    solve()