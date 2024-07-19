# import smtplib

# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)

# # start TLS for security
# s.starttls()

# # Authentication
# s.login("adityamandapaka39@gmail.com", "uslq ckde xfgl lxuf")

# # message to be sent
# message = "You have won 100000000 rupees only...."

# # sending the mail
# s.sendmail("adityamandapaka39@gmail.com", "adhiadhibro4@gmail.com", message)

# # terminating the session
# s.quit() NlIKjqa2tPuDkJOdYF1Zi4y7BWmnL5TbfRG8cXeQ0zSU6ovgwh3rwi7tvhUBXVfN2GkPRK8DW06SLY4j

# import requests 

# url = "https://www.fast2sms.com/dev/bulkV2"

# querystring = { 
# 	"authorization": "NlIKjqa2tPuDkJOdYF1Zi4y7BWmnL5TbfRG8cXeQ0zSU6ovgwh3rwi7tvhUBXVfN2GkPRK8DW06SLY4j", 
# 	"message": "This is test Message sent from \Python Script using REST API.", 
# 	"language": "english", 
# 	"route": "q", 
# 	"numbers": "9392814989"} 

# headers = { 
# 	'cache-control': "no-cache"
# } 
# try: 
# 	response = requests.request("GET", url, 
# 								headers = headers, 
# 								params = querystring) 
# 	print(response)
# 	print("SMS Successfully Sent") 
# except: 
# 	print("Oops! Something wrong")

def a():
    print("a")
    def b():
        print("b")
    return b
x=a()
print(x())