from flask import Flask, render_template, request, redirect, url_for
from DB_class import DB


class Main:
    def __init__(self):
        self.app = Flask(__name__)
        self.DB = DB(user='root', password='', host_address='',database_name='')

    def routing(self):
        data = self.DB.execute('SELECT *  FROM ')
        print(data)
        @self.app.route('/')
        def main_page():
            return render_template('index.html')

        """
        @self.app.route('/...')
        def ...():
            return render_tempalte('...html')
        """

    def run(self):
        self.routing()
        self.app.run()

if __name__ == '__main__':
    App = Main()
    App.run()

        
