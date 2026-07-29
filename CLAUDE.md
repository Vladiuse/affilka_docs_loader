# CLAUDE.md

Скрипты для выгрузки документации Affilka (закрытая вики wiki.affilka.net) в Markdown.

`project-instructions.md` — отдельный файл, системная инструкция для веб-версии Claude (Project), где эта база знаний используется для ответов на вопросы. К работе с кодом в этом репозитории отношения не имеет, не трогать без явного запроса.

## Пайплайн

1. `download_site.py` — Selenium (Chrome) обходит wiki.affilka.net в ширину по ссылкам, авторизуясь через JWT-cookie (`COOKIE_VALUE` в `.env`). Сохраняет отрендеренный HTML каждой страницы в `site/`, повторяя структуру URL как вложенные папки.
2. `extract.py` — берёт HTML из `site/`, находит блок статьи (`div.contents`) через BeautifulSoup, извлекает текст через `trafilatura` (`favor_recall=True` — без этого теряются куски контента) и сохраняет `.md` в `text/`. Имя файла = путь страницы, `/` заменён на `__`.
3. `config.py` — общие пути (`SITE_DIR`, `TEXT_DIR`).

## Прочее

- `api_docs/` — OpenAPI-схемы Affilka API, получены отдельно от пайплайна выше.

