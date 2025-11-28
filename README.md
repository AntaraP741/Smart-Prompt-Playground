# Smart Prompt Playground

## Overview

Smart Prompt Playground is an applied AI project that demonstrates how large language model behavior changes with **system prompts, temperature tuning, and conversational memory**.
The application is built using **LangChain**, **Streamlit**, and **LLaMA-3 via the Groq API**.

This project serves as a foundational step toward building **production-ready chatbots, RAG systems, and agent-based AI workflows**.

---

## Problem

LLM-based applications often behave unpredictably when prompt structure, temperature, and memory are poorly controlled.
This project explores how to reliably guide model responses through controlled experimentation.

---

## Solution

A chat application was built where:

* System prompts define model personality and constraints
* Conversation history is preserved across interactions
* Temperature controls response variability
* Model outputs are evaluated under fixed prompts

This structured setup enables repeatable analysis of LLM behavior.

---

## Features

* Context-aware chatbot with conversation memory
* System prompt–controlled behavior
* Temperature-based response variability
* Streamlit-based interactive UI
* LangChain-based message handling

---

## Architecture

```
User Input → Streamlit UI → LangChain Messages → LLM (Groq / LLaMA-3) → Response
```

---

## Tech Stack

* Python
* LangChain
* Groq API
* LLaMA-3.1-8B-Instant
* Streamlit
* dotenv

---

## Key Learnings

* Temperature affects response randomness, not model accuracy
* Strong system prompts reduce behavioral drift
* Memory amplifies both prompt quality and errors
* Lower temperatures are ideal for factual and RAG systems

---

## Industry Relevance

This project builds core skills used in:

* Conversational AI systems
* Prompt engineering
* Applied LLM development
* RAG pipelines
* AI agent workflows

---

## Setup

```bash
git clone https://github.com/AntaraP741/Smart-Prompt-Playground.git
cd smart-prompt-playground
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## Future Enhancements

* UI-based temperature control
* RAG integration with document retrieval
* Tool-enabled agents
* Deployment as an internal AI utility

---

## Author

**Antara Prasad**
Computer Engineering | Applied AI | LLM Systems
GitHub: [https://github.com/AntaraP741](https://github.com/AntaraP741)
