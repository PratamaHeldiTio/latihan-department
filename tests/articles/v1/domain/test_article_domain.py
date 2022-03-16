import pytest

from src.articles.v1.domain.article import Article

def test_from_dict():
    id = 1
    article = Article.from_dict({
        'id': id,
        'title': 'Title blog',
        'content': 'Content blog',
        'created_at': '2018-07-11',
        'created_by': 'system',
        'modified_at': '2018-07-12',
        'modified_by': 'system'
    })

    assert article.id == id
    assert article.title == 'Title blog'
    assert article.content == 'Content blog'
    assert article.created_at == '2018-07-11'
    assert article.created_by == 'system'
    assert article.modified_at == '2018-07-12'
    assert article.modified_by == 'system'
