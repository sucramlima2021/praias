# balneabilidade_praias_rj

Esta API consome o relatório de balneabilidade das praias da cidade do Rio de Janeiro e retorna um JSON com a listagem das praias, a referencia de cada uma, as coordenadas dos pontos onde foram realizados os testes e o HTML de um iframe com o mapa fornecido pelo google maps já apontando para as coordenadas da praia.

O sistema verifica 1x ao dia se o INEA lançou novos relatórios e faz a atualização das informações

Faça uma requisição GET para '*seu-dominio*/lista/' para retornar o referido JSON com as informações. 

já tem um administrador no Banco de dados: 
 - Username: marcus 
 - senha: 123. 
