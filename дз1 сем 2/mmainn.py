from productcard import (
    NumberError,
    NameError,
    StatusError,
    CategoryError,
    ProductCard,
    categories
)


def main() -> None:
    """Функция для запуска программы управления карточками товаров."""

    products = [ProductCard()]
    is_run = True

    while is_run:
        print('\n1) Выбрать товар из списка.')
        print('2) Добавить новый товар.')
        print('0) Выйти из программы.')
        print('\nВыберите действие: ', end='')

        try:
            first_choice = int(input())
        except ValueError:
            print('Ошибка: Введите число.')
            continue

        match first_choice:
            case 0:
                is_run = False
                print('Программа завершена.')

            case 1:
                # Показываем список товаров
                print('\nСписок доступных товаров:')
                for i, prod in enumerate(products):
                    print(f'{i + 1}) {prod.get_name()}')

                print('\nВведите номер товара: ', end='')

                try:
                    product_choice = int(input()) - 1

                    if not (0 <= product_choice < len(products)):
                        raise NumberError('Товара с таким номером нет')

                except ValueError:
                    print('Ошибка: Введите число.')
                    continue
                except NumberError as e:
                    print(f'Ошибка: {e}')
                    continue

                print(
                    '\nМеню действий с товаром:\n'
                    '1) Получить информацию о товаре.\n'
                    '2) Изменить название товара.\n'
                    '3) Изменить количество товара.\n'
                    '4) Изменить статус товара.\n'
                    '5) Изменить поставщика.\n'
                    '6) Изменить производителя.\n'
                    '7) Изменить цену товара.\n'
                    '8) Изменить местоположение.\n'
                    '9) Изменить цвет.\n'
                    '10) Изменить страну происхождения.\n'
                    '11) Изменить категорию.\n'
                    '12) Изменить код товара.\n'
                    '13) Показать доступные категории.\n'
                    '\nВыберите действие: ', end=''
                )

                try:
                    second_choice = int(input())
                except ValueError:
                    print('Ошибка: Введите число.')
                    continue

                match second_choice:
                    case 1:
                        print('\nИнформация о товаре:')
                        products[product_choice].print_info()

                    case 2:
                        print('Введите новое название товара: ', end='')
                        try:
                            new_name = input()
                            products[product_choice].set_name(new_name)
                            print('Название успешно изменено.')
                        except NameError as e:
                            print(f'Ошибка: {e}')

                    case 3:
                        print('Введите новое количество товара: ', end='')
                        try:
                            new_quantity = int(input())
                            products[product_choice].set_quantity(new_quantity)
                            print('Количество успешно изменено.')
                        except ValueError:
                            print('Ошибка: Введите целое число.')
                        except NumberError as e:
                            print(f'Ошибка: {e}')

                    case 4:
                        print(
                            '\nДоступные статусы:\n'
                            '1) В пути.\n'
                            '2) На складе.\n'
                            '3) Продан.\n'
                            '4) Возврат.\n'
                            '5) Зарезервирован.\n'
                            '\nВведите новый статус товара: ', end=''
                        )

                        try:
                            status_choice = int(input())

                            if status_choice == 1:
                                products[product_choice].set_status('В пути')
                            elif status_choice == 2:
                                products[product_choice].set_status('На складе')
                            elif status_choice == 3:
                                products[product_choice].set_status('Продан')
                            elif status_choice == 4:
                                products[product_choice].set_status('Возврат')
                            elif status_choice == 5:
                                products[product_choice].set_status('Зарезервирован')
                            else:
                                raise ValueError('Выберите корректное действие.')

                        except ValueError as e:
                            print(f'Ошибка: {e}')
                        except StatusError as e:
                            print(f'Ошибка: {e}')

                    case 5:
                        print('Введите нового поставщика: ', end='')
                        new_supplier = input()
                        if new_supplier:
                            products[product_choice].set_supplier(new_supplier)
                            print('Поставщик успешно изменен.')
                        else:
                            print('Ошибка: Поставщик не может быть пустым.')

                    case 6:
                        print('Введите нового производителя: ', end='')
                        new_developer = input()
                        if new_developer:
                            products[product_choice].set_developer(new_developer)
                            print('Производитель успешно изменен.')
                        else:
                            print('Ошибка: Производитель не может быть пустым.')

                    case 7:
                        print('Введите новую цену товара: ', end='')
                        try:
                            new_price = float(input())
                            products[product_choice].set_price(new_price)
                            print('Цена успешно изменена.')
                        except ValueError:
                            print('Ошибка: Введите число.')
                        except NumberError as e:
                            print(f'Ошибка: {e}')

                    case 8:
                        print('Введите новое местоположение: ', end='')
                        new_location = input()
                        if new_location:
                            products[product_choice].set_location(new_location)
                            print('Местоположение успешно изменено.')
                        else:
                            print('Ошибка: Местоположение не может быть пустым.')

                    case 9:
                        print('Введите новый цвет: ', end='')
                        new_color = input()
                        if new_color:
                            products[product_choice].set_color(new_color)
                            print('Цвет успешно изменен.')
                        else:
                            print('Ошибка: Цвет не может быть пустым.')

                    case 10:
                        print('Введите новую страну происхождения: ', end='')
                        new_country = input()
                        try:
                            products[product_choice].set_origincountry(new_country)
                            print('Страна происхождения успешно изменена.')
                        except NameError as e:
                            print(f'Ошибка: {e}')

                    case 11:
                        print(f'\nДоступные категории: {", ".join(categories)}')
                        print('Введите новую категорию: ', end='')
                        new_category = input().lower()
                        try:
                            products[product_choice].set_category(new_category)
                            print('Категория успешно изменена.')
                        except CategoryError as e:
                            print(f'Ошибка: {e}')

                    case 12:
                        print('Введите новый код товара: ', end='')
                        try:
                            new_code = float(input())
                            products[product_choice].set_codenumber(new_code)
                            print('Код товара успешно изменен.')
                        except ValueError:
                            print('Ошибка: Введите число.')
                        except NumberError as e:
                            print(f'Ошибка: {e}')

                    case 13:
                        print('\nДоступные категории товаров:')
                        for i, category in enumerate(categories, 1):
                            print(f'{i}) {category}')

            case 2:
                products.append(ProductCard())
                print('Новый товар успешно создан!')
                print(f'Всего товаров: {len(products)}')


if __name__ == "__main__":
    main()