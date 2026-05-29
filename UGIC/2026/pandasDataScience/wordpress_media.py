"""
Data classes for WordPress REST API media items.
Reference: https://developer.wordpress.org/rest-api/reference/media/
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ---------------------------------------------------------------------------
# Helper / nested types
# ---------------------------------------------------------------------------


@dataclass
class RenderedContent:
    """Wrapper for fields that return {'rendered': '...'}."""

    rendered: str

    @classmethod
    def from_dict(cls, data: dict) -> RenderedContent:
        return cls(rendered=data.get("rendered", ""))


@dataclass
class ImageSize:
    """A single size variant inside media_details.sizes."""

    file: str
    width: int
    height: int
    mime_type: str
    source_url: str
    filesize: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> ImageSize:
        return cls(
            file=data.get("file", ""),
            width=data.get("width", 0),
            height=data.get("height", 0),
            mime_type=data.get("mime_type", ""),
            source_url=data.get("source_url", ""),
            filesize=data.get("filesize"),
        )


@dataclass
class ImageMeta:
    """EXIF / IPTC metadata embedded in an image."""

    aperture: str = ""
    credit: str = ""
    camera: str = ""
    caption: str = ""
    created_timestamp: str = ""
    copyright: str = ""
    focal_length: str = ""
    iso: str = ""
    shutter_speed: str = ""
    title: str = ""
    orientation: str = ""
    keywords: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> ImageMeta:
        return cls(
            aperture=data.get("aperture", ""),
            credit=data.get("credit", ""),
            camera=data.get("camera", ""),
            caption=data.get("caption", ""),
            created_timestamp=data.get("created_timestamp", ""),
            copyright=data.get("copyright", ""),
            focal_length=data.get("focal_length", ""),
            iso=data.get("iso", ""),
            shutter_speed=data.get("shutter_speed", ""),
            title=data.get("title", ""),
            orientation=data.get("orientation", ""),
            keywords=data.get("keywords", []),
        )


@dataclass
class MediaDetails:
    """
    Details about the media file (media_details field).
    For images this includes dimensions, sizes, and image metadata.
    For non-image files the sizes dict and image_meta will be empty.
    """

    width: Optional[int] = None
    height: Optional[int] = None
    file: str = ""
    filesize: Optional[int] = None
    sizes: dict[str, ImageSize] = field(default_factory=dict)
    image_meta: ImageMeta = field(default_factory=ImageMeta)

    @classmethod
    def from_dict(cls, data: dict) -> MediaDetails:
        sizes = {
            name: ImageSize.from_dict(size_data)
            for name, size_data in data.get("sizes", {}).items()
        }
        raw_meta = data.get("image_meta", {})
        image_meta = ImageMeta.from_dict(raw_meta) if raw_meta else ImageMeta()
        return cls(
            width=data.get("width"),
            height=data.get("height"),
            file=data.get("file", ""),
            filesize=data.get("filesize"),
            sizes=sizes,
            image_meta=image_meta,
        )


# ---------------------------------------------------------------------------
# Main data class
# ---------------------------------------------------------------------------


@dataclass
class MediaItem:
    """
    A WordPress media item as returned by GET /wp/v2/media or GET /wp/v2/media/<id>.

    Fields marked 'read only' in the REST API schema are included here for
    deserialization but should not be sent when creating/updating a record.
    """

    # --- Identifiers (read only) ---
    id: int
    guid: RenderedContent
    link: str
    type: str

    # --- Timestamps ---
    date: Optional[datetime]
    date_gmt: Optional[datetime]
    modified: Optional[datetime]  # read only
    modified_gmt: Optional[datetime]  # read only

    # --- Slugs / status ---
    slug: str
    status: str  # publish | future | draft | pending | private

    # --- Content ---
    title: RenderedContent
    caption: RenderedContent
    description: RenderedContent

    # --- Media-specific (read only) ---
    alt_text: str
    media_type: str  # image | file
    mime_type: str
    media_details: MediaDetails
    source_url: str

    # --- Relationships ---
    author: int
    post: Optional[int] = None

    # --- Misc ---
    comment_status: str = "open"   # open | closed
    ping_status: str = "closed"    # open | closed
    template: str = ""
    meta: dict = field(default_factory=dict)

    # --- Edit-context only (read only) ---
    permalink_template: Optional[str] = None
    generated_slug: Optional[str] = None
    missing_image_sizes: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def from_dict(cls, data: dict) -> MediaItem:
        def parse_dt(value: Optional[str]) -> Optional[datetime]:
            if not value:
                return None
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                return None

        raw_details = data.get("media_details", {})
        media_details = MediaDetails.from_dict(raw_details) if raw_details else MediaDetails()

        return cls(
            id=data["id"],
            guid=RenderedContent.from_dict(data.get("guid", {"rendered": ""})),
            link=data.get("link", ""),
            type=data.get("type", ""),
            date=parse_dt(data.get("date")),
            date_gmt=parse_dt(data.get("date_gmt")),
            modified=parse_dt(data.get("modified")),
            modified_gmt=parse_dt(data.get("modified_gmt")),
            slug=data.get("slug", ""),
            status=data.get("status", ""),
            title=RenderedContent.from_dict(data.get("title", {"rendered": ""})),
            caption=RenderedContent.from_dict(data.get("caption", {"rendered": ""})),
            description=RenderedContent.from_dict(data.get("description", {"rendered": ""})),
            alt_text=data.get("alt_text", ""),
            media_type=data.get("media_type", ""),
            mime_type=data.get("mime_type", ""),
            media_details=media_details,
            source_url=data.get("source_url", ""),
            author=data.get("author", 0),
            post=data.get("post"),
            comment_status=data.get("comment_status", "open"),
            ping_status=data.get("ping_status", "closed"),
            template=data.get("template", ""),
            meta=data.get("meta", {}),
            permalink_template=data.get("permalink_template"),
            generated_slug=data.get("generated_slug"),
            missing_image_sizes=data.get("missing_image_sizes", []),
        )
