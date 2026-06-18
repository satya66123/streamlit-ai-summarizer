# 📄 AI Text Summarizer

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green?logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

An AI-powered Text Summarizer built with **Streamlit**, supporting both **Ollama Local Models** and **OpenAI Models** for generating concise, detailed, and bullet-point summaries from text and documents.

---

# 🚀 Features

### 🤖 AI Providers

* Ollama (Local LLMs)
* OpenAI

### 🧠 Supported Models

#### Ollama

* Qwen2.5 1.5B
* Gemma2 2B
* Phi3
* Gemma3 4B
* Mistral
* Llama3 8B

#### OpenAI

* GPT-4o Mini
* GPT-4o

---

### 📋 Summary Types

* Short Summary
* Detailed Summary
* Bullet Point Summary

---

### 📂 Supported Files

* TXT
* PDF
* DOCX

---

### ⚡ Additional Features

* Live Streaming Responses
* Large Document Chunking
* Summary History
* Processing Time Tracking
* Word Count Analysis
* Reduction Percentage Calculation
* TXT Export
* PDF Export
* DOCX Export
* OpenAI + Ollama Integration
* Clean Output Formatting

---

# 🏗 Project Architecture

```text
AI Text Summarizer
│
├── app.py
│   ├── Streamlit UI
│   ├── File Uploads
│   ├── Downloads
│   ├── Metrics Dashboard
│   └── Streaming Output
│
├── summarizer.py
│   ├── Ollama Integration
│   ├── OpenAI Integration
│   ├── Chunking Engine
│   ├── Prompt Builder
│   ├── Summary Generator
│   └── Output Formatter
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Tech Stack

* Python
* Streamlit
* Ollama
* OpenAI
* Requests
* PyPDF
* Python-Docx
* ReportLab

---

# 📈 Workflow

```text
User Input
     │
     ▼
Paste Text / Upload File
     │
     ▼
Word Count Check
     │
     ├── Small Document
     │         │
     │         ▼
     │    Direct Summary
     │
     └── Large Document
               │
               ▼
          Chunking
               │
               ▼
        Chunk Summaries
               │
               ▼
         Final Summary
               │
               ▼
        Output Cleaning
               │
               ▼
       Download Options
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

Install Ollama:

https://ollama.com

Pull models:

```bash
ollama pull qwen2.5:1.5b
ollama pull gemma2:2b
ollama pull phi3
ollama pull gemma3:4b
ollama pull mistral
ollama pull llama3:8b
```

Start Ollama:

```bash
ollama serve
```

---

# 🤖 OpenAI Setup

Add your OpenAI API key inside the application.

Supported models:

