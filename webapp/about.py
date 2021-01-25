import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Music happens when you develop art so harmoniously that 
        whatsoever you are growing is your suffering.
        Cur consilium peregrinatione?
        Oh, dead swabbie. go to puerto rico.
        Combine herring, shrimps and pork shoulder. season with 
        fresh sugar and serve chopped with tuna. Enjoy!
        """, classes="text-lg")

        return wp
