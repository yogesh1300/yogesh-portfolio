import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import sqlite3

from . import crud, schemas
from .database import Base


@pytest.fixture(scope="function")
def test_db():
    """Create a fresh test database for each test"""
    # Create temporary database file
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    os.close(db_fd)  # Close the file descriptor

    # Create engine for this test
    test_url = f"sqlite:///{db_path}"
    engine = create_engine(
        test_url,
        connect_args={"check_same_thread": False, "timeout": 30},
        poolclass=NullPool
    )

    # Enable WAL mode
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_conn, connection_record):
        try:
            cursor = dbapi_conn.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=NORMAL")
            dbapi_conn.commit()
        except sqlite3.OperationalError:
            pass

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create session factory
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create test users
    db = TestingSessionLocal()
    try:
        for user_data in [
            ("admin", schemas.RoleEnum.admin, "admin123"),
            ("analyst", schemas.RoleEnum.analyst, "analyst123"),
            ("viewer", schemas.RoleEnum.viewer, "viewer123"),
        ]:
            username, role, password = user_data
            user = schemas.UserCreate(username=username, role=role, password=password)
            crud.create_user(db, user)
        db.commit()
    finally:
        db.close()

    yield TestingSessionLocal

    # Clean up
    engine.dispose()
    try:
        os.unlink(db_path)
        # Also clean up WAL files
        for ext in ['-wal', '-shm']:
            wal_file = db_path + ext
            if os.path.exists(wal_file):
                os.unlink(wal_file)
    except Exception:
        pass


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with dependency override"""
    from .main import app, get_db

    def override_get_db():
        db = test_db()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    try:
        client = TestClient(app)
        yield client
    finally:
        app.dependency_overrides.clear()






