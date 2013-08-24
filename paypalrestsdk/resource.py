import uuid

import paypalrestsdk.util as util
import paypalrestsdk.api as api


# Base class for all REST service
class Resource(object):

    convert_resources = {}

    def __init__(self, attributes={}):
        super(Resource, self).__setattr__('__data__', {})
        super(Resource, self).__setattr__('error', None)
        super(Resource, self).__setattr__('headers', {})
        super(Resource, self).__setattr__('header', {})
        super(Resource, self).__setattr__('request_id', None)
        self.merge(attributes)

    # Generate uniq request id
    def generate_request_id(self):
        if self.request_id is None:
            self.request_id = str(uuid.uuid4())
        return self.request_id

    # Generate HTTP header
    def http_headers(self):
        return util.merge_dict(self.header, self.headers,
                               {'PayPal-Request-Id': self.generate_request_id()})

    def __str__(self):
        return self.__data__.__str__()

    def __repr__(self):
        return self.__data__.__str__()

    # Getter
    def __getattr__(self, name):
        return self.__data__.get(name)

    # Setter
    def __setattr__(self, name, value):
        try:
            # Handle attributes(error, header, request_id)
            super(Resource, self).__getattribute__(name)
            super(Resource, self).__setattr__(name, value)
        except AttributeError:
            self.__data__[name] = self.convert(name, value)

    # return True if no error
    def success(self):
        return self.error is None

    # Merge new attributes
    def merge(self, new_attributes):
        for k in new_attributes:
            self.__setattr__(k, new_attributes[k])

    # Convert the attribute values to configured class.
    def convert(self, name, value):
        if isinstance(value, dict):
            cls = self.convert_resources.get(name, Resource)
            return cls(value)
        elif isinstance(value, list):
            new_list = []
            for obj in value:
                new_list.append(self.convert(name, obj))
            return new_list
        else:
            return value

    def __getitem__(self, key):
        return self.__data__[key]

    def __setitem__(self, key, value):
        self.__data__[key] = self.convert(key, value)

    def to_dict(self):

        def parse_object(value):
            if isinstance(value, Resource):
                return value.to_dict()
            elif isinstance(value, list):
                new_list = []
                for obj in value:
                    new_list.append(parse_object(obj))
                return new_list
            else:
                return value

        data = {}
        for key in self.__data__:
            data[key] = parse_object(self.__data__[key])
        return data


# == Example
#   payment = Payment.find("PAY-1234")
class Find(Resource):

    @classmethod
    def find(cls, resource_id):
        url = util.join_url(cls.path, str(resource_id))
        return cls(api.default().get(url))


# == Example
#   payment_histroy = Payment.all({'count': 2})
class List(Resource):
    list_class = Resource

    @classmethod
    def all(cls, params=None):
        if params is None:
            url = cls.path
        else:
            url = util.join_url_params(cls.path, params)
        return cls.list_class(api.default().get(url))


# == Example
#   payment = Payment({})
#   payment.create() # return True or False
class Create(Resource):

    def create(self):
        new_attributes = api.default().post(self.path, self.to_dict(), self.http_headers())
        self.error = None
        self.merge(new_attributes)
        return self.success()


# == Example
#   credit_card.delete()
class Delete(Resource):

    def delete(self):
        url = util.join_url(self.path, str(self['id']))
        new_attributes = api.default().delete(url)
        self.error = None
        self.merge(new_attributes)
        return self.success()


# == Example
#   payment.post("execute", {'payer_id': '1234'}, payment)  # return True or False
#   sale.post("refund", {'payer_id': '1234'})  # return Refund object
class Post(Resource):

    def post(self, name, attributes={}, cls=Resource):
        url = util.join_url(self.path, str(self['id']), name)
        if not isinstance(attributes, Resource):
            attributes = Resource(attributes)
        new_attributes = api.default().post(url, attributes.to_dict(), attributes.http_headers())
        if isinstance(cls, Resource):
            cls.error = None
            cls.merge(new_attributes)
            return self.success()
        else:
            return cls(new_attributes)
