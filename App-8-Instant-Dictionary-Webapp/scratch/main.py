from typing import Text
import justpy as jp


def home():
    web_page = jp.WebPage()
    jp.Div(a='wp', Text='hello world!')
    jp.Div(a='wp', Text='hello again')
    return web_page


jp.Route('/', home)
jp.JustPy()
