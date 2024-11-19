from django.db.models import QuerySet

from cars.models import Comment, Car


class CarService:
    @staticmethod
    def get_all_cars() -> QuerySet[Car]:
        """
        Возвращает все автомобили.

        Returns:
            QuerySet[Car]: все автомобили
        """
        return Car.objects.all()

    @staticmethod
    def get_car_by_id(car_id: int) -> Car:
        """
        Возвращает автомобиль по его ID.

        Parameters:
            car_id (int): ID автомобиля

        Returns:
            Car: автомобиль
        """
        return Car.objects.get(id=car_id)


class CommentService:
    @staticmethod
    def get_comments_for_car(car: Car) -> QuerySet[Comment]:
        """
        Возвращает комментарии к автомобилю.

        Parameters:
            car (Car): автомобиль

        Returns:
            QuerySet[Comment]: комментарии к автомобилю
        """
        return Comment.objects.filter(car=car).select_related('author')

    @staticmethod
    def get_comments_for_car_id(car_id: int) -> QuerySet[Comment]:
        """
        Возвращает комментарии к автомобилю по его ID.

        Parameters:
            car_id (int): ID автомобиля

        Returns:
            QuerySet[Comment]: комментарии к автомобилю
        """
        return Comment.objects.filter(car_id=car_id).select_related('author')
