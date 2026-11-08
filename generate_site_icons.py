from pathlib import Path
from PIL import Image, ImageOps

src = Path("images/fmd.jpg")
out = Path("images")

if not src.exists():
    raise FileNotFoundError(f"Missing image: {src}. Put fmd.jpg in the images folder first.")

img = Image.open(src).convert("RGB")

# Keep main site profile aligned with selected photo too
profile = ImageOps.fit(img, (512, 512), method=Image.Resampling.LANCZOS)
profile.save(out / "profile.png", optimize=True)
profile.save(out / "profile-square.png", optimize=True)

# Build a square version for icon generation
square = ImageOps.fit(img, (512, 512), method=Image.Resampling.LANCZOS)

# Standard favicon sizes used by the template
sizes = [16, 32, 96]
for size in sizes:
    resized = square.resize((size, size), Image.Resampling.LANCZOS)
    if size == 16:
        resized.save(out / "favicon-16x16.png", optimize=True)
    elif size == 32:
        resized.save(out / "favicon-32x32.png", optimize=True)
    else:
        resized.save(out / "favicon-96x96.png", optimize=True)

# Android Chrome icons
for size in [36, 48, 72, 96, 144, 192, 256, 384, 512]:
    square.resize((size, size), Image.Resampling.LANCZOS).save(
        out / f"android-chrome-{size}x{size}.png", optimize=True
    )

# Apple touch icons
for size in [57, 60, 72, 76, 114, 120, 144, 152, 180]:
    square.resize((size, size), Image.Resampling.LANCZOS).save(
        out / f"apple-touch-icon-{size}x{size}.png", optimize=True
    )
square.resize((180, 180), Image.Resampling.LANCZOS).save(out / "apple-touch-icon.png", optimize=True)

# Windows tile icons
for size in [70, 150, 310]:
    square.resize((size, size), Image.Resampling.LANCZOS).save(
        out / f"mstile-{size}x{size}.png", optimize=True
    )
# wide tile
ImageOps.fit(img, (310, 150), method=Image.Resampling.LANCZOS).save(
    out / "mstile-310x150.png", optimize=True
)
# 310 square
square.resize((310, 310), Image.Resampling.LANCZOS).save(
    out / "mstile-310x310.png", optimize=True
)
square.resize((144, 144), Image.Resampling.LANCZOS).save(
    out / "mstile-144x144.png", optimize=True
)

# favicon.ico (best effort; some browsers prefer PNG favicon anyway)
sizes_ico = [(16, 16), (32, 32), (48, 48)]
img_ico = Image.open(src).convert("RGBA")
out_ico = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
# center crop
icon = ImageOps.fit(img_ico, (48, 48), method=Image.Resampling.LANCZOS)
out_ico.paste(icon, (0, 0))
out_ico.save(out / "favicon.ico")

print("Generated site icons from images/fmd.jpg")
