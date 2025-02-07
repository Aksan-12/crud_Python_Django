from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mahasiswa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(10), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    prodi = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Mahasiswa {self.nama}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    mahasiswas = Mahasiswa.query.all()
    return render_template('index.html', mahasiswas=mahasiswas)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_mahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        prodi = request.form['prodi']
        semester = request.form['semester']

        if not nim or not nama or not prodi or not semester:
            return "Semua field harus diisi!", 400

        if Mahasiswa.query.filter_by(nim=nim).first():
            return "NIM sudah terdaftar!", 400

        mahasiswa_baru = Mahasiswa(
            nim=nim, 
            nama=nama, 
            prodi=prodi, 
            semester=semester
        )
        
        db.session.add(mahasiswa_baru)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('tambah.html')

@app.route('/hapus/<int:id>')
def hapus_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    db.session.delete(mahasiswa)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    
    if request.method == 'POST':
        mahasiswa.nim = request.form['nim']
        mahasiswa.nama = request.form['nama']
        mahasiswa.prodi = request.form['prodi']
        mahasiswa.semester = request.form['semester']
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', mahasiswa=mahasiswa)

if __name__ == '__main__':
    app.run(debug=True)