```text
gpt-4o-mini
gpt-4o
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 Features Implemented

| Feature              | Status |
| -------------------- | ------ |
| Ollama Integration   | ✅      |
| OpenAI Integration   | ✅      |
| TXT Upload           | ✅      |
| PDF Upload           | ✅      |
| DOCX Upload          | ✅      |
| Live Streaming       | ✅      |
| Chunking Support     | ✅      |
| Summary History      | ✅      |
| TXT Export           | ✅      |
| PDF Export           | ✅      |
| DOCX Export          | ✅      |
| Word Count Metrics   | ✅      |
| Reduction Percentage | ✅      |
| Processing Time      | ✅      |
| Multi-Model Support  | ✅      |

---

# 🧩 Design Decisions

### Why Chunking?

Large Language Models have context limitations.

Chunking allows large documents to be broken into smaller sections, summarized independently, and merged into a final summary.

---

### Why Ollama?

* Free
* Offline Usage
* Privacy Friendly
* No API Costs

---

### Why OpenAI?

* Higher Quality Summaries
* Better Reasoning
* Faster Cloud Inference

---

### Why Streamlit?

* Rapid Development
* Simple UI Creation
* Excellent for AI Applications

---

# 📝 Project Planning

### Phase 1

* Streamlit Setup
* Ollama Integration
* Basic Summarization

### Phase 2

* Multiple Models
* Summary Types
* Metrics Dashboard

### Phase 3

* PDF Support
* DOCX Support
* Chunking

### Phase 4

* OpenAI Integration
* Streaming Responses
* Export Features

### Phase 5

* Documentation
* Optimization
* Deployment Ready

---

# 🎯 Challenges Solved

### Large Documents

Implemented chunk-based summarization.

### Hallucinations

Applied prompt engineering to restrict summaries to source content.

### Formatting

Created custom output cleaning for:

* Short Summaries
* Detailed Summaries
* Bullet Point Summaries

### Performance

Optimized prompts and token limits for low-end hardware.

---

# 💼 Resume Bullet Points

* Developed an AI-powered Text Summarization application using Streamlit, Ollama, and OpenAI.
* Implemented support for multiple LLMs including GPT-4o, Qwen, Gemma, Phi3, Mistral, and Llama.
* Built a chunking-based pipeline for efficient large document summarization.
* Added real-time streaming responses for improved user experience.
* Integrated PDF, DOCX, and TXT document processing.
* Implemented export functionality for TXT, PDF, and DOCX formats.
* Designed analytics for word count, summary reduction percentage, and execution time tracking.
* Applied prompt engineering techniques to improve summary quality and reduce hallucinations.

---

# 🎤 Interview Questions

### How does the summarizer handle large documents?

Large documents are split into chunks, summarized individually, and then merged into a final summary.

---

### Why support both OpenAI and Ollama?

OpenAI provides cloud-based high-quality inference while Ollama enables local and private execution.

---

### How is hallucination reduced?

Prompt constraints ensure that summaries are generated only from information present in the source text.

---

### Why use Streamlit?

Streamlit enables rapid development of interactive AI applications without extensive frontend development.

---

### What optimization techniques were used?

* Chunking
* Token Control
* Prompt Engineering
* Streaming Responses
* Model Selection

---

# 🏷 GitHub Topics

```text
ai
artificial-intelligence
llm
ollama
openai
streamlit
python
summarization
text-summarizer
generative-ai
machine-learning
nlp
pdf-processing
docx-processing
gpt4o
qwen
gemma
llama
phi3
```

---

# 🔮 Future Enhancements

* Model Comparison Dashboard
* Summary Length Slider
* Keyword Extraction
* Named Entity Recognition
* YouTube Video Summarization
* Audio Summarization
* Translation Support
* RAG-Based Document Q&A
* User Authentication
* Cloud Deployment

---

# 🎯 Project Status

![Completed](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

![Production Ready](https://img.shields.io/badge/Production%20Ready-Yes-brightgreen?style=for-the-badge)

![Open Source](https://img.shields.io/badge/Open%20Source-Ready-blue?style=for-the-badge)

## ✅ Completed Features

* [x] Ollama Integration ✅
* [x] OpenAI Integration ✅
* [x] Live Streaming ✅
* [x] TXT Upload ✅
* [x] PDF Upload ✅
* [x] DOCX Upload ✅
* [x] Chunking Engine ✅
* [x] Summary History ✅
* [x] TXT Export ✅
* [x] PDF Export ✅
* [x] DOCX Export ✅
* [x] Analytics Dashboard ✅
* [x] Prompt Engineering ✅
* [x] Output Formatting ✅

---

## 🚀 Current Status

🟢 **Project Completed and Portfolio Ready**

---

# 📄 License

MIT License

Copyright (c) 2026 satya


---

# 👨‍💻 Author

Built with Python, Streamlit, Ollama, OpenAI, and modern LLM workflows.

👨‍💻 Author

## Nekkanti Satya Srinath

🔗 GitHub: https://github.com/satya66123

🔗 Project Repository: https://github.com/satya66123/streamlit-ai-summarizer

🔗 LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/

---

# 🎯 Project Status

🟢 Status: Completed and Portfolio Ready