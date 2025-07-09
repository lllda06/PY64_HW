from datetime import datetime
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    points: Mapped[int] = mapped_column(default=0)

    orders: Mapped[list["Orders"]] = relationship(back_populates="user", lazy="selectin")
    tickets: Mapped[list["Tickets"]] = relationship(back_populates="user", lazy="selectin")

    def get_orders(self, session) -> list:
        return session.query(Orders).filter_by(user_id=self.id).all()

    @staticmethod
    def is_user_exists(session, username:str) -> bool:
        return session.query(Users).filter(Users.username==username).first() is not None

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)

    orders: Mapped[list["Orders"]] = relationship(back_populates="product", lazy="selectin")

class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    order_datetime: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)

    user: Mapped[Users] = relationship(back_populates="orders", lazy="selectin")
    product: Mapped[Products] = relationship(back_populates="orders", lazy="selectin")
class Tickets(Base):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    available: Mapped[bool] = mapped_column(default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    user: Mapped[Users] = relationship(back_populates="tickets", lazy="selectin")

    @staticmethod
    def valid_ticket(session, uuid_str: str) -> bool:
        ticket = session.query(Tickets).filter_by(uuid=uuid_str).first()
        return ticket is not None and ticket.available