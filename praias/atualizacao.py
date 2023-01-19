import traceback
import requests
from django.conf import settings
from praias.models import Relatorios, Praias
from bs4 import BeautifulSoup
from praias.pt_praias import PRAIAS
from PyPDF2 import PdfReader
from django.utils import timezone



def atualiza():
    
    #pega os boletins atuais no site do INEA
    url = "http://www.inea.rj.gov.br/rio-de-janeiro/"
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    links = soup.find_all('a')

    #lista com os links para os boletins
    link = []
    
    #lista com os nomes dos arquivos dos boletins
    arquivos=['\zona_oeste_sul.pdf', '\sepetiba.pdf', '\ilha.pdf', '\paqueta.pdf']

    #adiciona os links dos boletins a lista
    for l in links:
        txt = l.get_text()
        if txt == "Último Boletim Divulgado":
            link.append(l['href'])
    
    #pega todos os registros de boletins que estão no banco
    relatorios = Relatorios.objects.all()

    #se for a primeita vez que o sistema é iniciado serão gravados todos os dados sobre os boletins e os mesmos serão baixados para a pasta media
    inicio = len(relatorios)
    
    if inicio == 0:
        print(inicio)
        try:
            cont = 0
            for i in link:
                #grava o registro no banco
                relatorio = Relatorios(nome = arquivos[cont], url = i)
                relatorio.save()

                #grava o pdf com o boletim na pasta media
                r = requests.get(i, stream = True)
                arq = settings.MEDIA_ROOT + arquivos[cont]
                print(arq)
                with open(arq,"wb") as pdf: 
                    for chunk in r.iter_content(chunk_size=1024): 
                        if chunk: 
                            pdf.write(chunk)
                    pdf.close()
                cont +=1

            
            return True
        except Exception:
            
            traceback.print_exc()
        
            return False

    #caso os 4 registros já existam, faz a conferencia dos links e verifica se são os atuais, caso não sejam, atualiza o banco. 
    elif inicio == 4:
        try: 
            cont = 0
            for i in relatorios:
                if i != link[cont]:
                    i.url = link[cont]
                    i.save()
                    #grava o pdf com o boletim na pasta media
                    r = requests.get(i, stream = True)
                    arq = settings.MEDIA_ROOT + arquivos[cont]
                    with open(arq,"wb") as pdf: 
                        for chunk in r.iter_content(chunk_size=1024): 
                            if chunk: 
                                pdf.write(chunk)
                        pdf.close()
                    
                cont += 1
            
            return True
        except Exception:
            
            traceback.print_exc()
        
            return False
    else:
        try: 
            Relatorios.objects.all().delete()
            cont = 0
            for i in link:
                #grava o registro no banco
                relatorio = Relatorios(nome = arquivos[cont], url = i)
                relatorio.save()

                #grava o pdf com o boletim na pasta media
                r = requests.get(i, stream = True)
                arq = settings.MEDIA_ROOT + arquivos[cont]
                with open(arq,"wb") as pdf: 
                    for chunk in r.iter_content(chunk_size=1024): 
                        if chunk: 
                            pdf.write(chunk)
                    pdf.close()
                cont +=1

            
            return True
        except Exception:
            
            traceback.print_exc()
        
            return False
def atualiza2():
    try:
        #Se for a primeira vez que o sistema é iniciado ou se a tabela de praias não tiver nenhum registro, cadastra as praias que estão no arquivo pt-praias.py
        praias = Praias.objects.all()

        if len(praias) == 0:
            for br, pr in PRAIAS.items():
                for i in pr:
                    pra = Praias(nome = br+i[0], descr = "não tem", ref = i[0], bairro = br, coord = i[1], mapa = i[2], atualizado_em = timezone.now())
                    pra.save()
        
        return True
    except Exception:
            
        traceback.print_exc()
        
        return False



def atualiza3():
    try:
        #atualiza as informações sobre a balneabilidade das praias de acordo com ultimo relatório emitido.
        conteudo = PdfReader(settings.MEDIA_ROOT + '\zona_oeste_sul.pdf')
        pr = Praias.objects.all()
        pag = conteudo.pages[0]

        texto = pag.extract_text()
        tt = texto.splitlines()
        for i in tt:
            for j in pr:
                if j.ref in i:
                    if "Imprópria" in i:
                        j.propria = False
                        
                    else:
                        j.propria = True

                    j.atualizado_em = timezone.now()
                    j.save()
        
        return True
    except Exception:
            
        traceback.print_exc()
            
        return False