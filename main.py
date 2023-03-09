# # Создать двух пользователей (с помощью метода User.objects.create_user('username')).
User.objects.create_user('Иванов Иван Иванович')
User.objects.create_user('Петров Петр Петрович')
User.objects.all() - Проверка всех пользователей
#
# # Создать два объекта модели Author, связанные с пользователями.
author1 = Author(user_id=1)
author1.save()
author2 = Author(user_id=2)
author2.save()
#
# # Добавить 4 категории в модель Category.
category1 = Category(name_category = 'Спорт')
category1.save()
category2 = Category(name_category = 'Знаменитости')
category2.save()
category3 = Category(name_category = 'Рекорды')
category3.save()
category4 = Category(name_category = 'Политика')
category4.save()

# Добавить 2 статьи и 1 новость.
article1 = Post.objects.create(author = author1,
                               header = 'Роналду несётся к галактической отметке. Но правда ли он так хорош в Саудовской Аравии?',
                               text = 'По состоянию на сегодняшний день у Роналду 709 голов на клубном уровне и 118 голов за сборную Португалии. Итого — 827 результативных попаданий. И это без учета забитых мячей на юношеских и молодёжных турнирах! Зная любовь португальца к личным показателям, очень вероятно, что он захочет преодолеть отметку в 1000 голов.')
article1.save()
article2 = Post.objects.create(author = author1,
                               header = 'Месси всё-таки уйдёт? Похоже, в переговорах с «ПСЖ» есть проблемы.',
                               text = 'Это был идеальный план. Лео Месси, выиграв ЧМ, в начале января вернулся в Париж. И на пойманной волне счастья ему должны были подсунуть новый контракт с «ПСЖ». Инсайдеры уже больше месяца соревнуются в ложной информации. И назначают разные сроки. Первоначально ожидалось, что двухлетнее соглашение заключат в середине января. Потом в конце. Дальше – в начале февраля. Но уже середина месяца. И всё по-прежнему тихо. Может, с новым договором какие-то проблемы?')
article2.save()
news1 = Post.objects.create(author = author2,
                            header = 'В Швейцарии создали поезд длиной 1905 м.',
                            text = 'В материале от 31 октября уточняется, что железнодорожная компания RhB побила рекорд, когда поезд длиной 6253 фута (1905,9 м) со 100 вагонами проехал по рельсам. Ретийская железная дорога является крупнейшей в Швейцарии.')
news1.save()

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
article1=Post.objects.create(author=author1, header='1-st art', text='Text of 1-st')
article1.category.add(category1,category2)
article1.save()

article2=Post.objects.create(author=author1, header='2-nd art', text='Text of 2-nd')
article2.category.add(category1,category2)
article2.save()

news1=Post.objects.create(author=author2, header='1-st art', text='Text of 1-st')
news1.category.add(category3,category4)
news1.save()

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1=Comment.objects.create(post=Post.objects.get(id=1),user=User.objects.get(pk=1),text_comment='Siuuu')
comment1.save()

comment2=Comment.objects.create(post=Post.objects.get(id=1),user=User.objects.get(pk=2),text_comment='Wow')
comment2.save()

comment3=Comment.objects.create(post=Post.objects.get(id=2),user=User.objects.get(pk=1),text_comment='Bad news')
comment3.save()

comment4=Comment.objects.create(post=Post.objects.get(id=3),user=User.objects.get(pk=2),text_comment='Wow,sensational')
comment4.save()

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.


