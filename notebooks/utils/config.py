# config.py
from pathlib import Path

# S3 paths or local paths for data files
BUSINESS_DATA_PATH = "../sourcedata/yelp_academic_dataset_business.json"
REVIEW_DATA_PATH = "../sourcedata/yelp_academic_dataset_review.json"
USER_DATA_PATH = "../sourcedata/yelp_academic_dataset_user.json"

PHILADELPHIA = "../datasets/philadelphia.json"
USER = "../datasets/user.json"

# Spark
APP = "C:\spark"