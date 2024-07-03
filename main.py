import requests

def upload_file(file_path):
    upload_url = 'http://127.0.0.1:8000/api/upload/'
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, files={'file': file})
    if response.status_code == 201:
        print('Fayl muvaffaqiyatli yuklandi!')
        print('Javob:', response.json())
    else:
        print('Xatolik yuz berdi:', response.status_code)
        print('Javob:', response.json())

def list_files():
    list_url = 'http://127.0.0.1:8000/api/files/'
    response = requests.get(list_url)
    if response.status_code == 200:
        files = response.json()
        print('Yuklangan fayllar:')
        for file in files:
            print(file)
    else:
        print('Xatolik yuz berdi:', response.status_code)
        print('Javob:', response.json())

if __name__ == '__main__':
    # Faylni yuklash
    upload_file('Misha Xramovi - В экстазе.mp3')

    # Yuklangan fayllarni ko'rish
    list_files()
