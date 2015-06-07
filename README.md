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

      * Espécie
      * Altura
      * Diâmetro
      * Informações adicionais
      * Foto


## Contribuidores

@barbaralluz
@cadu-leite

## Tecnologias Utilizadas


* [**Django (versão 1.7)**](https://www.djangoproject.com/)  
Um framework Web Python de alto nível que incentiva o rápido desenvolvimento e design limpo e pragmático. É livre e open source.  
_** Observação: Junto com o Django, foi utilizado o [GeoDjango](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/) que trata-se de um módulo incluso no Django, que possibilita criar aplicações Geográficas, com serviços baseados em localização .... **_

* **[Django-Social-Auth (versão 0.7.28)](https://django-social-auth.readthedocs.org/en/latest/) e [Oauth2 (versão 1.5.211)](https://django-oauth2-provider.readthedocs.org/en/latest/)**  
Tratam-se de aplicações utilizadas para realizar autenticação e registro de usuários, o _**Django-Social-Auth**_ possibilita autenticação e registro através de redes sociais (como Facebook, Twitter e Google) e o _**Oauth2**_ através do cadastro de um usuário com e-mail e senha.

* **PostgreeSQL com PostGis**  
Banco de dados, o Postgis foi utilizado para armazenar dados geográficos no banco.

* **PIL (versão 1.1.7) e [Pillow (versão 2.8.1)](https://pillow.readthedocs.org/)**  
Para biblioteca de imagens em Python, utilizado para cadastrar imagens das árvores.


* [**OpenLayers**](http://openlayers.org/)  e [**Openstreetmap**](https://www.openstreetmap.org/)
Bibliotecas javascript open source utilizada para carregar e exibir mapas.


* [**Bootstrap**](http://getbootstrap.com/)  
Utilizado para criação dos templates do projeto.

## Fontes (Sites, Literatura, Documentos em Geral)

