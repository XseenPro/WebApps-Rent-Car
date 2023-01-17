# Caesar
from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'rental'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = 'kelompoksantuy'
mysql.init_app(app)
conn = mysql.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mobil/')
def mobil():
    return render_template('mobil.html')

@app.route('/informasi/')
def informasi():
    return render_template('informasi.html')
# Akhir Caesar

# Azkal
@app.route('/booking', methods = ['GET', 'POST'])
def booking():
    if request.method == 'POST':
        _nama = request.values.get('nama')
        _wa = request.values.get('wa')
        _email = request.values.get('email')
        _mobil = request.values.get('mobil')
        _tanggal = request.values.get('tanggal')
        _sopir = request.values.get('sopir')
        _lokasi_penjemputan = request.values.get('lokasi_penjemputan')
        _lokasi_tujuan = request.values.get('lokasi_tujuan')
        sql = "insert into user(nama, wa, email, mobil, tanggal, sopir, lokasi_penjemputan, lokasi_tujuan) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (_nama, _wa, _email, _mobil, _tanggal, _sopir, _lokasi_penjemputan, _lokasi_tujuan)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return redirect('/result')
    else:
        return render_template('booking.html')

@app.route('/result')
def result():
    cursor = conn.cursor()
    sql = ('select * from user')
    cursor.execute(sql)
    hasil = cursor.fetchall()
    return render_template('result.html', data=hasil)

@app.route('/result/nota/')
def nota():
    cursor = conn.cursor()
    cursor.execute("select * from user ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    print(result)
    return render_template('nota.html', hasil = result)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            msg = 'Username/password salah!'
    return render_template('login.html', msg=msg)
# Akhir Azkal

# Fery
@app.route('/login/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login/admin')
def admin():
    cursor = conn.cursor()
    sql = ('select * from user')
    cursor.execute(sql)
    hasil = cursor.fetchall()
    if 'loggedin' in session:
        return render_template('admin.html' , data=hasil)
    return redirect(url_for('login'))

@app.route('/hapus/<_id>')
def hapus_user(_id):
    cursor = conn.cursor()
    sql = 'delete from user where id = %s'
    data = (_id)
    cursor.execute(sql, data)
    conn.commit()
    return redirect('/login/admin')

@app.route('/ubah/<_id>')
def ubah_user(_id):
    cursor = conn.cursor()
    sql = ('select * from user where id = %s')
    data = (_id)
    cursor.execute(sql, data)
    hasil = cursor.fetchone()
    return render_template('ubah_booking.html', data=hasil)

@app.route('/perbarui', methods = ['POST'])
def perbarui_data():
        _id = request.values.get('id')
        _nama = request.values.get('nama')
        _wa = request.values.get('wa')
        _email = request.values.get('email')
        _mobil = request.values.get('mobil')
        _tanggal = request.values.get('tanggal')
        _sopir = request.values.get('sopir')
        _lokasi_penjemputan = request.values.get('lokasi_penjemputan')
        _lokasi_tujuan = request.values.get('lokasi_tujuan')
        sql = "update user set nama = %s, wa = %s, email = %s, mobil = %s, tanggal = %s, sopir = %s, lokasi_penjemputan = %s, lokasi_tujuan = %s where id = %s"
        data = (_nama, _wa, _email, _mobil, _tanggal, _sopir, _lokasi_penjemputan, _lokasi_tujuan, _id)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return redirect('/login/admin')
# Akhir Fery
    
if __name__ == '__main__':
    app.run(debug=True)