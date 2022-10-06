from prefect import flow, task
from prefect.blocks.system import Secret

@task
def get_secret(name):
    secret_block = Secret.load(name)
    print(secret_block.get())

@flow
def runall():
    x = get_secret("test-block")
    
if __name__ == "__main__":
    runall()
