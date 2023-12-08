from django.urls import reverse
from cliente.forms import ClienteForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        print(form.errors)  
        if form.is_valid():
            form.save()
            return redirect(reverse("core:index"))
    else:
        form = ClienteForm()

    return render(request, "cliente/crear.html", {"form": form})

def buscar_view(request):
    query = request.GET.get('q', '')
    borrar_resultados = 'borrar' in request.GET

    if borrar_resultados:
        
        if 'resultados' in request.session:
            del request.session['resultados']
        return redirect('core:index')  

   
    results = obtener_resultados_segun_busqueda(query)

    
    if not borrar_resultados:
        request.session['resultados'] = results

    return render(request, 'core/base.html', {'query': query, 'results': results})


def borrar_resultados(request):
    if request.method == 'POST':
      
        if 'resultados' in request.session:
            del request.session['resultados']

  
    return redirect('core:index')



def obtener_resultados_segun_busqueda(query):
    bateristas =[ 
        {"nombre": "Aquiles Priester", "imagen": 'core/img/aquiles-priester-drums.jpg', "descripcion": "Aquiles Priester (n. Otjo, Sudáfrica, 25 de junio de 1971) es un músico brasileño, baterista de las bandas de power metal Hangar y Primal Fear. En 2006 participó en el proyecto de Fábio Laguna, «Freakeys», y hasta 2008 fue el baterista de Angra."},
        {"nombre": "Lars Ulrich", "imagen": 'core/img/descarga.jpg', "descripcion": "Nació el 26 de diciembre de 1963 en Gentofte (Dinamarca), en el seno de una familia de clase media-alta. Siendo un prodigio del tenis en su juventud, Ulrich se trasladó a Los Ángeles, California, a la edad de dieciséis años para seguir con su educación, pero en vez de seguir jugando al tenis, decidió dedicarse a la batería. Después de publicar un anuncio en un periódico local de Los Ángeles, The Recycler, conoció a James Hetfield."},
        {"nombre": "Ray Luzier", "imagen": 'core/img/korn.jpg', "descripcion": 'Raymond Lee "Ray" Luzier (Pittsburgh, Pensilvania, 14 de junio de 1970) es un baterista de rock estadounidense. Es más conocido por haber formado parte de la banda Army of Anyone, un conjunto de rock compuesto por Richard Patrick y los hermanos Dean DeLeo y Robert DeLeo de Stone Temple Pilots. Actualmente es el baterista de la banda Korn y KXM.'},
        {"nombre": "Mike Terrana","imagen": 'core/img/terrana.jpg',"descripcion": 'Mike Terrana (Búfalo, Nueva York; 21 de enero de 1960) es un baterista estadounidense de heavy metal que ha grabado con multitud de bandas de todo el mundo. Actualmente es miembro de la nueva formación de la banda española Avalanch, y además participa en la banda de power metal italiana Vision Divine.'},
        {"nombre": "Nicko Mc Brain","imagen": 'core/img/nicko.jpeg',"descripcion": "Michael Henry McBrain (Hackney, Gran Londres, Inglaterra, 5 de junio de 1952) es el baterista del grupo británico de heavy metal Iron Maiden. El nombre de Nicko lo adoptó como sobrenombre tal y como se llamaba su osito de peluche preferido. McBrain es acreditado como uno de los pioneros del sonido de heavy metal. En 2009 la revista Rolling Stone publicó la lista de los 100 mejores baterías de todos los tiempos."},
        {"nombre": "Dave Lombardo","imagen": 'core/img/dave.jpeg',"descripcion": "David Lombardo (La Habana, Cuba, 16 de febrero de 1965), conocido artísticamente como Dave Lombardo, es un músico cubano-estadounidense, conocido principalmente por su trabajo como baterista de la banda de thrash metal Slayer, con la cual participó en siete de sus álbumes. Actualmente es baterista de Mr Bungle y Misfits, trabajando en su proyecto solitario y otros proyectos de ensamble."}    
    ]
    resultados = [baterista for baterista in bateristas if query.lower() in baterista['nombre'].lower()]
    return resultados
