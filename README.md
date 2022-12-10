## Скрипт, работающий со ссылками Битли и простыми ссылками

Скрипт выводит кол-во переходов по ссылке Битли или укорачивает простую ссылку до Битли

### Как установить

- Скачайте код и поместите в виртуальное окружение
```
python3 -m venv <название окружения>
```
```
<название окружения>\Scripts\activate.bat
```
```
git clone https://github.com/mihakurd2003/bitly.git
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как пользоваться
- В терминале набирайте команду(вместо url ваша ссылка):
```
python3 main.py url
```
- url - обязательный аргумент!

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).