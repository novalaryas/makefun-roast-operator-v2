from pathlib import Path

src = Path(__file__).with_name("entry.txt")
out = Path("/output") / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(src.read_bytes())
