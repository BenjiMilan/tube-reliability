from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Line(Base):
    __tablename__ = "lines"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]