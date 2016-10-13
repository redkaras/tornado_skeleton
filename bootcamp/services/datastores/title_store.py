from bootcamp.lib.database import get_db_session
from bootcamp.models.title import Title

from tornado.gen import coroutine


class TitleStore(object):

    @coroutine
    def get_titles(self):
        query = Title.query()
        return query.all()

    @coroutine
    def get_title(self, uuid):
        query = Title.query().filter(Title.uuid == uuid)
        return query.first()

    @coroutine
    def get_title_by_id(self, title_id):
        query = Title.query().filter(Title.title_id == title_id)
        return query.first()

    @coroutine
    def create_from_entity(self, title):
        new_title = Title(
            uuid=title.uuid,
            created_at=title.created_at,
            updated_at=title.updated_at,
            title_id=title.title_id,
            title=title.title,
            video_path=title.video_path,
            file_names=title.file_names,
            description=title.description,
            video_size=title.video_size,
            rate=title.rate,
        )
        new_title.validate()
        new_title.persist()
        get_db_session().commit()
        return new_title
