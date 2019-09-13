import psycopg2

def insert_noticias(noticias):
    for noticia in noticias:
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="db_noticias")
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO noticias (titulo, descricao, conteudo, created_at, path_image) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (str(noticia.titulo), str(noticia.descricao), str(noticia.conteudo), str(noticia.data), str(noticia.url_image))
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")
        except (Exception, psycopg2.Error) as error:
            if (connection):
                print("Failed to insert record into mobile table", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
