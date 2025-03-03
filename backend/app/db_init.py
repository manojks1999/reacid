from app.core.database import engine
from app.models.user import User

# Import all models here

def init_db():
    """Initialize database tables"""
    # Create all tables in the database
    # This is equivalent to "CREATE TABLE" statements in raw SQL
    from app.models.user import Base
    Base.metadata.create_all(bind=engine)