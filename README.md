# HeadSoccer-Python
Đồ án môn học Kỹ thuật lập trình Python - IE221.N23.CNCL

## LƯU Ý ĐẶC BIỆT
### CHƯƠNG TRÌNH NÀY CẦN CÀI ĐẶT CÁC THƯ VIỆN PYMUNK,PYGAME

**Window + R / cmd**
và nhập:
**pip install pymunk**


**pip install pygame**

### KHI CLONE CODE VỀ HÃY ĐẢM BẢO MỞ FOLDER CHÍNH BẰNG TRÌNH BIÊN DỊCH THÌ MỚI RUN FILE MAIN
### NẾU BẠN KHÔNG MỞ FOLDER MÀ TRỰC TIẾP RUN FILE MAIN THÌ SẼ PHẢI COPY TOÀN BỘ FILE AUDIO VÀ IMAGE THEO ĐƯỜNG DẪN BÁO LỖI TRÊN TERMINAL

## CÁC ĐẶC ĐIỂM

-	 Bộ điều khiển: Xây dựng hệ thống điều khiển cho game. Người chơi có thể sử dụng các phím mũi tên để di chuyển nhân vật thứ nhất và tổ hợp phím WASD để di chuyển nhân vật thứ 2

-	Vật lý: Xử lý các tính toán vật lý như va chạm, chuyển động, và hấp thụ cho các đối tượng trong game. Các thư viện như Pygame hoặc PyMunk cung cấp các công cụ hỗ trợ để xử lý các tính toán vật lý vật lý sau.:
o	Sự va chạm của hai nhân vật: Sẽ xuất hiện hiện tượng cản trở, đụng nhau của hai nhân vật
o	Sự va chạm của hai nhân vật với quả bóng: Sẽ có hiện tượng quả bóng sẽ nảy theo hướng di chuyển của nhân vật.
o	Sự nảy của quá bóng khi thả rơi tự do trên mặt sàn: Sẽ có hiện tượng đàn hồi trên mặt sàn
-	Đối tượng trong game: Gồm có hai nhân vật, có khả năng di chuyển theo bề ngang và động tác nhảy khi nhấn mũi tên đi lên cho nhân vật 1 và nhấn phím W cho nhân vật 2. 

-	Trạng thái game: Các trạng thái của game như màn hình start, màn hình chơi, màn hình tạm dừng và kết thúc game.
o	Màn hình Start gồm có 3 nút chức năng: 
	PLAY  Fto5 (First to 5): Khi chọn chức năng này, hai players sẽ chơi cho đến khi người nào chạm mốc điểm 5 trước là trò chơi kết thúc
	PLAY 5minS: Khi chọn chức năng này, hai players sẽ chơi trong vòng 2 phút.
	QUIT: Nút này nhấn khi người dùng muốn thoát trò chơi
o	Màn hình chơi gồm có các đối tượng sau :
	Gồm có bảng tỷ số 
	Nút chức năng tạm dừng trò chơi
	Hai nhân vật người chơi
	Một quả bóng
	Hai cầu gôn
o	Màn hình tạm dừng (diễn ra sau khi nhấn nút chức năng dừng trên màn hình trò chơi) gồm có 2 nút chức năng :
	RESUME: Người dùng có thể tiếp tục quay lại trò chơi
	START: Người dùng quay trở về màn hình Start
o	Màn hình kết thúc game gồm có tiêu đề “P1/P2 wins” và nút chức năng:
	START: Người dùng quay trở về màn hình Start
-	Âm thanh và âm nhạc: Thêm các hiệu ứng âm thanh và nhạc nền vào game. Em sẽ sử dụng các thư viện như Pygame để chơi các tệp âm thanh và nhạc nền. Nhạc nền sẽ tiếp diễn khi chúng ta mở chương trình game cho đến khi kết thúc. Một nhạc thông báo khi một người chơi ghi bàn.
-	Luật chơi: 
o	Chế độ Fto5 (First to 5): Hai người chơi sẽ đưa bóng vào khung thành cho đến khi bên nào chạm mốc 10 điểm đầu tiên thì sẽ được công nhận chiến thắng.
o	Chế độ Time: Hai người chơi sẽ cố gắng đưa bóng vào khung thành trong khoảng thời gian 2 phút. Khi thời gian kết thúc, người chơi nào nhận điểm cao hơn sẽ giành chiến thắng. Trong trường hợp hòa, sẽ hiển thị thông báo hòa.
o	Khi ghi bàn, màn hình sẽ hiển thị thông báo ‘GOAL”
o	Quả bóng sẽ được thả ở vị trí trung tâm sau khi có bàn thắng


