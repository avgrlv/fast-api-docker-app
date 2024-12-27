import databases
import ormar
import sqlalchemy
from ormar import OrmarConfig

from backend.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()
base_ormar_config = OrmarConfig(
    metadata=metadata,
    database=database
)


class User(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename='users')

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
