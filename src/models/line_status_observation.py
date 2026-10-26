from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class LineStatusObservation(Base):
    __tablename__ = "line_status_observation"

    id: Mapped[int] = mapped_column(primary_key=True)
    line_id: Mapped[str] = mapped_column(ForeignKey("lines.id"))

    observed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    severity: Mapped[int]
    status: Mapped[str]
    reason: Mapped[str | None] = mapped_column(Text)

    __table_args__ = (
        Index("ix_observation_line_time", "line_id", "observed_at"),
    )
