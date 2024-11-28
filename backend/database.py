from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@db/postgres')

# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()