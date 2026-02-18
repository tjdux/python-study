from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from contextlib import asynccontextmanager
from app.models import mongodb
from app.book_scraper import NaverBookScraper
from app.models.book import BookModel


BASE_DIR = Path(__file__).resolve().parent


templates = Jinja2Templates(directory=BASE_DIR / "templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb.connect()

    yield

    mongodb.close()


app = FastAPI(lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    keyword = q

    if not keyword:
        return templates.TemplateResponse(
            "./index.html", {"request": request, "title": "콜렉터 북북이"}
        )

    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        return templates.TemplateResponse(
            "./index.html",
            {"request": request, "title": "콜렉터 북북이", "books": books},
        )

    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)
    book_models = []
    for book in books:
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["price"],
            image=book["image"],
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)

    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이", "books": books}
    )
