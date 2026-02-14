# Local Translator

A simple local CLI translator powered by Ollama.
It translates text from one language to another using a locally running LLM.

Currently configured for:

- Italian → English translation
- Fully local inference
- Automatic copy of the response to the clipboard

---

## Features

- Runs entirely locally (no external APIs)
- Uses Ollama models
- Clean CLI interface
- Configurable model and languages
- Automatic model download (if missing)
- Copies translation to clipboard

---

## Requirements

- Python 3.9+
- Ollama installed and running locally

Install Ollama from:
https://ollama.com

---

## Install

Clone the repository, create and activate a virtual environment and install the dependencies:

```
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

---

## Configuration

You can configure:
- Model name
- Source language
- Target language

Example:
```yaml
model_name: translategemma:4b

source:
  lang: italian
  code: it

target:
  lang: english
  code: en
```

---

## Usage

```
python main.py
```
