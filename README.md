# Project7: Автоматическое обнаружение и анализ на субклеточном уровне

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()


## 📌 О проекте

Проект **project7_spines** посвящен созданию средств для автоматизации подготовки данных и разработке алгоритмов способных повысить отношение сигнал/шум на изображениях. 

Конечной целью является полная автоматизация процесса оценки динамики нейронных структур мозга.

### Актуальность
Ручная разметка изображений двухфотонной лазерной сканирующей микроскопии экспертами-биологами — трудоемкий и субъективный процесс. Автоматизированные средства (например, RESPAN)  обеспечивают высокую скорость анализа, воспроизводимость результатов и объективность детектирования.

### Научный контекст
Проект выполняется в рамках прикладного проекта Южного федерального университета (ЮФУ) по направлению «Гибридные нейросетевые и вейвлет-методы ИИ для реконструкции корковой активности и декодирования мысленных команд в мобильных системах ЭЭГ с ограниченным числом отведений».

---

## ✨ Возможности

- 🤖 **Предобработка 3D-изображений** z-стеков при помощи нейронной РБФ-сети.
- 🧮 **Подготовка данных** для дальнейшей работы в RESPAN
- 📈 **Визуализация результатов** с возможностью сравнения разметки экспертов и RESPAN.
- 📦 **Готовые примеры** использования в Jupyter Notebook.

---

## 🏗 Структура репозитория

```text
project7_spines/
├── assets/img/               # Изображения для документации и примеров
── example/                  # Примеры использования (Jupyter Notebooks)
│   ├── example_rbf.ipynb     # Пример работы с RBF-модулем
│   └── example_respan.ipynb  # Пример полного пайплайна анализа
├── modules/                  # Исходный код проекта
│   ├── RBF/                  # Модуль радиально-базисных функций
│   ├── respy/                # Основной пакет RESPAN для анализа
│   └── __init__.py
├── .gitattributes
├── .gitignore
├── README.md                 # Этот файл
├── RESPAN_INSTALLATION.md    # Подробная инструкция по установке ПО
├── RESPAN_METHODOLOGY.md     # Описание методологии сравнения разметок
└── requirements.txt          # Зависимости Python
```
---

## 🏗 Установка 
Создайте виртуальной окружение и установите зависимости:
```
cd path\to\project7_spines

python -m venv venv

venv\scripts\activate

pip install -r requirements.txt
```

После чего установите PyTorch с поддержкой CUDA:
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132
```

Если команда выше не работает, обратитесь на [официальный сайт PyTorch](https://pytorch.org/get-started/locally/).

--- 

## Запуск

Для работы с модулями репозитория в Jupyter Notebook введите в командной строке:
```
cd path\to\project7_spines

venv\scripts\activate

