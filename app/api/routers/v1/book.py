from http import HTTPStatus

from fastapi import Depends, HTTPException, status

from app import core

from ... import config, dependencies, dtos

book = config.APIRouter()

@book.post(
     path="/",
     name="add_booking_to_system",
     status_code=status.HTTP_200_OK,
     response_model=core.Book
)
def add_book_to_system(
        new_book: dtos.CreateBookRequestDTO,
        use_case: core.AddBook = Depends(dependencies.add_book_use_case)
):
    try:
        query_booking = use_case.execute(
            book_title=new_book.book_title,
            author_name=new_book.author_name,
            total_copies=new_book.total_copies,
            published_year=new_book.published_year
        )
        response = query_booking
        return response
    except core.exceptions.AuthorNotFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except core.exceptions.BookAlreadyExists as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(error))
