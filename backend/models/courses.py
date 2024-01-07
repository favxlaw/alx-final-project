from typing import List, Optional 
from pydantic import BaseModel, Field 

# Rating Model
class Rating(BaseModel):
    total: int = Field(0, description="The total sum of the ratings".)
    count: int = Field(0, description="The number of ratings.")


# Chapter Model
class Chapter(BaseModel):
    name: str = Field(..., description="The name of the chapter.")
    text: str = Field(..., description="The content of the chapter.")
    rating: Optional[Rating] = Field(None, description="The rating of the chapter.")

# Course overview Model
class CourseOverview(BaseModel):
    name: str = Field(..., description="the name of the course.")
    date: int = Field(..., description="The date of the course creation.")
    description: str = Field(..., description="The description of the course.")
    domain: List[str] = Field( description="The domain of the course.")
    rating: Optional[Rating] =Field(None, description="The rating of the course.")


# Course detail Model 
class CourseDetail(BaseModel):
      chapters: List[Chapter] = Field(..., description="The list of the chapters of the course.")

# Chapter Detail Model
name: str = Field(..., description="The name of the chapter.")
text: str = Field(..., description="The content of the chapter.")

# Define the rating input model
class RatingInput(BaseModel):
    rating: int = Field(..., gt=-2, lt=2, description="The rating value. Must be between -1 and 1.")

# Error response Model
class CourseNotFoundResponse(ErrorResponse):
    detail: str = Field('Course not found', description="The error message.")

# The chapter not found response model
class ChapterNotFoundResponse(ErrorResponse):
    detail: str = Field('Chapter not found', description="The error message.")

# Course Ratings Model
name: str = Field(..., description="The name of the course. ")
ratings: List[Rating] = Field(..., description="The list of ratings of the course.")

# Course list response Model
class CourseListResponse(BaseModel):
    pass 

# Chapter detail response Model
pass 