import os
from ..core.response import Response
from ..utils.logger import logger

STATIC_DIR = "static"

MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.ico': 'image/x-icon'
}

class StaticHandler:
    def handle_request(self, request):
        """Mencari dan mengembalikan file statis berdasarkan request path."""

        path = request.path
        if path == '/':
            path = '/index.html'
        
        file_path = os.path.join(STATIC_DIR, path.lstrip('/'))

        if os.path.exists(file_path) and os.path.isfile(file_path):
            try:
                _, file_extension = os.path.splitext(file_path)
                content_type = MIME_TYPES.get(file_extension.lower(), 'application/octet-stream')
                
                with open(file_path, 'rb') as f:
                    body = f.read()

                logger.info(f"Menyajikan file: {file_path} dengan Content-Type: {content_type}")
                return Response.build_response(200, "OK", body, content_type=content_type)
            except Exception as e:
                logger.error(f"Error saat membaca file {file_path}: {e}")
                body_content = b"<h1>Internal Server Error</h1><p>Terjadi kesalahan saat memproses permintaan Anda.</p>"
                return Response.build_response(500, "Internal Server Error", body=body_content)
        else:
            logger.warning(f"File tidak ditemukan: {file_path}")
            body_content = b"<h1>404 Not Found</h1><p>Halaman yang Anda minta tidak ditemukan.</p>"
            return Response.build_response(404, "Not Found", body=body_content)