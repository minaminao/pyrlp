from importlib.metadata import (
    version as __version,
)

from . import (
    sedes,
)
from .codec import (
    decode,
    encode,
    infer_sedes,
)
from .exceptions import (
    DecodingError,
    DeserializationError,
    EncodingError,
    RLPException,
    SerializationError,
)
from .lazy import (
    LazyList,
    decode_lazy,
    peek,
)
from .sedes import (
    Serializable,
)

__version__ = __version("rlp")

__all__ = [
    "__version__",
    "sedes",
    "decode",
    "encode",
    "infer_sedes",
    "DecodingError",
    "DeserializationError",
    "EncodingError",
    "RLPException",
    "SerializationError",
    "LazyList",
    "decode_lazy",
    "peek",
    "Serializable",
]
