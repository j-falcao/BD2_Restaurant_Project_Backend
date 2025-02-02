from django.db import connection


def fetch_from_view(view_name, filters=None):
    try:
        query = f"SELECT * FROM {view_name}"
        params = []

        if filters:
            filter_clauses = []
            for column, value in filters.items():
                if value is not None:
                    filter_clauses.append(f"{column} = %s")
                    params.append(value)

            if filter_clauses:
                query += " WHERE " + " AND ".join(filter_clauses)

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results[0] if len(results) == 1 else results

    except Exception as e:
        print(
            f"Ocorreu um erro ao executar fetch_all_from_view({view_name}): {e}")
        return []
