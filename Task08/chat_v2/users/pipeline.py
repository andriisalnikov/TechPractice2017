# -*- coding: utf-8 -*-
import requests
from slugify import slugify
from django.core.files.base import ContentFile

def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]
if backend.name == 'instagram':
            profile=Profiles.objects.get(user=user)
            new_profile.in_id = ''
            profile.save()   
	 if url:
        user.avatar = url
        user.save()

# Процедура для pipiline, сохраняющая изображение.
def set_user_avatar(backend, user, response, is_new=False, *args, **kwargs):

    # Если запись не новая, сразу уходим, не задерживаемся.
    if not is_new:
        return

    # response это словарь, сформированный из ответа провайдера на наш запрос.
    # Т.к. это устоявшиеся api, то не может быть такого, чтобы конечное поле
    # отсутствовало, (кроме тех что нужно указывать в scope). Так что здесь,
    # можно смело обращаться к данным по ключу (без применения метода get()).
    avatar_map = {
        'facebook': lambda: response['picture']['data']['url'],
        'google-oauth2': lambda: response['image']['url'],
        'vk-oauth2': lambda: response['photo_200_orig'],
        'github': lambda: response['avatar_url'],
    }

    try:
        # Важно не забыть добавить в avatar_map,
        # "разметку" для всех бекэндов AUTHENTICATION_BACKENDS
        avatar_url = avatar_map[backend.name]()
    except (TypeError, KeyError):
        # Если у нас случилось нечто фантастическое, то ссылке присваиваем None
        # Во время отладки приложения, проще обойтись без блоков try/except.
        # Так виновник найдется быстрее.
        avatar_url = None

    if avatar_url:
        # Для скачивания картинки используем любой, удобный вам клиент.
        r = requests.get(avatar_url)
        # У некоторых провайдеров, не получится узнать формат файла,
        # получив последнюю часть ссылки (после точки). Поэтому мы узнаем
        # формат файла из Content-Type (последней его части).
        ext = r.headers['Content-Type'].split('/')[-1]
        # иногда (с facebook) могут возникнуть проблемы с опознанием кодировки,
        # а также сохранением файлов с кириллическими названиями.
        # Эти проблемы конечно решаемы, но самый быстрый способ,
        # как мне кажется, преобразовать кириллицу в латиницу.
        # Для этого я использую пакет python-slugify.
        filename = '{}.{}'.format(slugify(user.username), ext)
        # Сохраняем поле с картинкой.
        user.avatar.save(filename, ContentFile(r.content))
