import os
import click
import uvicorn
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option('--host', default='127.0.0.1', help='Host address')
@click.option('--port', default=8000, help='Port')

def main(host, port):
  uvicorn.run(
    app="app.server:app",
    host=host,
    port=port,
    reload=True,
    workers=1
  )

if __name__ == "__main__":
  main()