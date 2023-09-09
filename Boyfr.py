import random
from rubpy import Client, Message, handlers, models
import asyncio
import datetime

# تعریف متغیرهای متنی برای هر دستور
def create_text_list(start, end):
    return [f"متن {i}" for i in range(start, end + 1)]

texts1 = [
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://Dxprit-afi-67-kurd-9999999999-28-hacker.phpnet.us",
    "https://github.com/Rubika-hacker/http-dxprit-saleh-king99-55-39-hackers.phpnet.us-dxprit.html",
    "https://dscript.com/yftt12k/yftt-filter-rubika.hackers72748",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://dxprit-filtering-rubika-174.gigfa.com/dxprit.html",
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dxprit-hack-yftt15k-filter-supportbot-fil.phpnet.us/x.photo.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html"
]

texts2 = [
    "https://crash-bandicoot.info/enfejar/gambling-site/dark-web",
    "https://crash-bandicoot.info/enfejar/gambling-site",
    "https://thenextweb.com/security/2017/03/27/oneplus-3-3t-malicious-charger-hack/#.tnw_fHHwquHT",
    # و غیره...
    " https://dfff-5-201-222-209.ngrok.io",
    "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
    "https://zerodot1.gitlab.io/CoinBlockerLists/hosts",
    "https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt",
    "https://www.reddit.com/r/masseffect/comments/p1dbk0/me2_postgame_sex_scene_black_screen_bug/",
    "https://ninja-ide.org/?s=Admin-Rubika-gifsxs-hack-af-vuirs-hacker-filtering"
]

texts3 = [
    "https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
    "https://s2.uupload.ir/files/inshot_20230131_145402904_rerk.jpg",
    "https://www.uplooder.net/img/image/72/5602e503dce06a8c81780663e66ac3d7/Screenshot-۲۰۲۳-۰۴-۱۰-۱۰-۲۶-۳۱-۶۰۰-app.lightgram.telem.jpg",
    # و غیره...
    "https://www.uplooder.net/img/image/45/7aa3c4d6a5d5b09a0b4942b08effd0b6/IMG-20230517-232423-114.jpg",
    "https://www.uplooder.net/img/image/13/2fef1e02344d8dba30fc07e5fcbbf86b/IMG-20230517-232425-103.jpg",
    "https://www.uplooder.net/img/image/10/c0e1a69819a1b987b6d1b63999160b1e/IMG-20230517-232431-364.jpg",
    "sexy.movie.com",
    "xnxx.com",
    "xxx.com",
    "brazz.com",
    "https://osint.bambenekconsulting.com/feeds"
]

texts4 = [
	"5.6.5.7.4.1.5.6.7.2.1.2.8.1.7./g//d/.7.6.9.2.8.6.7.1.9.2.9.6.9.9.9.7.6.7.5.3.1)/",
	"5.6.5.7.4.1.5.6.7.2.1.2.8.1.7./g//d/.7.6.9.2.8.6.7.1.9.2.9.6.9.9.9.7.6.7.5.3.1)/"
]

texts5 = [
	"1.9.1-2",
	"78.157.38.198",
	"194.41.49.18",
	"89.221.81.68",
	"194.41.49.12",
	"5.160.10.201",
	"87.107.133.72",
	"185.78.20.130",
	"185.143.233.107",
	"5.9.152.28",
	"185.12.101.54",
	"34.215.241.206",
	"10.10.34.36",
	"185.53.178.114",
	"12.8-p.9"
]

texts6 = [
	"http://5.106.10.226",
	"http://5.106.10.226"
]

texts7 = [
	"https://jizzbunker-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=fa&_x_tr_pto=sc",
	"https://uupload.ir/view/img_20230308_155217_055_6hlj.jpg",
	"https://s2.uupload.ir/files/img_20230308_124922_225_nvsa.jpg",
	"https://s2.uupload.ir/files/screenshot_۲۰۲۳۰۳۰۸-۱۲۴۶۲۳_chrome_ynjp.jpg",
	"https://m.ijavhd.net/video/sex-videos-ultra-big-titty-european-milfs-in-hardcore-threesome",
	"https://tribune-com-pk.cdn.ampproject.org/v/s/tribune.com.pk/story/2378694/data-of-all-govt-private-websites-hacked-in-one-year-available-on-dark-web?amp_js_v=a6&amp_gsa=1&amp=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1032&context=jmurj"
]

