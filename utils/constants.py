"""
HTTP Status Code Constants for Star Wars API
"""

# Success Status Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204

# Client Error Status Codes
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_409_CONFLICT = 409
HTTP_422_UNPROCESSABLE_ENTITY = 422

# Server Error Status Codes
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503

# Common Response Messages
MESSAGE_VALIDATION_FAILED = "Validation failed"
MESSAGE_CHARACTER_NOT_FOUND = "Character not found"
MESSAGE_CHARACTER_CREATED = "Character created successfully"
MESSAGE_CHARACTER_UPDATED = "Character updated successfully"
MESSAGE_CHARACTER_DELETED = "Character deleted successfully"
MESSAGE_ALL_CHARACTERS_DELETED = "All characters have been deleted"
MESSAGE_INTERNAL_ERROR = "Internal server error"
MESSAGE_INVALID_ID = "Invalid character ID"
MESSAGE_DUPLICATE_CHARACTER = "Character already exists"
