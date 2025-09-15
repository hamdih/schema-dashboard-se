import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Weaviate Schema Explorer", layout="wide")
st.title("🧠 Weaviate Schema Explorer")

# ------------------------
# Helpers
# ------------------------
def safe_stringify(val):
    """Convert dicts/lists to pretty JSON strings, leave scalars as-is."""
    if isinstance(val, (dict, list)):
        return json.dumps(val, indent=2)
    return val

def dict_to_table(d: dict) -> pd.DataFrame:
    """Flatten a dict into a two-column dataframe for display."""
    rows = []
    for k, v in d.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                rows.append((f"{k}.{sub_k}", safe_stringify(sub_v)))
        else:
            rows.append((k, safe_stringify(v)))
    return pd.DataFrame(rows, columns=["Key", "Value"])

def render_vector_index(cfg: dict, label: str):
    """Render vector index config with compression + dynamic indexing highlights."""
    st.markdown(f"#### 🔑 Vector Index Config ({label})")

    # Compression check
    compression_types = []
    for comp in ["pq", "sq", "rq"]:
        if cfg.get(comp, {}).get("enabled"):
            compression_types.append(comp.upper())
    compression_info = ", ".join(compression_types) if compression_types else "None"
    st.info(f"**Compression:** {compression_info}")

    # Dynamic indexing check
    if cfg.get("dynamic", False):
        st.info("**Dynamic Indexing:** ✅ Enabled")
    else:
        st.info("**Dynamic Indexing:** ❌ Not enabled")

    st.table(dict_to_table(cfg))


# ------------------------
# Main
# ------------------------
uploaded_file = st.file_uploader("Upload your Weaviate schema JSON", type="json")

if uploaded_file:
    data = json.load(uploaded_file)
    schema = data.get("schema", {})
    classes = schema.get("classes", [])

    if not classes:
        st.error("No classes found in schema.")
    else:
        class_names = [c["class"] for c in classes]
        selected_class = st.selectbox("Choose a Collection", class_names)

        for class_data in classes:
            if class_data["class"] == selected_class:
                st.subheader(f"📦 Collection: `{selected_class}`")

                # === Named Vectors Check ===
                vector_config = class_data.get("vectorConfig", {})
                if vector_config:
                    vector_names = list(vector_config.keys())
                    st.warning(f"📌 This class uses **Named Vectors**: {', '.join(vector_names)}")
                else:
                    st.info("📌 This class uses the **Default Vector** (no named vectors).")

                # === Class-level Configs ===
                st.markdown("### ⚙️ Class Configurations")

                for config_key in [
                    "invertedIndexConfig",
                    "moduleConfig",
                    "multiTenancyConfig",
                    "replicationConfig",
                    "shardingConfig",
                ]:
                    cfg = class_data.get(config_key)
                    if cfg:
                        st.markdown(f"#### {config_key}")
                        st.table(dict_to_table(cfg))

                # === Vector Index Config(s) ===
                # Case 1: Top-level (old style)
                if "vectorIndexConfig" in class_data:
                    render_vector_index(class_data["vectorIndexConfig"], "default")

                # Case 2: Named vectors
                for vec_name, vec_cfg in vector_config.items():
                    if "vectorIndexConfig" in vec_cfg:
                        render_vector_index(vec_cfg["vectorIndexConfig"], f"named vector `{vec_name}`")

                # === Properties ===
                st.markdown("### 🧾 Properties")
                for prop in class_data.get("properties", []):
                    with st.expander(f"🔹 {prop.get('name')} ({', '.join(prop.get('dataType', []))})"):
                        prop_table = pd.DataFrame(
                            [(k, safe_stringify(v)) for k, v in prop.items()],
                            columns=["Key", "Value"]
                        )
                        st.table(prop_table)
