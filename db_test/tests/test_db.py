
def test_table(db):
    '''Создание нового навыка в базе данных, проверка его наличия'''
    db.cursor.execute("INSERT INTO skills (title) VALUES ('Linux command line')")
    db.connection.commit()
    db.cursor.execute("SELECT * FROM skills")
    result = db.cursor.fetchall()
    assert result, 'Ошибка: Результат запроса пуст'
