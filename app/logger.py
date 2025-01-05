import logging
import os
from datetime import datetime

if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logger():
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        
        format= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        file_handler = logging.FileHandler(f'logs/app_{datetime.now().strftime("%Y%m%d")}.log')
        file_handler.setFormatter(format)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(format)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()