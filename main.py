import os
import requests
from bs4 import BeautifulSoup
page_url = 'https://this-person-does-not-exist.com/'  # Thay thế bằng URL của trang web cần lấy ảnh
response = requests.get(page_url)

soup = BeautifulSoup(response.content, 'html.parser')

# Tìm thẻ <body>
wrapper = soup.find('body')

# Ví dụ: Tìm tất cả các thẻ 
images = wrapper.find_all("img", {'id': 'avatar'})

for image in images:
    # Lấy đường dẫn ảnh
    img_src = image['src']

    # Kiểm tra nếu ảnh không phải là data URI
    if "data:image" not in img_src:
        # Kiểm tra nếu đường dẫn ảnh không rỗng
        if img_src:
            # Tạo tên file từ đường dẫn ảnh
            filename = img_src.split('/')[-1]

            # Tạo URL đầy đủ của ảnh
            pic_url = f"{page_url}/{img_src}"

            # Tải ảnh về
            response = requests.get(pic_url)

            # Tạo thư mục để lưu ảnh (nếu chưa tồn tại)
            directory = "Picture"
            os.makedirs(directory, exist_ok=True)

            # Tạo đường dẫn đầy đủ của file ảnh
            path = os.path.join(directory, filename)

            # Lưu ảnh vào thư mục đã đặt tên
            with open(path, "wb") as file:
                file.write(response.content)