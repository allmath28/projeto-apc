### Link para teste do programa: https://replit.com/@allmath28/Projeto-APC#main.py

# **Projeto Administração de Restaurante**



Este projeto foi criado como trabalho de faculdade com o intuito de simular um restaurante de forma básica, com comandos para:

* Inserção de áreas com mesas que possuem diferentes quantidades de cadeiras;
* Alocação de grupos de pessoas baseado na quantidade de pessoas e disponibilidade do restaurante;
* Adicionar ou remover mesas em uma determinada área;
* Mostrar a quantidade de mesas ocupadas e disponíveis em cada área;
* Mostrar a quantidade de cadeiras ocupadas e disponíveis em cada área;
* Fechamento do Restaurante com um balanço geral do movimento de pessoas e a quantidade de mesas e cadeiras;

## Funcionamento

No primeiro momento, o usuário deverá inserir o comando `--CONFIGURACAO` para dar início a parte de configuração dos ambientes do restaurante, adicionando as áreas, as mesas e as cadeiras. Então, após realizado a configuração, o usuário digitará `--ATENDIMENTO` para dar início ao atendimento, nessa parte ele irá inserir comandos ordenados de `1` a `4` para fazer alterações no restaurante, adicionar grupos de pessoas às mesas (caso seja possível), listar mesas e cadeiras ocupadas e livres em cada área, e também o comando `-1` que faz o fechamento do restaurante, e mostra um relatório das mesas e pessoas que foram atendidas no restaurante.

## Instruções

* `--CONFIGURACAO` - O usuário deverá digitar esse comando `--CONFIGURACAO`no terminal para dar início a parte de configuração do restaurante.

* Nas linhas seguintes, o usuário deverá digitar, separando com espaços, a área, a quantidade de mesas e a quantidade de cadeiras que cada mesa deverá ter, como no exemplo abaixo:

  * `--CONFIGURACAO`
    `A M C`

    onde _A_ representa o nome da área, *M* representa a quantidade de cadeiras e *C* representa a quantidade de cadeiras que cada mesa terá.

* A configuração ocorrerá automaticamente até que seja digitado o comando `--ATENDIMENTO` que marca o final da configuração do restaurante. Neste momento o usuário terá opção de executar 5 comandos diferentes listados abaixo:

  * `1`  -- O comando `1` é o comando que fará a alocação de grupos de pessoas para mesas, caso seja possível, ou retornará uma mensagem dizendo que não foi possível alocar. O funcionamento do comando `1` é o seguinte:

    * O usuário insere o comando `1` e na linha abaixo deve ser inserido a seguinte frase:

      * `Quero uma mesa para X pessoas na area Y`

        Onde *X* representa a quantidade de pessoas no grupo, e *Y* representa a área desejada (é necessário inserir uma área existente). Caso exista uma mesa na área inserida, será imprimido na tela uma mensagem confirmando no formato:
        
        `"Um grupo de X pessoas ocupou uma mesa de Y lugares na area Z."`
        
        na qual o _X_ representa a quantidade de pessoas do grupo, _Y_ representa o total de cadeiras que a mesa possui e _Z_ é a área desejada.
        
        Caso não tenha sido possível alocar o grupo de pessoas em uma mesa, será retornada a seguinte mensagem:
        
        `"Nao foi possivel levar o grupo de clientes para uma mesa."`
        
        Ainda no comando `1`, temos o tempo de permanência do grupo, que será calculado da seguinte maneira: `(2 * N) + 2`, em que _N_ representa a quantidade de pessoas no grupo. Cada vez que é inserido um comando (contando já com o comando `1` ) é subtraído uma unidade do tempo, e quando chegar a 0, a mesa será desocupada.
        
        
        
        #### ***\**Particularidades do Comando\**\***
        
        **Assuma que não serão requeridas mesas em áreas que não existem.**
        
        
    
  * `2` -- O comando `2` serve para mostrar ao usuário, ordenada alfabeticamente, a quantidade de mesas ocupadas e livres de cada área do restaurante.

  * `3` -- O comando `3` serve para mostrar ao usuário, ordenada alfabeticamente, a quantidade de cadeiras ocupadas e livres de cada área do restaurante.

  * `4` -- O comando `4` é utilizado para adicionar ou remover uma quantidade de mesas com um determinado número de cadeiras em uma área específica do restaurante:

    * O usuário insere o comando `4` e na linha abaixo deve ser inserido a seguinte frase:

    * `Quero OP mais Z mesas com X cadeiras cada na area Y` 

      ​	Onde _OP_ representa a operação desejada ('adicionar' ou 'remover'),  _Z_ é a quantidade de mesas a serem adicionadas, _X_ é a quantidade de cadeiras de cada mesa, e _Y_ é a área em que as mesas serão adicionadas/removidas.

      #### ***\**Particularidades do comando\**\***

      **Assuma que nunca serão adicionadas mesas em áreas não existentes, nem que serão removidas mesas que estão ocupadas ou que não existem!!!!**

  * `-1` -- O comando `-1` é utilizado para imprimir a configuração final do restaurante, após a adição e remoção de mesas (caso tenham ocorrido), separadas por área (ordenadas em ordem alfabética), com a configuração de mesas e cadeiras (ordenadas em ordem crescente de cadeiras), e a quantidade de pessoas que entraram no restaurante, com o seguinte formato:

    `Restaurante fechado.
    Balanco final de mesas:
    A1:
     M1 mesas de C1 cadeiras.
     M2 mesas de C2 cadeiras.
     M3 mesas de C3 cadeiras.
    A2:
     M4 mesas de C4 cadeiras.
     M5 mesas de C5 cadeiras.
    .
    .
    .
    Um total de T pessoas visitaram o restaurante hoje.
    Bom descanso!`

    

    Onde _A_ são as áreas, _M_ são quantas mesas de uma quantidade específica de cadeiras a área tem, _C_ são quantas cadeiras cada mesa tem e _T_ são quantas pessoas visitaram o restaurante.
