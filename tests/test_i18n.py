import hashlib
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = 'skills/whatsapp-ai-changelog/SKILL.md'
EN = 'skills/whatsapp-ai-changelog/references/i18n/en.md'
TRANSLATIONS = {
    EN: SKILL,
    'README.en.md': 'README.md',
    'PRIVACY.en.md': 'PRIVACY.md',
    'CHANGELOG.en.md': 'CHANGELOG.md',
}
SPEC = importlib.util.spec_from_file_location('package_skills', ROOT / 'scripts/package_skills.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
MARKERS = ('<!-- i18n:inicio -->', '<!-- i18n:fin -->')


def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')


class TranslationTests(unittest.TestCase):
    def test_translations_declare_status_and_current_source(self):
        for translation, source in TRANSLATIONS.items():
            header = read(translation).splitlines()[0]
            found = re.fullmatch(r'<!-- i18n fuente-sha256=([0-9a-f]{12}) estado=borrador-ia -->', header)
            self.assertIsNotNone(found, translation)
            digest = hashlib.sha256((ROOT / source).read_bytes()).hexdigest()[:12]
            self.assertEqual(found.group(1), digest, f'{translation} is stale: update it from {source}')

    def test_machine_contracts_are_kept_in_english_equivalences(self):
        text = read(EN)
        for token in ('/whatsapp-ai-changelog', 'idioma=', '[NOTA]', 'REPLY_NEEDED', 'REVIEW',
                      'READING_LATER', 'ARCHIVE', '🔴', '🟡', '🔵', '⚪'):
            self.assertIn(token, read(SKILL), token)
            self.assertIn(token, text, token)

    def test_ai_notice_in_public_english_documents(self):
        for translation in ('README.en.md', 'PRIVACY.en.md', 'CHANGELOG.en.md'):
            self.assertIn('AI-assisted; requires human review.', read(translation))
        self.assertNotIn('AI-assisted', read('PRIVACY.md'))

    def test_local_links_in_english_documents_exist(self):
        for translation in ('README.en.md', 'PRIVACY.en.md', 'CHANGELOG.en.md'):
            for target in re.findall(r'\]\(([^)#:]+)\)', read(translation)):
                self.assertTrue((ROOT / target).exists(), f'{translation}: {target}')


class LanguageBlockTests(unittest.TestCase):
    def test_markers_balanced_and_outside_frontmatter(self):
        for relative in (SKILL, 'README.md', 'CHANGELOG.md'):
            lines = read(relative).splitlines()
            starts = [i for i, line in enumerate(lines) if line == MARKERS[0]]
            ends = [i for i, line in enumerate(lines) if line == MARKERS[1]]
            self.assertEqual(len(starts), 1, relative)
            self.assertEqual(len(ends), 1, relative)
            self.assertLess(starts[0], ends[0], relative)
            if lines[0] == '---':
                self.assertGreater(starts[0], lines.index('---', 1), relative)

    def test_description_limit_and_english_trigger(self):
        text = read(SKILL)
        description = re.search(r'^description: "(.*)"$', text, re.M).group(1)
        self.assertLess(len(description), 500)
        self.assertIn('WhatsApp message about this AI tool', description)
        self.assertIn('/whatsapp-ai-changelog [URL]', description)

    def test_selection_rule_is_keyed_and_has_fail_safe(self):
        text = read(SKILL)
        block = text.split(MARKERS[0])[1].split(MARKERS[1])[0]
        flat = ' '.join(block.split())
        self.assertIn('`idioma=xx`', block)
        self.assertNotIn('lang=', block)
        self.assertIn('Translation machine-generated, not human-reviewed.', flat)
        self.assertIn('English version unavailable; continuing with the Spanish files.', flat)
        self.assertLessEqual(len(block.encode()), 3000)
        self.assertEqual(text.count('## Integración de este plugin'), 1)


class PackageTests(unittest.TestCase):
    def test_single_skill_packages_include_english_equivalences(self):
        with tempfile.TemporaryDirectory() as directory:
            skill, archives = MODULE.build(ROOT, Path(directory) / 'output')
            expected = (ROOT / EN).read_bytes()
            self.assertEqual((skill / 'references/i18n/en.md').read_bytes(), expected)
            for platform, archive in archives.items():
                prefix = 'whatsapp-ai-changelog/' if platform == 'mistral' else ''
                with zipfile.ZipFile(archive) as packaged:
                    self.assertEqual(packaged.read(prefix + 'references/i18n/en.md'), expected)
            self.assertIn('idioma=xx', (skill / 'SKILL.md').read_text(encoding='utf-8'))
            self.assertLessEqual(len(MODULE.DESCRIPTION.encode()), 490)


if __name__ == '__main__':
    unittest.main()
