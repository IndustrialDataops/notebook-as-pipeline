from testbook import testbook


@testbook("notebooks/Sample.ipynb", execute=True)
def test_func(tb):
    func = tb.get("SquareFunc")
    assert func(2) == 4
