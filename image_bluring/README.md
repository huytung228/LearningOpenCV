# LearningOpenCV
Learning Open CV python
# 1. Smoothing Images with Blurs
- Như đối với tín hiệu một chiều, ảnh có thể được lọc với LPF và HPF. LPF giúp loại bỏ nhiễu còn HPF giúp xác định biên trong một ảnh
- image blur (smoothing) được thực hiện bằng phép tích chập với bộ lọc thông thấp LPF. nó sẽ xóa các high frequency content (noise, edge). 
- Có 4 loại blur chính:
## Lọc trung bình
- Dùng cv.blur() or cv.boxFilter()
## Lọc Gaussian 
- Dùng cv.GaussianBlur()
- Hiệu quả với nhiễu Gause
- Có các tham số chính như: hight width (dương và lẻ) sigmaX, sigmaY là std
## Lọc Trung Vị (Median)
- Hiệu quả với nhiễu hạt tiêu
- Dùng cv.medianBlur()
## Lọc Song Phương (Bilateral)
- Hiệu quả đối với việc xóa noise nhưng giữ lại biên
- Dùng cv.bilateralFilter()



