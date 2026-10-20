# MineShelt

**Version: 1.2.0** — объёмная архитектура самих построек, палитры, терраформинг, деревья и визуальный разбор строительных работ.

**Architectural craft for AI agents building in Minecraft.**  
**MineShelt — навык ИИ-архитектора и профессионального Minecraft-билдера.**

MineShelt is an [Agent Skill](https://agentskills.io/specification), not a procedural structure generator, prefab catalog, or random block placer. It teaches an agent to **conceive, art-direct, plan, build, inspect, and refine** original Minecraft structures with the intentionality of an experienced human builder.

## Что умеет

- Проектировать постройки под биом, историю места, эпоху, стиль и техническое задание.
- **Реально подбирать и испытывать палитры блоков:** тестовые стенды, роли материалов, направленные градиенты, работа с текстурами и состояниями блоков.
- **Профессионально формировать рельеф:** холмы, скалы, слои пород, осыпи, реки, берега, террасы, экологичные переходы и маршруты.
- **Проектировать авторские деревья и посадки:** стволы, ветви, кроны, корни, подлесок и природные группы.
- Изучать изображения работ других строителей, выделять архитектурные принципы и адаптировать их, сохраняя атрибуцию.
- Мыслить силуэтом и архитектурной массой, а не начинать с хаотичного декора.
- **Проектировать реальный архитектурный рельеф здания:** фасады в нескольких плоскостях, утопленные окна и двери, эркеры, колонны, галереи, арки, карнизы, свесы и настоящие опоры. Проверять постройку сбоку, сзади, по диагонали и снизу; не пытаться исправлять плоские стены только декоративными люками.
- Подбирать взаимосвязанные палитры материалов и осмысленно распределять износ.
- Проектировать крыши, фасады, фундамент, входы, окна, интерьеры, окружение.
- Создавать асимметрию и живые детали **по архитектурным причинам**, а не случайным шумом.
- Реализовывать замысел в доступном для агента Minecraft-мире или исходном коде мода.
- Проверять результат с разных ракурсов, в контексте окружающего мира и в игре.
- Находить слабые места, исправлять их и честно сообщать, что реально построено и проверено.

## Чего в проекте нет

**Нет генератора зданий, процедурного рандомайзера, обязательных схем, NPC-строителя или библиотеки готовых домов.** Скилл направляет решения самого ИИ-агента. Не обещает магически дать агенту доступ к игровому миру, которого у него нет.

## Установка

~~~bash
git clone https://github.com/skaletun/MineShelt.git
~~~

Скопируйте **внутреннюю папку mineshelt/** в каталог навыков вашего агента. Варианты:

| Agent / workspace | Location |
| --- | --- |
| Claude Code project | .claude/skills/mineshelt/ |
| Codex project | .agents/skills/mineshelt/ |
| Any Agent Skills-compatible host | configured skills directory/mineshelt/ |

Пример для Linux/macOS после перехода в каталог проекта агента:

~~~bash
mkdir -p .agents/skills
cp -R /path/to/MineShelt/mineshelt .agents/skills/mineshelt
~~~

На Windows PowerShell:

~~~powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\MineShelt\mineshelt .agents\skills\mineshelt
~~~

Установка инструкции — не установка Minecraft, NeoForge, Fabric, WorldEdit или права записи в мир. Для реального строительства у агента должны быть инструменты, доступ к репозиторию или игровому окружению.

Подробнее: [docs/INSTALL.md](docs/INSTALL.md), [docs/USE.md](docs/USE.md) и [CHANGELOG.md](CHANGELOG.md).

## Пример вызова

> Используй MineShelt. В существующем моде Minecraft создай авторскую кузницу для поселения в еловой тайге. Она должна выглядеть как работа опытного строителя, вписываться в склон, иметь читаемый силуэт, функциональный интерьер и законченный окружающий участок. Реализуй её в имеющемся проекте, затем проверь непосредственно в игре и переработай слабые места. Не используй генератор построек.

## Состав

- [mineshelt/SKILL.md](mineshelt/SKILL.md) — основной контракт, процесс и правила действий агента.
- [mineshelt/references/](mineshelt/references/) — архитектура, пропорции, палитры, интерьеры, терраформинг, деревья, визуальные референсы, интеграция в Minecraft и ревизия.
- [mineshelt/references/architectural-depth-and-relief.md](mineshelt/references/architectural-depth-and-relief.md) — реальная трёхмерная архитектура построек: объём, выступы, углубления и опоры.
- [mineshelt/references/block-palette-workshop.md](mineshelt/references/block-palette-workshop.md) — палитры, пробы блоков, градиенты и борьба с визуальным шумом.
- [mineshelt/references/terrain-sculpting-masterclass.md](mineshelt/references/terrain-sculpting-masterclass.md) — ручное проектирование рельефа, скал и водоёмов.
- [mineshelt/references/reference-study-and-image-analysis.md](mineshelt/references/reference-study-and-image-analysis.md) — подбор визуальных источников и указание авторства.
- [mineshelt/examples/](mineshelt/examples/) — разборы кузницы, гавани со скалой, исправления палитры и превращения плоской мастерской в объёмное здание, **не шаблоны для копирования**.
- [tests/scenarios.md](tests/scenarios.md) — набор оценочных сценариев, включая отрицательные.
- [AGENTS.md](AGENTS.md) — правила поддержки проекта.
- [tests/review-sheet.md](tests/review-sheet.md) — форма оценки результата по реальным игровым изображениям.

## Главное правило

**No random detail before deliberate form.** Сначала место, идея, план, масса и силуэт; потом конструкция, фасады, интерьер и осмысленные следы жизни; затем критика по реальным изображениям/в игре и исправления.

## Compatibility

The skill follows the Agent Skills SKILL.md convention. Tooling and game integration are host-dependent. Edition, version, mod loader, block registry, world-generation pipeline, asset constraints, and access to screenshots must be discovered in each target project rather than presumed.

## License

MIT. See [LICENSE](LICENSE).
