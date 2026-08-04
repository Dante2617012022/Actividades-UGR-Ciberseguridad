#!/usr/bin/env python3
"""Block high-risk files from being added to the public academic repository."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

MAX_FILE_BYTES = 20 * 1024 * 1024

FORBIDDEN_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
    ".kdbx",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".pcap",
    ".pcapng",
    ".har",
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".tgz",
}

FORBIDDEN_NAMES = {
    ".env",
    "id_rsa",
    "id_ed25519",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".js",
    ".ts",
    ".html",
    ".css",
    ".csv",
    ".xml",
    ".sh",
}

SENSITIVE_MARKERS = {
    "-----BEGIN PRIVATE KEY-----": "clave privada",
    "-----BEGIN RSA PRIVATE KEY-----": "clave privada RSA",
    "-----BEGIN OPENSSH PRIVATE KEY-----": "clave privada OpenSSH",
    "zoom.us/rec/share": "enlace de grabación de Zoom",
    "zoom.us/rec/play": "enlace de grabación de Zoom",
}


def git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def changed_paths() -> list[Path]:
    base_sha = os.environ.get("BASE_SHA", "").strip()
    if base_sha and set(base_sha) != {"0"}:
        output = git("diff", "--name-only", "--diff-filter=ACMR", base_sha, "HEAD")
    else:
        output = git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD")

    return [Path(line.strip()) for line in output.splitlines() if line.strip()]


def is_forbidden(path: Path) -> str | None:
    lowered_name = path.name.lower()
    lowered_suffixes = [suffix.lower() for suffix in path.suffixes]

    if lowered_name in FORBIDDEN_NAMES or lowered_name.startswith(("id_rsa.", "id_ed25519.")):
        return "nombre reservado para credenciales o claves"

    if lowered_name.startswith(".env") and lowered_name != ".env.example":
        return "archivo de entorno no publicable"

    if any(suffix in FORBIDDEN_SUFFIXES for suffix in lowered_suffixes):
        return "formato sensible u opaco que requiere revisión manual"

    if lowered_name.endswith((".tar.gz", ".tar.bz2", ".tar.xz")):
        return "archivo comprimido opaco"

    return None


def inspect_text(path: Path) -> list[str]:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return []

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["archivo con extensión de texto pero contenido no UTF-8"]

    findings = []
    for marker, description in SENSITIVE_MARKERS.items():
        if marker.lower() in content.lower():
            findings.append(description)
    return findings


def main() -> int:
    violations: list[str] = []

    for path in changed_paths():
        if not path.exists() or not path.is_file():
            continue

        reason = is_forbidden(path)
        if reason:
            violations.append(f"{path}: {reason}")

        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            violations.append(
                f"{path}: tamaño {size / 1024 / 1024:.1f} MiB supera el máximo de 20 MiB"
            )

        for finding in inspect_text(path):
            violations.append(f"{path}: contiene {finding}")

    if violations:
        print("La compuerta de publicación bloqueó los siguientes elementos:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        print(
            "Conservar el original fuera del repositorio público y publicar una versión sanitizada.",
            file=sys.stderr,
        )
        return 1

    print("Compuerta de publicación aprobada: no se detectaron archivos nuevos de alto riesgo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
