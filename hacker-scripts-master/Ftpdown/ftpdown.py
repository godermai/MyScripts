 conn = FTP(hostname, timeout=60.)
 conn.set_pasv(True)
 conn.login()
 while True:
     localfile = open(local_filename, "wb")
     try:
         dlthread = threading.Thread(target=conn.retrbinary,
                 args=("RETR {0}".format(remote_filename), localfile.write))
         dlthread.start()
         dlthread.join(timeout=60.)
         if not dlthread.is_alive():
             break
         del dlthread
         print("download didn't complete within {timeout}s. "
                 "waiting for 10s ...".format(timeout=60))
         time.sleep(10)
         print("restarting thread")
     except KeyboardInterrupt:
         raise
     except:
         pass
     localfile.close()