from __future__ import annotations

from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "submission"
OUTPUT = ROOT / "submission.zip"

REQUIRED = {
    "agent.yaml",
    "eval_config.yaml",
    "configs/sampling.yaml",
    "configs/critic_sampling.yaml",
    "prompts/system.md",
    "prompts/critic.md",
    "sub_agents/patch_critic.yaml",
    "skills/deep-localization/SKILL.md",
    "skills/hard-debug/SKILL.md",
}


def collect_files() -> list[Path]:
    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    relative = {path.relative_to(SOURCE).as_posix() for path in files}
    missing = REQUIRED - relative
    if missing:
        raise RuntimeError(f"missing required files: {sorted(missing)}")

    for path in files:
        if path.is_symlink():
            raise RuntimeError(f"refusing symlink: {path}")

    return files


def main() -> None:
    files = collect_files()

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(SOURCE).as_posix())

    size = OUTPUT.stat().st_size
    print(f"wrote {OUTPUT.name}: {size:,} bytes")
    for path in files:
        print(path.relative_to(SOURCE).as_posix())


if __name__ == "__main__":
    main()
