import justpy as jp
import definition


class Dictionary:
    path="/dictionary"
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes=" bg-gray-200 h-screen ")
        jp.Div(a=div, text="The English Dictionary Page", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word as soon as you type", classes="text-lg ")
        Input_div=jp.Div(a=div,classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text lg border-2 h-40")
        Input_box = jp.Input(a=Input_div, placeholder="Type your word here...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 "
                                     "focus:bg-white focus:outline-none focus:border-purple-500",outputdiv = output_div)
        Input_box.on('input',cls.get_definition)
        #jp.Button(a=Input_div,text="Get Definition", classes= "border-2 border-blue-200 text-blue-500",
                  #click=cls.get_definition,outputdiv=output_div,inputbox=Input_box)

        print(cls,req)
        return wp
    @staticmethod
    def get_definition(widget,msg):
        defined=definition.Definition(widget.value).get()
        widget.outputdiv.text=" ".join(defined)
