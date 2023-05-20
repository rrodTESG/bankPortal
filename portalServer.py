from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi

class PortalRequestHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
       
        try:
            if self.path == '/addAccount':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                owner_name     = form.getvalue("oname")
                owner_ssn = int(form.getvalue("owner_ssn"))
                balance    = float(form.getvalue("balance"))
                acct_status = "active"
                ##Call the Database Method to a add a new student
                '''
                    Example call: self.database.addAccount(student_name, ownerName, owner_ssn, balance, status)
                '''

                print("grabbed values",owner_name,owner_ssn,balance)
                
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/deletAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Account have been added</h3>")
                self.wfile.write(b"<div><a href='/addAccount'>Add a New Account</a></div>")
                self.wfile.write(b"</center></body></html>")
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


        return


    def do_GET(self):
        try:

            if self.path == '/':
                data=[]
                records = self.database.getAllAccounts()
                print(records)
                data=records
                
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/deletAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>All Accounts</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Account ID </th>\
                                        <th> Account Owner</th>\
                                        <th> Balance </th>\
                                        <th> Status </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            if self.path == '/addAccount':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/deletAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Add New Account</h2>")

                self.wfile.write(b"<form action='/addAccount' method='post'>")
                self.wfile.write(b'<label for="oname">Owner Name:</label>\
                      <input type="text" id="oname" name="oname"><br><br>\
                      <label for="owner_ssn">Owner SSN:</label>\
                      <input type="number" id="owner_ssn" name="owner_ssn"><br><br>\
                      <label for="balance">Balance:</label>\
                      <input type="number" step="0.01" id="balance" name="balance"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                
                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/withdraw':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/deletAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Withdraw from an account</h2>")

                self.wfile.write(b"</center></body></html>")
                return
            
            if self.path =='/deposit':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Bank's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Bank's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addAccount'>Add Account</a>|\
                                  <a href='/withdraw'>Withdraw</a>|\
                                  <a href='/deposit'>Deposit </a>|\
                                  <a href='/searchTransactions'>Search Transactions</a>|\
                                  <a href='/deletAccount'>Delete Account</a></div>")
                self.wfile.write(b"<hr><h2>Deposit into an account</h2>")

                self.wfile.write(b"</center></body></html>")
                return
            if self.path =='/serachTransactions':
                return


            if self.path =='/deleteAccount':
                return



        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

     
            
def run(server_class=HTTPServer, handler_class=PortalRequestHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()
    
run()
