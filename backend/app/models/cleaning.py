from typing import Optional
from enum import Enum

from app.models.core import IDModelMixin, CoreModel


class CleaningType(str, Enum):
    dust_up = "dust_up"
    spot_clean = "spot_clean"
    full_clean = "full_clean"


# Base
class CleaningBase(CoreModel):
    """
    All common characteristics of our Cleaning resource
    """
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    cleaning_type: Optional[CleaningType] = "spot_clean"


# Create
class CleaningCreate(CleaningBase):
    name: str
    price: float


# Update
class CleaningUpdate(CleaningBase):
    cleaning_type: Optional[CleaningType]


# Out of DB
class CleaningInDB(IDModelMixin, CleaningBase):
    name: str
    price: float
    cleaning_type: CleaningType


# Public Resource
class CleaningPublic(IDModelMixin, CleaningBase):
    pass
