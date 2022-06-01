import requests

max_requests=200
count =0

for i in range(0,max_requests):
    res =requests.get('http://localhost:8080/')
    
    # convert byte to string
    content = res.content.decode('utf-8')

    # server should return either `Hello App1!` or `Hello App2!`
    # ⚡ when you change index.js return content, remember also change the following command
    if(content[-1-1] == '1'):
        count+=1
        

print(f"app1 server's loading is {count/max_requests}")
print(f"app2 server's loading is {(max_requests-count)/max_requests}")
# app1 server's loading is 0.7
# app2 server's loading is 0.3 
