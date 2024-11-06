from flask import Flask
from sifre import sifreyapici
from sayi_tutmak import sayi_tut



app = Flask(__name__)


@app.route("/")
def index():
    return '<a href="/şifre">Şifre Oluşturucuyu görüntüle</a>           <a href="/sayia">10 la 0 arası bir sayi tut </a> <h1>Ana Sayfa</h1>'

@app.route("/şifre")
def sifreweb():
    return f'<a href="/">Ana sayfayı görüntüle</a> <h1>Şifre Oluşturucu</h1><h3>{sifreyapici(8)}</h3>'

@app.route("/sayia")
def sayiweb():
    return f'<a href="/">Ana sayfayı görüntüle</a> <h1>Çıkan Sayı : {sayi_tut()}</h1>'


app.run(debug=True)


