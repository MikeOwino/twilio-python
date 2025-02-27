r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.function.function_version import (
    FunctionVersionList,
)


class FunctionInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the Function resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function resource.
    :ivar service_sid: The SID of the Service that the Function resource is associated with.
    :ivar friendly_name: The string that you assigned to describe the Function resource. It can be a maximum of 255 characters.
    :ivar date_created: The date and time in GMT when the Function resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Function resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Function resource.
    :ivar links: The URLs of nested resources of the Function resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[FunctionContext] = None

    @property
    def _proxy(self) -> "FunctionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionContext for this FunctionInstance
        """
        if self._context is None:
            self._context = FunctionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the FunctionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FunctionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FunctionInstance":
        """
        Fetch the FunctionInstance


        :returns: The fetched FunctionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FunctionInstance":
        """
        Asynchronous coroutine to fetch the FunctionInstance


        :returns: The fetched FunctionInstance
        """
        return await self._proxy.fetch_async()

    def update(self, friendly_name: str) -> "FunctionInstance":
        """
        Update the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    async def update_async(self, friendly_name: str) -> "FunctionInstance":
        """
        Asynchronous coroutine to update the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
        )

    @property
    def function_versions(self) -> FunctionVersionList:
        """
        Access the function_versions
        """
        return self._proxy.function_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionInstance {}>".format(context)


class FunctionContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the FunctionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to update the Function resource from.
        :param sid: The SID of the Function resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Functions/{sid}".format(**self._solution)

        self._function_versions: Optional[FunctionVersionList] = None

    def delete(self) -> bool:
        """
        Deletes the FunctionInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FunctionInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> FunctionInstance:
        """
        Fetch the FunctionInstance


        :returns: The fetched FunctionInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FunctionInstance:
        """
        Asynchronous coroutine to fetch the FunctionInstance


        :returns: The fetched FunctionInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, friendly_name: str) -> FunctionInstance:
        """
        Update the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, friendly_name: str) -> FunctionInstance:
        """
        Asynchronous coroutine to update the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def function_versions(self) -> FunctionVersionList:
        """
        Access the function_versions
        """
        if self._function_versions is None:
            self._function_versions = FunctionVersionList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._function_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionContext {}>".format(context)


class FunctionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> FunctionInstance:
        """
        Build an instance of FunctionInstance

        :param payload: Payload response from the API
        """
        return FunctionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.FunctionPage>"


class FunctionList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the FunctionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Function resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Functions".format(**self._solution)

    def create(self, friendly_name: str) -> FunctionInstance:
        """
        Create the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The created FunctionInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FunctionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, friendly_name: str) -> FunctionInstance:
        """
        Asynchronously create the FunctionInstance

        :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The created FunctionInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FunctionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[FunctionInstance]:
        """
        Streams FunctionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[FunctionInstance]:
        """
        Asynchronously streams FunctionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FunctionInstance]:
        """
        Lists FunctionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FunctionInstance]:
        """
        Asynchronously lists FunctionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FunctionPage:
        """
        Retrieve a single page of FunctionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionInstance
        """
        data = values.of(
            {
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
        return FunctionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FunctionPage:
        """
        Asynchronously retrieve a single page of FunctionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionInstance
        """
        data = values.of(
            {
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
        return FunctionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> FunctionPage:
        """
        Retrieve a specific page of FunctionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FunctionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FunctionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> FunctionPage:
        """
        Asynchronously retrieve a specific page of FunctionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FunctionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FunctionPage(self._version, response, self._solution)

    def get(self, sid: str) -> FunctionContext:
        """
        Constructs a FunctionContext

        :param sid: The SID of the Function resource to update.
        """
        return FunctionContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> FunctionContext:
        """
        Constructs a FunctionContext

        :param sid: The SID of the Function resource to update.
        """
        return FunctionContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.FunctionList>"
