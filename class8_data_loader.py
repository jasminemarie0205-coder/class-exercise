import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    df= pd.read_csv(filepath)
    logger.info(f"CSV data loaded successfully")
    return df
    
    # TODO 1:
    # Load filepath using pd.read_csv().
    # Log an INFO.
    # Return the DataFrame.
    pass