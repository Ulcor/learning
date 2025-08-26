import pandas as pd
import pandas_gbq
import logging
from typing import Optional
import os

class BigQueryCsvLoader:
    def __init__(self, file_path: str, project_id: str, sql: str):
        self.file_path = os.path.abspath(file_path)  # Convert to absolute path
        self.project_id = project_id
        self.sql = sql
        self.logger = self._init_logger()

    def _init_logger(self) -> logging.Logger:
        logger = logging.getLogger("BigQueryCsvLoader")
        if not logger.handlers:  # Avoid duplicate handlers
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(handler)
        return logger

    def fetch_data(self, sql: Optional[str] = None) -> pd.DataFrame:
        query = sql or self.sql
        self.logger.debug(f"Running query: {query}")
        return pandas_gbq.read_gbq(query, project_id=self.project_id)

    def save_to_csv(self, df: Optional[pd.DataFrame] = None, file_path: Optional[str] = None) -> None:
        # Default to file_path passed or instance file_path
        output_path = file_path or self.file_path
        output_path = os.path.abspath(output_path)  # Ensure absolute path
        if df is None:
            df = self.fetch_data()
        df.to_csv(output_path, index=False)
        self.logger.info(f"Saved DataFrame to {output_path}")