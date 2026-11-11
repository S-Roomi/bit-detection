# **Bit-Detection**  
Colaborators: Royce Nogales, Sina Roomi  
Email: roycen1@umbc.edu, sinar1@umbc.edu  

## **Project Description** 
A simple project to analyze how well Large Language Models (LLMs) detect irregularities in provided random data. The core of the project is in src/bit_detection, where main.py calls the objects from bit_create.py and imagine_gen.py. bit_create is an object that manipulates large bit arrays and has several functions to bias said arrays.

## **Installation**  
Project requires uv package manager

To install uv 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After cloning the repository, run the following
```
uv sync
source .venv/bin/activate
uv pip install -e .
```
## **How to Run**
```
## runs src/bit_detection/main.py
bd
```

## **LLM/AI Prompts Used**
Look in results folder for appropriate prompts and chats
