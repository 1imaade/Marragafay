import glob
import re

for filepath in glob.glob("*/blog/index.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up the old leftover CSS
    content = content.replace(
        "      .story-card-tall__media { aspect-ratio: 16/10; }",
        ""
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