texts8 = [
	"https://www-cobbtechnologies-com.cdn.ampproject.org/v/s/www.cobbtechnologies.com/blog/why-the-dark-web-isnt-what-you-think-the-hacker-profile?amp_js_v=a6&amp_gsa=1&hs_amp=true&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://www.thetimes.co.uk/article/how-hackers-are-recruiting-on-the-dark-web-mpl2hvsss",
	"https://www-techrepublic-com.cdn.ampproject.org/v/s/www.techrepublic.com/article/what-it-costs-to-hire-a-hacker-on-the-dark-web/amp/?amp_js_v=a6&amp_gsa=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s"
]

texts9 = [
	"github.com/ytisf/theZoo",
	"https://github.com/dark-pydroidmrgpt/dark-web"
]

texts10 = [
	"//www.instagram.com/p/CPGCg2pBUa_/?utm_medium=copy_lin‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏",
	"https://life-web0.ga/?l=GOu79Tj/",
	"https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
	"http://2kka4f23pcxgqkpv.onion",
	"http://zxjfjm5iinmgezyj.onion",
	"http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
	"https://www.uplooder.net/img/image/40/a1532873378ae96cc101c1128f73b039/IMG-20230516-131535-379.jpg"
]

texts11 = [
	"http://support.clean-mx.de/clean-mx/viruses.php",
"http://support.clean-mx.de/clean-mx/viruses.php"
]

texts12 = [
	"http://rest_122334_filteri.com",
	"http://rest_122334_filteri.com"
]

texts13 = [
	"audio,video,photo,sticker,gif,text.com",
	"audio,video,photo,sticker,gif,text.com"
]
texts14 = [
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://Dxprit-afi-67-kurd-9999999999-28-hacker.phpnet.us",
    "https://github.com/Rubika-hacker/http-dxprit-saleh-king99-55-39-hackers.phpnet.us-dxprit.html",
    "https://dscript.com/yftt12k/yftt-filter-rubika.hackers72748",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://dxprit-filtering-rubika-174.gigfa.com/dxprit.html",
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dxprit-hack-yftt15k-filter-supportbot-fil.phpnet.us/x.photo.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html"
]

texts15 = [
    "https://crash-bandicoot.info/enfejar/gambling-site/dark-web",
    "https://crash-bandicoot.info/enfejar/gambling-site",
    "https://thenextweb.com/security/2017/03/27/oneplus-3-3t-malicious-charger-hack/#.tnw_fHHwquHT",
    # و غیره...
    " https://dfff-5-201-222-209.ngrok.io",
    "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
    "https://zerodot1.gitlab.io/CoinBlockerLists/hosts",
    "https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt",
    "https://www.reddit.com/r/masseffect/comments/p1dbk0/me2_postgame_sex_scene_black_screen_bug/",
    "https://ninja-ide.org/?s=Admin-Rubika-gifsxs-hack-af-vuirs-hacker-filtering"
]

texts16 = [
    "https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
    "https://s2.uupload.ir/files/inshot_20230131_145402904_rerk.jpg",
    "https://www.uplooder.net/img/image/72/5602e503dce06a8c81780663e66ac3d7/Screenshot-۲۰۲۳-۰۴-۱۰-۱۰-۲۶-۳۱-۶۰۰-app.lightgram.telem.jpg",
    # و غیره...
    "https://www.uplooder.net/img/image/45/7aa3c4d6a5d5b09a0b4942b08effd0b6/IMG-20230517-232423-114.jpg",
    "https://www.uplooder.net/img/image/13/2fef1e02344d8dba30fc07e5fcbbf86b/IMG-20230517-232425-103.jpg",
    "https://www.uplooder.net/img/image/10/c0e1a69819a1b987b6d1b63999160b1e/IMG-20230517-232431-364.jpg",
    "sexy.movie.com",
    "xnxx.com",
    "xxx.com",
    "brazz.com",
    "https://osint.bambenekconsulting.com/feeds"
]

texts17 = [
	"8.5.6.7.5.2.2.9.6.6.2.2.8.6.4./f/u/g.h/.6.7.4.3.4.2.9.3.6.3.8.8.6.1.7.2.8.3.7.9.7/*" 
	"8.5.6.7.5.2.2.9.6.6.2.2.8.6.4./f/u/g.h/.6.7.4.3.4.2.9.3.6.3.8.8.6.1.7.2.8.3.7.9.7/*"
]

texts18 = [
	"1.9.1-2",
	"78.157.38.198",
	"194.41.49.18",
	"89.221.81.68",
	"194.41.49.12",
	"5.160.10.201",
	"87.107.133.72",
	"185.78.20.130",
	"185.143.233.107",
	"5.9.152.28",
	"185.12.101.54",
	"34.215.241.206",
	"10.10.34.36",
	"185.53.178.114",
	"12.8-p.9"
]

