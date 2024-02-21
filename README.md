__Discord Auto Poster - Автоматическая отправка сообщений Discord в каналы на серверах.__

Проект представляет собой приложение для автоматизации отправки сообщений в каналах на серверах платформы Discord. 

Функционал:
- Прикрепление изображений
- Установка временного интервала
- Работа в свернутом режиме
- Работа без использования клиента Discord
- Сохранение выбранных настроек
- Многопоточность

----------
# Инструкция по установке

- Скачать [архив](https://drive.google.com/file/d/1DQMxpu0_dPUHTbSJMx2sFA7qDg1uegtD/view?usp=drive_link).
- Распаковать в любую папку
- Запустить autods.exe

# Инструкция использования программы
__Получение токена пользователя:__
1. Откройте Discord в браузере или через приложение
2. Войдите в аккаунт, с которого будут отправляться сообщения
3. Нажмите сочетание CTRL + Shift + I
4. Откройте вкладку "Network"
5. В строке Filter вписать "/api"
6. Нажмите сочетание Ctrl + R . После появления множества вкладок, заходим в любую из них
7. В появившемся списке справа в третьем разделе "Request Headers" ищите пункт "authorization:"
8. В нем будет написан токен вашего аккаута (Пример: authorization: N9kghTFd671RTGgg)
9. Копируете его
10. Вставьте в программу (Внимание! Никому не сообщайте свой токен, вас могут взломать!)