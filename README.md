# cloud-xyz
Консольное приложение для примитивной обработки облаков точек в формате XYZ (тестовое задание).

## Зависимости

Необходим `python>=3.9`. Остальные зависимости указаны в `requirements.txt`.

## Использование

`python3 cloud FILE [-h] [-c] [-p] [-H [BINS]] [-r LO HI] [-o OUTPUT]`

- `FILE` — входной файл в формате XYZ
- `-c` — подсчёт количества точек
- `-p` — визуализация облака точек
- `-H` — построение гистограммы высот точек (Z)
- `-r` — удаление точек в диапазоне высот `[LO, HI]`
- `-o` — сохранение (возможно модифицированного) облака точек в файл `OUTPUT` в формате XYZ

## Примеры

Примеры входных данных лежат в папке `data`. Примеры запуска:

- `python3 cloud data/teapot_306.xyz -H -r 1 1.5 -o data/teapot_306_mod.xyz`
- `python3 cloud data/sphere_spiral_700.xyz -p -c`
- `python3 cloud data/helix_201.xyz -H 100 `

## Docker

Приложение также можно запустить в docker-контейнере (предварительно выполнив `docker build`). Пример:

```
docker build -t cloudxyz .
docker run --network host -e DISPLAY=$DISPLAY cloudxyz data/teapot_306.xyz -p
```
