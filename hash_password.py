import bcrypt


# Hash password for modules like insert_user.py or update_user
def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")