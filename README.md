# Checkpoint 3
Checkpoint 3 - AI Engineering, Cognitive and Semantics Computing & IoT

Nomes:

Adler Nunes Cordeiro RM 85158

Gabriel Faria Rodrigues RM 84483

Guilherme Oliveira da Silva RM 84917

Olá! Este é o repositório para a entrega do Checkpoint 3 da disciplina do professor Arnaldo Alves Viana Júnior (https://github.com/arnaldojr)

Nesta entrega fomos desafiados a desenvolver um sistema contando com a comunicação entre Python e Arduino.

# Detecção de mãos

Nosso projeto consiste em um programa que é capaz de contar a quantidade de dedos "em pé" utilizando um código Python e apresentar o dado no Arduino.

Para isso, desenvolvemos o código no arquivo main.py, e o sketch em sketch-arduinopython.

# Python

No main.py, o usuário precisa definir a porta serial correta na linha 9 para a comunicação com o Arduino (https://support.arduino.cc/hc/en-us/articles/4406856349970-Select-board-and-port-in-Arduino-IDE) e definir se ele usará o programa para uma gravação (neste caso, passar o endereço completo do vídeo como valor na linha 57) ou se usará um vídeo ao vivo, como uma webcam (neste caso, é necessário que o usuário descubra qual valor está atribuído para sua câmera, comumamente o valor é 0). Códigos .py podem ser facilmente alterados usando qualquer editor de texto. Obs.: Não se esqueça de instalar as bibliotecas necessárias e executar em uma pasta ou environment com acesso às bibliotecas instaladas na sua versão do Python.

Com estas alterações, o programa estará pronto para o uso!

# Arduino

Já para visualização no Arduino, caso não possua um display disponível para utilizar junto a placa, você pode instalar o Arduino IDE (https://www.arduino.cc/en/software) e abrir o sketch disponível neste repositório. Lembre-se de fazer a alteração na porta serial para a mesma presente no código python, para haver comunicação entre os sistemas.

Com isso, o sistema está pronto!
