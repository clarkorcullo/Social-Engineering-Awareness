#!/usr/bin/env python3
"""
Database Migration System
Safely updates database schema without losing user data
"""

import sqlite3
import os
from datetime import datetime

def get_db_path():
    """Get the correct database path for the environment"""
    import os
    if os.environ.get('RENDER'):
        return '/tmp/social_engineering_awareness.db'
    else:
        return 'social_engineering_awareness.db'

def backup_database():
    """Create a backup of the current database"""
    db_path = get_db_path()
    if os.path.exists(db_path):
        backup_path = f"{db_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        import shutil
        shutil.copy2(db_path, backup_path)
        print(f"✅ Database backed up to: {backup_path}")
        return backup_path
    return None

def check_table_exists(cursor, table_name):
    """Check if a table exists in the database"""
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?
    """, (table_name,))
    return cursor.fetchone() is not None

def check_column_exists(cursor, table_name, column_name):
    """Check if a column exists in a table"""
    cursor.execute("PRAGMA table_info(?)", (table_name,))
    columns = [column[1] for column in cursor.fetchall()]
    return column_name in columns

def migrate_database():
    """Safely migrate the database schema"""
    db_path = get_db_path()
    
    print("🔄 Starting database migration...")
    
    # Create backup
    backup_path = backup_database()
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if user table exists
        if not check_table_exists(cursor, 'user'):
            print("❌ User table does not exist. Creating new database...")
            conn.close()
            return False
        
        # Check for missing columns and add them safely
        missing_columns = []
        
        # Define required columns
        required_columns = [
            ('modules_completed', 'INTEGER DEFAULT 0'),
            ('total_score', 'INTEGER DEFAULT 0'),
            ('simulations_completed', 'INTEGER DEFAULT 0')
        ]
        
        # Check each required column
        for column_name, column_def in required_columns:
            if not check_column_exists(cursor, 'user', column_name):
                missing_columns.append((column_name, column_def))
        
        # Add missing columns
        if missing_columns:
            print(f"📝 Adding {len(missing_columns)} missing columns...")
            
            for column_name, column_def in missing_columns:
                try:
                    cursor.execute(f"ALTER TABLE user ADD COLUMN {column_name} {column_def}")
                    print(f"✅ Added column: {column_name}")
                except Exception as e:
                    print(f"❌ Failed to add column {column_name}: {e}")
                    continue
            
            # Commit changes
            conn.commit()
            print("✅ Database migration completed successfully!")
        else:
            print("✅ Database schema is up to date!")
        
        return True
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        if backup_path:
            print(f"🔄 Restoring from backup: {backup_path}")
            conn.close()
            import shutil
            shutil.copy2(backup_path, db_path)
            print("✅ Database restored from backup")
        return False
    
    finally:
        conn.close()

def safe_init_db():
    """Safely initialize database with migration support"""
    print("🚀 Initializing database with migration support...")
    
    # Try to migrate existing database
    if os.path.exists(get_db_path()):
        if migrate_database():
            print("✅ Database migrated successfully")
            return True
        else:
            print("❌ Migration failed, will create new database")
    
    # If no existing database or migration failed, create new one
    print("📝 Creating new database...")
    return False

if __name__ == "__main__":
    safe_init_db() 