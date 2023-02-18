from test_helpers.common_functions import *


def test_ping(booking_service):
    """
    1. Send GET reqiest to /ping.
    2. Validate response is 'Created'
    """
    r = booking_service.ping()
    assert r.status_code == HTTPStatus.CREATED, 'Status code is not as expected for /ping request'
    assert r.text == 'Created', 'Response text is not as expected for /ping request'


def test_create_booking(booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Try to get it by id.
    3. Validate response body is matches to request.
    """
    r = booking_service.get_booking(booking_id)
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "get booking" request'
    assert r.json() == booking_data_factory.create_booking_payload(rnd_value), 'Created booking is not as expected'


def test_create_booking_mandatory_fields_only(booking_service, booking_data_factory, booking_id):
    """
    1. Create booking with only mandatory fields.
    2. Try to get it by id.
    3. Validate response body is matches to request.
    """
    payload = booking_data_factory.create_booking_payload()
    del(payload['additionalneeds'])
    r = booking_service.create_booking(payload=payload)
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "get booking" request'


@pytest.mark.parametrize("field", ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"])
def test_create_booking_without_mandatory_field_negative(booking_service, booking_data_factory, booking_id, field):
    """
    1. Create booking with only mandatory fields.
    2. Try to get it by id.
    3. Validate response body is matches to request.
    """
    payload = booking_data_factory.create_booking_payload()
    del(payload[field])
    r = booking_service.create_booking(payload=payload)
    assert r.status_code == HTTPStatus.INTERNAL_SERVER_ERROR, 'Status code is not as expected for "get booking" request'


@pytest.mark.parametrize("param", ["firstname", "lastname"])
def test_get_bookings_by_name_parameter(booking_service, booking_data_factory, rnd_value, booking_id, param):
    """
    1. Create booking with custom value for specific param.
    2. Send get request with this param and value.
    3. Validate response data contains booking that was just created.
    """
    filter = (param, booking_data_factory.create_booking_payload(rnd_value)[param])
    r = booking_service.get_bookings([filter])
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "get bookings" request'
    assert len(r.json()) == 1, f"Only one result is expected for get bookings by {param}, but got {len(r.json())}"
    assert r.json()[0]['bookingid'] == booking_id, f"Returned id is not as expected for get bookings by {param}"


@pytest.mark.skip('skipped, because of the bug: not each booking for checkin filter exists in response')
@pytest.mark.parametrize("param", [("checkin", "2018-01-01"), ("checkout", "2019-01-01")])
def test_get_bookings_by_date_parameter(booking_service, booking_data_factory, rnd_value, booking_id, param):
    """
    1. Create booking with custom value for specific param.
    2. Send get request with this param and value.
    3. Validate response data contains booking that was just created.
    """
    r = booking_service.get_bookings([param])
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "get bookings" request'
    assert any(booking['bookingid'] == booking_id for booking in r.json()), \
        f"Booking with {param} was not returned in get by {param} response"


def test_update_booking(auth_booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Update booking data by POST.
    3. Get updated booking.
    4. Validate data was updated.
    """
    updated_payload = booking_data_factory.update_booking_payload()
    r = auth_booking_service.update_booking(booking_id, updated_payload)
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "update booking" request'
    assert r.json() == updated_payload, f'Booking data were not updated. Expected values: {updated_payload}. ' \
                                        f'Actual values: {r.json()}'


def test_update_booking_no_token(booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Try to update booking data by POST without token.
    3. Validate an error.
    """
    updated_payload = booking_data_factory.update_booking_payload()
    r = booking_service.update_booking(booking_id, updated_payload)
    assert r.status_code == HTTPStatus.FORBIDDEN, 'Status code is not as expected for "update booking" request without token'


def test_delete_booking(auth_booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Delete booking.
    3. Try to get deleted booking, validate 404 code in the response.
    """
    r = auth_booking_service.delete_booking(booking_id)
    assert r.status_code == HTTPStatus.CREATED, 'Status code is not as expected for "delete booking" request'
    r = auth_booking_service.get_booking(booking_id)
    assert r.status_code == HTTPStatus.NOT_FOUND, 'Status code is not as expected for "get unexisting booking" request'


def test_delete_unxesting_booking(auth_booking_service):
    """
    1. Create booking.
    2. Delete booking.
    3. Try to get deleted booking, validate 404 code in the response.
    """
    r = auth_booking_service.delete_booking('unexisting_booking_id')
    assert r.status_code == HTTPStatus.METHOD_NOT_ALLOWED, 'Status code is not as expected for "delete booking" request'


def test_delete_booking_no_token(booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Try to delete booking without token.
    3. Validate an error.
    """
    r = booking_service.delete_booking(booking_id)
    assert r.status_code == HTTPStatus.FORBIDDEN, 'Status code is not as expected for "delete booking" request without token'


def test_partial_update_booking(auth_booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Update some values by PATCH.
    3. Validate booking was updated in db.
    """
    updated_payload = booking_data_factory.update_booking_payload()
    r = auth_booking_service.partial_update_booking(booking_id, updated_payload)
    assert r.status_code == HTTPStatus.OK, 'Status code is not as expected for "update booking" request'
    assert r.json() == updated_payload, f'Booking data were not updated. Expected values: {updated_payload}. ' \
                                        f'Actual values: {r.json()}'


def test_partial_update_booking_no_token(booking_service, booking_data_factory, rnd_value, booking_id):
    """
    1. Create booking.
    2. Update some values by PATCH.
    3. Validate booking was updated in db.
    """
    updated_payload = booking_data_factory.update_booking_payload()
    r = booking_service.partial_update_booking(booking_id, updated_payload)
    assert r.status_code == HTTPStatus.FORBIDDEN, 'Status code is not as expected for "delete booking" request without token'

