# ClimateExplorer 🌦️  
**Flask lietotne klimata datu vizualizācijai un analīzei**  

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📋 Saturs  
1. [Uzstādīšana](#-uzstādīšana)  
2. [Datu bāze](#-datu-bāze)  
3. [Lietošana](#-lietošana)  
4. [Izvietošana](#-izvietošana)  
5. [Izstrāde](#-izstrāde)  
6. [BUJ](#-buj)  

---

## 🛠️ Uzstādīšana  

### Prasības  
- Python 3.8 vai jaunāks  
- Git (neobligāti)  

### Instalācijas soļi  

1. **Repozitorija klonēšana**  
```bash
git clone https://github.com/FreinHub/ClimateExplorer.git
cd ClimateExplorer
```

2. **Virtuālās vides izveide**  
```bash
python -m venv .venv
```

3. **Vides aktivizēšana**  
```bash
# Windows
.\.venv\Scripts\activate

# Linux/MacOS
source .venv/bin/activate
```

4. **Atkarību instalēšana**  
```bash
pip install -r requirements.txt
```

---

## 🗄️ Datu bāze  

### Inicializācija  
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Testa datu ievade  
```bash
python scripts/seed_data.py
```

---

## 🚀 Lietošana  

### Lokālā palaišana  
```bash
flask run
```  
Pēc tam atveriet: [http://localhost:5000](http://localhost:5000)  

### Pieejamās komandas  
| Komanda | Apraksts |
|---------|----------|
| `flask run --debug` | Atkļūdošanas režīms |
| `flask shell` | Interaktīvā Python vides palaišana |

---

## ☁️ Izvietošana  

### PythonAnywhere  
1. Izveidojiet kontu [pythonanywhere.com](https://www.pythonanywhere.com)  
2. Augšupielādējiet failus  
3. WSGI konfigurācijā norādiet:  
```python
from app import app as application
```

### Heroku  
```bash
heroku create
git push heroku main
heroku open
```

---

## 💻 Izstrāde  

### Koda struktūra  
```
ClimateExplorer/
├── app/               # Lietotnes kods
├── instance/          # Datu bāzes faili
├── scripts/           # Palīgskripti
├── .gitignore         # Ignorējamie faili
└── requirements.txt   # Atkarības
```

### Izmaiņu iesniegšana  
1. Izveidojiet jaunu zaru:  
```bash
git checkout -b jauna-iezime
```  
2. Veiciet izmaiņas un iesniedziet:  
```bash
git add .
git commit -m "Apraksts"
git push origin jauna-iezime
```  

---

## ❓ BUJ  

### Kā atjaunot atkarības?  
```bash
pip freeze > requirements.txt
```

### Kā atiestatīt datu bāzi?  
```bash
flask shell
>>> db.drop_all()
>>> db.create_all()
```

### Kādi dati tiek izmantoti?  
Projekts izmanda atvērtos klimata datus no [NOAA](https://www.noaa.gov/).

---

📬 **Kontakti**:  
Autors: [FreinHub](https://github.com/FreinHub)  
E-pasts: artomsolovej43@gmail.com  

📅 **Pēdējais atjauninājums**: 29.03.2025   

[![Standarta atjaunināšana](https://img.shields.io/badge/atjaunināts-marts%202025-lightgrey)](CHANGELOG.md)  

*Šis projekts ir lai iegut atzīmi Datariuma, Projekta developer- Artjoms Solovjovs, Ideju generešana- Viktors Verkins, Deniss Nikitins*
