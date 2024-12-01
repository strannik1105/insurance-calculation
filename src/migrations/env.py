from logging.config import fileConfig
import os
import sys
import inspect

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

currentdir = os.path.dirname(  # type: ignore
    os.path.abspath(inspect.getfile(inspect.currentframe()))  # type: ignore
)  # type: ignore
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from common.config import PostgresConfig
from migrations.models_meta import metadata
from utils.utils import UrlMaker

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

db_config = PostgresConfig.get_instance()


def _get_url() -> str:
    return UrlMaker.sync_pg_url(
        db_config.POSTGRES_USER,
        db_config.POSTGRES_PASSWORD,
        db_config.POSTGRES_HOST,
        db_config.POSTGRES_PORT,
        db_config.POSTGRES_DB,
    )


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = _get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    if not config.get_main_option("sqlalchemy.url", None):
        configuration["sqlalchemy.url"] = _get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
