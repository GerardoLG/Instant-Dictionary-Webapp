import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
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
