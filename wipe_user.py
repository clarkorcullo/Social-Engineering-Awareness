from app import app, db, User, UserProgress

def wipe_user(username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            # Delete all UserProgress records for this user
            UserProgress.query.filter_by(user_id=user.id).delete()
            # Delete the user
            db.session.delete(user)
            db.session.commit()
            print(f"✅ User '{username}' and related data wiped out.")
        else:
            print(f"❌ User '{username}' not found.")

if __name__ == '__main__':
    wipe_user('clarkorcullo86')