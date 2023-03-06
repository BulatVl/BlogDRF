def get_path_upload_avatar(instance, filename):
    ''' Построение пути к файлу аватвра '''
    return f'avatar/{instance.id}/{filename}'