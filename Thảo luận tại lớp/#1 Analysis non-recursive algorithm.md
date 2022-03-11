## PHÂN TÍCH ĐỘ PHỨC TẠP THUẬT TOÁN KHÔNG ĐỆ QUY

- Độ phức tạp lưu trữ: dung lượng bộ nhớ cần thiết
- Độ phức tạp tính toán: TG chiếm dụng CPU nhiều hay ít => đo số phép toán CPU cần dùng để xử lý

### XÁC ĐỊNH ĐỘ PHỨC TẠP BẰNG LÝ THUYẾT

•         Độ phức tạp tính toán của giải thuật: O(f(n))

•         Việc xác định độ phức tạp tính toán của giải thuật trong thực tế có thể tính bằng một số quy tắc đơn giản sau:

–        Quy tắc bỏ hằng số:

            T(n) = O(c.f(n)) = O(f(n)) với c là một hằng số dương

–        Quy tắc lấy max:

            T(n) = O(f(n)+ g(n)) = O(max(f(n), g(n)))

–         Quy tắc cộng:

            T1(n) = O(f(n))                     T2(n) = O(g(n))

            T1(n) + T2(n) = O(f(n) + g(n))

–         Quy tắc nhân:

            Đoạn chương trình có thời gian thực hiện T(n)=O(f(n))

            Nếu thực hiện k(n) lần đoạn chương trình với k(n) = O(g(n)) thì độ phức tạp sẽ là O(g(n).f(n))
### Hiểu đơn giản

Đếm số phép toán cơ sở (đại lượng tương đương là số lần lặp):
1. Đếm số vòng lặp
2. Đếm số phép so sánh/ phép gán rồi nhân số vòng lặp
3. Làm sấp xỉ bằng cách bỏ hệ số

### Big O, big Omega, big Theta

- Big O:
- Big Omega:
- Big Theta:

<p align="center">
  <a style="border: none;">
    <img src="https://itzone.com.vn/wp-content/uploads/2020/06/96851ae4-1258-4f5e-97ac-2a6a1d23e6fc.png" alt="bigO" style="width:50%;height:50%;">
  </a>
</p>

