# Анализ Stalker-RP.net
Несколько месяцев назад мне было интересно изучить техническую часть проекта stalker-rp, и в этом репозитории я опубликую все недочёты разработчиков.
Моё мнение что вся техническая часть проекта - просто дерьмо, которые разрабатывали какие-то скрипт кидди а не разработчики.

## Лаунчер
В лаунчере проекта имеется куча недочётов и уязвимостей, все показывать я не буду, но я покажу самую серьёзную - полный обход лаунчера.
То есть чтобы зайти в игру даже не придётся открывать лаунчер, и игрок сможет модифицировать и устанавливать любые файлы в директории игры.

**Ссылка на обход лаунчера: [BYPASS](https://github.com/atorisen/stalker-rp-analysis/launcher/)**

Также опишу вкратце логику лаунчера: при нажатии на кнопку "играть" лаунчер сканирует все папки и файлы в директории игры, и также он собирает md5 хэш всех файлов (кстати, весь процесс он записывает не в память, а в созданные файлы в папке игры XD).
Далее эти файлы удаляются, отправляются несколько запросов на их неофициальный api для лаунчера, и все сканы сверяются с ответом от api.
Если лаунчер сверив все сканы ничего не выявил, то отправляется get запрос api на регистрацию игрока, в котором передаются параметры: ucp логин, hwid, и сгенерированный никнейм для авторизации на игровом сервере.
На самом игровом сервере при входе проверяется, был ли данный никнейм зарегистрирован лаунчером. Если же некоторые файлы не прошли проверку лаунчера - они удаляются, и лаунчер делает попытку скачать их с api.

## Веб-сайт
Веб-сайт я анализировал меньше чем лаунчер, но всё равно нашёл парочку уязвимостей и недочётов.
Вот одна из уязвимостей: обход этапа с вопросами ucp регистрации. Сделан этот обход был как на релизной версии сайта, так и на бета версии.

**Ссылка на обход UCP регистрации: [WEB](https://github.com/atorisen/stalker-rp-analysis/web/)**

## Api
Также я хотел бы выложить свою документацию к неофициальному api проекта.

**Ссылка на документацию к API: [API](https://github.com/atorisen/stalker-rp-analysis/API.md)**
