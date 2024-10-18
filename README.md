# Мониторинг прохода пользователей связанных с учетными записями пользователей операционной системы Linux  
Позволяет:  
- периодически добавлять пользователей в систему мониторинга на основании учётных записей пользователей операционной системы Linux.  
- импортировать данные о контрольно-пропускных пунктах.  

## Стек технологий  
Python 3.11.9, Django 5.1.2, Django REST framework 3.15.2, Psycopg 3.2.3, PostgreSQL, SQLite  

## Как развернуть  
Создать окружение  
```  
python3 -m venv venv  
```  

Активировать окружение, обновить pip и установить зависимости  
```  
source venv/bin/activate  
python3 -m pip install --upgrade pip  
pip install -r requirements.txt  
```  

Настроить подключение к БД в settings.py, применить миграции, импортировать базовые сведения о КПП  
```  
python3 manage.py migrate  
python3 manage.py gates_import  
```  

Добавить в cron запуск скрипта добавления пользователей в систему мониторинга на основании учётных записей пользователей операционной системы Linux с интервалом 5 минут  
```  
sudo crontab -e  
*/5 * * * * /path/to/gates_for_rusel/venv/bin/python3 /path/to/gates_for_rusel/manage.py users_os_import  
```  

Перейти в браузере по адресу  
```  
http://127.0.0.1:8000/api/v1/  
```  

По окончании использования деактивировать окружение  
```  
deactivate  
```  

## Разработчик  
[Мишустин Василий](https://github.com/vvvas), v@vvvas.ru  
