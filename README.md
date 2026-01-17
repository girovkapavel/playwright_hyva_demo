# Playwright + Pytest (POM) — demo.hyva.io

Простой проект автотестов для сайта https://demo.hyva.io, написанный максимально понятным способом в стиле Page Object Model (POM).

## Структура
- `pages/base_page.py` — базовый класс страниц (goto, click, fill, text)
- `pages/home_page.py` — главная страница: открытие, поиск, открытие первого товара
- `pages/product_page.py` — страница товара: добавление в корзину, открытие мини‑корзины
- `tests/test_main_flow.py` — простой сценарий пользователя: поиск и добавление товара в корзину
- `conftest.py` — фикстуры pytest (браузер и страница), браузер запускается в headed режиме
- `requirements.txt` — зависимости

## Установка
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

## Запуск тестов
```bash
pytest --headed -q -s
```


## Идея POM (коротко)
- В тесте мы вызываем методы страниц, а не пишем селекторы напрямую.
- Это упрощает понимание: тест описывает шаги, а детали селекторов спрятаны в классах страниц.

## Что проверять на страницах

| Страница                       |Что проверять                                                                 |
|--------------------------------|------------------------------------------------------------------------------|
| **HomePage**                   | Блоки баннеров, карусели, рекомендации, ссылки в шапке, футере               |
| **Category / PLP**             | Сортировка, фильтры, отображение товаров, пагинация                          |
| **Product Page / PDP**         | Кнопка «Add to Cart», изображения, описание, атрибуты товара, рекомендации, отзывы |
| **Cart Page / Mini Cart**      | Добавление, удаление, изменение количества, расчёт цены, скидки              |
| **Checkout Page**              | Поля ввода, методы оплаты, валидация, оформление заказа                      |
| **Login / Register / Account** | Авторизация, регистрация, восстановление пароля, редиректы                   |
| **Search / Autocomplete**      | Поиск по сайту, результаты, фильтры                                          |
| **CMS Pages (About, Contact)** | Контент, ссылки, формы, SEO элементы                                         |

# Python AI Project

## Overview
This project demonstrates the use of Playwright for end-to-end testing of a Python-based web application. Below is a list of all the working tests categorized by their respective test files.

## Tests

### test_cart.py
- `test_add_to_cart_on_pdp`: Adds a product to the cart from the product details page.
- `test_open_cart_from_pdp`: Opens the cart from the product details page.
- `test_input_discount`: Inputs a discount code in the cart.
- `test_change_quantity`: Changes the quantity of an item in the cart.
- `test_remove_item_from_cart`: Removes an item from the cart.
- `test_proceed_to_checkout`: Proceeds to the checkout page.

### test_home.py
- `test_whats_new`: Clicks on the "What's New" section.
- `test_women`: Clicks on the "Women" section.
- `test_men`: Clicks on the "Men" section.
- `test_gear`: Clicks on the "Gear" section.
- `test_training`: Clicks on the "Training" section.
- `test_sale`: Clicks on the "Sale" section.

### test_login.py
- `test_authorization`: Logs in with a valid email and password.
- `test_forgot_password`: Tests the "Forgot Password" functionality.
- `test_register_account`: Registers a new account with valid details.

### test_search.py
- `test_search_product`: Searches for a product (e.g., "bag").

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `pytest`

## Notes
- Ensure Playwright is installed and set up correctly before running the tests.
