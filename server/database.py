from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://musicapp_0e0h_user:oKBj75Zr2D6U606iikegy2DDexJXnIM7@dpg-ct262ddsvqrc73e54230-a.oregon-postgres.render.com/musicapp_0e0h'
#DATABASE_URL = 'postgresql://postgres:root@localhost/fluttermusicapp'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()