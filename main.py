from flask import Flask, request, render_template_string
from sifre import sifreyapici
from sayi_tutmak import sayi_tut1
from sayi_tutmak import sayi_tut2

app = Flask(__name__)

# Ana sayfa
@app.route("/")
def index():
    return '''
        <a href="/şifre">Şifre Oluşturucuyu görüntüle</a>
        <a href="/sayia">10 ile 0 arası bir sayı tut</a>
        <a href="/sayia2">100 ile 0 arası bir sayı tut</a>
        <h1>Ana Sayfa</h1>
    '''

# Şifre oluşturucu sayfası
@app.route("/şifre", methods=["GET", "POST"])
def sifreweb():
    if request.method == "POST":
        # Kullanıcıdan gelen şifre uzunluğunu al
        try:
            uzunluk = int(request.form["uzunluk"])
            # Eğer sayı geçerliyse, şifreyi oluştur
            if uzunluk > 0:
                sifre = sifreyapici(uzunluk)
                return f'''
                    <a href="/">Ana sayfayı görüntüle</a>
                    <h1>Şifre Oluşturucu</h1>
                    <h3>Oluşturulan Şifre: {sifre}</h3>
                    <a href="/şifre">Tekrar şifre oluştur</a>
                '''
            else:
                return '''
                    <a href="/">Ana sayfayı görüntüle</a>
                    <h1>Şifre Oluşturucu</h1>
                    <p>Geçerli bir sayı girin (pozitif tam sayı olmalı)</p>
                    <a href="/şifre">Tekrar şifre oluştur</a>
                '''
        except ValueError:
            return '''
                <a href="/">Ana sayfayı görüntüle</a>
                <h1>Şifre Oluşturucu</h1>
                <p>Lütfen geçerli bir sayı girin.</p>
                <a href="/şifre">Tekrar şifre oluştur</a>
            '''
    return '''
        <a href="/">Ana sayfayı görüntüle</a>
        <h1>Şifre Oluşturucu</h1>
        <form method="POST">
            <label for="uzunluk">Şifre uzunluğunu girin:</label>
            <input type="number" name="uzunluk" id="uzunluk" min="1" required>
            <button type="submit">Şifreyi Oluştur</button>
        </form>
    '''

# Sayı tutma 1 (10 ile 0 arasında)
@app.route("/sayia")
def sayiweb():
    return f'<a href="/">Ana sayfayı görüntüle</a> <h1>Çıkan Sayı : {sayi_tut1()}</h1>'

# Sayı tutma 2 (100 ile 0 arasında)
@app.route("/sayia2")
def sayiweb2():
    return f'<a href="/">Ana sayfayı görüntüle</a> <h1>Çıkan Sayı : {sayi_tut2()}</h1>'

# Uygulama çalıştırma
if __name__ == "__main__":
    app.run(debug=True)
