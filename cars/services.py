from django.db.models import QuerySet

from cars.models import Comment, Car


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
