"""rate server module"""

from typing import Optional
import multiprocessing as mp
import sys
import socket
import threading
import requests
from datetime import datetime
import re
# Add support for the following client command

# GET 2019-01-03 EUR

# GET is the command name
# 2019-01-03 is the date of the current rates to retrieve
# EUR is the currency symbol to retrieve, DO NOT USE USD

# Call the Rates API using the USD as the base to get the currency rate
# for the specified date and return it to the client application

# Ideally your code will do the following:

# 1. Use a regular expression with named capture groups to extract parts
# of the command

# 2. Add a function named "process_client_command" to
# "ClientConnectionThread" that will process the parsed command including
# calling the API, extracting the API response, and send back the rate
# value to the client

# Data comes back as JSON

# *3. Send back an error message for an incorrectly formatted command or an
# unsupported command name (only the GET command is supported)


class ClientConnectionThread(threading.Thread):
    def __init__(self, conn: socket.socket) -> None:
        threading.Thread.__init__(self)
        self.__conn = conn

    def process_command(self,message: str) -> str:
        pattern = r"^(GET) (\d{4}-\d{2}-\d{2}) ([A-Z]{3})$"
        match = re.match(pattern, message)
        if match:
            action, date_string, currency = match.groups()
            business_day = datetime.strptime(date_string, "%Y-%m-%d").date()
            print(f"sending api call to upstream as http://localhost:8080/api/{business_day}"
                "?base=USD&symbols={currency} ")
            resp = requests.get((f"http://localhost:8080/api/{business_day}?base=USD&symbols={currency}"
            ), timeout=2)

            if resp.status_code == 200:
                return str(resp.json().get("rates",0.0))
        else:
            return "Invalid Command"

        return "N/A"
        
    def run(self) -> None:
        # conn.sendall("Connected to the Rates Server".encode("UTF-8"))
        self.__conn.sendall(b"Connected to the Rates Server")

        while True:
            message = self.__conn.recv(2048).decode("UTF-8")

            if not message:
                break

            print(f"recv: {message}")
            data = self.process_command(message)
            # GET <date> <currency>
            self.__conn.sendall(data.encode("UTF-8"))


def rate_server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        socket_server.bind((host, port))
        socket_server.listen()

        print(f"server is listening on {host}:{port}")

        while True:
            conn, addr = socket_server.accept()
            print(f"client from {addr} connected")
            a_thread = ClientConnectionThread(conn)
            a_thread.start()


def command_start_server(
    server_process: mp.Process | None, host: str, port: int
) -> mp.Process:
    """command start server"""

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        # step 1 - create a new process object to start the rates server
        server_process = mp.Process(target=rate_server, args=(host, port))
        # step 2 - start the new process object
        server_process.start()
        print("server started")

    return server_process


def command_stop_server(
    server_process: Optional[mp.Process],
) -> Optional[mp.Process]:
    """command stop server"""

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        print("server stopped")

    return None


def command_server_status(server_process: mp.Process | None) -> None:
    """command server status"""

    if server_process and server_process.is_alive():
        print("server is running")
    else:
        print("server is not running")


def main() -> None:
    """Main Function"""

    try:
        host = "127.0.0.1"
        port = 5050
        server_process: Optional[mp.Process] = None

        while True:
            command = input("> ")

            if command == "start":
                server_process = command_start_server(
                    server_process, host, port
                )
            elif command == "stop":
                server_process = command_stop_server(server_process)
            # step 3 - add a command named "status" that outputs to the
            # console if the server is current running or not
            # hint: follow the command function pattern used by the other
            # commands
            elif command == "status":
                command_server_status(server_process)
            elif command == "exit":
                # step 4 - terminate the "server_process" if the
                # "server_process" is an object and is alive
                if server_process and server_process.is_alive():
                    server_process.terminate()
                break

    except KeyboardInterrupt:
        # step 5 - terminate the "server_process" if the
        # "server_process" is an object and is alive
        if server_process and server_process.is_alive():
            server_process.terminate()
        pass

    sys.exit(0)


# to run the program, change into the `demos` folder, then
# run the following command:
# python -m rates_app.rates_server


if __name__ == "__main__":
    main()