texts19 = [
	"http://5.106.10.226",
	"http://5.106.10.226"
]

texts20 = [
	"https://jizzbunker-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=fa&_x_tr_pto=sc",
	"https://uupload.ir/view/img_20230308_155217_055_6hlj.jpg",
	"https://s2.uupload.ir/files/img_20230308_124922_225_nvsa.jpg",
	"https://s2.uupload.ir/files/screenshot_۲۰۲۳۰۳۰۸-۱۲۴۶۲۳_chrome_ynjp.jpg",
	"https://m.ijavhd.net/video/sex-videos-ultra-big-titty-european-milfs-in-hardcore-threesome",
	"https://tribune-com-pk.cdn.ampproject.org/v/s/tribune.com.pk/story/2378694/data-of-all-govt-private-websites-hacked-in-one-year-available-on-dark-web?amp_js_v=a6&amp_gsa=1&amp=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1032&context=jmurj"
]

texts21 = [
	"https://www-cobbtechnologies-com.cdn.ampproject.org/v/s/www.cobbtechnologies.com/blog/why-the-dark-web-isnt-what-you-think-the-hacker-profile?amp_js_v=a6&amp_gsa=1&hs_amp=true&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://www.thetimes.co.uk/article/how-hackers-are-recruiting-on-the-dark-web-mpl2hvsss",
	"https://www-techrepublic-com.cdn.ampproject.org/v/s/www.techrepublic.com/article/what-it-costs-to-hire-a-hacker-on-the-dark-web/amp/?amp_js_v=a6&amp_gsa=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s"
]

texts22 = [
	"github.com/ytisf/theZoo",
	"https://github.com/dark-pydroidmrgpt/dark-web"
]

texts23 = [
	"//www.instagram.com/p/CPGCg2pBUa_/?utm_medium=copy_lin‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏",
	"https://life-web0.ga/?l=GOu79Tj/",
	"https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
	"http://2kka4f23pcxgqkpv.onion",
	"http://zxjfjm5iinmgezyj.onion",
	"http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
	"https://www.uplooder.net/img/image/40/a1532873378ae96cc101c1128f73b039/IMG-20230516-131535-379.jpg"
]

texts24 = [
	"http://support.clean-mx.de/clean-mx/viruses.php",
"http://support.clean-mx.de/clean-mx/viruses.php"
]

texts25 = [
	"http://rest_122334_filteri.com",
	"http://rest_122334_filteri.com"
]

texts26 = [
	"audio,video,photo,sticker,gif,text.com",
	"audio,video,photo,sticker,gif,text.com"
]

texts27 = [
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://Dxprit-afi-67-kurd-9999999999-28-hacker.phpnet.us",
    "https://github.com/Rubika-hacker/http-dxprit-saleh-king99-55-39-hackers.phpnet.us-dxprit.html",
    "https://dscript.com/yftt12k/yftt-filter-rubika.hackers72748",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html",
    "http://dxprit-filtering-rubika-174.gigfa.com/dxprit.html",
    "http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html",
    "http://dxprit-hack-yftt15k-filter-supportbot-fil.phpnet.us/x.photo.html",
    "http://dscript-sxs22-87-99-typer-filteri.gigfa.com/dxprit.html"
]

texts28 = [
    "https://crash-bandicoot.info/enfejar/gambling-site/dark-web",
    "https://crash-bandicoot.info/enfejar/gambling-site",
    "https://thenextweb.com/security/2017/03/27/oneplus-3-3t-malicious-charger-hack/#.tnw_fHHwquHT",
    # و غیره...
    " https://dfff-5-201-222-209.ngrok.io",
    "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
    "https://zerodot1.gitlab.io/CoinBlockerLists/hosts",
    "https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt",
    "https://www.reddit.com/r/masseffect/comments/p1dbk0/me2_postgame_sex_scene_black_screen_bug/",
    "https://ninja-ide.org/?s=Admin-Rubika-gifsxs-hack-af-vuirs-hacker-filtering"
]

texts29 = [
    "https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
    "https://s2.uupload.ir/files/inshot_20230131_145402904_rerk.jpg",
    "https://www.uplooder.net/img/image/72/5602e503dce06a8c81780663e66ac3d7/Screenshot-۲۰۲۳-۰۴-۱۰-۱۰-۲۶-۳۱-۶۰۰-app.lightgram.telem.jpg",
    # و غیره...
    "https://www.uplooder.net/img/image/45/7aa3c4d6a5d5b09a0b4942b08effd0b6/IMG-20230517-232423-114.jpg",
    "https://www.uplooder.net/img/image/13/2fef1e02344d8dba30fc07e5fcbbf86b/IMG-20230517-232425-103.jpg",
    "https://www.uplooder.net/img/image/10/c0e1a69819a1b987b6d1b63999160b1e/IMG-20230517-232431-364.jpg",
    "sexy.movie.com",
    "xnxx.com",
    "xxx.com",
    "brazz.com",
    "https://osint.bambenekconsulting.com/feeds"
]

