def test_network_interfaces_path(host):
    f = host.file("/etc/network/interfaces.d")
    assert f.exists
    assert f.is_directory
