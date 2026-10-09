import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('package_skills', ROOT / 'scripts/package_skills.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PackageSkillsTests(unittest.TestCase):
    def test_single_skill_with_complete_internal_evaluation(self):
        with tempfile.TemporaryDirectory() as directory:
            skill, archives = MODULE.build(ROOT, Path(directory) / 'output')
            text = (skill / 'SKILL.md').read_text()
            self.assertNotIn('../bayesian-compose/', text)
            self.assertNotIn('debe estar instalada', text)
            self.assertNotIn('Requiere el skill bayesian-compose', text)
            self.assertIn('/releases/latest', text)
            self.assertIn('ni el README ni las', text)
            self.assertIn('language: es', text)
            self.assertLessEqual(len(MODULE.DESCRIPTION.encode()), 490)
            catalogue = 'references/criterios-30-emision.md'
            self.assertEqual((skill / catalogue).read_bytes(),
                             (ROOT / 'skills/bayesian-compose' / catalogue).read_bytes())
            protocol = (skill / 'references/protocolo-bayesian-compose.md').read_text()
            self.assertIn('score_final = Σ', protocol)
            self.assertIn('## PASO 6', protocol)
            self.assertNotIn('~/', protocol)
            self.assertNotIn('## PASO 7', protocol)
            for platform, archive in archives.items():
                prefix = 'whatsapp-ai-changelog/' if platform == 'mistral' else ''
                with zipfile.ZipFile(archive) as packaged:
                    self.assertIsNone(packaged.testzip())
                    names = packaged.namelist()
                    self.assertEqual(names.count(prefix + 'SKILL.md'), 1)
                    self.assertEqual(sum(name.rsplit('/', 1)[-1] == 'SKILL.md' for name in names), 1)
                    self.assertFalse(any('plugin.json' in name or name.endswith('.py') for name in names))
                    self.assertLess(archive.stat().st_size, 10 * 1024 * 1024)
                    for name in names:
                        relative = name.removeprefix(prefix)
                        self.assertEqual(packaged.read(name), (skill / relative).read_bytes())

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            sentinel = output / 'personal.txt'
            sentinel.write_text('datos del usuario')
            with self.assertRaises(ValueError):
                MODULE.build(ROOT, output)
            self.assertEqual(sentinel.read_text(), 'datos del usuario')
            self.assertEqual(list(output.iterdir()), [sentinel])

    def test_changed_source_fails_before_writing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source'
            shutil.copytree(ROOT / 'skills', source / 'skills')
            primary = source / 'skills/whatsapp-ai-changelog/SKILL.md'
            primary.write_text(primary.read_text().replace('**Dependencia obligatoria**', '**Dependencia renombrada**'))
            output = Path(directory) / 'output'
            with self.assertRaises(ValueError):
                MODULE.build(source, output)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
