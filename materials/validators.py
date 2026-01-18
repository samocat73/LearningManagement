from rest_framework.serializers import ValidationError


def validate_link(link):
    """
    Функция, которая проверяет, что в ссылке есть подстрока https://www.youtube.com/
    """
    if not "https://www.youtube.com/" in link:
        raise ValidationError('Ссылка должна вести на сайт "https://www.youtube.com/"')
