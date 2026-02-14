from ollama import Client

def pull_model(model):
    client = Client()

    models = client.list()
    for m in models['models']:
        if model in m['model']:
            return

    print(f"Downloading {model} model")
    response = client.pull(model)
    if response.status == 'success':
        print(f"Download completed")
    else:
        print(f"Download failed")
        exit(1)
