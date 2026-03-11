from pydantic import BaseModel
from typing import Optional
class Property(BaseModel):
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    total_area: Optional[float] = None
    parking_slots: Optional[int] = None
    neighborhood: Optional[str] = None
    iptu: Optional[float] = None

    def is_complete(self) -> bool:
        return all([
            self.bedrooms is not None,
            self.bathrooms is not None,
            self.total_area is not None,
            self.parking_slots is not None,
            self.neighborhood is not None,
            self.iptu is not None
        ])
    
    def to_dict(self):
        return self.dict(exclude_unset=True)