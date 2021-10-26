# gkhParsing

Реализация 1 части тестового задания.

Данный скрипт позволяет найти определенную информацию с сайта, используя Тестовую Выборку.
(Все компоненты указаны в положении тестового задания)

В процессе работы данного скрипта заполняется словарь Python. 
С ключами в виде номера строки из Тестовой Выборки (номером запроса) и значением в виде словарей, содержащих информацию об ошибках работы скрипта и собранные данные.

Скрипт использует "расширенный поиск" веб-источника. 
Недостатком скрипта является отсутствие алгоритма выбора предложенных элементов при поиске дома. (В скрипте выбирается первый элемент из предложенных в списке.)
Из-за указанного недостатка, большая часть поисковых "запросов" не достигают страницы с искомой информацией.

Решением недостатка может быть серия последовательных "запросов" с другим выбором предложенных вариантов. (На данный момент не реализовано)

Также при продолжительной работе скрипта сайт начинает проверять скрипт с помощью captcha.
Кроме как ручного ввода captcha данную проблему не решить. (Скрипт дважды пытается попасть на ресурс с некоторой задержкой. Между попытками можно успеть ввести captcha вручную).
