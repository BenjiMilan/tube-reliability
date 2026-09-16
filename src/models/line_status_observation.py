from datetime import datetime

from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class LineStatusObservation(Base):
    __table_name__ = "line_status_observation"

    id: Mapped[int] = mapped_column(primary_key=True)
    line_id: Mapped[int] = mapped_column(ForeignKey("lines.id"))

    observed_at: Mapped[datetime]
    severity: Mapped[int]
    status: Mapped[str]
    reason: Mapped[str | None] = mapped_column(Text)

    __table_args__ = (
        Index("ix_observation_line_time", "line_id", "observed_at"),
    )
