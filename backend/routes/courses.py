import contextlib
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi import APIRouter, Depends
from typing import List
from routes.auth import get_current_active_user 
from models.courses import CourseOverview, CourseDetail, ChapterDetail, RatingInput # CourseNotFoundResponse, ChapterNotFoundResponse
from models.auth import User


app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['courses']

router = APIRouter()

# function to get the course from the course_id
def get_course(course_id: str) -> CourseOverview:
    course = db.courses.find_one({'_id': ObjectId(course_id)}, {'_id': 0, 'chapters': 0})
    if not course:
        raise HTTPException(status_code=404, detail='Course not found', raise_exception=True)
    try:
        course['rating'] = course['rating']['total']
    except KeyError:
        course['rating'] = 'Not rated yet'
    return CourseOverview(**course)

# /courses
@router.get('/courses', response_model=List[CourseOverview])
def get_courses(sort_by: str = 'date', domain: str = None, current_user: User =
Depends(get_current_active_user)):
    # set the rating.total and rating.count to all the courses based on the sum of the chapters rating
    for course in db.courses.find():
        total = 0
        count = 0
        for chapter in course['chapters']:
            with contextlib.suppress(KeyError):
                total += chapter['rating']['total']
                count += chapter['rating']['count']
        db.courses.update_one({'_id': course['_id']}, {'$set': {'rating': {'total': total, 'count': count}}})

    # sort_by == 'date' [DESCENDING]
    if sort_by == 'date':
        sort_field = 'date'
        sort_order = -1

    # sort_by == 'rating' [DESCENDING]
    elif sort_by == 'rating':
        sort_field = 'rating.total'
        sort_order = -1

    # sort_by == 'alphabetical' [ASCENDING]
    else:  
        sort_field = 'name'
        sort_order = 1

    query = {}
    if domain:
        query['domain'] = domain


    courses = db.courses.find(query, {'name': 1, 'date': 1, 'description': 1, 'domain':1,'rating':1,'_id': 0}).sort(sort_field, sort_order)
    return [CourseOverview(**course) for course in courses]


"""
Endpoint to get the course overview
"""
@router.get('/courses/{course_id}', response_model=CourseOverview)
def get_course(course_id: str, current_user: User =
Depends(get_current_active_user)):
    course = get_course(course_id)
    return course
     
""" 
Endpoint to get a specific chapter information.
""" 
@router.get('/courses/{course_id}/{chapter_id}', response_model=ChapterDetail)
def get_chapter(course_id: str, chapter_id: str, current_user: User =
Depends(get_current_active_user)):    
    course = get_course(course_id)
    chapters = course.get('chapters', [])
    try:
        chapter = chapters[int(chapter_id)]
    except (ValueError, IndexError) as e:
        raise HTTPException(status_code=404, detail='Chapter not found', raise_exception=True) from e
    return ChapterDetail(**chapter)

# Endpoint to allow users to rate each chapter (positive/negative) 1 for Positive, -1 For Negative, while aggregating all ratings for each course.
@router.post('/courses/{course_id}/{chapter_id}', response_model=ChapterDetail)
def rate_chapter(course_id: str, chapter_id: str, rating: RatingInput, current_user: User = Depends(get_current_active_user)):
    course = get_course(course_id)
    chapters = course.get('chapters', [])
    try:
        chapter = chapters[int(chapter_id)]
    except (ValueError, IndexError) as e:
        raise HTTPException(status_code=404, detail='Chapter not found', raise_exception=True) from e
    try:
        chapter['rating']['total'] += rating.rating
        chapter['rating']['count'] += 1
    except KeyError:
        chapter['rating'] = {'total': rating.rating, 'count': 1}
    db.courses.update_one({'_id': ObjectId(course_id)}, {'$set': {'chapters': chapters}})
    return ChapterDetail(**chapter)

      
  
    
