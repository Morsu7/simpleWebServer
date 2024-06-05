#!/bin/env python
import sys, signal
import http.server
import socketserver

# Legge il numero della porta dalla riga di comando
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

# ThreadingTCPServer per gestire piu richieste
server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

server.daemon_threads = True  
server.allow_reuse_address = True  

#definiamo una funzione per permetterci di uscire alla pressione di Ctrl-C
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( server ):
        server.server_close()
    finally:
      sys.exit(0)

#interrompe l'esecuzione se da tastiera arriva la sequenza (CTRL + C) 
signal.signal(signal.SIGINT, signal_handler)

#loop
try:
  while True:
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close()
