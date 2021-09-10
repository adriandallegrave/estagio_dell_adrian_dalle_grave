import app as main_app


def test_answer():
    x = main_app.Saude()
    assert x.print_start() == "Carregando dados: aguarde..."