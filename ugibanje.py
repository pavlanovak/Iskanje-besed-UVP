import bottle
import bottle_session
from igra import Igra
from pathlib import Path
import os

app = bottle.app()


abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, 'views')
bottle.TEMPLATE_PATH.insert(0, abs_views_path ) # nastavitev direktorija za serviranje staticnih datotek

igra = None


@bottle.get("/")
@bottle.view('landing')
def osnovna_stran():
    return { 'get_url': bottle.url } 

@bottle.get("/igra_vmesnik")
def prikazi_igro():
    return bottle.template("igra.tpl",
                             mesana_beseda=igra.pomesana, 
                             poskus=igra.ugibanja,
                             rezultat=False,
                             beseda = igra.beseda)

@bottle.post("/ugibaj")
def ugibaj():
    ugibana_beseda = bottle.request.forms.getunicode("beseda")
    rezultat = igra.ugibaj(ugibana_beseda)
    return bottle.template("igra.tpl",
                            mesana_beseda=igra.pomesana,
                            rezultat= rezultat,
                            poskus=igra.ugibanja,
                            beseda = igra.beseda)

@bottle.post("/nova_igra")
def nova_igra():
    global igra
    igra = Igra()
    bottle.redirect("/igra_vmesnik")
    
@bottle.route('/views/:path#.+#', name='views')
def views(path):
    print(path)
    return bottle.static_file(path, root='views')

bottle.run(reloader=True, debug=False)