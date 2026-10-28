# KeeperRL PT-BR — arquitetura e compilação

## Estado da entrega
Código-base recebido com tradução PT-BR, inventário de **804 IDs gráficos únicos** e workflow de build Windows. **Nenhuma compilação ou execução Windows foi validada nesta entrega.** O workflow é experimental e pode exigir ajustes de dependências/código.

## Arquitetura definitiva
- `*.cpp` e `*.h`: motor do KeeperRL e regras de jogo.
- `data_free/game_config`: definições e identificadores; manter IDs em inglês.
- `data_free/game_config/translations/portugues.txt`: localização PT-BR.
- `data_free/game_config/tiles.txt`: catálogo de ViewIds usado pelo motor.
- `data_free/images`: recursos livres de interface existentes.
- `art_pipeline/inventario_sprites.csv`: inventário inicial e fila de substituição dos gráficos.
- `.github/workflows/build-windows.yml`: compilação automática pelo GitHub Actions.

## Compilar sem instalar nada
1. Crie um repositório GitHub **público** para facilitar conformidade com GPL e configuração inicial.
2. Envie o **conteúdo** desta pasta `keeperrl-master` para a raiz do repositório (não a pasta externa). Para centenas de arquivos, o método mais prático é o GitHub Web Editor ou upload via navegador com limites de arquivos; alternativamente use um Codespace no navegador e descompacte lá.
3. Em `Actions`, selecione `Windows x64 - Build PT-BR` e `Run workflow`.
4. Confira logs. Só haverá artefato para baixar se o build passar.
5. Não considere uma compilação bem-sucedida um teste de jogo: valide inicialização, menus, combate e carregamento de gráficos.

## Recursos e licenças
- Código: GPL-2.0 (vide LICENSE/COPYING.txt).
- `data_free`: CC BY-SA 2.0, segundo COPYING-MEDIA.txt.
- Diretório comercial `data`: não incluir na distribuição do projeto.
- Os recursos originais de sprites do jogo **ainda não foram substituídos**: o inventário é o primeiro artefato de produção gráfica.

## Inventário por categoria preliminar
- Criaturas, personagens ou outros: 549
- Terreno e ambiente: 120
- Itens e equipamento: 63
- Construcoes e mobiliario: 52
- Interface e efeitos: 20

## Qualidade antes de liberar
- Conferir todos os IDs e aliases após qualquer mudança em `tiles.txt`.
- Não traduzir identificadores internos.
- Conferir cobertura de chaves e placeholders de `portugues.txt`.
- Gerar/validar atlas e carregamento, realizar gameplay básico.
