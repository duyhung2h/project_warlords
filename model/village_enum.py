from __future__ import annotations

from enum import Enum
from typing import Union


class VillageDatasetBase(Enum):
    """
    This enum class is the base class to retrieve texts using variables in Village dataset (ex. Village.ARMS_RACE.REQ_TEXT)
    """

    @staticmethod
    def _id_map() -> dict:
        """
        **Private Method**

        Returns:
            A dict that maps the names of the properties to their index in the info tuple
        """
        return {'req_text': 0, 'threat_text': 1}

    def _get_property(self, name: str) -> Union[int, bool]:
        """
        **Private Method**

        Get the specified property by its name from an object of this (or its derived) class

        Args:
            name: the name of the property to get

        Returns:
        """
        return self.value[self._id_map()[name]]

    @property
    def REQ_TEXT(self) -> []:
        """
        Returns:
            The ID of the specified unit
        """
        return self._get_property('req_text')

    @property
    def THREAT_TEXT(self) -> []:
        """
        Returns:
            The ID of the specified unit
        """
        return self._get_property('threat_text')


class VillageInfo(VillageDatasetBase):
    """
    **Description**

    This is an enum class which provides information about villages (their response to threat, their request text, etc)

    **Examples**

    >>> VillageInfo.ARMS_RACE.REQ_TEXT
    >>> "We have suitable farmlands across %X% to feed everyone, rather than having enough men to protect those folks. "
    >>> "My lord, our realm would be pleased if we receive protection from thy men."
    """
    ARMS_RACE = \
        [
            "We have suitable farmlands across %X% to feed everyone,",
            "rather than having enough men to protect those folks.",
            "My lord, our realm would be pleased if we receive protection from thy men."
        ], \
        ["There will be places for scumbags like thee in hell!"]
    GATHERING = \
        [
            "%X% has always been a defensive position, but in the cost of sizable farming land.",
            "We needeth to secure surrounding resources to ourselves.",
            "My lord, shall thee beest able to lent us a hand?"
        ], \
        ["We will defend what's left of ours!"]
    REGENCY = \
        ["%X% re. "], \
        ["Thee'll get squandered like a bug thou art, traitor."]
    TRIBAL_FEUD = \
        [
            "There hast always been hostle relation between the warchief in this region. ",
            "Destroy other tribes in this province, my lord,",
            "and thee shall earn our respect."
        ], \
        ["Barbarians! Thou art just like the rest of them!"]
