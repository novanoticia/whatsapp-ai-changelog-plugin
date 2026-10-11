import hashlib
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = 'skills/whatsapp-ai-changelog/SKILL.md'
I18N = 'skills/whatsapp-ai-changelog/references/i18n'
LANGUAGES = {
    'en': {
        'notice': 'Translation machine-generated, not human-reviewed.',
        'failsafe': 'English version unavailable; continuing with the Spanish files.',
        'ai': 'AI-assisted; requires human review.',
    },
    'fr': {
        'notice': 'Traduction automatique, non relue par un humain.',
        'failsafe': 'Version française indisponible ; poursuite avec les fichiers espagnols.',
        'ai': 'Élaboré avec l’assistance de l’IA ; relecture humaine requise.',
    },
    'zh': {
        'notice': '机器翻译，未经人工审核。',
        'failsafe': '中文版本不可用；继续使用西班牙语文件。',
        'ai': '由 AI 辅助编写；需要人工审核。',
    },
}
TRANSLATIONS = {}
for code in LANGUAGES:
    TRANSLATIONS[f'{I18N}/{code}.md'] = SKILL
    TRANSLATIONS[f'README.{code}.md'] = 'README.md'
    TRANSLATIONS[f'PRIVACY.{code}.md'] = 'PRIVACY.md'
    TRANSLATIONS[f'CHANGELOG.{code}.md'] = 'CHANGELOG.md'
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

    def test_machine_contracts_are_kept_in_equivalences(self):
        for code in LANGUAGES:
            text = read(f'{I18N}/{code}.md')
            for token in ('/whatsapp-ai-changelog', 'idioma=', '[NOTA]', 'REPLY_NEEDED', 'REVIEW',
                          'READING_LATER', 'ARCHIVE', '🔴', '🟡', '🔵', '⚪'):
                self.assertIn(token, read(SKILL), token)
                self.assertIn(token, text, f'{code}: {token}')

    def test_equivalences_list_all_available_languages(self):
        for code in LANGUAGES:
            text = read(f'{I18N}/{code}.md')
            for available in ('`es`', '`en`', '`fr`', '`zh`'):
                self.assertIn(available, text, f'{code}: {available}')

    def test_ai_notice_in_public_translated_documents(self):
        for code, texts in LANGUAGES.items():
            for name in (f'README.{code}.md', f'PRIVACY.{code}.md', f'CHANGELOG.{code}.md'):
                self.assertIn(texts['ai'], read(name), name)
        self.assertNotIn('AI-assisted', read('PRIVACY.md'))

    def test_local_links_in_translated_documents_exist(self):
        for code in LANGUAGES:
            for name in (f'README.{code}.md', f'PRIVACY.{code}.md', f'CHANGELOG.{code}.md'):
                for target in re.findall(r'\]\(([^)#:]+)\)', read(name)):
                    self.assertTrue((ROOT / target).exists(), f'{name}: {target}')

    def test_translated_documents_keep_versions_and_code_blocks(self):
        version = re.search(r'^# WhatsApp AI Changelog (v[\d.]+)$', read('README.md'), re.M).group(1)
        for code in LANGUAGES:
            text = read(f'README.{code}.md')
            self.assertIn(f'# WhatsApp AI Changelog {version}', text)
            self.assertEqual(text.count('```'), read('README.md').count('```'), code)
            self.assertIn('/plugin marketplace add novanoticia/whatsapp-ai-changelog-plugin', text)
            self.assertIn(f'mistral-{version[1:]}.zip', text)
            self.assertIn(f'perplexity-{version[1:]}.zip', text)


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
        for phrase in ('mensaje WhatsApp sobre esta herramienta de IA', 'WhatsApp message about this AI tool',
                       'message WhatsApp sur cet outil d’IA', '关于这个AI工具的WhatsApp消息'):
            self.assertIn(phrase, description)
        self.assertIn('/whatsapp-ai-changelog [URL]', description)

    def test_selection_rule_is_keyed_and_has_fail_safe(self):
        text = read(SKILL)
        block = text.split(MARKERS[0])[1].split(MARKERS[1])[0]
        flat = ' '.join(block.split())
        self.assertIn('`idioma=xx`', block)
        self.assertNotIn('lang=', block)
        for code, texts in LANGUAGES.items():
            self.assertIn(texts['notice'], flat, code)
            self.assertIn(texts['failsafe'], flat, code)
            self.assertIn(f'`{code}`', block, code)
        self.assertLessEqual(len(block.encode()), 3500)
        self.assertEqual(text.count('## Integración de este plugin'), 1)

    def test_traditional_chinese_is_not_served_as_simplified(self):
        block = read(SKILL).split(MARKERS[0])[1].split(MARKERS[1])[0]
        for tag in ('zh-Hant', 'zh-TW', 'zh-HK'):
            self.assertIn(tag, block)
        self.assertIn('no está disponible', block)

    def test_fail_safe_answers_in_spanish(self):
        block = ' '.join(read(SKILL).split(MARKERS[0])[1].split(MARKERS[1])[0].split())
        self.assertIn('responde en español, sin aviso de traducción', block)


class PackageTests(unittest.TestCase):
    def test_single_skill_packages_include_equivalences(self):
        with tempfile.TemporaryDirectory() as directory:
            skill, archives = MODULE.build(ROOT, Path(directory) / 'output')
            for code in LANGUAGES:
                expected = (ROOT / f'{I18N}/{code}.md').read_bytes()
                self.assertEqual((skill / f'references/i18n/{code}.md').read_bytes(), expected)
                for platform, archive in archives.items():
                    prefix = 'whatsapp-ai-changelog/' if platform == 'mistral' else ''
                    with zipfile.ZipFile(archive) as packaged:
                        self.assertEqual(packaged.read(f'{prefix}references/i18n/{code}.md'), expected)
            self.assertIn('idioma=xx', (skill / 'SKILL.md').read_text(encoding='utf-8'))
            self.assertLessEqual(len(MODULE.DESCRIPTION.encode()), 490)


if __name__ == '__main__':
    unittest.main()
