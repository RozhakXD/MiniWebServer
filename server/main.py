import threading
import socket

from .core.requests import Request
from .handlers.static_handler import StaticHandler
from .utils.logger import logger

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        logger.info(f"Server akan berjalan di {self.host}:{self.port}")
    
    def start(self):
        """Membuat socket dan memulai loop utama untuk menerima koneksi."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            logger.info(f"Server berhasil berjalan, menunggu koneksi...")

            while True:
                try:
                    client_socket, client_address = self.server_socket.accept()

                    if not self.running:
                        client_socket.close()
                        logger.info("Server tidak lagi menerima koneksi baru.")
                        break

                    client_thread = threading.Thread(
                        target=self.handle_connection,
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                except KeyboardInterrupt:
                    logger.info("Server dihentikan oleh pengguna.")
                    break
        except OSError as e:
            logger.error(f"Gagal menjalankan server: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Membersihkan sumber daya yang digunakan oleh server."""
        self.running = False
        if self.server_socket:
            try:
                self.server_socket.close()
                logger.info("Server socket berhasil ditutup.")
            except:
                pass            
    
    def handle_connection(self, client_socket, client_address):
        """Menangani koneksi dari satu client."""
        logger.info(f"Menerima koneksi dari {client_address}")
        try:
            raw_request = client_socket.recv(1024).decode('utf-8')
            if not raw_request:
                return
            
            request = Request(raw_request)
            logger.info(f"Request diterima: {request.method} {request.path}")

            self.static_handler = StaticHandler()
            response = self.static_handler.handle_request(request)

            client_socket.sendall(response.to_bytes())
        except Exception as e:
            logger.error(f"Terjadi kesalahan saat menangani koneksi: {e}")
        finally:
            client_socket.close()
            logger.info(f"Koneksi dari {client_address} ditutup.")