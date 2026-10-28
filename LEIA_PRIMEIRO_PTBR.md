# KeeperRL PT-BR — Projeto integrado para GitHub Actions

Esta pasta contém o código C++ do KeeperRL fornecido pelo usuário, arquivo de tradução e **804 sprites procedurais originais** (`data/images/orig32`).

## Compilar online
1. Crie um repositório GitHub vazio.
2. Envie o **conteúdo** da pasta `keeperrl-ptbr` para a **raiz** do repositório (não envie a pasta externa). O GitHub no navegador limita o upload a 100 arquivos por operação; para centenas de arquivos, use o importador Git ou GitHub web editor em lotes, ou ferramenta Git instalada.
3. Acesse Actions > `Windows x64 - Build PT-BR` > Run workflow.
4. Confira o log. Se terminar com sucesso, baixe o artifact.

## Situação real
- O carregador de sprites foi modificado para ler `data/images/orig32/*.png`.
- O workflow inclui `data/` e `data_free/` no artefato.
- Os sprites são uma **primeira versão procedural**, não artes finais únicas, não há animações completas.
- A compilação **não foi executada** neste ambiente e o jogo **não foi validado em execução**. Erros de dependências/compilação ainda podem ocorrer.
- A tradução depende do arquivo de idioma existente e pode deixar mensagens sem localização.
- O projeto não contém gráficos/músicas proprietários do KeeperRL.

Licenças: consulte COPYING.txt, COPYING-MEDIA.txt e LICENSE.
