def test_analyze_ioc():
    mocked_create_table = mocker.patch("ioc_lover.check.ioc_crawler.create_tables")
    analyze_ioc()
    mocked_create_table.assert_called_once()
    test_dict = {
        "data": ["bla", "bla"]
    }
    assert analyze_ioc == test_dict