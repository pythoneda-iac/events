# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/infrastructure_update_failed.py

This file declares the InfrastructureUpdateFailed event.

Copyright (C) 2024-today pythoneda-shared-iac/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .abstract_infrastructure_event import AbstractInfrastructureEvent
from typing import List


class InfrastructureUpdateFailed(AbstractInfrastructureEvent):
    """
    Represents the moment the infrastructure update fails.

    Class name: InfrastructureUpdateFailed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new InfrastructureUpdateFailed instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            stackName,
            projectName,
            location,
            previousEventIds,
            reconstructedId,
            reconstructedPreviousEventIds,
        )

    @property
    def is_error(self):
        """
        Checks if the event is an error.
        :return: True if it's an error, False otherwise.
        :rtype: bool
        """
        return True


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: