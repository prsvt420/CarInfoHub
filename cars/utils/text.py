from pytils.translit import slugify
import uuid


def generate_slug(make: str, model: str, year: int) -> str:
    """
    Возвращает уникальный slug для автомобиля

    Params:
        make: str
            Марка автомобиля
        model: str
            Модель автомобиля
        year: int
            Год выпуска автомобиля

    Returns:
        str: Сгенерированный slug
    """

    return f'{slugify(make)}-{slugify(model)}-{year}-{str(uuid.uuid4())}'
