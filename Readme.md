# 🍽️ Restaurant Recommender

A machine learning-based system that recommends restaurants based on user preferences and reviews, powered by the Yelp Open Dataset.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

---

### Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### ✅ Prerequisites

- Python 3.8+
- PySpark
- Other dependencies listed in `requirements.txt`

---

### 📦 Step-by-Step Setup

#### 🔹 Step 1: Download Yelp Dataset

Download the Yelp Open Dataset (JSON format) from the official site:

🔗 [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/)

You will need the following files:
- `business.json`
- `review.json`
- `user.json`

#### 🔹 Step 2: Update Configuration Paths

Open the `config.py` file and update the paths to reflect where you saved the JSON files:

```python
# Example config.py snippet
BUSINESS_DATA_PATH = "/path/to/business.json"
REVIEW_DATA_PATH = "/path/to/review.json"
OUTPUT_CSV_PATH = "/path/to/output/folder"