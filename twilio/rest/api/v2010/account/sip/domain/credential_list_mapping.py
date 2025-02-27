r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class CredentialListMappingInstance(InstanceResource):
    """
    :ivar account_sid: The unique id of the Account that is responsible for this resource.
    :ivar date_created: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar date_updated: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar domain_sid: The unique string that is created to identify the SipDomain resource.
    :ivar friendly_name: A human readable descriptive text for this resource, up to 64 characters long.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar uri: The URI for this resource, relative to `https://api.twilio.com`
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        domain_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.domain_sid: Optional[str] = payload.get("domain_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.sid: Optional[str] = payload.get("sid")
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[CredentialListMappingContext] = None

    @property
    def _proxy(self) -> "CredentialListMappingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialListMappingContext for this CredentialListMappingInstance
        """
        if self._context is None:
            self._context = CredentialListMappingContext(
                self._version,
                account_sid=self._solution["account_sid"],
                domain_sid=self._solution["domain_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CredentialListMappingInstance":
        """
        Fetch the CredentialListMappingInstance


        :returns: The fetched CredentialListMappingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CredentialListMappingInstance":
        """
        Asynchronous coroutine to fetch the CredentialListMappingInstance


        :returns: The fetched CredentialListMappingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.CredentialListMappingInstance {}>".format(context)


class CredentialListMappingContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, domain_sid: str, sid: str):
        """
        Initialize the CredentialListMappingContext

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
        :param sid: A 34 character string that uniquely identifies the resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the CredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> CredentialListMappingInstance:
        """
        Fetch the CredentialListMappingInstance


        :returns: The fetched CredentialListMappingInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CredentialListMappingInstance:
        """
        Asynchronous coroutine to fetch the CredentialListMappingInstance


        :returns: The fetched CredentialListMappingInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.CredentialListMappingContext {}>".format(context)


class CredentialListMappingPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CredentialListMappingInstance:
        """
        Build an instance of CredentialListMappingInstance

        :param payload: Payload response from the API
        """
        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.CredentialListMappingPage>"


class CredentialListMappingList(ListResource):

    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the CredentialListMappingList

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json".format(
            **self._solution
        )

    def create(self, credential_list_sid: str) -> CredentialListMappingInstance:
        """
        Create the CredentialListMappingInstance

        :param credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.

        :returns: The created CredentialListMappingInstance
        """

        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    async def create_async(
        self, credential_list_sid: str
    ) -> CredentialListMappingInstance:
        """
        Asynchronously create the CredentialListMappingInstance

        :param credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.

        :returns: The created CredentialListMappingInstance
        """

        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CredentialListMappingInstance]:
        """
        Streams CredentialListMappingInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[CredentialListMappingInstance]:
        """
        Asynchronously streams CredentialListMappingInstance records from the API as a generator stream.
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
    ) -> List[CredentialListMappingInstance]:
        """
        Lists CredentialListMappingInstance records from the API as a list.
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
    ) -> List[CredentialListMappingInstance]:
        """
        Asynchronously lists CredentialListMappingInstance records from the API as a list.
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
    ) -> CredentialListMappingPage:
        """
        Retrieve a single page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListMappingInstance
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
        return CredentialListMappingPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CredentialListMappingPage:
        """
        Asynchronously retrieve a single page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListMappingInstance
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
        return CredentialListMappingPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> CredentialListMappingPage:
        """
        Retrieve a specific page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListMappingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CredentialListMappingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> CredentialListMappingPage:
        """
        Asynchronously retrieve a specific page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListMappingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CredentialListMappingPage(self._version, response, self._solution)

    def get(self, sid: str) -> CredentialListMappingContext:
        """
        Constructs a CredentialListMappingContext

        :param sid: A 34 character string that uniquely identifies the resource to fetch.
        """
        return CredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> CredentialListMappingContext:
        """
        Constructs a CredentialListMappingContext

        :param sid: A 34 character string that uniquely identifies the resource to fetch.
        """
        return CredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.CredentialListMappingList>"
