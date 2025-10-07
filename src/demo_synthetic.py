
#src/demo_synthetic.py

from pathlib import Path
import random
import pandas as pd
from PIL import Image, ImageDraw


#Path data folder (mkdir=make directory (a new folder))
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

#Path artifacts folder (mkdir=make directory (a new folder))
ART = Path("artifacts")
ART.mkdir(parents=True, exist_ok=True)


#Step 1: make fake team data
teams = ["FCB", "BVB", "RBL", "B04", "SGE", "VFB"] 
gw = 1
rows = []

for t in teams:
    lam_for = round(random.uniform(0.8, 2.5), 2)
    lam_against = round(random.uniform(0.5, 2.0), 2)
    rows.append({
        "gw": gw, 
        "teams_code": t,
        "lambda_for":lam_for,
        "lambda_against":lam_against
    })

df = pd.DataFrame(rows)
df.to_csv(OUT / "ratings_weekly.csv", index=False)
print("✅ Wrote data/processed/ratings_weekly.csv")


#Step 2: make fake poster
img = Image.new("RGB", (800, 600), (24, 24, 32))
draw = ImageDraw.Draw(img)
draw.text((40, 40), "BUNDESLIGA PREVIEW (FAKE)", fill=(255, 255, 255))


#save inside artifacts/ safely
out_path = ART / "demo_poster.png"
img.save(out_path)
print(f"✅ Wrote {out_path.as_posix()}")