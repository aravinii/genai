from pydantic import BaseModel
from typing import Optional
import pandas as pd

class Property(BaseModel):
    """
    Property data model for real estate information.

    Attributes:
        type (Optional[str]): Type of the property (e.g., House, Apartment).
        neighborhood (Optional[str]): Name of the neighborhood where the property is located.
        area (Optional[float]): Area of the property in square meters.
        bathrooms (Optional[int]): Number of bathrooms in the property.
        bedrooms (Optional[int]): Number of bedrooms in the property.
        iptu (Optional[float]): IPTU tax amount for the property.
        parking_slots (Optional[int]): Number of parking slots available.
    """
    type: Optional[str] = None
    neighborhood: Optional[str] = None
    area: Optional[float] = None
    bathrooms: Optional[int] = None
    bedrooms: Optional[int] = None
    iptu: Optional[float] = None
    parking_slots: Optional[int] = None

    def is_complete(self) -> bool:
        """
        Checks if all required fields of the Property instance are filled (not None).

        Returns:
            bool: True if all mandatory attributes are present, False otherwise.
        """
        return all([
            self.type is not None,
            self.neighborhood is not None,
            self.bedrooms is not None,
            self.bathrooms is not None,
            self.area is not None,
            self.parking_slots is not None,
            self.iptu is not None
        ])
    
    def to_pandas(self):
        """
        Convert the Property instance to a pandas DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing the instance's attribute values, 
            formatted for further processing or machine learning model input.
        """
        return pd.DataFrame([self.model_dump()])

    @classmethod
    def from_dict(cls, data: dict) -> "Property":
        """
        Create a Property instance from a dictionary.

        Args:
            data (dict): Dictionary containing property attributes (such as from an API request body or JSON).

        Returns:
            Property: A Property instance initialized with the values from the dictionary.
        """
        return cls(**data)