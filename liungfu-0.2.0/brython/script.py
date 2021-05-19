from browser.widgets.menu import Menu
from browser.widgets.dialog import *
from browser import document as doc
from browser import bind,window,html
from random import choice
from browser import timer


width  = int(window.innerWidth)
height = int(window.innerHeight)
doc["main"].style.width  = f"{width}px"
doc["main"].style.height = f"{height}px"
doc["main"] <= html.DIV(id="table")
doc["table"].style = dict({
    "width":f"{width}px",
    "height":f"{height / 3}px",
})
doc["g"] <= (html.BUTTON(i,id=i),for i in ["Nutup","Ngoyang"])
doc["f"] <= html.IMG(src="img/hide1.png",id="gambar")
doc["f"] <= html.IMG(src="img/img1.png",id="hasil",Class="hasil")

doc["gambar"].style = dict(
    width = f"{width / 5}px",
    height = f"{height / 5}px",
)
doc["hasil"].style = dict({
    "width"  : f"{width / 10}px",
    "height" : f"{height / 10}px",
    "margin-left" : f"{width / 10}px"
})
menu = ["Nagatur","Tentang","Masok"]
def Menu_options(opt):
    for i in opt:
        doc["menu"] <= html.SPAN(id=i)
    Nangatur = Menu(doc[opt[0]],default_css=False)
    settings = Nangatur.add_menu(opt[0])
    settings.add_menu("""
        bunyi nguncang:
        <select id="select_bool1">
            <option value="Ayakin">Ayakin</option>
            <option value="Ituhkin">Ituhkin</option>
        </select>""")
    settings.add_menu("""
        cioh kalo buka:
        <select id="select_bool2">
            <option value="Ayakin">Ayakin</option>
            <option value="Ituhkin">Ituhkin</option>
        </select>""")
    settings.add_menu("""
        warna tutup e:
        <select id="ttp">
            <option value="img/hide1">Putih</option>
            <option value="img/hide2">Itamp</option>
            <option value="img/hide3">Amas</option>
        </select>""")
    settings.add_menu("""
        gaatn e :
        <span>
        <select id="renames">
            <option value="name1">gaatn 1</option>
            <option value="name2">gaatn 2</option>
            <option value="name3">gaatn 3</option>
            <option value="name4">gaatn 4</option>
            <option value="name5">gaatn 5</option>
            <option value="name6">gaatn 6</option>
        </select>
        <input type="text" id="name">
        <button id="confir-name">nganti</button></span>""")
    
    Tentang = Menu(doc[opt[1]],default_css=False)
    Tentang.add_menu(opt[1])

    Masuk = Menu(doc[opt[2]],default_css=False)
    Masuk.add_menu(opt[2])

Menu_options(menu)
table = doc["tbl"]
table.style = dict(
    width=f"{width}px",
    height=f"{height / 1.5}px")

for i,dt in enumerate(list("abcdeh")):
    doc[dt] <= html.IMG(
        src = f"img/img{i+1}.png",
        id  = f"img{i+1}");
    doc[f"img{i+1}"].style = dict(
        width  = f"{width / 6}px",
        height = f"{height / 7}px",
    )
    doc[dt].style = dict({
        "width":f"{width / 1.5}px",
        "height":f"{height / 4}px",
    })

def clear_class():
    doc["gambar"].classList.remove("goyang")
    doc["Ngoyang"].classList.remove("active")

def random_image():
    for i in range(10):
        random =  choice(["img1","img2","img3","img4","img5","img5"])
    doc["hasil"].src = f"img/{random}.png"
    

@bind("#ttp","change")
def replace_image(ev):
    img = doc[ev.target.id].value
    doc["gambar"].src = f"{img}.png"

@bind("#Nutup","click")
def buka_hasil(ev):
    doc["hasil"].classList.toggle("buka")
    doc["gambar"].classList.toggle("gambar")
    if doc[ev.target.id].text == "Nutup":
        if doc["select_bool2"].value == "Ituhkin":
            doc["sound"].src = "sound/ohh.mp3"
        else:pass
        doc[ev.target.id].text = "Mukak"
        doc[ev.target.id].style.backgroundColor = "cyan"
    else:
        doc["sound"].src = ""
        doc[ev.target.id].text = "Nutup"
        doc[ev.target.id].style.backgroundColor = "azure"

@bind("#Ngoyang","click")
def goyang_efek(ev):
    if doc["Nutup"].text == "Nutup":
        if doc["select_bool1"].value == "Ituhkin":
            print(doc["select_bool1"].value)
            doc["sound"].src = "sound/sound.mp3"
        else:pass
        random_image()
        doc["gambar"].classList.add("goyang")
        doc[ev.target.id].classList.add("active")
        timer.set_timeout(clear_class,1500)
    else:pass

# buat tempat penyimpanan nama dengan P
for i,d in zip(
    list("abcdeh"),
    ['name1','name2','name3',
    'name4','name5','name6']):
    doc[i] <= html.P(id=d)

@bind("#confir-name","click")
def renames(ev):
    names = doc['renames'].value
    doc[names].textContent = doc['name'].value