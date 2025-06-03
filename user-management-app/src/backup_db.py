import shutil
import datetime
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'instance', 'users.db'))
BACKUP_DIR = os.path.join(os.path.dirname(__file__), 'db_backups')

def backup_sqlite_db():
    if not os.path.exists(DB_PATH):
        print(f" Database file not found at {DB_PATH}")
        return
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f'users_backup_{timestamp}.db')
    shutil.copy2(DB_PATH, backup_file)
    print(f" Backup created at {backup_file}")

if __name__ == "__main__":
    backup_sqlite_db()