from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Products, Tickets
import uuid

engine = create_engine("sqlite:///notShop.db", echo=True)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

    session = session_maker()
    if not session.query(Products).first():
        session.add_all([
            Products(name="Монитор", cost=500, count=15),
            Products(name="Системный блок", cost=2500, count=5),
            Products(name="Клавиатура", cost=200, count=10)
        ])
    if not session.query(Tickets).first():
        for _ in range(5):
            session.add(Tickets(uuid=str(uuid.uuid4()), available=True))
    session.commit()
    session.close()