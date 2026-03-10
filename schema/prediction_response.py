from pydantic import BaseModel, Field
from typing import Dict

class PriceRange(BaseModel):
    min: float = Field(..., description= "The Minimum Price of the house")
    max: float = Field(..., description= "The Highest price of the house")

class PredictionResponse (BaseModel):
    Predicted_price: float = Field(
        ...,
        description= "The Predicted price of the house",
        example = '89000'
    )
    
    Price_range: PriceRange =Field(...,
                                   
         description= "The Predicted price range",
         example = 'Min: 89,000, Max: 92,000'                          
    )
    Category: str = Field(
        ...,
        description= "The Predicted Category of the house",
        example = {'Medium','Low','High'}
    )