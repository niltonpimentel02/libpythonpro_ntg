from libpythonpro_ntg.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Nilton', email='niltonpimentel02@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Nilton', email='niltonpimentel02@gmail.com'),
        Usuario(nome='Renzo', email='niltonpimentel02@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
