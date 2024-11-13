# equipment_base

Компания выпускает сетевое оборудование. Каждому наименованию в зависимости от имени и типа выделяется свой диапазон IP адресов (в последствии могут добавляться) и присваивается свой заводской номер (нумерация сквозная).

Программа написана как back для front на Flet (не моя часть) для человека, который создает заказы на печать этикеток, указывая исполнителю начальные и конечные пары: заводской номер - IP адрес.

Пользователь выбирает имя,  тип и версию оборудования, и количество этикеток для заказа.
Программа может отдельно рассчитать предполагаемый заказ, а может рассчитать, сохранить в базу новую информацию о заказанных этикетках, а также сформировать файл с текстом письма для заказа.

В сервисной части можно добавить новое оборудование в базу, а также новые диапазоны для старого оборудования, если нынешний будет исчерпан.
