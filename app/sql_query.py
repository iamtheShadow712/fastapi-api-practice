SQL_QUERY = {
    "GET_ALL_POSTS": """SELECT * FROM posts""",
    "CREATE_POST": """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    "GET_POST_BY_ID": """SELECT * FROM posts WHERE posts.id = %s """,
    "DELETE_POST_BY_ID": """DELETE FROM posts WHERE posts.id = %s RETURNING * """,
    "UPDATE_POST_BY_ID": """UPDATE posts SET title = %s, content = %s, published = %s WHERE posts.id = %s RETURNING * """
}