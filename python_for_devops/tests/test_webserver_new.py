def test_nginx_is_installed(host):
    assert host.package('nginx').is_installed


def test_nginx_listens_on_port_80(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening


def test_nginx_is_running_systemd(host):
    assert host.service('nginx').is_running
    assert host.service('nginx').is_valid
