# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NetworkAccessProfileNetworkList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, network_access_profile_sid):
        """
        Initialize the NetworkAccessProfileNetworkList

        :param Version version: Version that contains the resource
        :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkList
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkList
        """
        super(NetworkAccessProfileNetworkList, self).__init__(version)

        # Path Solution
        self._solution = {'network_access_profile_sid': network_access_profile_sid, }
        self._uri = '/NetworkAccessProfiles/{network_access_profile_sid}/Networks'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams NetworkAccessProfileNetworkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists NetworkAccessProfileNetworkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    def create(self, network):
        """
        Create the NetworkAccessProfileNetworkInstance

        :param unicode network: The SID that identifies the Network resource

        :returns: The created NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        """
        data = values.of({'Network': network, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution['network_access_profile_sid'],
        )

    def get(self, sid):
        """
        Constructs a NetworkAccessProfileNetworkContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        """
        return NetworkAccessProfileNetworkContext(
            self._version,
            network_access_profile_sid=self._solution['network_access_profile_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a NetworkAccessProfileNetworkContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        """
        return NetworkAccessProfileNetworkContext(
            self._version,
            network_access_profile_sid=self._solution['network_access_profile_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.NetworkAccessProfileNetworkList>'


class NetworkAccessProfileNetworkPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the NetworkAccessProfileNetworkPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkPage
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkPage
        """
        super(NetworkAccessProfileNetworkPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NetworkAccessProfileNetworkInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        """
        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution['network_access_profile_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.NetworkAccessProfileNetworkPage>'


class NetworkAccessProfileNetworkContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, network_access_profile_sid, sid):
        """
        Initialize the NetworkAccessProfileNetworkContext

        :param Version version: Version that contains the resource
        :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource
        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        """
        super(NetworkAccessProfileNetworkContext, self).__init__(version)

        # Path Solution
        self._solution = {'network_access_profile_sid': network_access_profile_sid, 'sid': sid, }
        self._uri = '/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}'.format(**self._solution)

    def delete(self):
        """
        Deletes the NetworkAccessProfileNetworkInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the NetworkAccessProfileNetworkInstance

        :returns: The fetched NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution['network_access_profile_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.NetworkAccessProfileNetworkContext {}>'.format(context)


class NetworkAccessProfileNetworkInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, network_access_profile_sid, sid=None):
        """
        Initialize the NetworkAccessProfileNetworkInstance

        :returns: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        """
        super(NetworkAccessProfileNetworkInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'network_access_profile_sid': payload.get('network_access_profile_sid'),
            'friendly_name': payload.get('friendly_name'),
            'iso_country': payload.get('iso_country'),
            'identifiers': payload.get('identifiers'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'network_access_profile_sid': network_access_profile_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: NetworkAccessProfileNetworkContext for this NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkContext
        """
        if self._context is None:
            self._context = NetworkAccessProfileNetworkContext(
                self._version,
                network_access_profile_sid=self._solution['network_access_profile_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def network_access_profile_sid(self):
        """
        :returns: The unique string that identifies the Network Access Profile resource
        :rtype: unicode
        """
        return self._properties['network_access_profile_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable identifier of this resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def iso_country(self):
        """
        :returns: The ISO country code of the Network resource
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def identifiers(self):
        """
        :returns: The MCC/MNCs included in the resource
        :rtype: list[dict]
        """
        return self._properties['identifiers']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def delete(self):
        """
        Deletes the NetworkAccessProfileNetworkInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the NetworkAccessProfileNetworkInstance

        :returns: The fetched NetworkAccessProfileNetworkInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.network_access_profile_network.NetworkAccessProfileNetworkInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.NetworkAccessProfileNetworkInstance {}>'.format(context)
