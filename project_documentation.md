# 📋 Project Management Document

# Project Name

AI Text Summarizer

# Project Owner

Nekkanti Satya Srinath

# Project Type

Generative AI Application

# Project Duration

June 2026

# Project Status

✅ Completed

---

# 1. Project Overview

The AI Text Summarizer is a Generative AI application developed using Streamlit, Ollama, and OpenAI. The system allows users to upload or paste text and generate concise summaries using multiple Large Language Models (LLMs).

The application supports local inference through Ollama and cloud-based inference through OpenAI while providing multiple summary formats and export options.

---

# 2. Business Problem

Large documents require significant time to read and analyze.

Users need:

* Faster content understanding
* Reduced reading effort
* Quick extraction of important information
* Support for multiple document formats

---

# 3. Project Objectives

### Primary Objectives

* Build an AI-powered summarization platform
* Support local and cloud LLMs
* Process large documents efficiently
* Provide multiple summary formats

### Secondary Objectives

* Improve user experience through streaming
* Enable document exports
* Provide performance analytics

---

# 4. Scope

## In Scope

* Text Summarization
* PDF Processing
* DOCX Processing
* TXT Processing
* OpenAI Integration
* Ollama Integration
* Live Streaming
* Export Functionality

## Out of Scope

* User Authentication
* Database Storage
* Multi-user Support
* Cloud Deployment

---

# 5. Functional Requirements

### FR-1

User shall upload:

* TXT
* PDF
* DOCX

files.

### FR-2

User shall generate:

* Short Summary
* Detailed Summary
* Bullet Point Summary

### FR-3

User shall choose AI provider:

* Ollama
* OpenAI

### FR-4

User shall download summary as:

* TXT
* PDF
* DOCX

### FR-5

System shall support large document chunking.

### FR-6

System shall display:

* Word Count
* Summary Word Count
* Reduction Percentage
* Execution Time

---

# 6. Non-Functional Requirements

### Performance

* Small documents processed within seconds.
* Large documents processed using chunking.

### Reliability

* Handle invalid files gracefully.
* Prevent application crashes.

### Usability

* Simple Streamlit UI.
* Minimal learning curve.

### Maintainability

* Modular architecture.
* Reusable functions.

---

# 7. System Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Document Processor
 │
 ▼
Chunking Engine
 │
 ▼
Prompt Builder
 │
 ▼
AI Provider Layer
 ├── Ollama
 └── OpenAI
 │
 ▼
Summary Generator
 │
 ▼
Output Formatter
 │
 ▼
Downloads & Metrics
```

---

# 8. Technology Stack

Frontend:

* Streamlit

Backend:

* Python

AI Models:

* Ollama
* OpenAI

Libraries:

* Requests
* PyPDF
* Python-Docx
* ReportLab

---

# 9. Project Phases

## Phase 1

Planning

Deliverables:

* Requirements gathering
* Architecture design

Status:
✅ Completed

---

## Phase 2

Core Development

Deliverables:

* Streamlit UI
* Ollama Integration

Status:
✅ Completed

---

## Phase 3

Advanced Features

Deliverables:

* Chunking
* Multiple Summary Types
* Metrics

Status:
✅ Completed

---

## Phase 4

AI Enhancement

Deliverables:

* OpenAI Integration
* Prompt Engineering
* Streaming Responses

Status:
✅ Completed

---

## Phase 5

Export & Documentation

Deliverables:

* PDF Export
* DOCX Export
* README
* Documentation

Status:
✅ Completed

---

# 10. Risks and Mitigation

| Risk            | Impact | Mitigation         |
| --------------- | ------ | ------------------ |
| Large Documents | High   | Chunking Strategy  |
| Hallucinations  | Medium | Prompt Engineering |
| Slow Inference  | Medium | Lightweight Models |
| Invalid Files   | Medium | Validation Checks  |

---

# 11. Challenges Faced

### Challenge 1

Large document processing.

Solution:
Chunking implementation.

### Challenge 2

Output formatting.

Solution:
Custom output cleaning.

### Challenge 3

Model hallucinations.

Solution:
Strict prompt constraints.

### Challenge 4

Performance on low-end hardware.

Solution:
Model optimization and token control.

---

# 12. Achievements

✅ OpenAI Integration

✅ Ollama Integration

✅ Streaming Responses

✅ Large Document Chunking

✅ Multiple Summary Types

✅ Export Functionality

✅ Analytics Dashboard

✅ Multi-Model Support

---

# 13. Success Metrics

| Metric            | Result |
| ----------------- | ------ |
| Summary Types     | 3      |
| File Formats      | 3      |
| AI Providers      | 2      |
| Export Formats    | 3      |
| Streaming Support | Yes    |
| Chunking Support  | Yes    |

---

# 14. Future Roadmap

### Phase 2 Enhancements

* Model Comparison
* Summary Length Control
* Keyword Extraction

### Phase 3 Enhancements

* RAG Integration
* Vector Database
* User Authentication

### Phase 4 Enhancements

* YouTube Summarization
* Audio Summarization
* Cloud Deployment

---

# 15. Project Closure Report

Project Name:
AI Text Summarizer

Status:
✅ Successfully Completed

Outcome:
Delivered a production-ready AI summarization platform supporting multiple LLM providers, document formats, export options, streaming responses, and large document processing.

Lessons Learned:

* Prompt Engineering
* LLM Integration
* Streamlit Development
* Performance Optimization
* Document Processing Pipelines

Project Closure Date:
June 2026

