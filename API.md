# API лаунчера Stalker-RP.net
Для некоторых запросов понадобится использовать user-agent лаунчера: `STALKER/1.0`

Также лаунчер использует знак `^` как разделитель

---

`https://files.stalker-rp.net/launcher/api/register.php?nicknamu={login}&machinu={hwid}&hashu={nick}`

Принимает ucp логин, идентификатор устройства, и сгенерированный никнейм

Ничего не возвращает, данный запрос нужен для возможности войти в игру

---

`https://files.stalker-rp.net/launcher/game/.launcher/{checksum}`

Возвращает контрольные суммы которые хранятся на сервере (скан директории, хэш суммы)

Всего контрольных сумм 3: dirs.lists, file.lists, hash.lists

---

`https://files.stalker-rp.net/launcher/api/version.php`

Возвращает версию лаунчера

---

`https://files.stalker-rp.net/launcher/api/information.php`

Возвращает текст и ссылки для главной страницы лаунчера

---

`https://files.stalker-rp.net/launcher/api/stats.php`

Возвращает текущий онлайн и количество слотов

---

`https://files.stalker-rp.net/launcher/api/admlvl.php?name={username}`

Принимает никнейм и возвращает уровень администратора

(в данный момент уже не работает)

---

`https://files.stalker-rp.net/launcher/api/ip.php`

Возвращает айпи адрес и порт основного и тестового сервера
