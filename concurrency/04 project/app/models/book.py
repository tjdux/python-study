from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: str
    image: str

    model_config = {"collection": "books"}
