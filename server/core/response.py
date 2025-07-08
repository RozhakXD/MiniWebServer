class Response:
    """Kelas untuk membangun HTTP Response."""
    def __init__(self, status_code, status_message, headers, body):
        self.status_code = status_code
        self.status_message = status_message
        self.headers = headers
        self.body = body
    
    def to_bytes(self) -> bytes:
        """Mengubah objek response menjadi format bytes untuk dikirim via socket."""
        response_line = f"HTTP/1.1 {self.status_code} {self.status_message}\r\n"
        header_lines = ""
        for key, value in self.headers.items():
            header_lines += f"{key}: {value}\r\n"
        return (response_line + header_lines + "\r\n").encode('utf-8') + self.body
    
    @classmethod
    def build_response(cls, status_code, status_message, body=b'', content_type="text/html; charset=utf-8"):
        """Membangun objek Response dengan header default."""
        headers = {
            "Content-Type": content_type,
            "Content-Length": str(len(body)),
            "Connection": "close"
        }
        return cls(status_code, status_message, headers, body)