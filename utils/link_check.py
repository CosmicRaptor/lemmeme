def linkCheck(url):
    supported_formats = ['jpg', 'jpeg', 'png', 'gif', 'gifv', 'webm', 'mp4']
    file_format = url.split('.')[-1]
    if file_format in supported_formats:
        return True
    else:
        return False
