# Media foundation tooling

`media_tool.py` is a dependency-free, read-only audit tool. It never moves, renames, deletes, rewrites, compresses, or generates image files.

Run it from the project root or pass `--project-root` explicitly:

```bash
python3 scripts/media/media_tool.py inventory
python3 scripts/media/media_tool.py duplicates
python3 scripts/media/media_tool.py verify-types
python3 scripts/media/media_tool.py missing-references
python3 scripts/media/media_tool.py validate-manifest
```

To inspect a new external batch before importing it, repeat `--scan-root` as needed:

```bash
python3 scripts/media/media_tool.py inventory \
  --scan-root /home/imaade/Projects/Marragafay/Marragafay-media-source/inbox/<batch-id>/raw

python3 scripts/media/media_tool.py duplicates \
  --scan-root /home/imaade/Projects/Marragafay/Marragafay.com \
  --scan-root /home/imaade/Projects/Marragafay/Marragafay-media-source/inbox/<batch-id>/raw
```

Add `--json` to the inventory, duplicate, type, reference, or manifest command when a machine-readable report is useful. Existing audit findings are reported without changing the site; manifest validation returns a failing exit status when its entries are invalid or point to missing canonical files.