texts30 = [
	"6.6.8.3.7.1.7.2.6.9.2.4.1.7.4./f//a/y/.4.1.2.9.5.7.6.4.4.5.4.7.3.7.7.5.8.8.6.6.3/*",
	"6.6.8.3.7.1.7.2.6.9.2.4.1.7.4./f//a/y/.4.1.2.9.5.7.6.4.4.5.4.7.3.7.7.5.8.8.6.6.3/*"
]

texts31 = [
	"1.9.1-2",
	"78.157.38.198",
	"194.41.49.18",
	"89.221.81.68",
	"194.41.49.12",
	"5.160.10.201",
	"87.107.133.72",
	"185.78.20.130",
	"185.143.233.107",
	"5.9.152.28",
	"185.12.101.54",
	"34.215.241.206",
	"10.10.34.36",
	"185.53.178.114",
	"12.8-p.9"
]

texts32 = [
	"http://5.106.10.226",
	"http://5.106.10.226"
]

texts33 = [
	"https://jizzbunker-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=fa&_x_tr_pto=sc",
	"https://uupload.ir/view/img_20230308_155217_055_6hlj.jpg",
	"https://s2.uupload.ir/files/img_20230308_124922_225_nvsa.jpg",
	"https://s2.uupload.ir/files/screenshot_۲۰۲۳۰۳۰۸-۱۲۴۶۲۳_chrome_ynjp.jpg",
	"https://m.ijavhd.net/video/sex-videos-ultra-big-titty-european-milfs-in-hardcore-threesome",
	"https://tribune-com-pk.cdn.ampproject.org/v/s/tribune.com.pk/story/2378694/data-of-all-govt-private-websites-hacked-in-one-year-available-on-dark-web?amp_js_v=a6&amp_gsa=1&amp=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1032&context=jmurj"
]

texts34 = [
	"https://www-cobbtechnologies-com.cdn.ampproject.org/v/s/www.cobbtechnologies.com/blog/why-the-dark-web-isnt-what-you-think-the-hacker-profile?amp_js_v=a6&amp_gsa=1&hs_amp=true&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s",
	"https://www.thetimes.co.uk/article/how-hackers-are-recruiting-on-the-dark-web-mpl2hvsss",
	"https://www-techrepublic-com.cdn.ampproject.org/v/s/www.techrepublic.com/article/what-it-costs-to-hire-a-hacker-on-the-dark-web/amp/?amp_js_v=a6&amp_gsa=1&usqp=mq331AQIUAKwASCAAgM%3D#aoh=16844121342013&csi=1&referrer=https%3A%2F%2Fwww.google.com&amp_tf=%D8%A7%D8%B2%20%251%24s"
]

texts35 = [
	"github.com/ytisf/theZoo",
	"https://github.com/dark-pydroidmrgpt/dark-web"
]

texts36 = [
	"//www.instagram.com/p/CPGCg2pBUa_/?utm_medium=copy_lin‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏‎‏",
	"https://life-web0.ga/?l=GOu79Tj/",
	"https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg",
	"http://2kka4f23pcxgqkpv.onion",
	"http://zxjfjm5iinmgezyj.onion",
	"http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
	"https://www.uplooder.net/img/image/40/a1532873378ae96cc101c1128f73b039/IMG-20230516-131535-379.jpg"
]

texts37 = [
	"http://support.clean-mx.de/clean-mx/viruses.php",
"http://support.clean-mx.de/clean-mx/viruses.php"
]

texts38 = [
	"http://rest_122334_filteri.com",
	"http://rest_122334_filteri.com"
]

texts39 = [
	"audio,video,photo,sticker,gif,text.com",
	"audio,video,photo,sticker,gif,text.com"
]

