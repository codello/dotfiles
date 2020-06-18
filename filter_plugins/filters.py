#!/usr/bin/env python3

from typing import Any


class FilterModule(object):
    """
    Custom filters for playbooks.
    """

    def filters(self) -> dict:
        return {
            'onoff': self.onoff,
            'valoff': self.valoff
        }

    def onoff(self, value: Any) -> bool:
        """Custom filter for on-off values for macOS system defaults."""
        return 'On' if value else 'Off'

    def valoff(self, value: Any) -> bool:
        """Custom filter for value-off values for macOS system defaults."""
        return value if value else 'Off'
