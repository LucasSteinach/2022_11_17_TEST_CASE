from project_1.main import get_domains, edit_link, domain_check, is_link, get_data, METHODS, execute

domains = ['ru', 'com', 'de', 'info']


def test_get_domains():
    assert get_domains()[1] == 200


def test_edit_link():
    assert edit_link('none', 'foo.com') == 'https://www.foo.com'
    assert edit_link('www', 'www.var.ru') == 'https://www.var.ru'
    assert edit_link('http', 'http://baz.info') == 'https://www.baz.info'
    assert edit_link('full', 'https://www.perfekt.de') == 'https://www.perfekt.de'


def test_domain_check():
    link_true_1 = 'http://baz.info'
    link_false_1 = 'http://foo.in'
    assert domain_check(link_true_1, domains)
    assert not domain_check(link_false_1, domains)


def test_is_link():
    link_true_1 = 'dong.info'
    link_true_2 = 'http://billy.ru'
    link_true_3 = 'http://www.swarm.com'
    link_false_1 = 'http:/foo.com'
    link_false_2 = 'met.in.in'
    link_false_3 = 'www://var.de'

    assert is_link(link_true_1, domains)[0]
    assert is_link(link_true_2, domains)[0]
    assert is_link(link_true_3, domains)[0]
    assert not is_link(link_false_1, domains)[0]
    assert not is_link(link_false_2, domains)[0]
    assert not is_link(link_false_3, domains)[0]


def test_get_data():
    filename = 'tests/strings.txt'
    data = get_data(filename)
    assert str(type(data)) == "<class 'list'>"
    assert data[3] == 'www.mobile.de'


def test_execute():
    filename = 'tests/single_link.txt'
    assert type(execute(filename)) == type(dict())



