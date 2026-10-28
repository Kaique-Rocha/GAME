# Pipeline visual - KeeperRL PT-BR

Este catálogo foi extraído de `data_free/game_config/tiles.txt` da base fornecida. A categoria é uma estimativa automática: revise manualmente antes de gerar cada sprite.

## Contrato de IDs
- `view_id` é **imutável**; sprites são associados a ele.
- `sprite_alias` é uma referência técnica: nunca traduza.
- Gerar arte original com fundo transparente (preferência inicial: 32 x 32 px por tile), mantendo atlas/escala configuráveis. A resolução é proposta de produção, **não** a resolução já validada pelo motor.
- Atlas deve ser gerado por script, registrando origem, licença, hash, célula e coordenada, sem renomear IDs.
- Não copie nem reutilize os arquivos comerciais da pasta `data` da distribuição oficial.
- Categorização e mapeamento visual devem ser revisados por famílias (criaturas, terrenos, móveis, itens, UI, efeitos).

## Próximos entregáveis de arte
1. Protótipos de 16 tiles de terreno + 8 criaturas + 8 objetos.
2. Atlas PNG com mapa de IDs e testes de renderização.
3. Integração no carregador de texturas e varredura para detectar sprites ausentes.
4. Catálogo completo, animações e variantes.
