#!/usr/bin/env python3
"""
Manual Database Migration Runner
Run this script to safely migrate the database without losing user data
"""

from migrations import migrate_database, safe_init_db

def main():
    print("🔄 Database Migration Tool")
    print("=" * 40)
    
    choice = input("Choose an option:\n1. Safe migration (recommended)\n2. Force new database\nEnter choice (1 or 2): ")
    
    if choice == "1":
        print("\n🔄 Running safe migration...")
        if safe_init_db():
            print("✅ Migration completed successfully!")
            print("✅ User data preserved!")
        else:
            print("❌ Migration failed!")
    elif choice == "2":
        print("\n⚠️  WARNING: This will delete all user data!")
        confirm = input("Are you sure? Type 'YES' to continue: ")
        if confirm == "YES":
            import os
            db_path = "social_engineering_awareness.db"
            if os.path.exists(db_path):
                os.remove(db_path)
                print("✅ Old database deleted")
            print("✅ New database will be created on next app restart")
        else:
            print("❌ Operation cancelled")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main() 