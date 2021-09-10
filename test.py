import app


def test_answer_one():
    try:
        x = app.Saude('1', 'sao joao da urtiga')
        y = x.teste
    except SystemExit:
        pass
    finally:
        x = app.Saude('1', 'sao joao da urtiga')
        y = x.teste

    assert y
