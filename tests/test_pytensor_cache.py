from pytensor.bin.pytensor_cache import remove_extra_caches
from pytensor.link.utils import GENERATED_SRC_DIRNAME


def test_remove_extra_caches(tmp_path):
    for name in ("numba", GENERATED_SRC_DIRNAME, "compiledir_keep"):
        (tmp_path / name).mkdir()
        (tmp_path / name / "file").write_text("x")

    remove_extra_caches(tmp_path)

    assert sorted(p.name for p in tmp_path.iterdir()) == ["compiledir_keep"]

    # A second call, with the directories already gone, is a no-op.
    remove_extra_caches(tmp_path)
