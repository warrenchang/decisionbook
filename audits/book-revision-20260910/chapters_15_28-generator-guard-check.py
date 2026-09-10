"""Exercise the canonical-SVG guard in a temporary directory only."""
from pathlib import Path
import contextlib
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts/build_new_chapter_figures.py'
spec = importlib.util.spec_from_file_location('book_figure_builder', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
changed = subprocess.check_output(
    ['git', 'diff', '--name-only', '--', 'figures'], cwd=ROOT, text=True
).splitlines()
changed_outputs = {
    Path(path).stem for path in changed
    if path.endswith('.svg') and Path(path).stem in module.FIGURE_BUILDERS
}
assert changed_outputs <= module.HAND_MAINTAINED_SVGS, changed_outputs
module.validate_canonical_svgs(ROOT / 'figures')

with tempfile.TemporaryDirectory(prefix='book-svg-guard-') as temporary:
    temp_root = Path(temporary)
    figures = temp_root / 'figures'
    figures.mkdir()
    payload = '<svg xmlns="http://www.w3.org/2000/svg"><title>Reviewed source</title></svg>'
    for stem in module.HAND_MAINTAINED_SVGS:
        (figures / f'{stem}.svg').write_text(payload)
    module.validate_canonical_svgs(figures)

    def stale_builder():
        raise AssertionError('A protected historical builder must never execute')

    protected = sorted(module.HAND_MAINTAINED_SVGS)[0]
    protected_path = figures / f'{protected}.svg'
    before = hashlib.sha256(protected_path.read_bytes()).hexdigest()
    assert module.write_svg(protected, stale_builder, figures) == protected_path
    assert hashlib.sha256(protected_path.read_bytes()).hexdigest() == before
    unprotected = module.write_svg('temporary-generated-fixture', lambda: '<svg/>', figures)
    assert unprotected.read_text() == '<svg/>'

    protected_path.unlink()
    try:
        module.write_svg(protected, stale_builder, figures)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('A missing protected source must raise')

    # The CLI entry point must fail preflight before writing any other output.
    module.ROOT = temp_root
    module.FIGURES = figures
    module.FIGURE_BUILDERS = {'must-not-be-written': lambda: '<svg/>'}
    old_argv = sys.argv
    sys.argv = [str(SCRIPT)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                module.main()
            except FileNotFoundError:
                pass
            else:
                raise AssertionError('CLI preflight should reject the missing SVG')
    finally:
        sys.argv = old_argv
    assert not (figures / 'must-not-be-written.svg').exists()

result = {
    'status': 'pass',
    'changed_generator_outputs_protected': sorted(changed_outputs),
    'protected_builder_never_called': True,
    'canonical_bytes_unchanged': True,
    'missing_canonical_source_raises': True,
    'cli_preflight_prevents_partial_generation': True,
    'unprotected_temporary_output_generated': True,
    'repository_figures_written': False,
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
