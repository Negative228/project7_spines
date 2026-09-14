# Денритные шипики!!!!

#### TODO: придумать какое-нибудь прикольное название

## Описание

Самая приятная часть приватного репо, это то, что я могу написать всё, что хочу, и остальной мир об этом не узнает. <br>
А вообще говоря TODO: сделать нормальное описание

## Как это всё запустить
#### TODO: сделать нормальные заголовки

### Системные требования
#### TODO: сделать нормально и на русском, пока возьму с оригинального репо RESPAN

| | **Minimum Recommended** | **Recommended** |
|---|---|---|
| OS | Windows 10/11 ×64 | Windows 10/11 ×64 |
| GPU | NVIDIA ≥ 8 GB VRAM | NVIDIA RTX 4090 (24 GB) |
| RAM | 32 GB | 128–256 GB |
| Storage | HDD | SSD |

> *RESPAN should work for NVIDIA GPUs with less than 8GB, but this has not been tested.<br>
> *RESPAN implements data chunking and tiling, but for some steps, larger images currently necessitate increased RAM requirements. <br>
> *Please refer to the table at the end of this document for further performance testing information.


### Установка
Предполагается, что вы используете Windows.
Если вы используете Linux/MacOS, то вы крутые, следовательно сами разберетесь.
```
cd path\to\project7_spines

python -m venv venv

venv\scripts\activate

pip install -r requirements.txt
```

Также очень желательно установить pytorch с поддержкой CUDA.
На данные момент команда следующая:
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132
```

Если она не работает, то ищите нужную [здесь](https://pytorch.org/get-started/locally/).

### Запуск программы

На данный момент у нас только два несчасных jupyter notebook, поэтому: <br>
В командной строке введите:
```
cd path\to\project7_spines

venv\scripts\activate

jupyter notebook
```

Альтернативно, нужный notebook можно открыть в вашей любимой IDE.

## Распростаненные проблемы

Пока никаких и слава Богу.

## Авторы

TODO: сделать красивые ссылки на нас всех

## Источники

* [RESPAN](https://github.com/lahammond/RESPAN)