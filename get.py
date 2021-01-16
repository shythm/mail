import requests
from bs4 import BeautifulSoup
import lxml
import re
from urllib import parse

school_urls = """http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=top
http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=157620025&siteId=gisool2&menuUIType=top
http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=157615558&siteId=gunsu&menuUIType=top
http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156894686&siteId=tong-new&menuUIType=top
http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=159014200&siteId=haengjeong&menuUIType=top
http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=158327574&siteId=bangpogyo&menuUIType=top""".split('\n')

def memberSeq(name, birth, school):
    name = parse.quote(name)
    sid = re.search(r'siteId=[a-zA-Z0-9\-]+', school_urls[int(school)])
    sid = sid.group()
    url = 'http://www.airforce.mil.kr:8081/user/emailPicViewSameMembers.action?{0}&searchName={1}&searchBirth={2}'.format(sid, name, birth)

    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'lxml')
    seq = soup.find('input')
    if(seq == None):
        return None
    seq = seq.get('onclick')
    seq = str.replace(seq, "resultSelect('", '')
    seq = str.replace(seq, "')", '')
    return seq

def mailUrl(name, birth, seq, school):
    name = parse.quote(name)
    sid = re.search(r'codyMenuSeq=\d+&siteId=[0-9A-Za-z\-]+', school_urls[int(school)])
    sid = sid.group()
    url = "http://www.airforce.mil.kr:8081/user/indexSub.action?{0}&menuUIType=top&dum=dum&command2=getEmailList&searchName={1}&searchBirth={2}&memberSeq={3}".format(sid, name, birth, seq)
    return url