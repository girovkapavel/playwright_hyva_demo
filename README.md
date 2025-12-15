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

