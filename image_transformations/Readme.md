# Image transformations
## Image translation (dịch ảnh)
- Dùng cv2.warpAffine() với tham số matrix có dạng (1 0 x][0 1 y)
- Nếu x âm/dương -> trái/phải, y âm/dương -> trên/dưới
## Rotation
- Xoay ảnh theo một góc nhất định
- Dùng cv2.warpAffine() nhưng cần truyền vào tham số matrix được tạo ra bởi:
-  Hàm cv2.getRotationMatrix2D: rotPoint - điểm neo để xoay, angle - góc xoay
## Flipping (lật)
- Dùng cv2.flip()
- Tham số thứ 2 là để config lật theo chiều dọc hay ngang hoặc cả 2

 

