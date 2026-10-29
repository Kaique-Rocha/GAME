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

# Animacoes originais basicas (spritesheets horizontais) utilizadas pelo motor.
from PIL import ImageDraw
animations = root / "dist" / "keeperrl-ptbr" / "data" / "images" / "animations"
animations.mkdir(parents=True, exist_ok=True)
for name, frames, color in (("death", 8, (198, 65, 88, 220)), ("attack", 3, (255, 196, 95, 225))):
    sheet = Image.new("RGBA", (32 * frames, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(sheet)
    for frame in range(frames):
        center = frame * 32 + 16
        radius = max(2, 3 + (frame * 10 // frames))
        opacity = max(35, color[3] - frame * 20)
        draw.ellipse((center - radius, 16 - radius, center + radius, 16 + radius), outline=(*color[:3], opacity), width=2)
        draw.line((center - radius, 16, center + radius, 16), fill=(*color[:3], opacity), width=2)
    sheet.save(animations / (name + ".png"))
print("Animacoes originais: attack.png (3 quadros), death.png (8 quadros)")
