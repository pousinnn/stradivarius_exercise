from app import envio_gratis

def test_envio_gratis():
    assert envio_gratis(800) is True
    assert envio_gratis(100) is False
