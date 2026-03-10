from pydantic import BaseModel, Field, computed_field, field_validator, computed_field
from typing import Annotated, Literal, Optional


class UserInput (BaseModel):
    Area_Sq: Annotated[int,Field(...,gt=0, description="Provide the Size of the house in sq.ft")]
    Income: Annotated[float, Field(..., gt=0,description="Provide your Annual Income in LPA", example="8.9")]
    Bedrooms: Annotated[int, Field(...,gt =0, description ="Provide the Bedrooms you required")]
    Bathrooms: Annotated[int, Field(..., gt=0,description = "Provide the Number of Bathrooms you required")]
    floors: Annotated[int, Field(..., gt=0,description = "Provide Number of floors required")]
    House_age: Annotated[int, Field(..., gt=0, description="Age of house in years")]
    location_score: Annotated[Optional[float], Field(gt = 0, description="The Popularity of the area")]
    Parking: Annotated[Optional[int], Field(description="Prodive how many parkings do you required")]
    
    @field_validator('Income')
    @classmethod
    def check_income(cls,value):
        if value > 100:
             raise ValueError("Income seems unrealistic. Please enter income in LPA.")
        return value
    
    @field_validator('Area_Sq')
    @classmethod
    def validate_area(cls,value):
        if value < 100:
            raise ValueError("House area too small")
        if value > 20000:
            raise ValueError("House is too big")
        return value
    
    @computed_field
    @property
    def area_per_bedroom(self) -> float:
        return self.Area_Sq / self.Bedrooms
    
    @computed_field
    @property
    def has_parking(self) -> bool:
        return self.Parking is not None
    