from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    "user_name",
    "password",
    "host（127.0.0.1）",
    "database_name",
)
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)
Base = declarative_base()
Base.query = session.query_property()