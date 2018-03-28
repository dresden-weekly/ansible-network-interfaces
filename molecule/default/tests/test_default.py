def test_dummy_file(host):
    f = host.file("/tmp/dummy")
    assert f.exists
    assert f.is_file
