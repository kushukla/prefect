from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
import yfinance as yf

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def download(ticker):
    print(ticker+'abc')
    return yf.download(ticker)

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def head(df):
    print(df.head())

@flow
def runall():
    x = download('CSCO')
    head(x)
    
if __name__ == "__main__":
    runall()
