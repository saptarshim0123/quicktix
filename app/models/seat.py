from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Seat(Base):
    __tablename__ = "seats"
    
    __table_args__ = (
        UniqueConstraint('event_id', 'label')
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"), 
        index=True,
        nullable=False
        )  # Foreign key to Event
    label: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="available")
    version: Mapped[int] = mapped_column(nullable=False, default=0)