
def test_table(db):
    '''Создание нового навыка в базе данных, проверка его наличия'''
    db.execute("INSERT INTO skills (title) VALUES ('Linux command line')")
    db.connection.commit()
    db.execute("SELECT * FROM skills")
    result = db.fetchall()
    assert result, 'Ошибка: Результат запроса пуст'
