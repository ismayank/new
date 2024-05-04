import requests

def get_current_ISS_location():
    try:
        
        response = requests.get("http://api.open-notify.org/iss-now.json")

        if response.status_code == 200:
            data = response.json()

            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            
            print(f"Lat: {latitude}  Long: {longitude}")
        else:
            print("Failed to fetch ISS location. Please try again later.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_current_ISS_location()
