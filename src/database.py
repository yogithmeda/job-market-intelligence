import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class JobDatabase:
    def __init__(self):
        self.db_path = os.getenv('DB_PATH', 'data/jobs.db')
        self.create_tables()
    
    def create_tables(self):
        """Create database tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Jobs table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company TEXT,
            location TEXT,
            salary_min INTEGER,
            salary_max INTEGER,
            experience_level TEXT,
            job_type TEXT,
            remote_option TEXT,
            description TEXT,
            url TEXT UNIQUE,
            scraped_date DATE,
            post_date DATE
        )
        ''')
        
        # Skills table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT UNIQUE NOT NULL,
            category TEXT
        )
        ''')
        
        # Job-Skills junction table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_skills (
            job_id INTEGER,
            skill_id INTEGER,
            FOREIGN KEY (job_id) REFERENCES jobs(id),
            FOREIGN KEY (skill_id) REFERENCES skills(id),
            PRIMARY KEY (job_id, skill_id)
        )
        ''')
        
        conn.commit()
        conn.close()
        print(f"✅ Database initialized at {self.db_path}")

if __name__ == "__main__":
    # Test database creation
    db = JobDatabase()