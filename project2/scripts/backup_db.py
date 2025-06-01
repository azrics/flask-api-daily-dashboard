# Backs up SQLite DB to a timestamped file  
import shutil  
from datetime import datetime  

def backup_db():  
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d')}.db"  
    shutil.copy2("data.db", f"backups/{backup_name}")  

if __name__ == "__main__":  
    backup_db()  