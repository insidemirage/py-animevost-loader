import requests
from multiprocessing import Pool, Manager

ANIMEVOST_TEMPLATE = "https://a{}.agorov.org"


def check_mirror(args):
    link = args[0]
    q = args[1]
    try:
        res = requests.get(link, timeout=3)
    except requests.exceptions.RequestException:
        print(f"Mirror {link} doesn't work fine...")
        return None
    if res.status_code != 200:
        print(f"Mirror {link} doesn't work fine")
        return None
    q.put(link)
    print(f"Mirror {link} works!")


def look_for_mirror(start, end):
    mirror_link = None
    manager = Manager()
    queue = manager.Queue()
    pool = Pool(25)
    links = [(ANIMEVOST_TEMPLATE.format(i), queue) for i in range(start,end)]
    pool.map(check_mirror, links)
    pool.close()
    while True:
        mirror_link = queue.get()
        if mirror_link:
            pool.terminate()
            print(mirror_link)
            break
    return mirror_link

