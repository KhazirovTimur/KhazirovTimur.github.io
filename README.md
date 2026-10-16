# KhazirovTimur.github.io

Bilingual (EN / RU) portfolio of Timur Khazirov, Technical Game Designer.
Built with plain Jekyll — no custom plugins — so GitHub Pages builds it as is.

## Как устроено

| Что | Где |
|---|---|
| Контакты, ссылка на CV | `_data/profile.yml` |
| Тексты главной (EN и RU) | `_data/home.yml` |
| Карьера / таймлайн | `_data/career.yml` |
| Подписи интерфейса, меню | `_data/i18n.yml` |
| Страницы проектов (EN) | `experience/*.md`, `projects/*.md` |
| Страницы проектов (RU) | `ru/experience/*.md`, `ru/projects/*.md` |
| Обо мне | `about/index.md`, `ru/about/index.md` |
| Файлы (CV, сертификаты) | `assets/files/` |
| Стили | `assets/css/main.css` |

**Переключатель языка.** У английской и русской версии страницы одинаковое поле `ref` во front matter. Переключатель EN/RU ищет страницу с тем же `ref` на другом языке. Всё, что лежит в `ru/`, — русская версия.

### Добавить новый проект
1. Скопируйте, например, `projects/helicopter.md` → `projects/new-thing.md`, поменяйте `ref`, `title`, `permalink`, `order` и текст.
2. Сделайте русскую пару в `ru/projects/new-thing.md` с тем же `ref` и permalink `/ru/projects/new-thing/`.
3. Карточка появится в списке автоматически (раздел определяется полем `section`).

Полезные поля front matter: `cover` (картинка обложки, 460×215), `youtube` (ID видео — встроится плеер), `links`, `highlights`, `loop` (схема кор-лупа), `stack`.

### Локальный запуск
```
bundle install
bundle exec jekyll serve
```
