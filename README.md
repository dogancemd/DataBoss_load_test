1. Install the requirements
pip install -r requirements <br>
2. Adjust the data
change post_data.json according to request<br>
3. Run locust 
run "locust" onn terminal inside this folder and then on adjust test parameters on localhost:8089
OR
run "locust --headless -u \<peak_user_count\> -s \<spawn rate of users\> --host \<host\> -t \<runtime(like 60 or 1h30m)\>  