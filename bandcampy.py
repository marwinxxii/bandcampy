from urllib.request import urlopen

import rson

def get_embed_data(url):
    '''Get data needed for embedding player.'''

    data = get_data(url, 'EmbedData')
    result = {
        'artist': data['artist'],
        'artist_id': data['art_id'],
        'album_title': data['album_title'],
        'base_url': data['swf_base_url']
    }

    album_param = data['tralbum_param']
    track = result['track'] = album_param['name'] == 'track'
    if track:
        track_data = data['album_embed_data']
        result['album_id'] = track_data['tralbum_param']['value']
        result['track_num'] = track_data['t']
    else:
        result['album_id'] = album_param['value']
    return result

SEARCH_EXPR = 'var {} ='

def get_data(url, field):
    '''Read Bandcamp response and fetch data from it.'''

    data = get_page(url)
    search = SEARCH_EXPR.format(field)
    i = data.find(search)
    if i == -1:
        return None
    i = i + len(search)
    k = data.find('};', i)
    if k == -1:
        return None
    value = data[i:k + 1]
    return parse_json(value)

def parse_json(s):
    # s contains urls as "http://..." + "/album/album"
    s = s.replace('" + "', '')
    return rson.loads(s)

def get_page(url):
    with urlopen(url) as f:
        data = f.read().decode('utf-8')
    return data
