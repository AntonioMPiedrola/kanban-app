from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    boards = relationship("Board", back_populates="owner", cascade="all, delete")


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="boards")
    columns = relationship("BoardColumn", back_populates="board", cascade="all, delete")


class BoardColumn(Base):
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)

    board = relationship("Board", back_populates="columns")
    cards = relationship("Card", back_populates="column", cascade="all, delete")


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    position = Column(Integer, nullable=False)
    due_date = Column(DateTime, nullable=True)
    file_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    column_id = Column(Integer, ForeignKey("columns.id"), nullable=False)

    column = relationship("BoardColumn", back_populates="cards")
