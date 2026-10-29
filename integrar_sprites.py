"""Extrai atlas de arte original para o formato orig32 esperado pelo TileSet do KeeperRL.
Nao altera IDs nem distribui recursos comerciais.
"""
import csv
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent
source = root / "art_pipeline"
output = root / "dist" / "keeperrl-ptbr" / "data" / "orig32"
output.mkdir(parents=True, exist_ok=True)
atlases = {}
total = 0
with (source / "mapa_sprites.csv").open(encoding="utf-8-sig", newline="") as file:
    for sprite in csv.DictReader(file):
        name = sprite["id"]
        atlas_path = source / sprite["atlas"]
        if atlas_path not in atlases:
            atlases[atlas_path] = Image.open(atlas_path).convert("RGBA")
        image = atlases[atlas_path]
        x, y, w, h = (int(sprite[k]) for k in ("x", "y", "w", "h"))
        if (w, h) != (32, 32):
            raise ValueError(f"Sprite {name}: tamanho inesperado {w}x{h}")
        if x < 0 or y < 0 or x + w > image.width or y + h > image.height:
            raise ValueError(f"Sprite {name}: fora dos limites do atlas")
        if "/" in name or "\\" in name or name in (".", ".."):
            raise ValueError(f"Sprite id invalido: {name}")
        image.crop((x, y, x + w, y + h)).save(output / f"{name}.png")
        total += 1
print(f"Sprites integrados no carregador orig32: {total}")
if total != 804:
    raise RuntimeError(f"Esperados 804 sprites, encontrados {total}")
