from ..utils.logger import logger

class Request:
    """Kelas untuk menampung data HTTP Request yang sudah diparsing."""
    def __init__(self, raw_request: str):
        self.method = None
        self.path = None
        self.http_version = None

        self.parse(raw_request)

    def parse(self, raw_request: str):
        """Mem-parsing request line dari raw HTTP request."""
        try:
            request_line = raw_request.split('\r\n')[0]
            parts = request_line.split(' ')

            if len(parts) == 3:
                self.method = parts[0]
                self.path = parts[1]
                self.http_version = parts[2]
        except IndexError:
            logger.error("Gagal mem-parsing request: request tidak valid.")