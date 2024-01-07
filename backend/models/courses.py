from typing import List, Optional 
from pydantic import BaseModel, Field #PydanticValueError, validator




# Rating Model
class Rating(BaseModel):
    total: int = Field(0, description="The total sum of the ratings.")
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
class ChapterDetail(BaseModel):
    name: str = Field(..., description="The name of the chapter.")
    text: str = Field(..., description="The content of the chapter.")

# Define the rating input model
class RatingInput(BaseModel):
    rating: int = Field(..., gt=-2, lt=2, description="The rating value. Must be between -1 and 1.")

# Error response Model
"""
class CourseNotFoundError(PydanticValueError):
    code = 'course_not_found'
    msg_template = 'Course not found: {course_id}'
    @validator('id')
    def check_id(cls, v):
        if v not in [1, 2, 3]: # some dummy condition
            raise CourseNotFoundError(course_id=v)
        return v
        
# The chapter not found response model
class ChapterNotFoundError(PydanticValueError):
    code = 'chapter_not_found'
    msg_template = 'Chapter not found: {chapter_id}'
    @validator('id')
    def check_id(cls, v):
        if v not in [1, 2, 3]: # some dummy condition
            raise CourseNotFoundError(course_id=v)
        return v
"""
# Course Ratings Model
name: str = Field(..., description="The name of the course. ")
ratings: List[Rating] = Field(..., description="The list of ratings of the course.")

# Course list response Model
class CourseListResponse(BaseModel):
    pass 

# Chapter detail response Model
pass 