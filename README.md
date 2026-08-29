# Multi-Agent-AI-Research-System

## 📝 Description

**ResearchMind** — A multi-agent AI research system that automatically searches the web, analyzes sources, generates structured research reports, and evaluates them using specialized LLM-powered agents. Built with LangChain and Streamlit, featuring a modern dark-mode interface.

## 🛠️ Tech Stack

Language: Python 3
Framework / runtime: Streamlit (web UI) + LangChain (agentic orchestration)
Notable libraries:
OpenAI GPT-4o-mini (LLM backbone)
Tavily Search API (web search)
BeautifulSoup + requests (web scraping)
LangChain agents & chains for agentic workflow

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/Chandangorain/Multi-Agent-AI-Research-System/tree/main.git

# 2. Create & activate a virtualenv
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 📦 Key Dependencies

```
langchain: 0.2.0
langchain-core: 0.2.0
langchain-community: 0.2.0
langchain-openai: 0.1.0
openai: 1.30.0
tavily-python: 0.3.0
beautifulsoup4: 4.12.0
requests: 2.31.0
lxml: 5.0.0
python-dotenv: 1.0.0
aiohttp: 3.9.0
pandas: 2.0.0
tiktoken: 0.6.0
rich: 13.7.0
tenacity: 8.2.0
```

## 📁 Project Structure

```
.
├── App.py
├── agents.py
├── pipeline.py
├── requirements.txt
└── tools.py
```

## 🛠️ Development Setup

### Python
1. Install Python (v3.10+ recommended)
2. `python -m venv venv && source venv/bin/activate`  (Windows: `venv\Scripts\activate`)
3. `pip install -r requirements.txt`

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/Chandangorain/Multi-Agent-AI-Research-System/tree/main.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a pull request

Please follow the existing code style and include tests for new behavior where applicable.

---

<div align="center">

[![Made with ReadmeBuddy](https://img.shields.io/badge/Made%20with-ReadmeBuddy-8B5CFF?style=for-the-badge&logo=markdown&logoColor=white)](https://readmebuddy.com)

<sub>Generate beautiful READMEs in seconds → <a href="https://readmebuddy.com">readmebuddy.com</a></sub>

</div>
