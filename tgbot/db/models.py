from datetime import datetime

from sqlalchemy import DateTime, Column, Integer, event

from .database import Base

UNKNOWN = "Unknown"


class BaseModel(Base):
    __abstract__ = True

    __created_at_name__ = "created_at"
    __updated_at_name__ = "updated_at"
    __datetime_func__ = datetime.utcnow

    __mapper_args__ = {"eager_defaults": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(
        __created_at_name__,
        DateTime,
        default=__datetime_func__,
        nullable=False,
    )
    updated_at = Column(
        __updated_at_name__,
        DateTime,
        default=__datetime_func__,
        onupdate=__datetime_func__,
        nullable=False,
    )

    def __repr__(self):
        columns = [col for col in self.__dict__.keys() if not col.startswith("_")]
        values_dict = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

        repr_string = "<{}({})>"
        attrs_string = ""

        for col_name in columns:
            attrs_string += "{}=".format(col_name) + "{" + col_name + "}, "
        attrs_string = attrs_string.format(**values_dict)
        return repr_string.format(self.__class__.__name__, attrs_string)
