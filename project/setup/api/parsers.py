from flask_restx.reqparse import RequestParser

#служит для вывода определенного количества записей на одной странице
page_parser: RequestParser = RequestParser()
page_parser.add_argument(name='page', type=int, location='args', required=False)
