from singer import bookmarks
from singer import metadata
from singer import utils
from singer.schema import Schema
from singer.catalog import Catalog, CatalogEntry


def main_impl():
    pass

def main():
    try:
        main_impl()
    except Exception as exc:
        LOGGER.critical(exc)
        raise exc
