from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_movie(mid)

    def get_all(self, filters):
        if filters.get('director_id') is not None:
            movie = self.dao.get_by_did(filters.get('director_id'))
        elif filters.get('genre_id') is not None:
            movie = self.dao.get_by_gid(filters.get('genre_id'))
        elif filters.get('year') is not None:
            movie = self.dao.get_by_year(filters.get('year'))
        elif filters.get('status') is not None and filters['status'] == 'new':
            movie = self.dao.get_status()
        else:
            movie = self.dao.get_all()
        if filters.get('page') is not None:
            return movie.limit(12).offset((int(filters.get('page'))-1)*12).all()
        return movie

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        return self.dao.delete_movie(mid)

    def update(self, data):
        movie = self.get_one(data['id'])
        if data.get('title') is not None:
            movie.title = data.get('title')
        if data.get('description') is not None:
            movie.description = data.get('description')
        if data.get('trailer') is not None:
            movie.trailer = data.get('trailer')
        if data.get('year') is not None:
            movie.year = data.get('year')
        if data.get('rating') is not None:
            movie.rating = data.get('rating')
        if data.get('genre_id') is not None:
            movie.genre_id = data.get('genre_id')
        if data.get('director_id') is not None:
            movie.director_id = data.get('director_id')
        return self.dao.update_movie(data)
