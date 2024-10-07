from typing import TypedDict, List, Optional

class DateValue(TypedDict):
    value: int

class SourceOrcid(TypedDict):
    uri: str
    path: str
    host: str

class Source(TypedDict):
    source_orcid: SourceOrcid
    source_client_id: Optional[None]
    source_name: DateValue
    assertion_origin_orcid: Optional[None]
    assertion_origin_client_id: Optional[None]
    assertion_origin_name: Optional[None]

class URL(TypedDict):
    value: str

class ResearcherUrl(TypedDict):
    created_date: DateValue
    last_modified_date: DateValue
    source: Source
    url_name: str
    url: URL
    visibility: str
    path: str
    put_code: int
    display_index: int

class ResearcherUrlsResponse(TypedDict):
    last_modified_date: DateValue
    researcher_url: List[ResearcherUrl]
    path: str