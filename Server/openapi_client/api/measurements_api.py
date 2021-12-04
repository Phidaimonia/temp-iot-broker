"""
    Envi Server

    Server pro účely předmětu ZČU KKY/ITE 2021  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.error import Error
from openapi_client.model.measurement import Measurement
from openapi_client.model.measurement_body import MeasurementBody
from openapi_client.model.measurements import Measurements


class MeasurementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_measurement_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/measurements',
                'operation_id': 'create_measurement',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'team_uuid',
                    'measurement',
                ],
                'required': [
                    'team_uuid',
                    'measurement',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'team_uuid':
                        (str,),
                    'measurement':
                        (Measurement,),
                },
                'attribute_map': {
                    'team_uuid': 'teamUUID',
                },
                'location_map': {
                    'team_uuid': 'header',
                    'measurement': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_measurement_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/measurements/{measurementId}',
                'operation_id': 'delete_measurement',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'measurement_id',
                    'team_uuid',
                ],
                'required': [
                    'measurement_id',
                    'team_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'measurement_id':
                        (str,),
                    'team_uuid':
                        (str,),
                },
                'attribute_map': {
                    'measurement_id': 'measurementId',
                    'team_uuid': 'teamUUID',
                },
                'location_map': {
                    'measurement_id': 'path',
                    'team_uuid': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.read_all_measurements_endpoint = _Endpoint(
            settings={
                'response_type': (Measurements,),
                'auth': [],
                'endpoint_path': '/measurements',
                'operation_id': 'read_all_measurements',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'team_uuid',
                    'sensor_uuid',
                ],
                'required': [
                    'team_uuid',
                    'sensor_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'team_uuid':
                        (str,),
                    'sensor_uuid':
                        (str,),
                },
                'attribute_map': {
                    'team_uuid': 'teamUUID',
                    'sensor_uuid': 'sensorUUID',
                },
                'location_map': {
                    'team_uuid': 'header',
                    'sensor_uuid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.read_single_measurement_endpoint = _Endpoint(
            settings={
                'response_type': (MeasurementBody,),
                'auth': [],
                'endpoint_path': '/measurements/{measurementId}',
                'operation_id': 'read_single_measurement',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'measurement_id',
                    'team_uuid',
                ],
                'required': [
                    'measurement_id',
                    'team_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'measurement_id':
                        (str,),
                    'team_uuid':
                        (str,),
                },
                'attribute_map': {
                    'measurement_id': 'measurementId',
                    'team_uuid': 'teamUUID',
                },
                'location_map': {
                    'measurement_id': 'path',
                    'team_uuid': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_measurement_endpoint = _Endpoint(
            settings={
                'response_type': (MeasurementBody,),
                'auth': [],
                'endpoint_path': '/measurements/{measurementId}',
                'operation_id': 'update_measurement',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'measurement_id',
                    'team_uuid',
                    'measurement_body',
                ],
                'required': [
                    'measurement_id',
                    'team_uuid',
                    'measurement_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'measurement_id':
                        (str,),
                    'team_uuid':
                        (str,),
                    'measurement_body':
                        (MeasurementBody,),
                },
                'attribute_map': {
                    'measurement_id': 'measurementId',
                    'team_uuid': 'teamUUID',
                },
                'location_map': {
                    'measurement_id': 'path',
                    'team_uuid': 'header',
                    'measurement_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_measurement(
        self,
        team_uuid,
        measurement,
        **kwargs
    ):
        """Store a measurement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_measurement(team_uuid, measurement, async_req=True)
        >>> result = thread.get()

        Args:
            team_uuid (str): Authorize by the teamUUID of your team
            measurement (Measurement): Measurement body

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['team_uuid'] = \
            team_uuid
        kwargs['measurement'] = \
            measurement
        return self.create_measurement_endpoint.call_with_http_info(**kwargs)

    def delete_measurement(
        self,
        measurement_id,
        team_uuid,
        **kwargs
    ):
        """Delete a specific measurement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_measurement(measurement_id, team_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            measurement_id (str): The id of the measurement to delete
            team_uuid (str): Authorize by the teamUUID of your team

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['measurement_id'] = \
            measurement_id
        kwargs['team_uuid'] = \
            team_uuid
        return self.delete_measurement_endpoint.call_with_http_info(**kwargs)

    def read_all_measurements(
        self,
        team_uuid,
        sensor_uuid,
        **kwargs
    ):
        """List all measurements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_all_measurements(team_uuid, sensor_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            team_uuid (str): Authorize by the teamUUID of your team
            sensor_uuid (str): Read measurements for the particular sensor identified by its sensorUUID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Measurements
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['team_uuid'] = \
            team_uuid
        kwargs['sensor_uuid'] = \
            sensor_uuid
        return self.read_all_measurements_endpoint.call_with_http_info(**kwargs)

    def read_single_measurement(
        self,
        measurement_id,
        team_uuid,
        **kwargs
    ):
        """Read a specific measurement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_single_measurement(measurement_id, team_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            measurement_id (str): The id of the measurement to retrieve
            team_uuid (str): Authorize by the teamUUID of your team

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MeasurementBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['measurement_id'] = \
            measurement_id
        kwargs['team_uuid'] = \
            team_uuid
        return self.read_single_measurement_endpoint.call_with_http_info(**kwargs)

    def update_measurement(
        self,
        measurement_id,
        team_uuid,
        measurement_body,
        **kwargs
    ):
        """Update a specific measurement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_measurement(measurement_id, team_uuid, measurement_body, async_req=True)
        >>> result = thread.get()

        Args:
            measurement_id (str): The id of the measurement to update
            team_uuid (str): Authorize by the teamUUID of your team
            measurement_body (MeasurementBody): Measurement body

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MeasurementBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['measurement_id'] = \
            measurement_id
        kwargs['team_uuid'] = \
            team_uuid
        kwargs['measurement_body'] = \
            measurement_body
        return self.update_measurement_endpoint.call_with_http_info(**kwargs)