jupyter notebook
```
---

## 👥 Команда
* **Филимонов Максим** — лаборант-исследователь, Центр Сквозных Технологий ЮФУ — [@Negative228](https://github.com/Negative228)
* **Диана Сушкова** — студент 2 курса ИММиКН им. И.И. Воровича — [@DiankaS](https://github.com/DiankaS)

---
## Список литературы
* Soria Lopez J. A., González H. M., Léger G. C. Alzheimer's disease // Handb. Clin. Neurol. – 2019. – Vol. 167. – P. 231–255. – DOI: 10.1016/B978-0-12-804766-8.00013-3.
* Knobloch M., Mansuy I. M. Dendritic spine loss and synaptic alterations in Alzheimer's disease // Mol. Neurobiol. – 2008. – Vol. 37, No. 1. – P. 73–82. – DOI: 10.1007/s12035-008-8018-z.
* Dorostkar M. M., Zou C., Blazquez-Llorca L., Herms J. Analyzing dendritic spine pathology in Alzheimer's disease: problems and opportunities // Acta Neuropathol. – 2015. – Vol. 130, No. 1. – P. 1–19. – DOI: 10.1007/s00401-015-1449-5.
* Reza-Zaldivar E. E., Hernández-Sápiens M. A., Minjarez B., Gómez-Pinedo U., Sánchez-González V. J., Márquez-Aguirre A. L., Canales-Aguirre A. A. Dendritic Spine and Synaptic Plasticity in Alzheimer's Disease: A Focus on MicroRNA // Front. Cell Dev. Biol. – 2020. – Vol. 8. – Art. 255. – DOI: 10.3389/fcell.2020.00255.
* Handbook of Biological Confocal Microscopy / ed. by J. B. Pawley. – – 3rd ed. – New York : Springer, 2006.
* Pchitskaya E., Vasiliev P., Smirnova D. et al. SpineTool is an open-source software for analysis of morphology of dendritic spines // Sci. Rep. – 2023. – Vol. 13. – Art. 10561. – DOI: 10.1038/s41598-023-37406-4. 
* Bernal-Garcia S., Schlotter A. P., Pereira D., Polleux F., Hammond L. A. A deep learning pipeline for accurate and automated restoration, segmentation, and quantification of dendritic spines // Cell Rep. Methods. – 2025. – Vol. 5, No. 10. – Art. 101179. – DOI: 10.1016/j.crmeth.2025.101179.
* Fernholz M. H. P., Guggiana Nilo D. A., Bonhoeffer T., Kist A. M. DeepD3, an open framework for automated quantification of dendritic spines // PLOS Comput. Biol. – 2024. – Vol. 20, No. 2. – Art. e1011774. – DOI: 10.1371/journal.pcbi.1011774. 
* Das N., Baczynska E., Bijata M., Ruszczycki B., Zeug A., Plewczynski D., Saha P. K., Ponimaskin E., Wlodarczyk J., Basu S. 3dSpAn: An interactive software for 3D segmentation and analysis of dendritic spines // Neuroinformatics. – 2021. – DOI: 10.1007/s12021-021-09549-0. – Epub ahead of print.
* Gilles J. F., Mailly P., Ferreira T. et al. Spot Spine, a freely available ImageJ plugin for 3D detection and morphological analysis of dendritic spines // F1000Research. – 2024. – Vol. 13. – Art. 176. – DOI: 10.12688/f1000research.13.176.2.
* Hering H., Sheng M. Dendritic spines: structure, dynamics and regulation // Nat. Rev. Neurosci. – 2001. – Vol. 2. – P. 880–888. – DOI: 10.1038/35104061.	 
* González-Burgos I. Dendritic spines plasticity and learning/memory processes: Theory, evidence and perspectives // Dendritic Spines: Biochemistry, Modeling and Properties / ed. by L. R. Baylog. – New York : Nova Science Publishers, 2009. – P. 163–186.	
* Ma S., Zuo Y. Synaptic modifications in learning and memory – A dendritic spine story // Semin. Cell Dev. Biol. – 2022. – Vol. 125. – P. 84–90. – DOI: 10.1016/j.semcdb.2021.05.015.
* Rochefort N. L., Konnerth A. Dendritic spines: from structure to in vivo function // EMBO Rep. – 2012. – Vol. 13, No. 8. – P. 699–708. – DOI: 10.1038/embor.2012.102.
* Pchitskaya E., Bezprozvanny I. Dendritic Spines Shape Analysis – Classification or Clusterization? Perspective // Front. Synaptic Neurosci. – 2020. – Vol. 12. – Art. 31. – DOI: 10.3389/fnsyn.2020.00031.
* von Bohlen und Halbach O. Structure and function of dendritic spines within the hippocampus // Ann. Anat. – 2009. – Vol. 191, No. 6. – P. 518–531. – DOI: 10.1016/j.aanat.2009.08.006.
* Papa M., Bundman M. C., Greenberger V., Segal M. Morphological analysis of dendritic spine development in primary cultures of hippocampal neurons // J. Neurosci. – 1995. – Vol. 15, No. 1, Pt. 1. – P. 1–11. – DOI: 10.1523/JNEUROSCI.15-01-00001.1995.
* Korkotian E., Segal M. Regulation of dendritic spine motility in cultured hippocampal neurons // J. Neurosci. – 2001. – Vol. 21, No. 16. – P. 6115–6124. – DOI: 10.1523/JNEUROSCI.21-16-06115.2001.
* Fiala J. C., Feinberg M., Popov V., Harris K. M. Synaptogenesis via dendritic filopodia in developing hippocampal area CA1 // J. Neurosci. – 1998. – Vol. 18, No. 21. – P. 8900–8911. – DOI: 10.1523/JNEUROSCI.18-21-08900.1998.
* Zuo Y., Lin A., Chang P., Gan W. B. Development of long-term dendritic spine stability in diverse regions of cerebral cortex // Neuron. – 2005. – Vol. 46, No. 2. – P. 181–189. – DOI: 10.1016/j.neuron.2005.04.001.
* Grutzendler J., Kasthuri N., Gan W. B. Long-term dendritic spine stability in the adult cortex // Nature. – 2002. – Vol. 420, No. 6917. – P. 812–816. – DOI: 10.1038/nature01276.
* Spires-Jones T. L., Meyer-Luehmann M., Osetek J. D., Jones P. B., Stern E. A., Bacskai B. J., Hyman B. T. Impaired spine stability underlies plaque-related spine loss in an Alzheimer's disease mouse model // Am. J. Pathol. – 2007. – Vol. 171, No. 4. – P. 1304–1311. – DOI: 10.2353/ajpath.2007.070055.
* Matukhno A. E., Tkacheva P. V., Voinov V. B. et al. Chronic Imaging of Dendritic Spine Morphology in Transgenic Mice of the 5xFAD-M Hybrid Strain, a Model of Alzheimer's Disease // Neurosci. Behav. Phys-iol. – 2025. – Vol. 55. – P. 657–666. – DOI: 10.1007/s11055-025-01811-1. 
* Grienberger C., Konnerth A. Imaging calcium in neurons // Neuron. – 2012. – Vol. 73, No. 5. – P. 862–885. – DOI: 10.1016/j.neuron.2012.02.011.
* Xu C., Nedergaard M., Fowell D. Multiphoton fluorescence microscopy for in vivo imaging // Cell. – 2024. – Vol. 187. – P. 4458–4487. – DOI: 10.1016/j.cell.2024.07.036.
* Luu P., Fraser S. E., Schneider F. More than double the fun with two-photon excitation microscopy // Commun. Biol. – 2024. – Vol. 7. – Art. 364. – DOI: 10.1038/s42003-024-06057-0. 
* Greenberg D. S., Kerr J. N. Automated correction of fast motion artifacts for two-photon imaging of awake animals // J. Neurosci. Methods. – 2009. – Vol. 176, No. 1. – P. 1–15. – DOI: 10.1016/j.jneumeth.2008.08.020.
* Nikolaev D. M., Metelkina E. M., Shtyrov A. A., Li F., Panov M. S., Ryazantsev M. N. Noise Sources and Strategies for Signal Quality Im-provement in Biological Imaging: A Review Focused on Calcium and Cell Membrane Voltage Imaging // Biosensors. – 2026. – Vol. 16. – Art. 31. – DOI: 10.3390/bios16010031. 
* Theer P., Denk W. On the fundamental imaging-depth limit in two-photon microscopy // J. Opt. Soc. Am. A. – 2006. – Vol. 23, No. 12. – P. 3139–3149. – DOI: 10.1364/josaa.23.003139.
* Podgorski K., Ranganathan G. Brain heating induced by near-infrared lasers during multiphoton microscopy // J. Neurophysiol. – 2016. – Vol. 116, No. 3. – P. 1012–1023. – DOI: 10.1152/jn.00275.2016.
* Park J., Sandberg I. W. Universal Approximation Using Radial-Basis-Function Networks // Neural Comput. – 1991. – Vol. 3, No. 2. – P. 246–257. – DOI: 10.1162/neco.1991.3.2.246.
* Shcherban I. V., Fedotova V. S., Matukhno A. E., Shepelev I. E., Shcherban O. G., Lysenko L. V. A method for detecting spatiotemporal patterns of cancer biomarkers-evoked activity using radial basis function network extracted time-domain features from calcium imaging data // J. Neurosci. Methods. – 2024. – Vol. 405. – Art. 110097. – DOI: 10.1016/j.jneumeth.2024.110097.
* Soper D. S. Using an Opportunity Matrix to Select Centers for RBF Neural Networks // Algorithms. – 2023. – Vol. 16. – Art. 455. – DOI: 10.3390/a16100455
* Haykin S. Neural Networks: A Comprehensive Foundation. – Englewood Cliffs : Prentice-Hall, 1998.
* Gonzalez R. C., Woods R. E. Digital Image Processing. – 4th ed. – Pearson, 2018.
