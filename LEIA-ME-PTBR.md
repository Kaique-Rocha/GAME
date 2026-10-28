# KeeperRL — código-fonte com tradução PT-BR

Esta distribuição contém o código-fonte enviado pelo usuário (snapshot de 27/10/2025), acrescido de `data_free/game_config/translations/portugues.txt`.

## Idioma

Na versão moderna, o idioma é carregado automaticamente dos arquivos em `data_free/game_config/translations`. O nome do arquivo `portugues.txt` é exibido como **Portugues** no seletor de idioma em Configurações.

## Compilação

Este é o CÓDIGO-FONTE, não um jogo executável. Consulte `README.md`, `CMakeLists.txt` e `Makefile-win` para dependências e instruções de compilação. No Windows, é necessário configurar uma toolchain e bibliotecas.

O arquivo `data_free` usa licença Creative Commons BY-SA 2.0 e o código-fonte tem suas próprias licenças descritas nos arquivos `COPYING*` e `LICENSE`. Os recursos comerciais em `data` não estão incluídos.

## Verificação realizada

Todas as chaves presentes no `english.txt` possuem entrada no arquivo PT-BR, e os placeholders numerados foram comparados. Não foi realizada compilação e teste de execução do jogo; traduções de mensagens produzidas fora do sistema de idiomas não estão garantidas.

## Segurança

Não modifique valores identificadores em `game_config` para traduzir nomes técnicos; utilize o arquivo de idiomas.
