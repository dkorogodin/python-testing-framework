from typing import Generic, TypeVar, Type, List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseDao(Generic[T]):
    """Generic DAO base similar to Java BaseDao<T>."""

    def __init__(self, session: Session, entity_class: Type[T]):
        self.session = session
        self.entity_class = entity_class

    def get(self, entity_id: int) -> Optional[T]:
        return self.session.get(self.entity_class, entity_id)

    def get_all(self) -> List[T]:
        stmt = select(self.entity_class)
        return list(self.session.scalars(stmt))

    def find_by_field(self, field_name: str, value) -> List[T]:
        stmt = select(self.entity_class).where(getattr(self.entity_class, field_name) == value)
        return list(self.session.scalars(stmt))

    def save(self, entity: T):
        self.session.add(entity)
        self.session.commit()

    def save_all(self, entities: List[T]):
        self.session.add_all(entities)
        self.session.commit()

    def delete(self, entity: T):
        self.session.delete(entity)
        self.session.commit()
