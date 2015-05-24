#! coding: utf-8
from django.db import models

from solo.models import SingletonModel

from colorfield.fields import ColorField


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(u'Название сайта', max_length=255,
                                 default=u'Консультирование и практическая помощь по открытию магазинов')

    #------------------------ Block1
    block1_visibility = models.BooleanField(u'Показывать', default=True)
    block1_background = ColorField(u'Блок1 Цвет фона', blank=True, default='#5287a7')
    block1_logo = models.ImageField(u'Блок1 Логотип', upload_to='block1_images/', default='images/logo.png',
                                    blank=True, null=True)
    block1_text = models.CharField(u'Блок1 Текст', max_length=200, blank=True,
                                   default=u'Помощь при открытии магазинов</br>с гарантией получения прибыли</br><span>'
                                           u'в Краснодарском крае и Крыму</span>')
    block1_phone = models.CharField(u'Блок1 Телефон', max_length=100, blank=True, default=u'7 (918) 930-03-16')
    block1_button_color = ColorField(u'Блок1 Цвет кнопки', blank=True, default='#fff600')
    block1_button_text = models.CharField(u'Блок1 Текст кнопки', max_length=100, blank=True, default=u'ЗАКАЗАТЬ ЗВОНОК')

    #------------------------ Block2
    block2_visibility = models.BooleanField(u'Показывать', default=True)
    block2_background = models.ImageField(u'Блок2 Картинка', upload_to='block2_images/', default='images/hats.jpg',
                                          blank=True, null=True)
    block2_text = models.CharField(u'Блок2 Текст', max_length=200, blank=True,
                                   default=u'ОТКРОЙТЕ СВОЙ МАГАЗИН</br><span>БЕЗ ЗОНЫ РИСКА!</span>')

    #------------------------ Block3
    block3_visibility = models.BooleanField(u'Показывать', default=True)
    block3_text = models.CharField(u'Блок3 Заголовок', max_length=200, blank=True,
                                   default=u'ТОЛЬКО СЕГОДНЯ!</br>Вы получаете<span> БЕСПЛАТНО!</span>')
    block3_image = models.ImageField(u'Блок3 Изображение под Заголовком', upload_to='block3_images/',
                                     default='images/decoration_1.jpg',
                                     blank=True, null=True)
    block3_list_icon = models.ImageField(u'Блок3 Изображение для списка', upload_to='block3_images/', default='images/ok.png',
                                         blank=True, null=True)
    block3_item1 = models.BooleanField(u'Блок3 Первый пункт', default=True)
    block3_item1_text = models.CharField(u'Блок3 Текст первого пункта', max_length=200, blank=True,
                                         default=u'Пошаговый план открытия минимаркета')
    block3_item2 = models.BooleanField(u'Блок3 Второй пункт', default=True)
    block3_item2_text = models.CharField(u'Блок3 Текст второго пункта', max_length=200, blank=True,
                                         default=u'Метод увеличения среднего чека в магазине')
    block3_item3 = models.BooleanField(u'Блок3 Третий пункт', default=True)
    block3_item3_text = models.CharField(u'Блок3 Текст третьего пункта', max_length=200, blank=True,
                                         default=u'3D модель вашего будущего магазина')
    block3_time = models.TimeField(u'Время до конца акции', default='08:31:57', blank=True, null=True)

    #------------------------ Block4
    block4_visibility = models.BooleanField(u'Показывать', default=True)
    block4_text = models.CharField(u'Блок4 Текст', max_length=200, blank=True,
                                   default=u'УЧАСТВУЙТЕ В АКЦИИ</br><span>и Ваш бизнес выйдет</br>на новый уровень!'
                                           u'</span>')
    block4_button_text = models.CharField(u'Блок4 Текст на кнопке', max_length=100, blank=True,
                                          default=u'ПОЛУЧИТЬ БЕСПЛАТНО')
    block4_under_button_text = models.CharField(u'Блок4 Текст после кнопки', max_length=100, blank=True,
                                                default=u'Ваши контактные данные в безопасности</br>и не будут переданы'
                                                        u' третьим лицам')
    block4_back_color = ColorField(u'Блок4 Цвет фона', blank=True, default='#5287a7')
    block4_button_color = ColorField(u'Блок4 Цвет кнопки', blank=True, default='#fff600')
    block4_field_color = ColorField(u'Блок4 Цвет полей', blank=True, default='#294353')

    #------------------------ Block5
    block5_visibility = models.BooleanField(u'Показывать', default=True)
    block5_text = models.CharField(u'Блок5 Заголовок', max_length=100, blank=True,
                                   default=u'СТАТИСТИЧЕСКИЕ ДАННЫЕ')
    block5_back = models.ImageField(u'Блок5 Изображение', upload_to='block5_images/',
                                    default='images/stats.jpg',
                                    blank=True, null=True)
    block5_item1_text = models.CharField(u'Блок5 Текст первого пункта', max_length=200, blank=True,
                                         default=u'Каждый 5 открывающийся магазин</br>проживет не более 6 месяцев</br>')
    block5_item2_text = models.CharField(u'Блок5 Текст второго пункта', max_length=200, blank=True,
                                         default=u'Каждый 3 магазин даст первую</br>прибыль не ранее чем через '
                                                 u'8</br>месяцев')
    block5_item3_text = models.CharField(u'Блок5 Текст третьего пункта', max_length=200, blank=True,
                                         default=u'Каждый второй магазин столкнется с</br>огромной долговой нагрузкой'
                                                 u'</br>и собственник не сможет закрыть</br>его без убытка')
    block5_item4_text = models.CharField(u'Блок5 Текст четверного пункта', max_length=200, blank=True,
                                         default=u'Каждый магазин столкнется с</br>проблемой человеческого фактора и'
                                                 u'</br>воровства персонала')

    #------------------------ Block6
    block6_visibility = models.BooleanField(u'Показывать', default=True)
    block6_text = models.CharField(u'Блок6 Заголовок', max_length=100, blank=True,
                                   default=u'МЫ ЗАЩИТИМ ВАС ОТ ЭТИХ ПРОБЛЕМ!')
    block6_back = models.ImageField(u'Блок6 Изображение', upload_to='block6_images/',
                                    default='images/decoration_2.png',
                                    blank=True, null=True)
    block6_text2 = models.CharField(u'Блок6 Текст под заголовком', max_length=200, blank=True,
                                    default=u'* Статистика предоставлена независимой экспертной группой '
                                            u'"Предприниматели Юга">')

    #------------------------ Block7
    block7_visibility = models.BooleanField(u'Показывать', default=True)
    block7_text = models.CharField(u'Блок7 Заголовок', max_length=100, blank=True,
                                   default=u'ПОЧЕМУ МЫ ГАРАНТИРУЕМ РЕЗУЛЬТАТ')
    block7_back = models.ImageField(u'Блок7 Изображение фона', upload_to='block7_images/',
                                    default='images/rezult.jpg',
                                    blank=True, null=True)
    block7_item1_icon = models.ImageField(u'Блок7 Пункт1 Изображение', upload_to='block7_images/',
                                          default='images/rez_1.png',
                                          blank=True, null=True)
    block7_item1_text = models.CharField(u'Блок7 Текст первого пункта', max_length=200, blank=True,
                                         default=u'Адекватная и</br>либеральная</br>стоимость на услуги</br></br>')
    block7_item2_icon = models.ImageField(u'Блок7 Пункт2 Изображение', upload_to='block7_images/',
                                          default='images/rez_2.png',
                                          blank=True, null=True)
    block7_item2_text = models.CharField(u'Блок7 Текст второго пункта', max_length=200, blank=True,
                                         default=u'Работаем только</br>в практическом поле</br></br></br>')
    block7_item3_icon = models.ImageField(u'Блок7 Пункт3 Изображение', upload_to='block7_images/',
                                          default='images/rez_3.png',
                                          blank=True, null=True)
    block7_item3_text = models.CharField(u'Блок7 Текст третьего пункта', max_length=200, blank=True,
                                         default=u'Эксперты из</br>профессиональной</br>элиты бизнеса</br></br>')
    block7_item4_icon = models.ImageField(u'Блок7 Пункт4 Изображение', upload_to='block7_images/',
                                          default='images/rez_4.png',
                                          blank=True, null=True)
    block7_item4_text = models.CharField(u'Блок7 Текст четверного пункта', max_length=200, blank=True,
                                         default=u'Иностранные</br>эксперты в области</br>архитектуры и</br>'
                                                 u'производства')
    block7_item5_icon = models.ImageField(u'Блок7 Пункт5 Изображение', upload_to='block7_images/',
                                          default='images/rez_5.png',
                                          blank=True, null=True)
    block7_item5_text = models.CharField(u'Блок7 Текст четверного пункта', max_length=200, blank=True,
                                         default=u'Оперативность</br>принятия решений с</br>нацеленностью на</br>'
                                                 u'результат')

    #------------------------ Block8
    block8_visibility = models.BooleanField(u'Показывать', default=True)
    block8_text = models.CharField(u'Блок8 Заголовок', max_length=100, blank=True,
                                   default=u'СОТРУДНИЧАЯ С НАМИ</br><span>НАШИ КЛИЕНТЫ ПОЛУЧАЮТ</span>')
    block8_back = models.ImageField(u'Блок8 Изображение фона', upload_to='block8_images/',
                                    default='images/bg_1.png',
                                    blank=True, null=True)
    block8_item1_icon = models.ImageField(u'Блок8 Пункт1 Изображение', upload_to='block8_images/',
                                          default='images/client_1.png',
                                          blank=True, null=True)
    block8_item1_text = models.CharField(u'Блок8 Текст первого пункта', max_length=200, blank=True,
                                         default=u'Безопасный</br>бизнес</br></br>')
    block8_item2_icon = models.ImageField(u'Блок8 Пункт2 Изображение', upload_to='block8_images/',
                                          default='images/client_2.png',
                                          blank=True, null=True)
    block8_item2_text = models.CharField(u'Блок8 Текст второго пункта', max_length=200, blank=True,
                                         default=u'Грамотный и</br>обученный</br>персонал')
    block8_item3_icon = models.ImageField(u'Блок8 Пункт3 Изображение', upload_to='block8_images/',
                                          default='images/client_3.png',
                                          blank=True, null=True)
    block8_item3_text = models.CharField(u'Блок8 Текст третьего пункта', max_length=200, blank=True,
                                         default=u'Автоматизирован</br>-ные процессы</br>работы')
    block8_item4_icon = models.ImageField(u'Блок8 Пункт4 Изображение', upload_to='block8_images/',
                                          default='images/client_4.png',
                                          blank=True, null=True)
    block8_item4_text = models.CharField(u'Блок8 Текст четверного пункта', max_length=200, blank=True,
                                         default=u'Сервисное</br>сопровождение</br></br>')
    block8_item5_icon = models.ImageField(u'Блок8 Пункт5 Изображение', upload_to='block8_images/',
                                          default='images/client_5.png',
                                          blank=True, null=True)
    block8_item5_text = models.CharField(u'Блок8 Текст четверного пункта', max_length=200, blank=True,
                                         default=u'Стабильный</br>доход</br></br>')
    block8_button_color = ColorField(u'Блок8 Цвет кнопки', blank=True, default='#fff600')
    block8_button_text = models.CharField(u'Блок8 Текст кнопки', max_length=100, blank=True,
                                          default=u'НАЧАТЬ СОТРУДНИЧЕСТВО')

    #------------------------ Block9
    block9_visibility = models.BooleanField(u'Показывать', default=True)
    block9_header = models.CharField(u'Блок9 Заголовок', max_length=100, blank=True,
                                     default=u'НАШИ УСЛУГИ')
    block9_under_text = models.CharField(u'Блок9 текст под заголовком', max_length=200, blank=True,
                                         default=u'Открытие магазинов самообслуживания:</br>от визуализированного '
                                                 u'проекта до гарантированного получения прибыли')
    block9_item_color = ColorField(u'Блок9 Цвет фона цифр', blank=True, default='#5287a7')
    block9_item1_text = models.CharField(u'Блок9 Текст1', max_length=200, blank=True,
                                         default=u'<span>Замер экономической</span>&nbsp; эффективности</br>'
                                                 u'месторасположения торговой точки')
    block9_item2_text = models.CharField(u'Блок9 Текст2', max_length=200, blank=True,
                                         default=u'<span>Разработка концепции магазина:</span>&nbsp; по</br>цене, по '
                                                 u'товару, по сервису обслуживания')
    block9_item3_text = models.CharField(u'Блок9 Текст3', max_length=200, blank=True,
                                         default=u'<span>Разработка схемы</span>&nbsp; эффективного</br>расположения '
                                                 u'торгового оборудования -</br>правило потока покупателей</br>')
    block9_item4_text = models.CharField(u'Блок9 Текст4', max_length=200, blank=True,
                                         default=u'<span>Проект автоматизации</span>&nbsp; процессов</br>работы '
                                                 u'магазина: ПО, кассовый пост, IP</br>контроль товара, приемка и'
                                                 u' отпуск</br>')
    block9_item5_text = models.CharField(u'Блок9 Текст5', max_length=200, blank=True,
                                         default=u'<span>Внедрение системы</span>&nbsp; выкладки товаров на</br>полке '
                                                 u'магазина - правило золотой полки и</br>ходовой продукции')
    block9_item6_text = models.CharField(u'Блок9 Текст6', max_length=200, blank=True,
                                         default=u'<span>Внедрение системы</span>&nbsp; мотивации и</br>ответственности'
                                                 u' персонала (обучение</br>персонала с ноля)')
    block9_item7_text = models.CharField(u'Блок9 Текст7', max_length=200, blank=True,
                                         default=u'<span>Разработка и внедрение</span>&nbsp; маркетинговых</br>"якорей"'
                                                 u' для магазина (увеличение</br>среднего чека)')
    block9_item8_text = models.CharField(u'Блок9 Текст8', max_length=200, blank=True,
                                         default=u'<span>Внедрение программы</span>&nbsp;анализа</br>оборачиваемости '
                                                 u'полочного пространства</br></br>')
    block9_item9_text = models.CharField(u'Блок9 Текст9', max_length=200, blank=True,
                                         default=u'<span>Обучение собственников бизнеса</span>&nbsp;(выход</br>на '
                                                 u'сетевой формат)</br>')

    block9_button_color = ColorField(u'Блок9 Цвет кнопки', blank=True, default='#fff600')
    block9_button_text = models.CharField(u'Блок8 Текст кнопки', max_length=100, blank=True,
                                          default=u'ПОЛУЧИТЬ БЕСПЛАТНУЮ КОНСУЛЬТАЦИЮ')

    #------------------------ Block10
    block10_visibility = models.BooleanField(u'Показывать', default=True)
    block10_background = models.ImageField(u'Блок10 Фоновое изображение', upload_to='block10_images/',
                                           default='images/big_form.jpg',
                                           blank=True, null=True)
    block10_text = models.CharField(u'Блок10 Заголовок', max_length=200, blank=True,
                                    default=u'ТОЛЬКО СЕГОДНЯ!</br>Вы получаете<span> БЕСПЛАТНО!</span>')
    block10_image = models.ImageField(u'Блок10 Изображение под Заголовком', upload_to='block10_images/',
                                      default='images/decoration_1.jpg',
                                      blank=True, null=True)
    block10_list_icon = models.ImageField(u'Блок10 Изображение для списка', upload_to='block10_images/', default='images/ok.png',
                                          blank=True, null=True)
    block10_item1 = models.BooleanField(u'Блок10 Первый пункт', default=True)
    block10_item1_text = models.CharField(u'Блок10 Текст первого пункта', max_length=200, blank=True,
                                          default=u'Пошаговый план открытия минимаркета')
    block10_item2 = models.BooleanField(u'Блок10 Второй пункт', default=True)
    block10_item2_text = models.CharField(u'Блок3 Текст второго пункта', max_length=200, blank=True,
                                          default=u'Метод увеличения среднего чека в магазине')
    block10_item3 = models.BooleanField(u'Блок10 Третий пункт', default=True)
    block10_item3_text = models.CharField(u'Блок10 Текст третьего пункта', max_length=200, blank=True,
                                          default=u'3D модель вашего будущего магазина')
    block10_time = models.TimeField(u'Время до конца акции', default='08:31:57', blank=True, null=True)
    block10_text1 = models.CharField(u'Блок10 Текст', max_length=200, blank=True,
                                     default=u'УЧАСТВУЙТЕ В АКЦИИ</br><span>и Ваш бизнес выйдет</br>на новый уровень!'
                                             u'</span>')
    block10_button_text = models.CharField(u'Блок10 Текст на кнопке', max_length=100, blank=True,
                                           default=u'ПОЛУЧИТЬ БЕСПЛАТНО')
    block10_under_button_text = models.CharField(u'Блок10 Текст после кнопки', max_length=100, blank=True,
                                                 default=u'Ваши контактные данные в безопасности</br>и не будут переданы'
                                                         u' третьим лицам')
    block10_back_color = ColorField(u'Блок10 Цвет рамки', blank=True, default='#f7582e')
    block10_button_color = ColorField(u'Блок10 Цвет кнопки', blank=True, default='#fff600')
    block10_field_color = ColorField(u'Блок10 Цвет полей', blank=True, default='#294353')

    #------------------------ Block11
    block11_visibility = models.BooleanField(u'Показывать', default=True)
    block11_text = models.CharField(u'Блок11 Заголовок', max_length=200, blank=True,
                                    default=u'О НАС В ЦИФРАХ')
    block11_back_color = ColorField(u'Блок11 Цвет фона', blank=True, default='#97c4e3')
    block11_square_color = ColorField(u'Блок11 Цвет фона блоков', blank=True, default='#97c4e3')
    block11_number_color = ColorField(u'Блок11 Цвет цифр', blank=True, default='#f7582e')
    block11_item1_number = models.CharField(u'Блок11 Цифра первого пункта', max_length=20, blank=True,
                                            default=u'7')
    block11_item1_text = models.CharField(u'Блок11 Текст первого пункта', max_length=200, blank=True,
                                          default=u'Руководителей проектов')
    block11_item2_number = models.CharField(u'Блок11 Цифра второго пункта', max_length=20, blank=True,
                                            default=u'70')
    block11_item2_text = models.CharField(u'Блок11 Текст второго пункта', max_length=200, blank=True,
                                          default=u'Работающих</br>экспертов')
    block11_item3_number = models.CharField(u'Блок11 Цифра третьего пункта', max_length=20, blank=True,
                                            default=u'4.5')
    block11_item3_text = models.CharField(u'Блок11 Текст третьего пункта', max_length=200, blank=True,
                                          default=u'Опыт</br>работы')
    block11_item4_number = models.CharField(u'Блок11 Цифра четвертого пункта', max_length=20, blank=True,
                                            default=u'2')
    block11_item4_text = models.CharField(u'Блок11 Текст четвертого пункта', max_length=200, blank=True,
                                          default=u'Открытие</br>магазина с нуля')
    block11_item5_number = models.CharField(u'Блок11 Цифра пятого пункта', max_length=20, blank=True,
                                            default=u'45')
    block11_item5_text = models.CharField(u'Блок11 Текст пятого пункта', max_length=200, blank=True,
                                          default=u'Выход на</br>рентабельность')

    #------------------------ Block12
    block12_visibility = models.BooleanField(u'Показывать', default=True)
    block12_text = models.CharField(u'Блок12 Заголовок', max_length=100, blank=True,
                                    default=u'КАК МЫ РАБОТАЕМ')
    block12_back = models.ImageField(u'Блок12 Фоновое изображение', upload_to='block12_images/',
                                     default='images/bg_1.png', blank=True, null=True)
    block12_image = models.ImageField(u'Блок12 Изображение с цифрами', upload_to='block12_images/',
                                      default='images/kak_rabotaem.png', blank=True, null=True)
    block12_item1_text = models.CharField(u'Блок12 Текст первого пункта', max_length=200, blank=True,
                                          default=u'Заказ бесплатной</br>консультации')
    block12_item2_text = models.CharField(u'Блок12 Текст второго пункта', max_length=200, blank=True,
                                          default=u'Готовим для Вас пошаговый</br>план решения задачи')
    block12_item3_text = models.CharField(u'Блок12 Текст третьего пункта', max_length=200, blank=True,
                                          default=u'Получаем</br>результат')
    block12_item4_text = models.CharField(u'Блок12 Текст четверного пункта', max_length=200, blank=True,
                                          default=u'Наша команда анализирует</br>информацию')
    block12_item5_text = models.CharField(u'Блок12 Текст четверного пункта', max_length=200, blank=True,
                                          default=u'Согласовываем условие</br>сотрудничества')
    block12_button_text = models.CharField(u'Блок12 Текст на кнопке', max_length=100, blank=True,
                                           default=u'ЗАКАЗАТЬ БЕСПЛАТНУЮ КОНСУЛЬТАЦИЮ')
    block12_button_color = ColorField(u'Блок12 Цвет кнопки', blank=True, default='#fff600')

    #------------------------ Block13
    block13_visibility = models.BooleanField(u'Показывать', default=True)
    block13_header = models.CharField(u'Блок13 Заголовок', max_length=100, blank=True,
                                      default=u'ОТЗЫВЫ НАШИХ КЛИЕНТОВ')
    block13_image1 = models.ImageField(u'Блок13 Изображение 1', upload_to='block13_images/',
                                       default='images/otziv_1.png', blank=True, null=True)
    block13_fio1 = models.CharField(u'Блок13 ФИО 1', max_length=100, blank=True,
                                    default=u'Людмила Орлова')
    block13_event1 = models.CharField(u'Блок13 Событие 1', max_length=100, blank=True,
                                      default=u'Открытие "Минимаркет Первый"')
    block13_text1 = models.TextField(u'Блок13 Текст 1', blank=True, default=u'Мы обратились в компанию BFC за услугами по открытию супермаркета, нам было важно не допустить ошибок в процессе открытия и как можно больше понять специфику данного рынка. Наше основное направление это строительство и открытие магазина стало не профильным направлением. И так мы пригласили экспертов на этапе отделки магазина все , что происходило дальше было выстроено сотрудниками компании ВFC . Была создана схема расположения оборудование , подробно описаны зоны магазина с их товарным наполнением, дизайн и оформление торгового зала с размещением навигации по магазину. Подбор и обучение продавцов с системой заработных плат и договоров ответственности. После оформления и заполнения магазина , ребята продумали план акций на открытие и последующее привлечение клиентов. Откровенно мы не ожидали в день открытия увидеть огромное количество посетителей и каждый из которых совершил закупку. Для нас это сотрудничество стало самым ценным т.к. накопить весь полученный опыт за два месяца не реально. Выражаем огромную благодарность и приглашаем в наш магазин г.Славянск на Кубани ул. Пролетарская 246 "Минимаркет Первый"')
    block13_image2 = models.ImageField(u'Блок13 Изображение 2', upload_to='block13_images/',
                                       default='images/otziv_4.png', blank=True, null=True)
    block13_fio2 = models.CharField(u'Блок13 ФИО 2', max_length=100, blank=True,
                                    default=u'Владимир Попилевич')
    block13_event2 = models.CharField(u'Блок13 Событие 2', max_length=100, blank=True,
                                      default=u'Сеть магазинов “Beer Box”')
    block13_text2 = models.TextField(u'Блок13 Текст 2', blank=True, default=u'Очень признателен сотрудникам компании в том,</br> что помогли разобраться в системе настройки</br> заработных плат и мотиваций. Ушло много</br> головных болей по поводу недоделок и просрочки</br> продукции.')

    #------------------------ Block14
    block14_visibility = models.BooleanField(u'Показывать', default=True)
    block14_header = models.CharField(u'Блок14 Заголовок', max_length=100, blank=True,
                                      default=u'НАШИ ПАРТНЕРЫ', help_text=u'Партнеров можно добавить ниже')

    #------------------------ Block15
    block15_visibility = models.BooleanField(u'Показывать', default=True)
    block15_logo = models.ImageField(u'Блок15 Логотип', upload_to='block15_images/', default='images/logo2.png',
                                     blank=True, null=True)
    block15_back = models.ImageField(u'Блок15 Фоновое изображение', upload_to='block15_images/', default='images/footer.jpg',
                                     blank=True, null=True)
    block15_text = models.CharField(u'Блок15 Текст', max_length=200, blank=True,
                                    default=u'<b>Мы создаем возможности обеспечивающие Ваше будущее!</b></br>работаем '
                                            u'в Краснодарском крае и Крыму')
    block15_button_color = ColorField(u'Блок15 Цвет кнопки', blank=True, default='#fff600')
    block15_button_text = models.CharField(u'Блок15 Текст кнопки', max_length=100, blank=True, default=u'ЗАКАЗАТЬ ЗВОНОК')
    block15_phone = models.CharField(u'Блок15 Телефон', max_length=100, blank=True, default=u'7 (918) 930-03-16')
    block15_under_phone_text = models.CharField(u'Блок15 Текст под телефоном', max_length=200, blank=True,
                                                default=u'email:info@consalt-bf.ru</br>ИНН 233603955530 ОГРН 314231105100090')

    def __unicode__(self):
        return u'Настройки сайта'

    class Meta:
        verbose_name = u'Настройки сайта'


class Partner(models.Model):
    config = models.ForeignKey(SiteConfiguration)
    title = models.CharField(u'Название', max_length=100, blank=True)
    image = models.ImageField(u'Изображение', upload_to='block14_images/')

    def __unicode__(self):
        return u'Партнер %s' % self.id

    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'

