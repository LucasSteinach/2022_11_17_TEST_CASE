# Тестовое задание

## Стек

Python, poetry, pytest, coverage.

## Приложение

CLI приложение, которое:

1) Получает на вход произвольное множество строк.
2) Итерируется по этим строкам и определяет, является ли эта строка ссылкой или нет.
3) Если эта строка не ссылка, выводится уведомление: Строка "X" не является ссылкой.
4) Если является ссылкой, то
	1) Приложение должно определить какие методы доступны по этой ссылки
		1) Проверяются все http методы.
		2) Доступным считается метод, обработка которого завершилась не 405 ошибкой.
	3) Передаваемые данные и ошибки от сервера не важны.
	4) Выполнив запрос приложение сохраняет код ответа.
6) Результатом работы приложением будет словарь, состоящий из ссылок и информации о доступных метода.


```json
// Пример консольного ответа от программы
{
	"https://google.com": {
		"GET": 301,
	},
	"https://www.facebook.com": {
		"GET": 200,
		"OPTIONS": 200,
	}
}
```

## Дополнительно

Стремитесь к минимизации времени выполнения программы. Использование памяти не важно.

## Тестирование

Для тестирования используете `pytest`.

Стремитесь к 100% покрытию тестами.
Предоставьте отчет о покрытии. Для этого используйте библиотеку `coverage`.

## Сдача

Результатом выполнения принимается ссылка на гит репозиторий.

Засеките пожалуйста сколько времени вы уделили заданию и укажите это в readme.
