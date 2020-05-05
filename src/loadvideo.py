import requests
from bs4 import BeautifulSoup
import re
import json
import sys
import multiprocessing #for a while
API_LINK = "https://api.animevost.org/animevost/api/v0.2/GetInfo/{}"
VIDEOS_PREFIX = "{}/frame2.php?play={}"

def download_video(params):
    link = params[0]
    queue = params[2]
    i = params[1]
    with open(f"{i}.mp4", "wb") as f:
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            prev_done = 0
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(100 * dl / total_length)
                if done == prev_done:
                    continue
                prev_done = done
                print("Process changed state")
                queue.put({"done":done, "item":i})


def load(link,base_link, quality=0):
    '''

    :param link:
    :param quality: 0 for 480 1 for 720
    :return:
    '''
    # Get anime id
    reg_animeid = link.split("/")[-1].split("-")[0]
    # Get series ids
    response = requests.get(API_LINK.format(reg_animeid))
    response = response.json()
    series = {}
    # we need to parse json cause someone thinks that it's nice idea to give it as a string ffs
    # and yap we change '  to " cause someone don't know about json format xD
    series_values = json.loads(response["data"][0].get("series").replace("'", '"')).values()


    # now we can get the pages of videos with baselink
    video_links = []
    for i, item in enumerate(series_values):
        res = requests.get(VIDEOS_PREFIX.format(base_link, item))
        soup = BeautifulSoup(res.text, 'html.parser')
        iframe = soup.find("iframe")
        res = requests.get(iframe["src"])
        soup = BeautifulSoup(res.text, 'html.parser')
        tab = soup.find("div", {"id":"dow"})
        video_links.append(tab.find_all("a")[quality]["href"])
    return video_links

if __name__ == "__main__":
    # load("https://a49.agorov.org/tip/tv/2425-fruits-basket-2nd-season.html")
    # get_video_id("ajax2(2147415176,0);")
    queue = multiprocessing.Queue()
    ar = ['http://filestd.roomfish.ru/2147415241.mp4?md5=x4ZwQR0i3jHKi3S9PriqHQ&time=1588714457',1, queue]
    proc = multiprocessing.Process(target=download_video, args=(ar,))
    proc.start()
    proc.join()
