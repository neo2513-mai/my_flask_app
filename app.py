from flask import Flask, render_template
import requests

app = Flask(__name__)

GAS_API_URL = "https://script.google.com/macros/s/AKfycbz1jw4nkWJhsKqbRG2WMNdl31OBb59vXIvJNkrIdTLVwsksmRfvVjHOSQgzlZVGgtlo/exec"

@app.route('/')
def index():
    try:
        response = requests.get(GAS_API_URL, allow_redirects=True)
        result = response.json()
        
        # ต้องดึงค่าจาก key ที่ชื่อว่า 'data' ตามโครงสร้าง JSON ของคุณ
        if result.get("status") == "success":
            products = result.get("data", [])
        else:
            products = []
            
    except Exception as e:
        products = []
        print(f"Error: {e}")
    
    return render_template('index.html', products=products)
if __name__ == '__main__':
    app.run(debug=True)