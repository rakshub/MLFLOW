import os 
import sys
import numpy as np
import pandas as pd

#Defining commi=on constant variable for training pipeline

TARGET_COLUMN="Result"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR="Artifcats"
FILE_NAME="phisingData.csv"

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

#Data Ingestion related constants start with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="Raksha"
DATA_INGETSION_DIR_NAME:str="data_ingetsion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGETSION_INGESTED_DIR:str="ingested"
DATA_INGETSION_TRAIN_TEST_SPLIT_RATION:float=0.2

