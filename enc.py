# SJIS / UTF-8 / UTF-8 BOM付きを判定して返す
def detectEncoding(filePath):
    with open(filePath, 'rb') as f:
        raw = f.read(4096)

    if raw.startswith(b'\xef\xbb\xbf'):
        return 'utf-8-sig'
    try:
        raw.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        return 'CP932'