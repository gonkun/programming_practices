def test_nginx_is_installed(host):
    assert host.package('nginx').is_installed


def test_nginx_is_running(host):
    assert host.service('nginx').is_running


def test_nginx_listens_on_port_80(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_get_content_from_site(host):
    output = host.check_output('wget -qO- 0.0.0.0:80')
    assert 'Welcome to nginx' in output
