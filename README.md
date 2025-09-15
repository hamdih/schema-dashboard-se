# 🧠 Weaviate Schema Explorer

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)  
[![Streamlit](https://img.shields.io/badge/streamlit-app-red)](https://streamlit.io/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **Streamlit app** for visualizing and exploring **Weaviate schema JSON files**.  
This tool helps developers, solutions engineers, and data teams quickly inspect collections, vector index configs, class-level settings, and properties in a structured, user-friendly way.

---

## ✨ Features

✅ Upload a Weaviate schema (`.json`) and browse collections/classes  
✅ Detect whether a class uses **named vectors** or the default vector  
✅ Visualize key class-level configs:
- Inverted Index Config  
- Module Config  
- Multi-Tenancy Config  
- Replication Config  
- Sharding Config  

✅ Vector Index Insights:
- Compression types (**PQ, SQ, RQ**)  
- Dynamic indexing status  
- Tabular breakdown of vector index configuration  

✅ Property Explorer with expandable sections for each property  

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/weaviate-schema-explorer.git
cd weaviate-schema-explorer

### 2. **Install Dependencies**

Make sure you have Python 3.9+ installed, then run:

```bash
pip install -r requirements.txt
Your requirements.txt should look like this:

txt
Copy code
streamlit>=1.36.0
pandas>=2.0.0
Run the App

bash
Copy code
streamlit run app.py
Upload Your Schema

Export your Weaviate schema as JSON (via weaviate schema dump or API).

Upload it via the file uploader in the UI.

Explore collections, configs, and properties interactively.
