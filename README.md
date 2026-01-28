# 🧠 Medium Article Generator (Local LLM, Multi‑Agent System)

A **fully local, multi‑agent research & article generation system** built using **Agno Framework** and **Ollama**.  
This project allows you to type **one topic in CMD**, automatically research it from multiple sources, and generate a **long‑form, Medium‑style article (1500–2500 words)** — **without using any external APIs**.

> ✅ **No OpenAI / paid APIs**  
> ✅ **100% Local LLMs via Ollama**  
> ✅ **Multi‑agent research (Arxiv, Wikipedia, YouTube, News, Web, HackerNews)**  
> ✅ **Markdown output ready for Medium / GitHub / Blogs**

---

## 🚀 Key Features

- **Local LLM Execution** using Ollama (no API keys required)
- **Multi‑Agent Research System** (parallel research)
- **Automatic Research Saving** (raw notes per source)
- **Professional Medium‑Style Blog Generation**
- **Markdown (.md) Output** ready for publishing
- **Command‑Line Interface (CMD)** — simple & fast
- **In‑Memory Database** for session context

---

## 🧩 System Architecture Overview

```text
User Topic
   ↓
Research Agents (Parallel)
   ├── Arxiv Agent
   ├── Wikipedia Agent
   ├── HackerNews Agent
   ├── YouTube Agent
   ├── Newspaper Agent
   └── DuckDuckGo Web Agent
   ↓
Research Notes Saved (.txt)
   ↓
Team Orchestrator (Local LLM)
   ↓
Medium‑Style Article (.md)
```

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|-----------|
| Language | Python 3.10+ |
| Framework | Agno |
| LLM Runtime | Ollama (Local) |
| Database | InMemoryDB |
| Output Format | Markdown (.md) |
| Interface | Command Line |

---

## 🤖 Models Used (IMPORTANT)

> ⚠️ **This project uses ONLY LOCAL MODELS via Ollama**  
> ❌ **NO API CALLS**  
> ❌ **NO OPENAI / CLOUD BILLING**

### 🔹 Orchestrator Model (Team Leader)
```text
deepseek-v3.1:671b-cloud
```
- Responsible for:
  - Coordinating all agents
  - Synthesizing research
  - Writing final Medium‑style article

### 🔹 Research Agents Model
```text
gpt-oss:120b-cloud
```
- Used by:
  - Arxiv Agent
  - Wikipedia Agent
  - HackerNews Agent
  - YouTube Agent
  - Newspaper Agent
  - Web Search Agent

### 🔹 Ollama Host
```text
http://localhost:11434
```

> 🧠 **All inference happens locally on your machine via Ollama**

---

## 📂 Project Directory Structure

```text
project_root/
│
├── research_paper/
│   ├── arxiv_research_agent_AI.txt
│   ├── wikipedia_research_agent_AI.txt
│   └── ...
│
├── medium_articals/
│   ├── ai_future.md
│   └── machine_learning.md
│
├── app.py
├── README.md
```

---

## 🧠 Research Agents Explained

### 📄 Arxiv Research Agent
- Searches scientific & technical papers
- Extracts:
  - Methodology
  - Key findings
  - Conclusions

### 📰 HackerNews Research Agent
- Finds trending tech & AI discussions
- Extracts:
  - Opinions
  - Debates
  - Emerging trends

### 📚 Wikipedia Research Agent
- Provides:
  - Definitions
  - History
  - Core concepts

### 🎥 YouTube Research Agent
- Analyzes video transcripts & metadata
- Extracts:
  - Explanations
  - Examples
  - Key insights

### 🗞️ Newspaper Research Agent
- Gathers news articles
- Extracts:
  - Statistics
  - Quotes
  - Trends

### 🌐 Web Search Agent (DuckDuckGo)
- Searches blogs, forums, posts
- Provides real‑world insights

---

## 🧠 Team Orchestrator

The **Medium Article Creation Team**:

- Collects research from all agents
- Synthesizes information
- Writes:
  - Long‑form
  - Professional
  - Engaging
  - Medium‑style articles

### Output Rules
- ✅ Markdown only
- ❌ No file paths
- ❌ No raw tables
- ❌ No PC‑specific info

---

## ▶️ How to Run

### 1️⃣ Install Ollama
```bash
https://ollama.com
```

### 2️⃣ Pull Required Models
```bash
ollama pull deepseek-v3.1:671b-cloud
ollama pull gpt-oss:120b-cloud
```

> ⚠️ Ensure your system has sufficient RAM / GPU

### 3️⃣ Install Python Dependencies
```bash
pip install agno newspaper4k duckduckgo-search
```

### 4️⃣ Run the Application
```bash
python app.py
```

---

## 🖥️ CMD Usage

```text
🧠 Medium Article Generator (CMD Mode)
Type 'exit' to quit

>>> write a detailed article about Artificial Intelligence
```

### Workflow
1. Enter topic
2. Research agents run automatically
3. Raw research saved
4. Medium‑style article generated
5. Preview shown in terminal
6. Confirm to save (.md)

---

## 💾 Output Example

```text
medium_articals/
└── artificial_intelligence.md
```

Ready to publish on:
- Medium
- GitHub
- Hashnode
- Dev.to

---

## 🔒 Privacy & Cost

- ✅ 100% Offline
- ✅ No API keys
- ✅ No usage limits
- ✅ No hidden costs

---

## 🧪 Customization Ideas

- Change models in `Ollama()`
- Add more research agents
- Convert CMD to FastAPI
- Add citation formatter
- Auto‑publish to Medium

---

## ⚠️ Disclaimer

This project is for **educational & research purposes**.  
Ensure compliance with content platforms before publishing.

---

## ⭐ Support

If you find this project useful:
- ⭐ Star the repo
- 🧠 Fork & improve
- 📢 Share with others

---

## 👤 Author

**Abubakar Saddique**  
AI • Data Science • Multi‑Agent Systems

---

Happy Writing 🚀

