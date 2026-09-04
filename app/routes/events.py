from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.event import Event
from app.schemas.event import EventCreate, EventResponse, EventUpdate

router = APIRouter(prefix="/events", tags=["events"])


@router.post("/", response_model=EventResponse)
async def create_event(
    event: EventCreate,
    db: AsyncSession = Depends(get_db),
):
    new_event = Event(
        name=event.name,
        description=event.description,
        start_time=event.start_time,
        location=event.location,
    )
    db.add(new_event)
    await db.commit()
    await db.refresh(new_event)

    return new_event


@router.get("/", response_model=list[EventResponse])
async def get_events(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Event))
    events = result.scalars().all()
    return events


@router.delete("/{event_id}", response_model=dict)
async def delete_event(
    event_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    await db.delete(event)
    await db.commit()

    return {"message": "Event deleted successfully"}


@router.get("/{event_id}", response_model=EventResponse)
async def get_event_by_id(
    event_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


@router.patch("/{event_id}", response_model=EventResponse)
async def update_event(
    event_id: int,
    event_update: EventUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found",
        )

    event_data = event_update.model_dump(exclude_unset=True)

    for key, value in event_data.items():
        setattr(event, key, value)

    await db.commit()
    await db.refresh(event)

    return event
