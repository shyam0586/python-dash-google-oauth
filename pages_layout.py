import dash_core_components as dcc
import dash_html_components as html

class WebPages(object):
    @staticmethod
    def generate_page_logout():
        return html.Div(className = "logout-screen", 
            children = [
                html.Div('Succesfully Logged Out'), 
                html.Div(
                    children = [html.A('Login Back' , href = '/')])
            ])

    @staticmethod
    def generate_page_1_layout():                
        return html.Div("Logged In Message")

