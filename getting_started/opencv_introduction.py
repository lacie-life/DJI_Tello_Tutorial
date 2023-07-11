import cv2
import numpy as np

# Đọc ảnh RGB
img = cv2.imread('../data/test.jpg', cv2.IMREAD_COLOR)

cv2.imshow('color', img)

img2 = img.copy()

# Chuyển ảnh sang ảnh xám
cv2.cvtColor(img, img2, cv2.COLOR_BGR2RGB)

cv2.imshow('gray', img2)

cv2.waitKey(0)

# Lưu ảnh
cv2.imwrite('../data/test_gray.jpg', img2)

cv2.destroyAllWindows()
