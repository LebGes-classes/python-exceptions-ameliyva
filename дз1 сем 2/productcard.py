class NumberError(Exception):
    """Ошибка отрицательного числа"""

    pass


class NameError(Exception):
    """Ошибка пустого поля"""

    pass


class StatusError(Exception):
    """Ошибка присвоения уже имеющегося статуса товара"""

    pass


class CategoryError(Exception):
    """Ошибка не соответствия категории товара со списком категорий"""

    pass


categories = ["электроника", "одежда", "продукты", "мебель", "инструменты", "другое"]


class ProductCard:
    """Класс карточки товара"""

    def __init__(self) -> None:
        """Инициализация конструктора класса"""

        self.name = 'Не указано'
        self.quantity = 0
        self.status = 'В пути'
        self.supplier = 'Не указан'
        self.developer = 'Не указан'
        self.price = None
        self.location = 'Не указано'
        self.color = 'Не указан'
        self.origincountry = 'Не указаны'
        self.category = 'Не указано'
        self.codenumber = None

    def get_name(self) -> str:
        """Геттер для наименования товара.

        Returns:
            str: Наименование товара
        """

        return self.name

    def print_info(self) -> None:
        """Получение всей возможной информации о товаре.

        Выводит все атрибуты товара в формате "ключ: значение".
        """

        for key, value in self.__dict__.items():
            print(f'{key}: {value}')

    def set_name(self, new_name: str) -> None:
        """Сеттер для наименования товара.

        Args:
            new_name: Новое наименование товара

        Raises:
            NameError: Если new_name является пустой строкой
        """

        if len(new_name) == 0:
            raise NameError("Товар не может быть без названия!")
        else:
            self.name = new_name

    def set_quantity(self, new_quantity: int) -> None:
        """Сеттер для количества товара.

        Args:
            new_quantity: Новое количество товара

        Raises:
            NumberError: Если new_quantity меньше 0
        """

        if new_quantity < 0:
            raise NumberError("Количество товара не может быть отрицательным. Введите корректное число!")
        else:
            self.quantity = new_quantity

    def set_status(self, new_status: str) -> None:
        """Сеттер для статуса товара.

        Args:
            new_status: Новый статус товара

        Raises:
            StatusError: Если новый статус совпадает с текущим
        """

        if self.status == new_status:
            raise StatusError("У товара уже установлен аналогичный статус")
        else:
            self.status = new_status

    def set_supplier(self, new_supplier: str) -> None:
        """Сеттер для поставщика товара.

        Args:
            new_supplier: Новый поставщик товара
        """

        self.supplier = new_supplier

    def set_developer(self, new_developer: str) -> None:
        """Сеттер для производителя товара.

        Args:
            new_developer: Новый производитель товара
        """

        self.developer = new_developer

    def set_price(self, new_price: float) -> None:
        """Сеттер для цены товара.

        Args:
            new_price: Новая цена товара

        Raises:
            NumberError: Если new_price меньше 0
        """

        if new_price < 0:
            raise NumberError("Цена товара не может быть отрицательным числом! Введите корректное значение")
        else:
            self.price = new_price

    def set_location(self, new_location: str) -> None:
        """Сеттер для местоположения товара.

        Args:
            new_location: Новое местоположение товара
        """

        self.location = new_location

    def set_color(self, new_color: str) -> None:
        """Сеттер для цвета товара.

        Args:
            new_color: Новый цвет товара
        """

        self.color = new_color

    def set_origincountry(self, new_origincountry: str) -> None:
        """Сеттер для страны происхождения товара.

        Args:
            new_origincountry: Новая страна производителя
        """

        if len(new_origincountry) == 0:
            raise NameError("Введите корректную страну производителя. Оно не может быть пустым.")
        else:
            self.origincountry = new_origincountry

    def set_category(self, new_category: str) -> None:
        """Сеттер для категории товара.

        Args:
            new_category: Новая категория товара
        """

        if new_category in categories:
            self.category = new_category
        else:
            raise CategoryError("Такой категории не существует!")

    def set_codenumber(self, new_codenumber: float) -> None:
        """Сеттер для кода товара.

        Args:
            new_codenumber: Новый код товара
        """

        if new_codenumber <= 0:
            raise NumberError("Код товара не может быть меньше, либо равен 0")
        else:
            self.codenumber = new_codenumber