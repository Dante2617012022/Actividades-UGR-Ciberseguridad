from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_publication.py"
SPEC = importlib.util.spec_from_file_location("check_publication", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("No se pudo cargar la compuerta de publicación")

publication = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publication)


class PublicationGuardTests(unittest.TestCase):
    def test_rejects_environment_and_private_key_files(self) -> None:
        self.assertIsNotNone(publication.is_forbidden(Path(".env")))
        self.assertIsNotNone(publication.is_forbidden(Path("evidence/private-key.pfx")))
        self.assertIsNotNone(publication.is_forbidden(Path("id_ed25519")))

    def test_rejects_opaque_archives_and_network_captures(self) -> None:
        self.assertIsNotNone(publication.is_forbidden(Path("entrega.zip")))
        self.assertIsNotNone(publication.is_forbidden(Path("captura.pcapng")))
        self.assertIsNotNone(publication.is_forbidden(Path("evidencia.tar.gz")))

    def test_allows_curated_text_and_pdf_paths(self) -> None:
        self.assertIsNone(publication.is_forbidden(Path("README.md")))
        self.assertIsNone(publication.is_forbidden(Path("case-studies/resumen.pdf")))
        self.assertIsNone(publication.is_forbidden(Path(".env.example")))

    def test_detects_private_key_markers_in_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "evidence.md"
            sample.write_text("-----BEGIN OPENSSH PRIVATE KEY-----\n", encoding="utf-8")
            self.assertIn("clave privada OpenSSH", publication.inspect_text(sample))

    def test_detects_private_recording_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "notes.txt"
            sample.write_text("https://example.zoom.us/rec/share/example", encoding="utf-8")
            self.assertIn("enlace de grabación de Zoom", publication.inspect_text(sample))


if __name__ == "__main__":
    unittest.main()