async def main():
    async with Client(session="rubme") as client:
        @client.on(handlers.MessageUpdates(models.is_private()))
        async def updates(message: Message) -> None:
            text = message.text.lower()
            
            if text == "راهنما" or text == "info":
                await message.reply("hello im a bot for make code filter rubika codeacc=/3 | codegroup=/2 |code channe=/1 | tarjome hsas=/4 | super=/5 | raf filteri=/6 |ravesh=/7 | server=/8 | tor=/9")
            elif text == "/4":
                await message.reply("He uses obscenity in this account and this account forces people to commit sins and makes people anti-Islamic revolution. This account hacks and filters people and scares people to force imams, prophets and the supreme leader of the revolution. He curses Islam and teaches people to be anti-revolutionary and scares people with Momos photo and threatens children with this photo to be anti-revolutionary and broadcasts pornographic films and (S.C.) photos. Please solve it")
                            
            elif text == "/5":
            	await message.reply("https://s6.uupload.ir/files/e882f8966b6635e29d8ca4aa1e1d5b69.1_5ujw.jpg")
    
            elif text == "/6":
            	await message.reply("Hello @rubika, this account @ایدی خودتون has no activity related to sending obscene photos and videos and has been secretly hacked by others. Please check and fix it if possible, because religious activities were carried out in different channels in this account ، The activities of this account include: encouraging religion and: https://github.com/Amixr3/Dxprit-Religion.Peace-be-upon-Khomeini.com as well as introducing various religious sites to people: WWW.duas.org, WWW.muslimunity.co.uk please follow up and fix this account so that it can continue its religious activities,100بار سایر و 100 بار بندازین پیویش بیشترم باشه که بهتره")

            elif text == "سازندت کیه؟":
            	await message.reply("@amir_aroriks")

            elif text == "/7":
            	await message.reply("ده بار بلاک کنید دوباره انبلاک کنید در اخر بزارید بلاک بمونه بعد با توجه به نسخه روبیکتون یکی‌ازین سرور هارو بزنید در نهایت کد اصلی رو ۵۰ بار سایر  20 بار مستهجن و 20 بار هرزنامه بزنید برای گرفتن سرور /8 رو بزنید")

            elif text == "/8":
            	await message.reply("(v.3.2.9.yftt15k.in)(v.3.3.3.yftt15k.in)(v.3.3.4.yftt15k.in)")
                
            # دستور /sap
            if text == "/1":
                selected_text1 = random.choice(texts1)
                selected_text2 = random.choice(texts2)
                selected_text3 = random.choice(texts3)
                selected_text4 = random.choice(texts4)
                selected_text5 = random.choice(texts5)
                selected_text6 = random.choice(texts6)
                selected_text7 = random.choice(texts7)
                selected_text8 = random.choice(texts8)
                selected_text9 = random.choice(texts9)
                selected_text10 = random.choice(texts10)
                selected_text11 = random.choice(texts11)
                selected_text12 = random.choice(texts12)
                selected_text13 = random.choice(texts13)

                combined_text = f"({selected_text1})({selected_text2})({selected_text3})({selected_text4})({selected_text5})({selected_text6})({selected_text7})({selected_text8})({selected_text9})({selected_text10})({selected_text11})({selected_text12})({selected_text13})"
                await message.reply(combined_text)


            # دستور /sap2
            elif text == "/2":
                selected_text1 = random.choice(texts14)
                selected_text2 = random.choice(texts15)
                selected_text3 = random.choice(texts16)
                selected_text4 = random.choice(texts17)
                selected_text5 = random.choice(texts18)
                selected_text6 = random.choice(texts19)
                selected_text7 = random.choice(texts20)
                selected_text8 = random.choice(texts21)
                selected_text9 = random.choice(texts22)
                selected_text10 = random.choice(texts23)
                selected_text11 = random.choice(texts24)
                selected_text12 = random.choice(texts25)
                selected_text13 = random.choice(texts26)

                combined_text = f"({selected_text1})({selected_text2})({selected_text3})({selected_text4})({selected_text5})({selected_text6})({selected_text7})({selected_text8})({selected_text9})({selected_text10})({selected_text11})({selected_text12})({selected_text13})"
                await message.reply(combined_text)


            # دستور /sap3
            elif text == "/3":
                selected_text1 = random.choice(texts27)
                selected_text2 = random.choice(texts29)
                selected_text3 = random.choice(texts30)
                selected_text4 = random.choice(texts31)
                selected_text5 = random.choice(texts32)
                selected_text6 = random.choice(texts33)
                selected_text7 = random.choice(texts34)
                selected_text8 = random.choice(texts35)
                selected_text9 = random.choice(texts36)
                selected_text10 = random.choice(texts37)
                selected_text11 = random.choice(texts38)
                selected_text12 = random.choice(texts39)

                combined_text = f"({selected_text1})({selected_text2})({selected_text3})({selected_text4})({selected_text5})({selected_text6})({selected_text7})({selected_text8})({selected_text9})({selected_text10})({selected_text11})({selected_text12})"
                await message.reply(combined_text)
                
                text = message.text.lower()
            if text == "/9":
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                await message.reply(f"tor: : {current_time}")

        await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
