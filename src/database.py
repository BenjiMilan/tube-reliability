from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://tube:tube@localhost:5432/tube"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)