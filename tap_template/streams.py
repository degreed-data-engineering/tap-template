"""Stream type classes for tap-template."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_template.client import templateStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

#       - Copy-paste as many times as needed to create multiple stream types.


# https://jsonpath.com 
class OrgStream(templateStream):
    """Define custom stream."""
    name = "orgs"
    path = "/api/v2/organizations.json"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("id", th.NumberType),
        th.Property("name", th.StringType),
    ).to_dict()


# https://jsonpath.com 
# class OrgStream(templateStream):
#     """Define custom stream."""
#     name = "orgs"
#     path = "/api/v2/organizations.json"
#     primary_keys = ["id"]
#     replication_key = None
#     # Optionally, you may also use `schema_filepath` in place of `schema`:
#     # schema_filepath = SCHEMAS_DIR / "users.json"
#     schema = th.PropertiesList(
#         th.Property("id", th.NumberType),
#         th.Property(
#             "id",
#             th.StringType,
#             description="The user's system ID"
#         ),
#         th.Property(
#             "age",
#             th.IntegerType,
#             description="The user's age in years"
#         ),
#         th.Property(
#             "email",
#             th.StringType,
#             description="The user's email address"
#         ),
#         th.Property("street", th.StringType),
#         th.Property("city", th.StringType),
#         th.Property(
#             "state",
#             th.StringType,
#             description="State name in ISO 3166-2 format"
#         ),
#         th.Property("zip", th.StringType),
#     ).to_dict()