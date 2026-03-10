class Property:
    def __init__(
        self,
        bedrooms: int = None,
        bathrooms: int = None,
        total_area: float = None,
        region_name: str = None,
        parking_slots: int = None,
        iptu: float = None,
        type: str = None
    ):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.total_area = total_area
        self.region_name = region_name
        self.parking_slots = parking_slots
        self.iptu = iptu
        self.type = type

    def is_complete(self) -> bool:
        """Checks if all required property fields are filled in"""
        return all([
            self.bedrooms is not None,
            self.bathrooms is not None,
            self.total_area is not None,
            self.region_name is not None,
            self.parking_slots is not None,
            self.iptu is not None,
            self.type is not None
        ])

    def to_dict(self) -> dict:
        """Returns the data as a dictionary for use in the pricing tool"""
        return {
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "total_area": self.total_area,
            "region_name": self.region_name,
            "parking_slots": self.parking_slots,
            "iptu": self.iptu,
            "type": self.type
        }