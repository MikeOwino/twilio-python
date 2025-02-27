r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.video.v1.room.participant.anonymize import AnonymizeList
from twilio.rest.video.v1.room.participant.published_track import PublishedTrackList
from twilio.rest.video.v1.room.participant.subscribe_rules import SubscribeRulesList
from twilio.rest.video.v1.room.participant.subscribed_track import SubscribedTrackList


class ParticipantInstance(InstanceResource):

    class Status(object):
        CONNECTED = "connected"
        DISCONNECTED = "disconnected"

    """
    :ivar sid: The unique string that we created to identify the RoomParticipant resource.
    :ivar room_sid: The SID of the participant's room.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomParticipant resource.
    :ivar status: 
    :ivar identity: The application-defined string that uniquely identifies the resource's User within a Room. If a client joins with an existing Identity, the existing client is disconnected. See [access tokens](https://www.twilio.com/docs/video/tutorials/user-identity-access-tokens) and [limits](https://www.twilio.com/docs/video/programmable-video-limits) for more info. 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar start_time: The time of participant connected to the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :ivar end_time: The time when the participant disconnected from the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :ivar duration: The duration in seconds that the participant was `connected`. Populated only after the participant is `disconnected`.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        room_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.status: Optional["ParticipantInstance.Status"] = payload.get("status")
        self.identity: Optional[str] = payload.get("identity")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.start_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "room_sid": room_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ParticipantContext] = None

    @property
    def _proxy(self) -> "ParticipantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                room_sid=self._solution["room_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "ParticipantInstance":
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ParticipantInstance":
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, status: Union["ParticipantInstance.Status", object] = values.unset
    ) -> "ParticipantInstance":
        """
        Update the ParticipantInstance

        :param status:

        :returns: The updated ParticipantInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: Union["ParticipantInstance.Status", object] = values.unset
    ) -> "ParticipantInstance":
        """
        Asynchronous coroutine to update the ParticipantInstance

        :param status:

        :returns: The updated ParticipantInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    @property
    def anonymize(self) -> AnonymizeList:
        """
        Access the anonymize
        """
        return self._proxy.anonymize

    @property
    def published_tracks(self) -> PublishedTrackList:
        """
        Access the published_tracks
        """
        return self._proxy.published_tracks

    @property
    def subscribe_rules(self) -> SubscribeRulesList:
        """
        Access the subscribe_rules
        """
        return self._proxy.subscribe_rules

    @property
    def subscribed_tracks(self) -> SubscribedTrackList:
        """
        Access the subscribed_tracks
        """
        return self._proxy.subscribed_tracks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.ParticipantInstance {}>".format(context)


class ParticipantContext(InstanceContext):

    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the ParticipantContext

        :param version: Version that contains the resource
        :param room_sid: The SID of the room with the participant to update.
        :param sid: The SID of the RoomParticipant resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "sid": sid,
        }
        self._uri = "/Rooms/{room_sid}/Participants/{sid}".format(**self._solution)

        self._anonymize: Optional[AnonymizeList] = None
        self._published_tracks: Optional[PublishedTrackList] = None
        self._subscribe_rules: Optional[SubscribeRulesList] = None
        self._subscribed_tracks: Optional[SubscribedTrackList] = None

    def fetch(self) -> ParticipantInstance:
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ParticipantInstance:
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, status: Union["ParticipantInstance.Status", object] = values.unset
    ) -> ParticipantInstance:
        """
        Update the ParticipantInstance

        :param status:

        :returns: The updated ParticipantInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status: Union["ParticipantInstance.Status", object] = values.unset
    ) -> ParticipantInstance:
        """
        Asynchronous coroutine to update the ParticipantInstance

        :param status:

        :returns: The updated ParticipantInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    @property
    def anonymize(self) -> AnonymizeList:
        """
        Access the anonymize
        """
        if self._anonymize is None:
            self._anonymize = AnonymizeList(
                self._version,
                self._solution["room_sid"],
                self._solution["sid"],
            )
        return self._anonymize

    @property
    def published_tracks(self) -> PublishedTrackList:
        """
        Access the published_tracks
        """
        if self._published_tracks is None:
            self._published_tracks = PublishedTrackList(
                self._version,
                self._solution["room_sid"],
                self._solution["sid"],
            )
        return self._published_tracks

    @property
    def subscribe_rules(self) -> SubscribeRulesList:
        """
        Access the subscribe_rules
        """
        if self._subscribe_rules is None:
            self._subscribe_rules = SubscribeRulesList(
                self._version,
                self._solution["room_sid"],
                self._solution["sid"],
            )
        return self._subscribe_rules

    @property
    def subscribed_tracks(self) -> SubscribedTrackList:
        """
        Access the subscribed_tracks
        """
        if self._subscribed_tracks is None:
            self._subscribed_tracks = SubscribedTrackList(
                self._version,
                self._solution["room_sid"],
                self._solution["sid"],
            )
        return self._subscribed_tracks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.ParticipantContext {}>".format(context)


class ParticipantPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ParticipantInstance:
        """
        Build an instance of ParticipantInstance

        :param payload: Payload response from the API
        """
        return ParticipantInstance(
            self._version, payload, room_sid=self._solution["room_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.ParticipantPage>"


class ParticipantList(ListResource):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the ParticipantList

        :param version: Version that contains the resource
        :param room_sid: The SID of the room with the Participant resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
        }
        self._uri = "/Rooms/{room_sid}/Participants".format(**self._solution)

    def stream(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ParticipantInstance]:
        """
        Streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;ParticipantInstance.Status&quot; status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ParticipantInstance]:
        """
        Asynchronously streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;ParticipantInstance.Status&quot; status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ParticipantInstance]:
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;ParticipantInstance.Status&quot; status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                status=status,
                identity=identity,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ParticipantInstance]:
        """
        Asynchronously lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;ParticipantInstance.Status&quot; status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param str identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param datetime date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param datetime date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                status=status,
                identity=identity,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ParticipantPage:
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        """
        data = values.of(
            {
                "Status": status,
                "Identity": identity,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return ParticipantPage(self._version, response, self._solution)

    async def page_async(
        self,
        status: Union["ParticipantInstance.Status", object] = values.unset,
        identity: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ParticipantPage:
        """
        Asynchronously retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param status: Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
        :param identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
        :param date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        """
        data = values.of(
            {
                "Status": status,
                "Identity": identity,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ParticipantPage:
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ParticipantPage:
        """
        Asynchronously retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    def get(self, sid: str) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param sid: The SID of the RoomParticipant resource to update.
        """
        return ParticipantContext(
            self._version, room_sid=self._solution["room_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param sid: The SID of the RoomParticipant resource to update.
        """
        return ParticipantContext(
            self._version, room_sid=self._solution["room_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.ParticipantList>"
