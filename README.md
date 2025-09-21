# 📡 Diameter Message Parser with DPath Queries

Этот проект реализует парсер Diameter-сообщений с использованием ANTLR4 и поддержку XPath-подобного языка запросов (DPath) для поиска по AVP (Attribute-Value Pairs).

---

## 🚀 Возможности
- Разбор Diameter-сообщений с помощью ANTLR-грамматики.
- Поддержка XML-представления сообщений.
- Реализация DPath-запросов с осями:
  - child:: — дочерние AVP (по умолчанию, если ось не указана).
  - descendant:: — все дочерние AVP рекурсивно.
  - descendant_or_self:: — как descendant плюс текущая AVP.
  - parent:: — родительский AVP.
  - ancestor:: — все предки AVP.
  - ancestor_or_self:: — как ancestor плюс текущая AVP.
  - following:: — все AVP после текущего.
  - following_sibling:: — братские AVP справа.
  - preceding:: — все AVP до текущего.
  - preceding_sibling:: — братские AVP слева.
- Обработка примеров с нулевым, одним и несколькими совпадениями.

---

## 🛠 Технологии
- [Python 3](https://www.python.org/)
- [ANTLR4](https://www.antlr.org/)
- [dpath](https://github.com/akesterson/dpath-python) / [xmltodict](https://github.com/martinblech/xmltodict)

---

## 📦 Установка
`bash
git clone https://github.com/Alekcey5977/DPath
cd diameter-parser
pip install -r requirements.txt
