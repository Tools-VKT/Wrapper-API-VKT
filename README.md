# ⚙️ Wrapper-API-VKT
Специальная обертка для методов **VK API** секции `bugtracker`

## ❓ Как работает?
Обертка каждый день будет обновлять токен (вечный получить нельзя, т.к. не **Standalone-приложение**) от приложения [мобильного Баг-трекера](https://vk.com/app6831669). 
В `config.py` нужно будет указать креды от аккауна (только логин и пароль), обновление же происходит с помощью прямой авторизации в VK.com (в этом нам помогает пакет `selenium`)

В обертке доступен один метод - получение карточки тестировщика по пути `/vk-bugs-api/?method=getReporter&id={USER_ID}`

## 👨‍💻 А как запустить?
Перед запуском нужно поставить некоторые пакеты, команды:
```
pip3 install selenium==4.14.0
pip3 install flask
pip3 install flask-restful
```

Запускаем главный файл с помощью команды:
```
python3 api.py
```

Profit!