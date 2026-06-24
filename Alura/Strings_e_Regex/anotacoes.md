# Strings e Regex

## Strings

### strip()

#### Uso sem argumentos (strip())
Remove apenas espaços em branco, tabs e quebras de linha do início e do fim.

#### strip(chars)

Remove quaisquer caracteres passados no argumento, do início e do fim.
é uma lista posso colocar varios caracteres mas só vai remover do inicio e do fim

### startwich

booleano

texto.startwith("Py")

### endswich

booleano

texto.endswich("on")

### string.replace(old, new, count)


## Regex

### Tabela de caracteres especiais do Regex

| Caractere | Nome / Significado                                 Exemplo   
| --------- | ------------------------------------------------ | --------------------------------- |
| `.`       | Qualquer caractere (exceto quebra de linha `\n`) | `a.c` em `"abc" "axc"` 
| `^`       | Início da string/linha                           | `^ola` em `"ola mundo"` 
| `$`       | Fim da string/linha                              | `fim$` em `"é o fim"` 
| `[]`      | Classe de caracteres (um conjunto)               | `[aeiou]` em `"casa"` 
| `[^ ]`    | Negação (não casa com os que estão no conjunto)  | `[^0-9]`
| `         | `                                                | OU lógico            | `cão | gato`em`"cão", "gato"` |
| `()`      | Grupo / Captura                                  | (ab)+ em "ababab"
|`(?: )`    |Grupo sem captura                                 |(?:ab)+
|`| `       |Escapar caractere especial                        |\. casa "." literal
|`\d`       |Dígito (equiv. [0-9])                             |\d+ em "123abc"
|`\D`       |Não dígito (equiv. [^0-9])                        |\D+ em "abc123"
|`\w`       |Palavra (letra, número ou _)                      |\w+ em "var_123"
|`\W`       |Não palavra (qualquer caractere que não seja \w)  |\W+ em "@#!"
|`\s`       |Espaço em branco (espaço, tab, quebra de linha)   |\s+ em "a b"
|`\S`       |Não espaço em branco                              |\S+ em "abc 123"
|`(?=...)`  |Lookahead positivo (tem que ter depois)           |\d(?=kg) em "5kg"
|`(?!...)`  |Lookahead negativo (não pode ter depois)          |\d(?!kg) em "5g"
|`(?<=...)` |Lookbehind positivo (tem que ter antes)           |(?<=R\$)\d+ em "R$50"
|`(?<!...)` |Lookbehind negativo (não pode ter antes)	       |(?<!R\$)\d+ em "50"

### Classes de caracteres no Regex

| Classe         | Significado                                   |
| -------------- | --------------------------------------------- |
| `[abc]`        | Qualquer um dos caracteres `a`, `b` ou `c`    |
| `[^abc]`       | Qualquer caractere **exceto** `a`, `b` ou `c` |
| `[a-z]`        | Qualquer letra minúscula de `a` até `z`       |
| `[A-Z]`        | Qualquer letra maiúscula                      |
| `[0-9]`        | Qualquer dígito                               |
| `[a-zA-Z]`     | Qualquer letra (maiúscula ou minúscula)       |
| `[A-Za-z0-9_]` | Letras, dígitos ou `_` (igual a `\w`)         |


### Quantificadores no Regex

| Quantificador | Significado                      | Exemplo   | Casa com                          |
| ------------- | -------------------------------- | --------- | --------------------------------- |
| `*`           | **0 ou mais** ocorrências        | `ab*`     | `"a"`, `"ab"`, `"abb"`, `"abbbb"` |
| `+`           | **1 ou mais** ocorrências        | `ab+`     | `"ab"`, `"abb"`, `"abbbb"`        |
| `?`           | **0 ou 1** ocorrência (opcional) | `colou?r` | `"color"`, `"colour"`             |
| `{n}`         | Exatamente **n** vezes           | `a{3}`    | `"aaa"`                           |
| `{n,}`        | **n ou mais** vezes              | `a{2,}`   | `"aa"`, `"aaa"`, `"aaaa..."`      |
| `{n,m}`       | Entre **n e m** vezes            | `a{2,4}`  | `"aa"`, `"aaa"`, `"aaaa"`         |

| Flag                      | Descrição                                                                           
| ------------------------- | ----------------------------------------------------------------------------------- | 
| `re.IGNORECASE` ou `re.I` | Ignora maiúsculas/minúsculas                                                        |
| `re.MULTILINE` ou `re.M`  | Faz `^` e `$` funcionarem em **cada linha**, não só no início/fim da string inteira |
| `re.DOTALL` ou `re.S`     | Faz `.` casar também com **quebras de linha (`\n`)**                                |
| `re.VERBOSE` ou `re.X`    | Permite escrever regex mais **legíveis**, ignorando espaços e comentários           |



### Observações importantes

Para usar literais de caracteres especiais (. ^ $ * + ? { } [ ] ( ) | \), você precisa escapar com `\`

### Métodos

#### re.search(regex, string, flags=0)

quando quiser encontrar o padrão em qualquer lugar.


#### re.match(regex, string, flags=0)

Retorna um objeto Match se o padrão casar com o **início** da string.
Retorna None se não casar.

#### re.findall()

Retorna uma lista com todas as ocorrências encontradas.
Se não encontrar nada, retorna uma lista vazia ([]).

#### re.sub(regex, repl, string, count=0, flags=0)

- regex -> expressão regular que será substituída
- repl → string ou função que irá substituir o padrão.
- string -> texto aonde ocorrerá a substituição
- count (opcional) → número máximo de substituições; 0 significa todas.

Retorna uma nova string com as substituições aplicadas.

#### re.subn

Mesma coisa que sub, mas também retorna o número de substituições
