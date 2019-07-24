from pages_layout import WebPages as wp
import dash
from dash import Dash

from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, session, redirect, url_for
from dash_google_auth import GoogleOAuth
from flask import request
from flask_dance.contrib.google import google


server = Flask(__name__)

server = Flask(__name__)
APP = Dash(__name__,
           server=server, external_stylesheets=external_stylesheets,
           url_base_pathname='/', auth='auth')


@server.route('/')
def home_page():
    return APP.index()


APP.config['suppress_callback_exceptions'] = True
server.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
server.config["GOOGLE_OAUTH_CLIENT_ID"] =  # client id
server.config["GOOGLE_OAUTH_CLIENT_SECRET"] =  # client secret
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

APPLICATION = APP.server


APP.layout = html.Div([
    navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(className="container main-container", children=[])


    authorized_emails=[]
    auth=GoogleOAuth(
        APP,
        authorized_emails,
    )


    @APP.callback(
        Output('username', 'children'),
        [Input('placeholder', 'value')]
    )
    def on_load(value):
        return "{},".format(session['email'])




    @APP.callback(dash.dependencies.Output('page-content', 'children'),
                  [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return wp.generate_page_1_layout()
        elif pathname == '/logout':

            resp=google.post(
                'https://accounts.google.com/o/oauth2/revoke',
                params={'token': session['google_oauth_token']['access_token']},
                headers={'content-type': 'application/x-www-form-urlencoded'}
        )
            if resp.ok:
                session.clear()
            return wp.generate_page_logout()

        return wp.generate_page_1_layout('nodebug')


    if __name__ == '__main__':
    APPLICATION.run(debug=True, host='0.0.0.0', port=8000)
