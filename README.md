# Objetivo desse Projeto

Construir um inventário ["crowdsourcing"](http://pt.wikipedia.org/wiki/Crowdsourcing) georreferenciado de árvores urbanas, ou seja, uma ferramenta que permite que a população, organizações e governos contribuam de forma colaborativa para a criação de um inventário interativo e dinâmico das árvores urbanas.

## Principais Funções

  1. Cadastro de usuário (cadastro de usuário e email ou se conectar com conta do gmail);
  1. Realizado cadastro, usuário terá acesso aos dados do inventário e poderá adicionar, editar e excluir árvores;
  1. O usuário poderá adicionar comentários sobre árvores já existentes no sistema (cadastrada por outros usuários). - Função ainda em desenvolvimento.


  * **Informações das árvores:**

    1. Para adicionar uma árvore ao sistema, é necessário incluir:
      * Endereço (Rua, Número, Bairro, Cidade, Estado, País e CEP, Ponto de Referencia).  

      **_Observação: É necessário realizar busca de endereço ou clicar sobre o botão "Me localize" para que as informações de rua, bairro, cidade, estado e país sejam adicionados)._**
      
      * Condição da Árvore
      * Espécie
      * Altura
      * Condição das Raizes
      * Presença de rede elétrica
      * Necessidade de Manutenção
      * Descrição
      * Fotos (3 fotos)
      
      _Alterado em 16/08/2015_


## Contribuidores

Barbara Lopes Luz (@barbaralluz)  
Carlos E. C. Leite (@cadu-leite)  
Luiz Fernando Barbosa Vital (@luizvital)  
ZNC Sistemas  

## Tecnologias Utilizadas


* [**Django (versão 1.7)**](https://www.djangoproject.com/)  
Um framework Web Python de alto nível que incentiva o rápido desenvolvimento e design limpo e pragmático. É livre e open source.  
_** Observação: Junto com o Django, foi utilizado o [GeoDjango](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/) que trata-se de um módulo incluso no Django, que possibilita criar aplicações Geográficas, com serviços baseados em localização **_

* **PostgreeSQL com PostGis**  
Banco de dados, o Postgis foi utilizado para armazenar dados geográficos no banco.


* [**OpenLayers**](http://openlayers.org/)  e [**Openstreetmap**](https://www.openstreetmap.org/)
Bibliotecas javascript open source utilizada para carregar e exibir mapas.


* [**Bootstrap**](http://getbootstrap.com/)  
Utilizado para criação dos templates do projeto.

## Fontes (Sites, Literatura, Documentos em Geral)

