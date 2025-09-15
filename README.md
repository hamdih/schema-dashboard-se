# se-schema-dashboard
🧠 Weaviate Schema Explorer

A Streamlit app for visualizing and exploring Weaviate schema JSON files.
This tool helps developers, solutions engineers, and data teams quickly inspect collections, vector index configs, class-level settings, and properties in a structured, user-friendly way.

✨ Features

Upload & Explore
Upload a Weaviate schema (.json) and browse collections/classes.

Named Vector Detection
Highlights whether a class uses named vectors or the default vector.

Config Visualizations
Displays key class-level configs:

Inverted Index Config

Module Config

Multi-Tenancy Config

Replication Config

Sharding Config

Vector Index Insights

Shows enabled compression types (PQ, SQ, RQ)

Flags dynamic indexing

Tabular breakdown of vector index configuration

Property Explorer
Expandable sections for each property with full details in a table view.

🚀 Getting Started
1. Clone the Repo
git clone https://github.com/your-username/weaviate-schema-explorer.git
cd weaviate-schema-explorer

2. Install Dependencies

Make sure you have Python 3.9+ installed, then:

pip install -r requirements.txt


requirements.txt should include:

streamlit
pandas

3. Run the App
streamlit run app.py

4. Upload Your Schema

Export your Weaviate schema as JSON (weaviate schema dump or via API).

Upload it via the file uploader in the UI.

Explore classes, configs, and properties interactively.

🖼️ Screenshot

(Optional: add a screenshot of the UI here)

🛠️ Tech Stack

Streamlit
 – interactive frontend

Pandas
 – table rendering

Weaviate
 – schema JSON source

📌 Roadmap

 Add search/filter across properties

 Support multiple schema file uploads

 Generate schema insights summary (e.g., number of classes, named vector usage %)

 Export explored view to Markdown/PDF

🤝 Contributing

PRs are welcome! Please open an issue first to discuss what you’d like to add.

📜 License

MIT License
