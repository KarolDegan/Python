# Shebang

Em ambientes Linux é muito importante definir o comentário especial Shebang, nele especificamos qual interpretador será usado para executar o programa

`#!/usr/bin/env python3`

print("Hello, World!")
A primeira linha informa o terminal que aquele programa roda com o Python3 da env em execução, esta forma é possivel omitir o interpretador e executar o script diretamente pelo seu nome.

## primeiro damos parmissão de execução ao script

chmod +x hello.py
Agora podemos executar de 2 formas

## especificando o interpretador na linha de comando

python3 hello.py

## usando o interpretador especificado na linha `#!/usr/bin/env python`

./hello.py
A vantagem da segunda forma é que podemos mudar a extensão de .py para .exe por exemplo, ou podemos até remover a extensão e executar ./hello
