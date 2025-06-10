from sqlalchemy import create_engine, Column, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class UserProfile(Base):
    __tablename__ = "profiles"
    id = Column(String, primary_key=True)
    transcription = Column(Text)
    extracted_info = Column(JSON)

def init_db():
    Base.metadata.create_all(engine)

def save_user_profile(transcription, profile):
    session = Session()
    profile_obj = UserProfile(
        id=os.urandom(8).hex(),
        transcription=transcription,
        extracted_info=profile
    )
    session.add(profile_obj)
    session.commit()
    session.close()

def get_all_profiles():
    session = Session()
    results = session.query(UserProfile).all()
    data = []
    for row in results:
        data.append({
            "id": row.id,
            "transcription": row.transcription,
            "extracted_info": row.extracted_info
        })
    session.close()
    return data
